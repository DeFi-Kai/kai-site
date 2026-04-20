+++
date = '2026-04-19T20:15:00-04:00'
draft = false
title = 'Automated ETL Pipeline for Onchain Analysis'
categories = ['Data']
+++

Onchain analysis is bottlenecked by SQL and data plumbing. This causes researchers to spend valuable time creating queries and moving data between Dune and external sources.

At Blocmates, we solved this with an [agent-driven ETL pipeline](https://github.com/DeFi-Kai/dune-etl-agent) to automate dashboard production for the research team.

You fill out a data spec, the agent writes, tests and pushes queries to Dune, using GitHub for version control. If the spec involves heavy API calls, the agent sets up a Github action to collect and load data into Dune. Queries are generated in minutes and available on Dune to create visualizations through the UI.

We used this workflow to create the [MetaDAO dashboard](https://dune.com/blocmates_research/metadao-blocmates-pro).

![Screenshot From 2026-04-19 19-57-37](images/Screenshot%20From%202026-04-19%2019-57-37.png)
*MetaDAO dashboard -- produced by the pipeline.*

Here's how it works.

## Dune ETL Agent

The data spec is the single entry point. The user fills out the spec with the target blockchain(s), APIs, and a numbered list of visualizations with short descriptions. Then invokes `/run-spec <path>` (or pastes the spec inline) to kick off the run.

On each run the agent (via Claude Code) loads the DuneSQL best practices skill containing notes on SQL query structure, optimization, and error-handling. Depending on the user's spec, the agent can load two additional skills:
1. API references skill: shared techniques for Dune's LiveFetch function (http_get / http_post, JSON parsing, error handling). It points to per-API leaves -- `api-defillama`, etc. -- for endpoints, auth, and rate limits.
2. Chain references skill: shared techniques for querying chain tables on Dune. Points to per-chain leaves (`chain-solana`, `chain-ethereum`, etc.) with table lists, partition windows, and chain-specific quirks.

Skills are separated this way to avoid context bloat. Documentation is required for each unique data source, however loading all of it per run would be costly and unreliable. Skill files load only when the spec declares a matching chain or API.

![automated-etl-pipeline-onchain-analysis-architecture](images/automated-etl-pipeline-onchain-analysis-architecture.svg)

If the spec includes onchain data, the agent loads Chain references (the shared technique doc) plus the matching leaf for that chain (i.e. `chain-solana`, `chain-ethereum`, etc.). The leaf contains the recommended tables, data schemas, and chain-specific knowledge.

When the spec includes an external source, the agent loads API references plus the matching leaf (i.e. `api-defillama`, etc.) for endpoints, auth, and rate limits.

The starter ships `chain-solana` and `api-defillama` as worked examples -- the shape to copy when adding a new chain or API.

````markdown
---
project: solana-defi-health
chains: [solana]
apis: [defillama]
refresh: daily 06:00 UTC
---

## Visualizations

1. **Solana DEX volume, last 30 days.** Daily stacked area, split by protocol. Add a 7-day rolling mean. Mark 2026-03-15 as "Jupiter v6 launch".

2. **Stablecoin net flow onto Solana.** Weekly bars for the last 12 weeks, USDC + USDT combined. Green for inflow, red for outflow.

3. **Top 10 Solana wallets by DEX volume (30d).** Simple table, sortable by volume.
````
*Example data spec*

By default, APIs are called inline via the LiveFetch function. However, Dune caps each query at a 5-second timeout per request, 4 MB response size, and 80 requests/second per proxy.

When the agent encounters a data limit error (429), it will ask the user to create a new datasource. If the user confirms, it creates a Python script (triggered by a GitHub Action) to fetch JSON directly from the API. The script stores a CSV in the repo, and loads it as a dataset on Dune.

Each query is processed through `verify.py`, a script for static lint + dry run on Dune. If the query fails, the agent refers back to the error handling section of the best practices skill and retries, up to a cap of 2 revisions per query. On the third failure it stops and surfaces the error.

Once queries are successfully created, the user validates the results in Dune's UI and configures the visualizations there. Additional edits can be prompted by referencing the query ID. When satisfied, the user asks the agent to open a PR.

To close the loop, the agent runs `pull_from_dune.py` to capture any UI edits (or no-ops if there were none), commits the synced state, and opens the PR. You or team members can merge the PR.
