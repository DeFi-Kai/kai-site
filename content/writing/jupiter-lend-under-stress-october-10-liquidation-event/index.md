+++
date = '2026-10-05T09:00:00-04:00'
draft = false
title = 'Jupiter Lend Under Stress: Analyzing the October 10 Liquidation Event'
slug = 'jupiter-lend-under-stress-october-10-liquidation-event'
tags = ['Data & Methods', 'Technical Writing']
writing_category = 'research-analysis'
+++

Read [part one](https://defi-kai.github.io/kai-site/work/reverse-engineering-jupiter-lend-liquidations-part-1/) and [part two](https://defi-kai.github.io/kai-site/work/jupiter-lend-liquidations-part-2/) of this series.

Parts one and two of this series covered how I reverse-engineered Jupiter Lend’s liquidation instructions and used them to build a transaction-level liquidation dataset. In this report, we use that dataset to examine how the October 10 selloff affected Jupiter Lend during its first major market-wide stress event.

---

On October 10, 2025, U.S. President Donald Trump announced that the U.S. would impose an additional 100% tariff on Chinese imports. This announcement was followed by a rapid market selloff: over the course of October 10, the price of ETH fell as much as 12% and SOL fell as much as 24%. 

The wave of selling ultimately triggered $19B in liquidations across derivative markets. But how did this affect other venues that offer leverage, like credit markets?

Credit markets let borrowers submit collateral and borrow assets up to a specified loan-to-value (LTV) ratio. When collateral falls in value relative to the borrowed asset, the position's LTV moves closer to its liquidation threshold. 

In this report, we examine how the October 10 selloff event affected Jupiter Lend, a credit market on Solana, during its first major market-wide stress event. 

## October 10, 2025 Liquidation Event Overview

At the start of October 10, Jupiter Lend had $755M in total value locked (TVL). Over the course of the day, SOL traded between $224.46 and $168.79, a 24.8% peak-to-trough decline. Ultimately, liquidators seized $1.33M in collateral, equivalent to 0.17% of TVL. SOL-linked assets, including WSOL, JITOSOL, JUPSOL, and INF, accounted for 70% of the total collateral seized, representing 0.30% of SOL-linked TVL.

### Headline numbers
- ~$1.29M in estimated debt repaid
- ~$1.33M in estimated collateral seized
- 484 liquidation events
- Averge liquidation size: $2,757.35
- Median liquidation size: $52.93
- The largest liquidated collateral assets were WSOL ( ~$567k), cbBTC (~$372k), and JUPSOL (~$264k)

## Timeline of events

Jupiter Lend processed its first two liquidations during the five-minute window from 15:15–15:20 UTC, totaling $12.22 in debt repaid. During this period, SOL’s price fell from $218.44 to $216.60.

From 15:15–20:55 UTC, SOL’s price decreased by 6.6%, falling from $218.44 to $203.90. During this five-hour-and-40-minute window, liquidators repaid $31K in debt across 270 liquidations.

![Figure 1. Jupiter Lend debt repaid and SOL price in five-minute intervals on October 10, 2025](images/Figure%201.%20Jupiter%20Lend%20debt%20repaid%20and%20SOL%20price%20in%20five-minute%20intervals%20on%20October%2010,%202025.png)

The sharp increase in liquidation volume followed SOL’s steepest five-minute decline of the day. Between 21:10–21:15 UTC, SOL fell 4.98%, from $197.22 to $187.39. During the 20-minute window beginning with this decline, from 21:10–21:30 UTC, 65 liquidations repaid $753K in debt, representing 58.37% of the day’s total debt repaid. The top assets seized by value during this period were cbBTC ($372K), JUPSOL ($260K), and JITOSOL ($91K).

Another major wave of liquidations occurred from 21:30–22:35 UTC. During this 65-minute window, 64 liquidations repaid $372K in debt, representing 28.90% of the day’s total debt repaid.

Liquidation activity largely subsided during the final hour and 25 minutes of the day. During this period, SOL traded between $187.32 and $197.11, while only 23 additional liquidations occurred, repaying $14K in debt.

### Conclusion

Jupiter Lend processed its first major market-wide stress event with liquidations remaining small relative to its overall collateral base. Although 484 liquidations occurred, the $1.33M in collateral seized represented just 0.17% of the protocol’s starting TVL.

Liquidation activity was highly concentrated by dollar value. From 15:15–20:55 UTC, 270 liquidations repaid just $31K in debt. Following SOL’s sharpest five-minute decline, however, liquidators repaid $753K over the next 20 minutes, equivalent to 58.37% of the day’s total debt repaid.

The large difference between the $2,757 average liquidation and $52.93 median further shows that a relatively small number of large positions drove much of the event’s notional volume. Rather than producing uniformly large liquidations across the protocol, the October 10 selloff created a concentrated burst of deleveraging around the market’s sharpest price shock.

---
