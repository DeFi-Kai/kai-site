from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

import requests


def http_get_json(url: str, params: dict | None = None, timeout: int = 30):
    response = requests.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    return response.json()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, headers: Iterable[str], rows: Iterable[Iterable]) -> None:
    ensure_dir(path.parent)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(list(headers))
        writer.writerows(rows)
