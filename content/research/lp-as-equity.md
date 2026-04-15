+++
date = '2026-04-15T09:00:00-04:00'
draft = false
title = 'LP-as-Equity'
+++

The default assumption in crypto is that the token is the equity. But, for perp DEXs, the LP is what equity actually looks like.

LPs have a direct, mechanical claim on protocol revenue, including fees, spread, and liquidation penalties. LP revenue compounds into share price without needing a buyer on the other side. In contrast, tokens require someone else to bid.

Over the past year, Perp DEX LPs have returned -1% to 46% while most of their corresponding tokens are down 45% to 58%.

The market effectively pays a liquidity premium for the worse-performing asset.

## LP-as-Equity: Why the LP earns its fees

Perp DEXs are structurally credit systems where LPs loan capital to leverage traders. In return, share prices increase as the vault earns revenue (spread, funding, fees, etc.). But, LP profitability is ultimately determined by order flow.

As the direct counterparty to traders, LPs absorb the directional risk of every position. For that reason, it is in the protocol's best interest to attract uninformed flow and resolve toxic flow.

The vault's design, including pricing, oracles, and execution, is the operational moat that mitigates toxic flow and turns the credit exposure into positive edge.

Let's consider Hyperliquid. The HLP vault's quoting logic sets the spread, which is effectively the protocol's take rate. In times of volatility, the vault widens the spread to reduce the vault's exposure to adverse selection. In addition, Hyperliquid uses private oracles to perform timely liquidations and reduce latency arbitrage.

Each LP carries design trade-offs that balance trader execution quality and vault profitability. In this way, an LP's design is essentially the underwriting criteria which reflect the risk-return profile.

Comparing the performance across 5 USDC-based LPs since December 2025 demonstrates the gaps in risk-adjusted efficiency from one strategy to another. More volume and better risk-management translate to lower MDDs, higher Sharpes, and overall higher yields.

{{< img src="images/lp-as-equity/lp-comparison-bsc-dec2025-2026-04-13.png" alt="Comparison chart of USDC-based perp DEX LP performance" >}}

*Sources: Dune, Lighter API, Hyperliquid.*

While HLP and OLP returned 6-7%, HLP demonstrated better operational efficiency. HLP achieved a Sharpe of 1.39 and MDD of -0.5%, compared to OLP which recorded a Sharpe of 0.84 and MDD of -6.2%. In other words, OLP experienced 26% more volatility and still returned less than HLP.

In comparison, gUSDC, ALP, and LLP resembled cash-plus instruments the most, yielding around 3% with sub-2% volatility.

Because value accrues mechanically without needing a buyer, the LP is structurally a better claim on protocol revenue than the token. And because the LP underwrites the risk the protocol runs on, it is the instrument that actually earns its fees.

The token has to justify its cut some other way.

## Why most tokens don't earn their fees

Value capture is only justified if the token does a job no other instrument can do (underwriting risk, securing an L1, etc.). With a real job, fees reinforce the function: each dollar that accrues gives holders more reason to hold. Without one, fees are extractive.

For Perp DEXs, the instrument actually managing risk is the LP. This leaves the token with little claim on the fees it takes.

To date, the majority of projects have used tokens for airdrops. While it has been an effective strategy for Perp DEXs, it comes at the cost of subsidizing customer acquisition with tokens. After the airdrop, if the token has no function in the system, there is no value for it to capture.

To justify long-term value capture in a risk system, the token must take part in risk management.

Some Perp DEXs allow tokenholders to vote on high-level parameters like market listings and fee splits. Meanwhile, the team is responsible for actively managing the operational layer where the platform's edge is actually produced. This includes quoting, hedging, and oracle choice.

Moreover, during time-sensitive emergencies like exploits, the internal team makes decisions among themselves. As an example, the Hyperliquid team froze trading and executed trades to avoid a roughly $14M hit to the protocol during the JELLY-JELLY exploit.

In tight situations, decentralized governance takes a back seat. The most vital decisions are often managed by a small group of specialists and service providers.

Teams have experimented with tokens to backstop risk, but the mechanism breaks down in high-leverage venues like Perp DEXs. The reason is reflexivity.

When the backstop kicks in, selling pressure drops the token price. The lower token price means each new loss requires more tokens to cover the same dollar amount. The backstop only works if the token can absorb losses without its own price collapsing faster than the losses arrive.

As an example, during the Terra/Luna crash, traders placed LUNA shorts on Gains causing stress to the LP. To limit losses, Gains' backstop kicked in which sold GNS over three days (05.11-05.13), during which the market cap dropped from $47m to $21m, forcing them to pause GNS minting.

Without a defined job for the token, mechanisms like fee switches and buybacks become inefficient. Each of these mechanisms require a secondary buyer to hold the token for the value to hold. If nobody holds, value leaks to sellers.

Tokens direct incentives away from the LP and cost the project more dilution.

## LP vs. token performance

The structure of LPs allows them to capture and retain value more efficiently than governance tokens. The LP reprices in real time based on fees, trader PNL, and liquidation revenue which flow directly into the NAV.

In comparison, tokens require buyers for the price to increase. Tokens are also exposed to sentiment and narrative which affect their ability to retain value long term.

This trend becomes clear when we compare Perp DEX tokens to their LPs over the last 12 months.

| Platform         | Token | Token Delta (12m) | Token MDD | Token Sharpe | LP                 | LP Delta (12m) | LP MDD | LP Sharpe |
| ---------------- | ----- | ----------------- | --------- | ------------ | ------------------ | -------------- | ------ | --------- |
| Hyperliquid      | HYPE  | +183%             | -64%      | 1.51         | HLP                | +23%           | -0.8%  | 1.49      |
| Jupiter Perps    | JUP   | -54%              | -78%      | -0.42        | Jupiter LP (JLP)   | -1%            | -41%   | -0.01     |
| Lighter          | LIT   | -58% (<1y)        | -         | -            | Lighter LP (LLP)   | +46%           | -5.3%  | 3.63      |
| Gains (Arbitrum) | GNS   | -45%              | -71%      | -0.33        | Gains USDC (gUSDC) | +10%           | 0%     | 12.39     |

*Sources: CoinGecko, Dune, Lighter API, Hyperliquid.*

Across the set, LPs experienced less volatility and outperformed their tokens, except for HYPE.

Hyperliquid is an example where each instrument earns its keep. The HYPE token secures the L1 and the orderbook, and the LP underwrites risks.

Hyperliquid directs 40% of platform fees to HYPE buyback-and-burn, and 20% are routed to HLP. Demand from builder codes and new HIP-3 markets reinforces HYPE's role as the platform's fee sink.

Over the last year, HLP's share price grew 23%, compared to HYPE's price, which increased by 183%. Still, HYPE experienced more volatility recording a max drawdown (MDD) of 64% compared to HLP's MDD of 0.8%.

{{< img src="images/lp-as-equity/hlp-vs-hype-chart-2026-04-13.png" alt="HLP versus HYPE performance chart" >}}

*Sources: CoinGecko, Hyperliquid.*

Tokens and LPs are essentially priced as claims on the same revenue through different channels. To see how the market prices these cash claims, we compare token vs. LP P/S on Gains, Hyperliquid, Avantis, and Jupiter, the 4 protocols with clean data on fees and FDV.

To calculate P/S:

- **Token P/S** = Token FDV / (token's fee share x trailing-12-month fees)
- **LP P/S** = LP TVL / (LP's fee share x trailing-12-month fees)

While token P/S tells us what the market is willing to pay for a dollar claim on token revenue, LP P/S reveals the capital commitment per dollar claim on LP revenue.

A high LP P/S means the vault is well-funded relative to fees, signaling low forward fee yield. Similar to equity-style dilution, each new deposit dilutes fee-per-share until volume and fees grow. In the past, Hyperliquid has even capped deposits when the multiple gets too high.

Comparing the two ratios tells us how the market values sentiment-driven token revenue versus the fee-linked LP claim.

| Platform         | Token P/S | LP P/S | Token vs. LP P/S ratio |
| ---------------- | --------- | ------ | ---------------------- |
| Hyperliquid      | 94.6x     | 2.0x   | 46.4x                  |
| Jupiter Perps    | 4.5x      | 3.4x   | 1.3x                   |
| Avantis          | 24.3x     | 4.9x   | 5.0x                   |
| Gains (Arbitrum) | 2.7x      | 7.4x   | 0.37x                  |

*Sources: CoinGecko, Dune, Avantis analytics, Hyperliquid.*

Notably, Gains' token-to-LP P/S ratio sits at 0.37x, meaning the market values the LP's claim on fees more than the token's. This signals misaligned incentives.

Gains' token, GNS, is fully diluted with a $17m marketcap. Gains directs around 60% of total trading fees to GNS buybacks and 15% to gVault LPs.

Over the last year, the team spent around $6m in buybacks. Meanwhile, the GNS token is down 45% with an MDD of around 71%, compared to gUSDC which increased by 10% with no drawdowns.

{{< img src="images/lp-as-equity/gains-gusdc-vs-gns-chart-2026-04-13.png" alt="gUSDC versus GNS performance chart" >}}

*Sources: CoinGecko, Dune.*

Gains directs the majority of fees to GNS, yet the market is not pricing GNS positively on its claim on revenue. Projects that direct fees to the token (via buyback) over the LP are actively subsidizing token growth instead of rewarding the equity that runs the platform.

Similarly, Jupiter's LP outperformed its token despite more fees routed to token buybacks.

Jupiter is a DeFi stack on Solana. It runs a lending market, aggregator, and perps. The team directs 60% of total fees across the product suite to JUP buybacks. JLP earns 75% of fees from the perp product, with the remaining 25% going back to the DAO.

The JLP pool is an index including SOL, BTC, ETH, and USDC, that provides liquidity to traders. The price of JLP is exposed to the price movements of the underlying basket, on top of the existing counterparty risks.

Over the last year, the pool earned $384m in fees plus trader PNL, helping it outperform the raw index (BTC, SOL, ETH) by 18%. During this period JLP decreased by around 1%, compared to the JUP token, which dropped by around 50%.

{{< img src="images/lp-as-equity/jupiter-jlp-vs-jup-chart-2026-04-13.png" alt="JLP versus JUP performance chart" >}}

*Sources: CoinGecko, Dune.*

## Closing thoughts

Until projects give the token a job it alone can do, capital should flow to the instrument that actually earns its fees.

Perp DEXs will increasingly reach retail through mobile front-ends. As they do, LP designs (MM, oracles, liquidations, etc.) will have more at stake to manage. Tokens with fee shares, including staking rewards and buybacks, redirect revenue away from the risk-management engine.

Teams that can solve fundraising and marketing without a token can sidestep this problem entirely. Securitize and Flashbots are both examples. Presently, out of the top ten Perp DEXs by open interest (OI), seven are tokenless. Each one has the option to keep compounding the LP rather than print a separate claim on the same fees.

The obvious objection is that much of the OI is farming for expected airdrops. This is fair pushback, and it is exactly the point. If the token's job is to subsidize user acquisition, then it is a marketing budget.

It is also a liquidity vehicle. Founders launch tokens partly for the VC and team to have the optionality to sell tokens OTC or to the market. This is a function the LP cannot serve.

The market pays a liquidity premium for the token and a liquidity discount for the LP. The people who can access the LP earn the premium.

Perp DEX tokens are a marketing budget. The LP is the equity.

---

Sources and methodology: [LP-as-Equity sources and methodology](https://github.com/DeFi-Kai/lp-as-equity-sources)
