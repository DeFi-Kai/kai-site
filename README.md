# Kai - Digital Asset Research

This repo contains the Hugo source for my personal website where I publish research and technical notes on DeFi market structure, protocol risk, and blockchain data analysis.

## Sections

- **Research**: Analysis of DeFi market structure, protocol economics, risk, and investment theses.
- **Data**: Onchain data work, SQL notes, and data-pipeline research.
- **Projects**: Technical projects supporting digital asset research and analysis.
- **About**: Background, experience, and technical skills.

## Data Pipeline

The pipeline in `data-pipeline/` generates CSV datasets into `static/data/<post_id>/` using the configuration in `data-pipeline/config.yaml`.

```bash
cd data-pipeline
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run_all.py --config config.yaml
```

Edit `config.yaml` to select datasets and configure their output paths.
