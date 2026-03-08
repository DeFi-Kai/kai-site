from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from fetch_defillama import build_defillama_dataset


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def resolve_output_path(repo_root: Path, post_id: str, dataset: dict) -> Path:
    output = dataset.get("output")
    if output:
        return repo_root / output
    name = dataset.get("name", "dataset")
    return repo_root / "static" / "data" / post_id / f"{name}.csv"


def main() -> None:
    parser = argparse.ArgumentParser(description="Run data pipeline datasets")
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to pipeline config file"
    )
    args = parser.parse_args()

    pipeline_dir = Path(__file__).resolve().parent
    repo_root = pipeline_dir.parent
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = (Path.cwd() / config_path).resolve()
    if not config_path.exists() and not config_path.suffix:
        yaml_path = config_path.with_suffix(".yaml")
        yml_path = config_path.with_suffix(".yml")
        if yaml_path.exists():
            config_path = yaml_path
        elif yml_path.exists():
            config_path = yml_path

    config = load_config(config_path)
    post_id = config.get("post_id", "default-post")
    datasets = config.get("datasets", [])

    if not datasets:
        print("No datasets configured")
        return

    for dataset in datasets:
        source = dataset.get("source")
        if not source:
            raise ValueError("Dataset missing source")

        output_path = resolve_output_path(repo_root, post_id, dataset)
        name = dataset.get("name", "dataset")

        print(f"Running dataset: {name} -> {output_path}")

        if source == "defillama":
            build_defillama_dataset(dataset, output_path)
        else:
            raise ValueError(f"Unsupported dataset source: {source}")


if __name__ == "__main__":
    main()
