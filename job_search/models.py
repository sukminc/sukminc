from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class ResumeVariant:
    key: str
    label: str
    filename: str
    eyebrow: str
    summary: str
    strengths: list[str]
    signal_title: str
    signal_body: list[str]

    @property
    def path(self) -> Path:
        return Path(self.filename)


@dataclass(frozen=True)
class CandidateProfile:
    name: str
    headline: str
    location: str
    email: str
    open_to: list[str]
    links: dict[str, str]
    direction: list[str]
    workflow_steps: list[str]
    search_queries: dict[str, list[str]]
    resume_variants: dict[str, ResumeVariant]

    def to_dict(self) -> dict:
        payload = asdict(self)
        payload["resume_variants"] = {
            key: {
                **asdict(value),
                "path": str(value.path),
            }
            for key, value in self.resume_variants.items()
        }
        return payload


@dataclass(frozen=True)
class JobPosting:
    source: str
    title: str
    company: str
    location: str
    url: str
    description: str = ""
    salary: str = ""
    posted_at: str = ""
    employment_type: str = ""
    job_id: str = ""
    notes: str = ""

    def combined_text(self) -> str:
        return " ".join(
            [
                self.title,
                self.company,
                self.location,
                self.description,
                self.employment_type,
                self.notes,
            ]
        ).lower()

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class MatchDetail:
    track_key: str
    track_label: str
    score: int
    reasons: list[str]
    blockers: list[str]
    recommended_resume: str
    recommended_resume_path: str
    status: str
    talking_points: list[str]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class JobMatch:
    posting: JobPosting
    best_match: MatchDetail
    alternatives: list[MatchDetail] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "posting": self.posting.to_dict(),
            "best_match": self.best_match.to_dict(),
            "alternatives": [option.to_dict() for option in self.alternatives],
        }

