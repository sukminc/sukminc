from __future__ import annotations

import plistlib
from pathlib import Path


def build_launch_agent_payload(
    *,
    label: str,
    command: list[str],
    working_directory: str,
    run_hour: int,
    run_minute: int,
    stdout_path: str,
    stderr_path: str,
) -> dict:
    return {
        "Label": label,
        "ProgramArguments": command,
        "WorkingDirectory": working_directory,
        "StartCalendarInterval": {
            "Hour": run_hour,
            "Minute": run_minute,
        },
        "StandardOutPath": stdout_path,
        "StandardErrorPath": stderr_path,
        "RunAtLoad": False,
    }


def write_launch_agent(path: Path, payload: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as fh:
        plistlib.dump(payload, fh, sort_keys=False)
    return path

