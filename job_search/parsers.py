from __future__ import annotations

import csv
import json
from pathlib import Path

from .models import JobPosting

FIELD_ALIASES = {
    "source": ("source", "platform", "site"),
    "title": ("title", "job_title", "role"),
    "company": ("company", "company_name"),
    "location": ("location", "city", "region"),
    "url": ("url", "link", "job_url", "apply_url"),
    "description": ("description", "job_description", "summary"),
    "salary": ("salary", "compensation"),
    "posted_at": ("posted_at", "posted", "date_posted"),
    "employment_type": ("employment_type", "type"),
    "job_id": ("job_id", "platform_job_id", "id"),
    "notes": ("notes", "memo", "comment"),
}


def _normalize_row(raw: dict) -> dict:
    lowered = {str(key).strip().lower(): value for key, value in raw.items()}
    normalized = {}
    for target, aliases in FIELD_ALIASES.items():
        normalized[target] = ""
        for alias in aliases:
            if alias in lowered and lowered[alias] is not None:
                normalized[target] = str(lowered[alias]).strip()
                break
    normalized["source"] = normalized["source"].lower() or "unknown"
    return normalized


def _coerce_posting(raw: dict) -> JobPosting:
    normalized = _normalize_row(raw)
    return JobPosting(
        source=normalized["source"],
        title=normalized["title"],
        company=normalized["company"],
        location=normalized["location"],
        url=normalized["url"],
        description=normalized["description"],
        salary=normalized["salary"],
        posted_at=normalized["posted_at"],
        employment_type=normalized["employment_type"],
        job_id=normalized["job_id"],
        notes=normalized["notes"],
    )


def load_job_postings(path: Path) -> list[JobPosting]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            return [_coerce_posting(row) for row in reader if any(row.values())]
    if suffix == ".json":
        with path.open("r", encoding="utf-8") as fh:
            payload = json.load(fh)
        if isinstance(payload, dict):
            items = payload.get("jobs") or payload.get("postings") or []
        else:
            items = payload
        return [_coerce_posting(item) for item in items]
    raise ValueError(f"Unsupported input format: {path}")

