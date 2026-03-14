from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from .models import CandidateProfile, JobMatch


def write_profile_snapshot(profile: CandidateProfile, output_dir: Path) -> Path:
    path = output_dir / "profile_snapshot.json"
    path.write_text(json.dumps(profile.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def write_match_payload(matches: list[JobMatch], output_dir: Path) -> Path:
    path = output_dir / "job_matches.json"
    payload = [match.to_dict() for match in matches]
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def build_markdown_report(profile: CandidateProfile, matches: list[JobMatch], input_path: Path) -> str:
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Job Search Report",
        "",
        f"- Generated: {generated_at}",
        f"- Input: `{input_path}`",
        f"- Candidate: {profile.name}",
        f"- Headline: {profile.headline}",
        "",
        "## Current Direction",
        "",
    ]
    for item in profile.direction:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## Workflow",
            "",
        ]
    )
    for item in profile.workflow_steps:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## Search Queries",
            "",
        ]
    )
    for platform, queries in profile.search_queries.items():
        lines.append(f"### {platform.title()}")
        lines.append("")
        for query in queries:
            lines.append(f"- {query}")
        lines.append("")

    lines.extend(
        [
            "## Top Matches",
            "",
            "| Status | Score | Track | Role | Company | Source | Resume |",
            "| --- | ---: | --- | --- | --- | --- | --- |",
        ]
    )
    for match in matches[:15]:
        best = match.best_match
        posting = match.posting
        lines.append(
            f"| {best.status} | {best.score} | {best.track_label} | "
            f"[{posting.title}]({posting.url or '#'}) | {posting.company} | {posting.source} | {best.recommended_resume} |"
        )

    lines.extend(["", "## Detailed Queue", ""])
    for index, match in enumerate(matches[:10], start=1):
        best = match.best_match
        posting = match.posting
        lines.extend(
            [
                f"### {index}. {posting.title} @ {posting.company}",
                "",
                f"- Status: `{best.status}`",
                f"- Score: `{best.score}`",
                f"- Source: `{posting.source}`",
                f"- Location: `{posting.location or 'n/a'}`",
                f"- Posted: `{posting.posted_at or 'n/a'}`",
                f"- Apply link: {posting.url or 'n/a'}",
                f"- Recommended resume: `{best.recommended_resume_path}`",
                "",
                "Reasons:",
            ]
        )
        for reason in best.reasons or ["직접 검토 필요"]:
            lines.append(f"- {reason}")
        lines.append("")
        lines.append("Talking points:")
        for point in best.talking_points:
            lines.append(f"- {point}")
        if best.blockers:
            lines.append("")
            lines.append("Blockers:")
            for blocker in best.blockers:
                lines.append(f"- {blocker}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def write_markdown_report(profile: CandidateProfile, matches: list[JobMatch], input_path: Path, output_dir: Path) -> Path:
    path = output_dir / "job_search_report.md"
    path.write_text(build_markdown_report(profile, matches, input_path), encoding="utf-8")
    return path

