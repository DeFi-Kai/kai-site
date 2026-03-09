from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

import time

import requests


def http_get_json(
    url: str,
    params: dict | None = None,
    timeout: int = 60,
    retries: int = 3,
    backoff_seconds: float = 1.5,
):
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, params=params, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(backoff_seconds * attempt)
                continue
            raise
    if last_error:
        raise last_error


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, headers: Iterable[str], rows: Iterable[Iterable]) -> None:
    ensure_dir(path.parent)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(list(headers))
        writer.writerows(rows)
