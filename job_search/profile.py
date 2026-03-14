from __future__ import annotations

import json
from pathlib import Path

from .models import CandidateProfile, ResumeVariant


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT.parent / "one-percent-better-os" / "public_profile.json"
RESUME_DIR = ROOT / "resume"

TRACK_LABELS = {
    "data_engineer": "Data Engineer",
    "ai_product_engineer": "AI Product Engineer",
}

DEFAULT_WORKFLOW_STEPS = [
    "LinkedIn과 Indeed에서 저장한 공고를 CSV 또는 JSON으로 모은다.",
    "매처를 실행해서 점수, 추천 레쥬메, 블로커를 확인한다.",
    "ready_to_apply 상태만 먼저 열고 수동으로 제출한다.",
    "제출한 공고는 ATS, referral, follow-up 일정까지 따로 기록한다.",
]

DEFAULT_SEARCH_QUERIES = {
    "linkedin": [
        "Data Engineer",
        "Senior Data Engineer",
        "Analytics Engineer",
        "AI Product Engineer",
        "AI Product Owner",
        "Founding Engineer AI",
    ],
    "indeed": [
        "data engineer airflow sql python",
        "analytics engineer dbt sql",
        "ai product engineer llm fastapi",
        "ai product owner startup",
    ],
}


def _load_profile_payload() -> dict:
    with PROFILE_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_candidate_profile() -> CandidateProfile:
    payload = _load_profile_payload()
    variants = {}
    for key, raw in payload["resume_variants"].items():
        variants[key] = ResumeVariant(
            key=key,
            label=TRACK_LABELS.get(key, key.replace("_", " ").title()),
            filename=str(RESUME_DIR / raw["filename"]),
            eyebrow=raw["eyebrow"],
            summary=raw["summary"],
            strengths=raw["strengths"],
            signal_title=raw["signal_title"],
            signal_body=raw["signal_body"],
        )

    return CandidateProfile(
        name=payload["person"]["name"],
        headline=payload["person"]["headline"],
        location=payload["person"]["location"],
        email=payload["person"]["email"],
        open_to=payload["person"]["open_to"],
        links=payload["links"],
        direction=payload["public_direction"],
        workflow_steps=DEFAULT_WORKFLOW_STEPS,
        search_queries=DEFAULT_SEARCH_QUERIES,
        resume_variants=variants,
    )

