+++
date = '2026-09-26T12:00:00-04:00'
draft = false
title = 'Reverse-Engineering Jupiter Lend Liquidations: Part 2'
slug = 'reverse-engineering-jupiter-lend-liquidations-part-2'
description = 'Reconstructing a Jupiter Lend liquidation dataset by following the live DuneSQL query from liquidation keys to final USD values.'
tags = ['Data & Methods', 'Technical Writing']
cte_explorer = true
+++

In [part one](https://defi-kai.github.io/kai-site/work/reverse-engineering-jupiter-lend-liquidations-part-1/), we observed liquidations on Solscan.io and mapped them to columns on Dune's [Solana instruction calls](https://dune.com/data/solana.instruction_calls) table. In this walkthrough we assemble those findings into one event-level dataset using common table expressions (CTEs) and join the results to the [`prices.hour`](https://dune.com/data/prices.hour) table to compute the value of liquidations.

This walkthrough focuses on the order of the CTEs and the data passed between them.

The query is organized into four phases:
1. identify liquidation contexts: `liq_keys`
2. reconstruct the amount legs: `inners_raw`, `operate_ranked`, `op_decoded`, `op_ui_per_rn`
3. attach liquidation metadata: `liq_meta`
4. value and present the results: the final `SELECT` and price joins

Click a CTE in the query to see what it does, and how it advances the data through its phase.

{{< cte-explorer >}}
