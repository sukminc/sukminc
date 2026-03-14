from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .parsers import load_job_postings
from .profile import ROOT, load_candidate_profile
from .reporting import write_markdown_report, write_match_payload, write_profile_snapshot
from .schedule import build_launch_agent_payload, write_launch_agent
from .scoring import score_postings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resume-aware job search matcher")
    parser.add_argument(
        "--input",
        type=Path,
        default=ROOT / "job_search" / "input" / "jobs.sample.csv",
        help="CSV or JSON file with job postings",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "tmp" / "job_search" / "latest",
        help="Directory for generated report files",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="How many postings to summarize in stdout",
    )
    parser.add_argument(
        "--write-launchd-plist",
        type=Path,
        help="Optional path for a launchd plist that reruns this command daily",
    )
    parser.add_argument("--run-hour", type=int, default=9, help="launchd hour")
    parser.add_argument("--run-minute", type=int, default=0, help="launchd minute")
    parser.add_argument(
        "--label",
        default="com.chrisyoon.jobsearch.report",
        help="launchd label when writing a plist",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input.exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")

    profile = load_candidate_profile()
    postings = load_job_postings(args.input)
    matches = score_postings(postings, profile)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    profile_path = write_profile_snapshot(profile, args.output_dir)
    matches_path = write_match_payload(matches, args.output_dir)
    report_path = write_markdown_report(profile, matches, args.input, args.output_dir)

    plist_path = None
    if args.write_launchd_plist:
        payload = build_launch_agent_payload(
            label=args.label,
            command=[
                sys.executable,
                "-m",
                "job_search.cli",
                "--input",
                str(args.input),
                "--output-dir",
                str(args.output_dir),
            ],
            working_directory=str(ROOT),
            run_hour=args.run_hour,
            run_minute=args.run_minute,
            stdout_path=str(args.output_dir / "job_search.stdout.log"),
            stderr_path=str(args.output_dir / "job_search.stderr.log"),
        )
        plist_path = write_launch_agent(args.write_launchd_plist, payload)

    summary = {
        "total_postings": len(matches),
        "ready_to_apply": sum(match.best_match.status == "ready_to_apply" for match in matches),
        "worth_reviewing": sum(match.best_match.status == "worth_reviewing" for match in matches),
        "needs_review": sum(match.best_match.status == "needs_review" for match in matches),
        "report_path": str(report_path),
        "matches_path": str(matches_path),
        "profile_path": str(profile_path),
    }
    if plist_path:
        summary["launchd_plist"] = str(plist_path)

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    for match in matches[: args.top]:
        posting = match.posting
        best = match.best_match
        print(
            f"- {best.status:16} {best.score:>3} | {best.track_label:<26} | "
            f"{posting.title} @ {posting.company}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

