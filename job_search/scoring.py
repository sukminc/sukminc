from __future__ import annotations

from collections import defaultdict
from datetime import date, datetime

from .models import CandidateProfile, JobMatch, JobPosting, MatchDetail

TRACK_DEFINITIONS = {
    "data_engineer": {
        "label": "Data Engineer",
        "resume_key": "data_engineer",
        "title_keywords": {
            "data engineer": 18,
            "senior data engineer": 20,
            "analytics engineer": 14,
            "data platform": 12,
            "etl": 8,
            "elt": 8,
            "airflow": 8,
            "warehouse": 7,
            "dbt": 7,
            "bigquery": 7,
            "redshift": 7,
            "sql": 6,
            "python": 6,
        },
        "body_keywords": {
            "pipeline": 6,
            "orchestration": 5,
            "reconciliation": 7,
            "data quality": 8,
            "schema drift": 7,
            "audit": 6,
            "sox": 7,
            "batch": 4,
            "streaming": 4,
            "observability": 6,
        },
    },
    "ai_product_engineer": {
        "label": "AI Product Owner / Engineer",
        "resume_key": "ai_product_engineer",
        "title_keywords": {
            "ai product engineer": 20,
            "product engineer": 16,
            "ai product owner": 18,
            "ai product manager": 16,
            "founding engineer": 14,
            "full stack engineer": 12,
            "ai engineer": 12,
            "prototype": 8,
            "llm": 10,
            "agent": 8,
            "generative ai": 10,
        },
        "body_keywords": {
            "0 to 1": 8,
            "mvp": 8,
            "shipping": 6,
            "user feedback": 5,
            "product sense": 7,
            "prompt": 5,
            "fastapi": 5,
            "next.js": 5,
            "experimentation": 6,
            "iteration": 6,
            "ai workflow": 7,
        },
    },
}

BLOCKER_RULES = {
    "security clearance required": "보안 클리어런스 요구",
    "must be located in the us": "미국 거주 필수",
    "must reside in the us": "미국 거주 필수",
    "us citizens only": "미국 시민권 요구",
    "no sponsorship": "비자 스폰서 없음",
    "5 days onsite": "주 5일 상주",
    "five days onsite": "주 5일 상주",
}

PREFERRED_LOCATIONS = ("remote", "canada", "toronto", "hybrid")


def _keyword_score(text: str, keywords: dict[str, int]) -> tuple[int, list[str]]:
    score = 0
    hits: list[tuple[str, int]] = []
    for term, weight in keywords.items():
        if term in text:
            score += weight
            hits.append((term, weight))
    hits.sort(key=lambda item: item[1], reverse=True)
    reasons = [f"{term} (+{weight})" for term, weight in hits[:5]]
    return score, reasons


def _location_score(text: str) -> tuple[int, list[str]]:
    reasons = []
    score = 0
    for location in PREFERRED_LOCATIONS:
        if location in text:
            score += 3
            reasons.append(f"{location} 선호 조건 매치 (+3)")
            break
    return score, reasons


def _parse_posted_at(raw: str) -> date | None:
    raw = raw.strip()
    if not raw:
        return None
    formats = ("%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y", "%b %d, %Y", "%B %d, %Y")
    for pattern in formats:
        try:
            return datetime.strptime(raw, pattern).date()
        except ValueError:
            continue
    return None


def _recency_score(posted_at: str) -> tuple[int, list[str]]:
    posted_date = _parse_posted_at(posted_at)
    if not posted_date:
        return 0, []
    age = (date.today() - posted_date).days
    if age <= 3:
        return 5, [f"최근 공고 {age}일 이내 (+5)"]
    if age <= 7:
        return 3, [f"최근 공고 {age}일 이내 (+3)"]
    if age <= 14:
        return 1, [f"최근 공고 {age}일 이내 (+1)"]
    return 0, []


def _blockers(text: str) -> list[str]:
    hits = []
    for phrase, label in BLOCKER_RULES.items():
        if phrase in text:
            hits.append(label)
    return hits


def _status_for(score: int, blockers: list[str]) -> str:
    if blockers:
        return "needs_review"
    if score >= 45:
        return "ready_to_apply"
    if score >= 28:
        return "worth_reviewing"
    return "skip"


def score_posting(posting: JobPosting, profile: CandidateProfile) -> JobMatch:
    title_text = posting.title.lower()
    full_text = posting.combined_text()
    option_scores: list[MatchDetail] = []

    for track_key, config in TRACK_DEFINITIONS.items():
        score = 0
        reasons: list[str] = []
        blockers = _blockers(full_text)

        title_score, title_reasons = _keyword_score(title_text, config["title_keywords"])
        body_score, body_reasons = _keyword_score(full_text, config["body_keywords"])
        location_score, location_reasons = _location_score(full_text)
        recency_score, recency_reasons = _recency_score(posting.posted_at)

        score += title_score + body_score + location_score + recency_score
        reasons.extend(title_reasons)
        reasons.extend(body_reasons)
        reasons.extend(location_reasons)
        reasons.extend(recency_reasons)

        resume = profile.resume_variants[config["resume_key"]]
        talking_points = [
            resume.summary,
            *resume.strengths[:2],
            resume.signal_body[0],
        ]

        option_scores.append(
            MatchDetail(
                track_key=track_key,
                track_label=config["label"],
                score=score,
                reasons=reasons[:6],
                blockers=blockers,
                recommended_resume=resume.label,
                recommended_resume_path=resume.filename,
                status=_status_for(score, blockers),
                talking_points=talking_points,
            )
        )

    option_scores.sort(key=lambda detail: detail.score, reverse=True)
    return JobMatch(posting=posting, best_match=option_scores[0], alternatives=option_scores[1:])


def score_postings(postings: list[JobPosting], profile: CandidateProfile) -> list[JobMatch]:
    matches = [score_posting(posting, profile) for posting in postings]
    grouped = defaultdict(list)
    for match in matches:
        grouped[match.best_match.status].append(match)

    ordered_status = {"ready_to_apply": 0, "worth_reviewing": 1, "needs_review": 2, "skip": 3}
    matches.sort(key=lambda item: (ordered_status[item.best_match.status], -item.best_match.score))
    return matches

