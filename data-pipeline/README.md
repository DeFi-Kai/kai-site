# Data Pipeline

This folder contains the local data pipeline that generates CSV files into `static/data/<post_id>/`.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python run_all.py --config config.yaml
```

## Config

Edit `config.yaml` to set `post_id` and datasets. Outputs are written to `static/data/<post_id>/`.
