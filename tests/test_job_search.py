from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from job_search.parsers import load_job_postings
from job_search.profile import load_candidate_profile
from job_search.scoring import score_postings


ROOT = Path(__file__).resolve().parents[1]
SAMPLE_INPUT = ROOT / "job_search" / "input" / "jobs.sample.csv"


class JobSearchTests(unittest.TestCase):
    def test_csv_parser_loads_expected_rows(self) -> None:
        postings = load_job_postings(SAMPLE_INPUT)
        self.assertEqual(len(postings), 3)
        self.assertEqual(postings[0].source, "linkedin")
        self.assertEqual(postings[1].title, "AI Product Owner")

    def test_scoring_picks_data_engineer_resume(self) -> None:
        profile = load_candidate_profile()
        postings = load_job_postings(SAMPLE_INPUT)
        matches = score_postings(postings, profile)
        top = matches[0]
        self.assertEqual(top.posting.title, "Senior Data Engineer")
        self.assertEqual(top.best_match.track_key, "data_engineer")
        self.assertEqual(top.best_match.status, "ready_to_apply")

    def test_blockers_force_manual_review(self) -> None:
        profile = load_candidate_profile()
        postings = load_job_postings(SAMPLE_INPUT)
        matches = score_postings(postings, profile)
        blocked = [match for match in matches if "Security" in match.posting.company][0]
        self.assertEqual(blocked.best_match.status, "needs_review")
        self.assertTrue(blocked.best_match.blockers)


if __name__ == "__main__":
    unittest.main()
