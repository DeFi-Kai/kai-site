+++
date = '2026-04-19T20:15:00-04:00'
draft = false
title = 'Building an Agentic Pipeline for Onchain Data Analysis'
slug = 'building-an-agentic-pipeline-for-onchain-analytics'
aliases = ['/data/automated-etl-pipeline-for-onchain-analysis/']
tags = ['Data & Methods', 'Technical Writing']
+++

Using an LLM for data analysis can sometimes create more problems than it solves. In a chat-based workflow, the analyst still has to supply table schemas, API documentation, and project-specific context while copying and pasting data between multiple interfaces and tools. If you're not careful, this setup can increase token costs and introduce errors -- undermining the time saved by using an LLM in the first place.

At [Blocmates](https://x.com/blocmates), we created an agentic pipeline to automate these tasks. Instead of manually providing context and coordinating each step, the analyst fills out a data specification and sends it to Claude Code. The agent loads the necessary context, writes SQL queries, fetches data from APIs, and tests and publishes the queries to Dune.

The pipeline uses GitHub for version control and GitHub Actions for coordinating scheduled API ingestion to update datasets in Dune. Once the queries are published, analysts can inspect them in Dune's interface for final verification and configure the visualizations.

We used this workflow to generate queries and create custom datasets for the [MetaDAO ICO dashboard](https://dune.com/blocmates_research/metadao-blocmates-pro) and [Chain GDP dashboard](https://dune.com/blocmatesresearch/chain-gdp).

Here, we walk through the setup, including the architecture and design choices, so you can fork the project or build something similar. The [source code and setup instructions are available on GitHub](https://github.com/DeFi-Kai/dune-etl-agent).

## Architecture/design choices

Our original workflow required switching between Claude, Dune, and external APIs. We generated SQL queries in Claude, tested and executed them in Dune, and occasionally used Claude to write Python scripts for external data.

The first iteration of the pipeline connected Claude Code to Dune's API. This allowed us to generate, test, and publish queries without manually transferring code between interfaces.

Dune offers an API and an MCP server that let you create and update queries. We chose Dune's API to create, test, and publish queries programmatically. We also tested Dune's MCP server, but in our tests it consumed ~2x as many Dune credits for equivalent tasks. In contrast, using the API gave us more control over which endpoints were called, although it required writing and maintaining the integration code.

### Context management and resource selection

Connecting Claude to Dune solved the problem of manually transferring data between interfaces, but it didn't address how we managed context across projects.

Each new project required submitting the same sets of information, which became repetitive. To avoid this, I tried to use the same chat for multiple projects, but it caused me to hit context usage limits faster and resulted in queries that included data from the wrong project.

To fix this, I created a standardized framework for Claude to access the necessary information.

![Automated ETL pipeline architecture](images/automated-etl-pipeline-onchain-analysis-architecture.svg)

We use `CLAUDE.md` as the "master guide" for project-wide instructions and separate skill files for source-specific knowledge. I also created a data specification template that identifies the blockchains and APIs required for each analysis. Skill files are only loaded when the spec declares a matching chain or API. This gives the agent a structured way to select relevant references instead of loading every available source.

This setup requires maintaining structured documentation, but it ultimately reduces the amount of irrelevant context supplied on each run.

### GitHub for version control and GitHub Actions for refreshing datasets

We added GitHub support to maintain a versioned history of SQL queries. This allowed us to use GitHub as the source of truth, review changes, and roll back to previous versions when necessary.

We also incorporated GitHub Actions to schedule external API ingestion. By default, the agent uses Dune's LiveFetch to retrieve external data, but its request and response limits can make certain datasets difficult to maintain. GitHub Actions provides an alternative by running Python scripts to retrieve external data and upload it to Dune on a schedule.

## Building the pipeline with Claude

To identify the requirements for the pipeline, I mapped our manual workflow on paper and documented recurring errors during testing. These observations informed the following design decisions.

With the requirements set, I used Claude to create the Python scripts for pushing queries to and pulling queries from Dune, testing queries, and ingesting API data. I took notes on the documentation for each blockchain or API and provided the necessary notes to Claude so that it could create skill files.

After creating each skill, I tested it by asking Claude Code to generate a SQL query or Python script using the new references. In some runs, Claude failed to access the correct skill file. Explicitly naming the file in my prompt improved the results but required me to manage resource selection manually.

This helped motivate the data specification template, which identifies the required blockchains and APIs so the agent can select the corresponding references.

## How it works

We begin each run by filling out a data spec with the target blockchain(s), API source(s), and a numbered list of visualizations with short descriptions. Next, we invoke `/run-spec <path>` (or paste the spec inline) to kick off the run using Claude Code.

```markdown
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
```

_Example data spec._

When the agent begins, it loads a DuneSQL best practices skill covering query structure, optimization, and error handling. Depending on the spec, the agent can also load two additional skills:

1. API references skill: shared techniques for Dune LiveFetch (`http_get`, `http_post`, JSON parsing, and error handling). It points to per-API leaves such as `api-defillama` for endpoints, auth, and rate limits.
2. Chain references skill: shared techniques for querying chain tables on Dune. It points to per-chain leaves (`chain-solana`, `chain-ethereum`, and others) with table lists, partition windows, and chain-specific quirks.

Documentation is required for each unique data source, but loading every source on every run would be expensive and unreliable. Skill files are only loaded when the spec declares a matching chain or API.

If the spec includes onchain data, the agent loads the chain references skill plus the chain leaf (for example, `chain-solana` or `chain-ethereum`). The leaf contains recommended tables, schema notes, and chain-specific guidance.

When the spec includes external sources, the agent loads API references plus the matching API leaf (for example, `api-defillama`) for endpoints, auth, and rate limits.

The starter ships with `chain-solana` and `api-defillama` as worked examples and templates for adding new chains or APIs.

Each query is processed through `verify.py`, which runs static lint checks and a dry run against Dune. If a query fails, the agent revisits the best-practices error-handling guidance and retries, with a cap of two revisions per query. On the third failure, it stops and surfaces the error.

Each dashboard is assigned a YAML file that lists queries, each with a unique ID and a link to the live query on Dune. If you start a new session and want to make an edit, you can reference the URL, ID, or dashboard name so the agent can identify which query to access.

After the query is created, we manually configure the visualizations in Dune's UI. We perform row-level spot checks and check the math by hand to validate the accuracy of the data. When live sources exist, we check directly against them.

### Handling API limits

By default, APIs are called inline through LiveFetch. But Dune enforces the following limits: a 5-second timeout per request, a maximum response size of 4 MB, and 80 requests per second per proxy.

When the agent hits a data limit error (for example, HTTP 429), it asks the user to approve creating a new data source. If approved, it creates a Python script (triggered by GitHub Actions) to fetch JSON directly from the API, save a CSV in the repo, and load it as a dataset on Dune.

### Publishing workflow

The agent publishes queries to Dune before opening a pull request so the analyst can verify the results and configure visualizations. Analysts can also edit the SQL directly in Dune's interface.

Once the queries are verified, the analyst asks the agent to open a pull request. The agent runs `pull_from_dune.py` to synchronize the latest SQL from Dune with the local repository, capturing any edits made in the interface.

The agent then commits the synchronized files to a feature branch and opens a pull request on GitHub. Team members can review the changes before merging them into the main branch, preserving a versioned history of the queries.

## Conclusion

Building this pipeline showed us that using an LLM to generate SQL is only one part of automating data analysis. The bigger challenge was creating a repeatable workflow for managing context, coordinating tools, and verifying outputs.

The pipeline doesn't eliminate the need for an analyst. Queries still require verification, and visualizations must be configured manually in Dune. But it allows us to spend less time coordinating tools and more time analyzing the results.

I've published a [recreated version of the pipeline on GitHub](https://github.com/DeFi-Kai/dune-etl-agent) without Blocmates' internal data. You can fork the repository, review the implementation, or extend it with support for additional blockchains and APIs.
