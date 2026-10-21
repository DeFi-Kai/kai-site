+++
date = '2026-09-26T12:00:00-04:00'
draft = false
title = 'Reverse-Engineering Jupiter Lend Liquidations: Part 2'
slug = 'reverse-engineering-jupiter-lend-liquidations-part-2'
tags = ['Data & Methods', 'Technical Writing']
cte_explorer = true
+++

In [Part 1](https://defi-kai.github.io/kai-site/work/reverse-engineering-jupiter-lend-liquidations-part-1/), we identified Jupiter Lend's liquidation instructions, mapped their account arguments, and decoded the raw amounts of debt repaid and collateral seized.

In this walkthrough, we'll combine those findings into a single DuneSQL query using common table expressions (CTEs). The query reconstructs liquidation records from raw instructions and joins Dune's [`prices.hour`](https://dune.com/data/prices.hour) table to calculate the USD value of debt repaid and collateral seized.

We'll work through the query in four phases, following how each CTE transforms and passes data to the next. **Select a CTE in the interactive query below** to explore its role in building the final dataset.

You can [view the complete query on Dune](https://dune.com/queries/8711844/12764525) or explore the [source code and exported dataset on GitHub](https://github.com/DeFi-Kai/Jupiter-lend-liquidation-risk).

{{< cte-explorer >}}
