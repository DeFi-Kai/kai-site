from __future__ import annotations

from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from time import sleep
from typing import Dict, Iterable

from dateutil.relativedelta import relativedelta

from utils import http_get_json, write_csv

BASE_URL = "https://api.llama.fi"
COINGECKO_URL = "https://api.coingecko.com/api/v3"


def _cutoff_date(months: int) -> date:
    today = date.today()
    return today - relativedelta(months=months)


def _fetch_historical_tvl(scope: str) -> list[dict]:
    if scope == "global":
        url = f"{BASE_URL}/charts"
        data = http_get_json(url)
        normalized = []
        for entry in data:
            if not isinstance(entry, dict):
                continue
            timestamp = entry.get("date")
            tvl = entry.get("totalLiquidityUSD")
            if timestamp is None:
                continue
            try:
                timestamp = int(timestamp)
            except (TypeError, ValueError):
                continue
            normalized.append({
                "date": timestamp,
                "tvl": tvl
            })
        return normalized
    url = f"{BASE_URL}/v2/historicalChainTvl/{scope}"
    return http_get_json(url)


def _fetch_protocols() -> list[dict]:
    url = f"{BASE_URL}/protocols"
    return http_get_json(url)


def _fetch_protocol(slug: str) -> dict:
    url = f"{BASE_URL}/protocol/{slug}"
    return http_get_json(url)


def _fetch_fees_overview(data_type: str) -> dict:
    url = f"{BASE_URL}/overview/fees"
    return http_get_json(url, params={"dataType": data_type})


def _fetch_coingecko_market_caps(gecko_id: str, start_ts: int, end_ts: int) -> list:
    url = f"{COINGECKO_URL}/coins/{gecko_id}/market_chart/range"
    params = {
        "vs_currency": "usd",
        "from": start_ts,
        "to": end_ts,
    }
    data = http_get_json(url, params=params)
    return data.get("market_caps", [])


def _extract_borrowed_series(chain_tvls: dict) -> Dict[int, float]:
    series_totals: Dict[int, float] = defaultdict(float)
    if not isinstance(chain_tvls, dict):
        return {}
    for chain_key, chain_data in chain_tvls.items():
        if not isinstance(chain_key, str) or not chain_key.endswith("-borrowed"):
            continue
        series = None
        if isinstance(chain_data, dict) and isinstance(chain_data.get("tvl"), list):
            series = chain_data.get("tvl")
        elif isinstance(chain_data, list):
            series = chain_data
        if not series:
            continue
        for point in series:
            if not isinstance(point, dict):
                continue
            timestamp = point.get("date") or point.get("timestamp")
            if timestamp is None:
                continue
            try:
                timestamp = int(timestamp)
            except (TypeError, ValueError):
                continue
            value = point.get("totalLiquidityUSD")
            if value is None:
                value = point.get("tvl")
            if not isinstance(value, (int, float)):
                continue
            series_totals[timestamp] += float(value)
    return dict(series_totals)


def _parse_bool(value: object, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    value_str = str(value).strip().lower()
    if value_str in {"1", "true", "yes", "y"}:
        return True
    if value_str in {"0", "false", "no", "n"}:
        return False
    return default


def _normalize_name(value: str) -> str:
    return "".join(ch for ch in value.lower() if ch.isalnum())


def _collect_lending_name_keys(protocols: Iterable[dict]) -> Dict[str, str]:
    name_map: Dict[str, str] = {}
    for protocol in protocols:
        name = protocol.get("name")
        display_name = protocol.get("displayName")
        slug = protocol.get("slug")
        for candidate in (name, display_name, slug):
            if isinstance(candidate, str) and candidate:
                name_map[_normalize_name(candidate)] = candidate
    return name_map


def build_lending_revenue_marketshare(dataset: dict, output_path: Path) -> None:
    params = dataset.get("params", {})
    start_date_str = params.get("start_date", "2025-05-01")
    top_n = int(params.get("top_n", 5))
    data_type = params.get("data_type", "dailyRevenue")
    as_percent = _parse_bool(params.get("percent", False), default=False)

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

    protocols = _fetch_protocols()
    lending_slugs = {protocol.get("slug") for protocol in protocols if protocol.get("category") == "Lending"}

    overview = _fetch_fees_overview(data_type)
    overview_protocols = overview.get("protocols", [])
    lending_protocols = [
        protocol for protocol in overview_protocols
        if protocol.get("slug") in lending_slugs
    ]

    lending_name_keys = _collect_lending_name_keys(lending_protocols)

    breakdown = overview.get("totalDataChartBreakdown", [])
    if not isinstance(breakdown, list):
        write_csv(output_path, ["date", "Other"], [])
        return

    series_by_name: Dict[str, Dict[date, float]] = defaultdict(dict)

    for entry in breakdown:
        if not isinstance(entry, list) or len(entry) != 2:
            continue
        timestamp, values = entry
        if not isinstance(values, dict):
            continue
        try:
            timestamp = int(timestamp)
        except (TypeError, ValueError):
            continue
        entry_date = datetime.utcfromtimestamp(timestamp).date()
        if entry_date < start_date:
            continue
        for name, value in values.items():
            if not isinstance(name, str):
                continue
            normalized = _normalize_name(name)
            if normalized not in lending_name_keys:
                continue
            if not isinstance(value, (int, float)):
                continue
            current = series_by_name[name].get(entry_date, 0.0)
            series_by_name[name][entry_date] = current + float(value)

    if not series_by_name:
        write_csv(output_path, ["date", "Other"], [])
        return

    all_dates = set()
    for series in series_by_name.values():
        all_dates.update(series.keys())
    sorted_dates = sorted(all_dates)

    latest_date = max(sorted_dates)
    latest_values = []
    for name, series in series_by_name.items():
        latest_values.append((series.get(latest_date, 0.0), name))
    latest_values.sort(reverse=True, key=lambda item: item[0])

    top_names = [name for _, name in latest_values[:top_n]]
    other_names = [name for _, name in latest_values[top_n:]]

    headers = ["date"] + top_names + ["Other"]
    rows = []

    for entry_date in sorted_dates:
        total = 0.0
        for series in series_by_name.values():
            total += series.get(entry_date, 0.0)
        if total <= 0:
            continue
        row = [entry_date.isoformat()]
        for name in top_names:
            value = series_by_name[name].get(entry_date, 0.0)
            if as_percent:
                value = (value / total) * 100
            row.append(value)
        other_value = 0.0
        for name in other_names:
            other_value += series_by_name[name].get(entry_date, 0.0)
        if as_percent:
            other_value = (other_value / total) * 100
        row.append(other_value)
        rows.append(row)

    write_csv(output_path, headers, rows)


def _daily_series_from_market_caps(market_caps: list) -> Dict[date, float]:
    series: Dict[date, float] = {}
    for point in market_caps:
        if not isinstance(point, list) or len(point) < 2:
            continue
        timestamp_ms, value = point[0], point[1]
        if not isinstance(timestamp_ms, (int, float)):
            continue
        if not isinstance(value, (int, float)):
            continue
        entry_date = datetime.utcfromtimestamp(timestamp_ms / 1000).date()
        series[entry_date] = float(value)
    return series


def _latest_value(series: Dict[date, float]) -> float:
    if not series:
        return 0.0
    latest_date = max(series.keys())
    return series.get(latest_date, 0.0)


def build_lending_mcap_to_outstanding_loans(dataset: dict, output_path: Path) -> None:
    params = dataset.get("params", {})
    start_date_str = params.get("start_date", "2025-05-01")
    top_n = int(params.get("top_n", 5))
    debug_output = params.get("debug_output")
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

    protocols = _fetch_protocols()
    lending_protocols = [
        protocol for protocol in protocols
        if protocol.get("category") == "Lending" and protocol.get("slug")
    ]

    protocol_series: Dict[str, Dict[date, float]] = {}
    protocol_names: Dict[str, str] = {}
    protocol_gecko: Dict[str, str] = {}

    for protocol in lending_protocols:
        slug = protocol.get("slug")
        if not slug:
            continue
        detail = _fetch_protocol(slug)
        chain_tvls = detail.get("chainTvls", {})
        series = _extract_borrowed_series(chain_tvls)
        if not series:
            continue
        filtered_series: Dict[date, float] = {}
        for timestamp, value in series.items():
            entry_date = datetime.utcfromtimestamp(timestamp).date()
            if entry_date < start_date:
                continue
            filtered_series[entry_date] = filtered_series.get(entry_date, 0.0) + value
        if not filtered_series:
            continue
        protocol_series[slug] = filtered_series
        protocol_names[slug] = detail.get("name") or protocol.get("name") or slug
        gecko_id = detail.get("gecko_id")
        if isinstance(gecko_id, str) and gecko_id:
            protocol_gecko[slug] = gecko_id

    if not protocol_series:
        write_csv(output_path, ["date"], [])
        return

    ranked = []
    for slug, series in protocol_series.items():
        ranked.append((_latest_value(series), slug))
    ranked.sort(reverse=True, key=lambda item: item[0])

    top_slugs = [slug for _, slug in ranked[:top_n]]
    top_slugs = [slug for slug in top_slugs if slug in protocol_gecko]

    if debug_output:
        repo_root = output_path.parents[2]
        debug_path = Path(debug_output)
        if not debug_path.is_absolute():
            debug_path = repo_root / debug_path
        debug_rows = []
        for value, slug in ranked:
            debug_rows.append([
                slug,
                protocol_names.get(slug, slug),
                protocol_gecko.get(slug, ""),
                value,
                "yes" if slug in top_slugs else "no"
            ])
        write_csv(debug_path, ["slug", "name", "gecko_id", "latest_outstanding_loans", "selected"], debug_rows)

    if not top_slugs:
        write_csv(output_path, ["date"], [])
        return

    end_ts = int(datetime.utcnow().timestamp())
    start_ts = int(datetime.combine(start_date, datetime.min.time()).timestamp())

    mcap_series_by_slug: Dict[str, Dict[date, float]] = {}

    for slug in top_slugs:
        gecko_id = protocol_gecko[slug]
        market_caps = _fetch_coingecko_market_caps(gecko_id, start_ts, end_ts)
        mcap_series_by_slug[slug] = _daily_series_from_market_caps(market_caps)
        sleep(1)

    all_dates = set()
    for series in mcap_series_by_slug.values():
        all_dates.update(series.keys())
    for series in protocol_series.values():
        all_dates.update(series.keys())
    sorted_dates = sorted(date for date in all_dates if date >= start_date)

    headers = ["date"] + [protocol_names[slug] for slug in top_slugs]
    rows = []

    for entry_date in sorted_dates:
        row = [entry_date.isoformat()]
        include_row = False
        for slug in top_slugs:
            mcap_value = mcap_series_by_slug.get(slug, {}).get(entry_date)
            loans_value = protocol_series.get(slug, {}).get(entry_date)
            if not mcap_value or not loans_value:
                row.append("")
                continue
            ratio = mcap_value / loans_value if loans_value else None
            if ratio is None:
                row.append("")
                continue
            row.append(ratio)
            include_row = True
        if include_row:
            rows.append(row)

    write_csv(output_path, headers, rows)


def build_outstanding_loans_marketshare(dataset: dict, output_path: Path) -> None:
    params = dataset.get("params", {})
    start_date_str = params.get("start_date", "2025-05-01")
    top_n = int(params.get("top_n", 5))
    as_percent = _parse_bool(params.get("percent", True), default=True)

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

    protocols = _fetch_protocols()
    lending_protocols = [
        protocol for protocol in protocols
        if protocol.get("category") == "Lending" and protocol.get("slug")
    ]

    protocol_series: Dict[str, Dict[date, float]] = {}
    protocol_names: Dict[str, str] = {}

    for protocol in lending_protocols:
        slug = protocol.get("slug")
        if not slug:
            continue
        detail = _fetch_protocol(slug)
        chain_tvls = detail.get("chainTvls", {})
        series = _extract_borrowed_series(chain_tvls)
        if not series:
            continue
        filtered_series: Dict[date, float] = {}
        for timestamp, value in series.items():
            entry_date = datetime.utcfromtimestamp(timestamp).date()
            if entry_date < start_date:
                continue
            filtered_series[entry_date] = filtered_series.get(entry_date, 0.0) + value
        if not filtered_series:
            continue
        protocol_series[slug] = filtered_series
        protocol_names[slug] = detail.get("name") or protocol.get("name") or slug

    if not protocol_series:
        write_csv(output_path, ["date", "Other"], [])
        return

    latest_values = []
    for slug, series in protocol_series.items():
        latest_date = max(series.keys())
        latest_values.append((series[latest_date], slug))
    latest_values.sort(reverse=True, key=lambda item: item[0])

    top_slugs = [slug for _, slug in latest_values[:top_n]]
    other_slugs = [slug for _, slug in latest_values[top_n:]]

    all_dates = set()
    for series in protocol_series.values():
        all_dates.update(series.keys())
    sorted_dates = sorted(all_dates)

    headers = ["date"] + [protocol_names[slug] for slug in top_slugs] + ["Other"]
    rows = []

    for entry_date in sorted_dates:
        total = 0.0
        for series in protocol_series.values():
            total += series.get(entry_date, 0.0)

        if total <= 0:
            continue

        row = [entry_date.isoformat()]
        for slug in top_slugs:
            value = protocol_series[slug].get(entry_date, 0.0)
            if as_percent:
                value = (value / total) * 100
            row.append(value)
        other_value = 0.0
        for slug in other_slugs:
            other_value += protocol_series[slug].get(entry_date, 0.0)
        if as_percent:
            other_value = (other_value / total) * 100
        row.append(other_value)
        rows.append(row)

    write_csv(output_path, headers, rows)


def build_defillama_dataset(dataset: dict, output_path: Path) -> None:
    kind = dataset.get("kind", "historical_tvl")
    if kind == "historical_tvl":
        params = dataset.get("params", {})
        scope = params.get("scope", "global")
        months = int(params.get("months", 6))

        raw = _fetch_historical_tvl(scope)
        cutoff = _cutoff_date(months)
        rows = []

        for entry in raw:
            timestamp = entry.get("date")
            tvl = entry.get("tvl")
            if timestamp is None:
                continue
            entry_date = datetime.utcfromtimestamp(timestamp).date()
            if entry_date < cutoff:
                continue
            rows.append([entry_date.isoformat(), tvl])

        write_csv(output_path, ["date", "tvl"], rows)
        return
    if kind == "outstanding_loans_marketshare":
        build_outstanding_loans_marketshare(dataset, output_path)
        return
    if kind == "lending_revenue_marketshare":
        build_lending_revenue_marketshare(dataset, output_path)
        return
    if kind == "lending_mcap_to_outstanding_loans":
        build_lending_mcap_to_outstanding_loans(dataset, output_path)
        return

    raise ValueError(f"Unsupported DefiLlama dataset kind: {kind}")
