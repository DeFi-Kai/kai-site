+++
date = '2026-09-26T12:00:00-04:00'
draft = true
title = 'Reverse-Engineering Jupiter Lend Liquidations: Part 2'
slug = 'reverse-engineering-jupiter-lend-liquidations-part-2'
description = 'Reconstructing a Jupiter Lend liquidation dataset by following the live DuneSQL query from liquidation keys to final USD values.'
tags = ['Data & Methods', 'Technical Writing']
cte_explorer = true
+++

Part 1 identified the liquidation discriminator, account positions, inner `operate` calls, and serialized amount fields. Here, I assemble those findings into one event-level dataset and join Dune's hourly prices to value the debt repaid and collateral seized.

The query produces one row per observed liquidation context, keyed by transaction ID and outer-instruction index. Follow it through four phases: identify liquidation contexts, reconstruct the amount legs, attach liquidation metadata, then value and present the results. The complete query stays visible; select a CTE to see how it advances the data through its phase and what assumptions apply.

{{< cte-explorer >}}
