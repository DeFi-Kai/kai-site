+++
date = '2026-09-26T12:00:00-04:00'
draft = true
title = 'Reverse-Engineering Jupiter Lend Liquidations: Part 2'
slug = 'reverse-engineering-jupiter-lend-liquidations-part-2'
description = 'Reconstructing a Jupiter Lend liquidation dataset by following the live DuneSQL query from liquidation keys to final USD values.'
tags = ['Data & Methods', 'Technical Writing']
cte_explorer = true
+++

Part 1 identified the liquidation discriminator, account positions, inner `operate` calls, and serialized amount fields. Part 2 assembles those findings into one event-level dataset using common table expressions (CTEs).

This walkthrough focuses on the order of the CTEs and the data passed between them. Click a CTE in the query to see what it does, what it receives, and what limitation applies to the published dataset.

{{< cte-explorer >}}
