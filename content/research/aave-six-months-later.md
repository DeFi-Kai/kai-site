+++
date = '2026-03-07T10:30:00-05:00'
draft = false
title = 'Aave Six Months Later'
+++

![Aave Six Months Later](/images/aave-six-months-later/aave-six-months-later-new.png)

In July 2025, we published a research report on Aave at Blocmates predicting the protocol would reach $157M in Annually Recurring Revenue (ARR). Six months later, Aave ended 2025 with a 90-day ARR of ~$160M -- ~2% above our base case target.

Full-year 2025 revenue came in at $135.2M, 86% of the base case target -- and is currently running at **$130M ARR** (90-day) in March 2026 with **$26.5B** in total value locked across all deployments and a **~63% market share**.

The original thesis was built on four catalysts: the V4 upgrade, SVR revenue growth, the Horizon instance deployment, and regulatory tailwinds from the GENIUS Act and CLARITY Act.

Since writing the initial report, Aave has been steeped in controversy with key service providers stepping down over disagreements about the DAO's direction.

This writeup will revisit the projections from the original thesis and cover what we got right, what we missed, and what it means for the road ahead.

## The revenue story

In the 2nd half of 2025, Aave experienced ebbs and flows; while developments like Horizon launched on time, the protocol's public image took a hit with the ongoing token ownership drama.

Despite the ups and downs, Aave exited 2025 with a 90-day ARR of ~$160M -- ~2% above our base case target which was $157M in ARR by December 2025.

Here are our projections from the original report in July 25':

![Revenue projections](/images/aave-six-months-later/image16.jpg)

Source(s): Token Terminal and Chaos Labs

**Here's what happened in H2 2025:**

Crypto's total market cap peaked at $4.28T in October 2025. Shortly after, the entire crypto market took a hit, dropping 30% to $3T -- a ~$1.3T decline.

![Crypto total market cap](/images/aave-six-months-later/market-cap-peak.png)

[source](https://coinmarketcap.com/charts/)

Naturally, this downwards trend bled into the lending market sector: active loans across the entire lending industry peaked in September at $44.97B but dropped to $34.99B by the end of December ([source](https://tokenterminal.com/explorer/markets/lending)).

As demand lessened throughout the entire industry it caused deposit rates to deteriorate. In July 2025, the interest rate for USDC on Aave's Ethereum deployment sat at 4.21%, but by year's end it dropped by nearly 80 basis points to 3.41%.

![Aave USDC rates](/images/aave-six-months-later/usdc-rate.png)

[source](https://aave.tokenlogic.xyz/rates)

Aave's metrics followed a similar trend: from July to September Active loans grew ~41% from ~$20.6B to $29B. But in H2 2025, active loans dropped ~28% from $29B to $21B ([source](https://tokenterminal.com/explorer/markets/lending/metrics/active-loans)).

Despite this drop, Active loans were still up 43% over the course of 2025 ($14.7B to $21B).

As a result, lending revenue across V3 and V2 (including SVR, liquidiations, and flashloans) ended the year at $152M ARR (14% above our $133M exit-ARR projection).

However, the outperformance was almost entirely driven by SVR liquidations, which made up **$20.4M of that figure** -- way above our $8M projection for the entire liquidations/SVR/other category.

GHO was a different story. The GHO supply grew roughly 141% through 2025 going from ~$150M at the start of the year to ~$361M by year-end. Impressive growth, but GHO supply still fell short of our expected $627M, with **EoY ARR for GHO falling to $7.9M**.

Across all projects, ARR reached a total of $160.2M by the end of the year.

| Stream                           | Jul-25 ARR | EoY 2025 ARR | 2025 Actual |
| -------------------------------- | ---------- | ------------ | ----------- |
| V3 (lending + liq + SVR + flash) | $86.3M     | $148.2M      | $116.5M     |
| V2 (legacy lending)              | $3.9M      | $4.0M        | $9.3M       |
| GHO                              | $9.5M      | $7.9M        | $9.4M       |
| **TOTAL**                        | **$99.7M** | **$160.2M**  | **$135.2M** |

Via TokenTerminal

## Revisiting the four catalysts

### Aave V4 launch

Status: Delayed

The [Aave V4 upgrade](https://governance.aave.com/t/aave-v4-launch-roadmap/23134), which expands Aave's capabilities and capital efficiency, was set to go live in Q4 2025. However, it's currently March 2026 and Aave V4 is yet to hit mainnet.

To date, Aave V4 has undergone multiple [audits](https://github.com/trailofbits/publications/blob/master/reviews/2026-02-aave-v4-securityreview.pdf), and recently in February 2026, [TokenLogic released a report](https://governance.aave.com/t/v4-spoke-liquidation-parameters-impact-on-revenue/23993) on the updates liquidation parameters and its impact on future revenue.

TokenLogic's report shows that liquidations under Aave V4 could generate anywhere from **$3.1M to $27.6M** depending on how the DAO configures each spoke. With this freedom they can choose to increase liquidation fees on riskier markets (spokes), compared to stablecoin markets.

While the delay of Aave V4 doesn't necessarily decrease revenue, it potentially places a ceiling on revenue growth.

### Chainlink SVR rollout

Status: Partial rollout

[Chainlink SVR](https://blog.chain.link/chainlink-smart-value-recapture-svr/) (Smart Value Recapture) is a liquidation system that redirects value from liquidations back to the DAO and users. SVR was released in December 2024, and has been slowly rolled out to support assets across Aave markets since then.

At present, SVR is configured for AAVE, ETH (and ETH LRTs), on Aave's Ethereum V3 instance.

In December 2025, Chainlink expanded coverage of SVR to Arbitrum, and Base. When Chainlink expands SVR-coverage it allows Aave to retain more fees, increasing revenue during liquidations. While there's no exact timeline of further updates, Chainlink has hinted at [support for new assets in Q1/Q2 2026.](https://governance.aave.com/t/temp-check-svr-expansion-new-markets/23524/3)

Recently in February 2026, [$202.47M in collateral was seized in a single liquidation event.](https://governance.aave.com/t/chaos-labs-risk-report-insights-from-recent-market-events-02-02-26/23986) Aave captured a total of $2.83M, 1.4% of notional liquidated value with $1.85M in revenue stemming from SVR and the remaining $980K coming from standard liquidation fees.

### Horizon RWA platform

Status: Live

Aave Horizon is an RWA protocol, launched in August 2025 developed to let institutions borrow stablecoins against RWA collateral. Since launch, the protocol has experienced mixed success.

On one hand, the protocol reached mainnet and acheived $388.67M in TVL by the end of December.

But on the other hand, the supply was attributed to a few key RLUSD whales farming incentives. In addition Horizon was positioned to be a catalyst for GHO growth, yet its the least borrowed asset with only $0.30 of GHO in outstanding loans ([source](https://governance.aave.com/t/aave-labs-86-million-23-of-the-token-supply-and-this-is-their-track-record/24159)). Horizon holds 79.5M in idle GHO, which is 15.1% of total supply and has cost Aave ~$1.05M over 5.8 months.

In other words, the user base isn't diverse, signaling unsustainable performance. In terms of revenue, Horizon has generated ~$216K, even though the protocol has spent ~$5.18M (including incentives and sGHO interest rate), since launch.

Still, this is a new development, and most protocols that go to market (GTM) require some initial bootstrapping until adoption is self-sustained. As more RWA assets are whitelisted, It's expected for the protocol to experience more usage.

### Regulatory clarity

Status: Pending

The GENIUS Act and the CLARITY Act are positioned to set a precedent for all crypto companies, especially those dealing in stablecoins.

The GENIUS Act (Stablecoin Act) was signed into law on June 18th, 2025 and is set to go into effect in December 2026 or 120 days after federal regulators issue final rules, whichever comes sooner.

This bill requires stablecoin issuers to back all stablecoins 1:1 with reserves like U.S. currency, deposits at insured institutions, or Treasury securities with maturities under 93 days. The GENIUS ACT also completely outlaws algorithmic stablecoins.

This bill provides much needed regulation but crypto startups are also finding a problem with some of its implications. Specifically, the GENIUS Act prohibits stablecoin issuers from paying interest or yield directly to holders. This has caused an ongoing debate between banks and crypto advocates, on whether third-party platforms can offer rewards on stablecoins.

The outcome of the stablecoin yield issue will largely be decided by the CLARITY Act (Digital Asset Market Structure), the bill that decides how digital assets are classified under law. The CLARITY Act passed the house, but is still awaiting a senate vote. At present, banks are attempting to use the CLARITY Act to close the "Stablecoin Yield Loophole", to stop platforms like Coinbase from offering interest on stablecoins issued by other providers.

Whether or not banks successfully close this loophole will have a direct impact on Aave's core business. Aave allows users to deposit regulated stablecoins like USDC and USDT and earn interest from borrowers, which is essentially third-party yield. If banks can succesully implement a broad yield ban it could create legal risk for the protocol's interaction with these regulated payment stablecoins.

GHO, Aave's stablecoin is a separate matter. As a decentralized, overcollateralized stablecoin minted against crypto collateral and governed by a DAO, it doesn't fit the GENIUS Act's definition of a payment stablecoin. But, the CLARITY Act could potentially introduce broader definitions and frameworks that touch decentralized stablecoins like GHO.

**What should you monitor?:** The CLARITY Act's senate vote and final language. Pay attention to whether banks succeed in closing the third-party yield loophole, which would directly threaten Aave's core lending business. In addition, watch whether the CLARITY Act's digital asset definitions extend to decentralized stablecoins like GHO.

### Key DAO developments & Business Operations Events

Aave has experienced controversy over the last few months. Aave Labs and the DAO's service providers are in a power struggle over evenue allocation, brand ownership, and the protocol's future direction.

The conflict escalated through a series of governance disputes that ultimately led to the departure of BGD Labs (the team responsible for Aave V3 upgrades) and ACI (Aave Chan Initiative).

Below, I detail the rough timeline of events over the last few months in Aave's operations:

1. **March 13, 2025:** Aave Labs proposes [a new token with Horizon](https://governance.aave.com/t/temp-check-building-horizon-s-rwa-product-an-aave-licensed-instance-for-institutions/21384)
2. **December 11, 2025:** Community member EzR3aL [raises a discussion](https://governance.aave.com/t/aave-cowswap-integration-tokenholder-questions/23530) on why fees from a new CoW Swap integration were being routed to Aave Labs instead of the DAO treasury
3. **December 21, 2025:** [BGD Labs proposes](https://snapshot.org/#/s:aavedao.eth/proposal/0xbc606159ddeae0184c2086055637d3f357351ec0adc4c9f4150751bc41918eba) transferring control of Aave's brand assets -- including domains, trademarks, and social accounts -- to the DAO, removing ownership from any single service provider
4. **February 12, 2026:** Aave Labs proposes the [Aave Will Win framework](https://governance.aave.com/t/temp-check-aave-will-win-framework/24055), requesting $51M in funds from the DAO treasury
5. **February 17, 2026:** Marc Zeller, head of ACI, releases [a public audit](https://x.com/Marczeller/status/2023811473055904253) of ACI's budget and return on investment
6. **February 20, 2026:** [BGD Labs announces its departure](https://governance.aave.com/t/bgd-leaving-aave/24122) from Aave
7. **February 24, 2026:** [Aave Labs publishes an audit](https://governance.aave.com/t/aave-labs-contributions-report/24155) of their costs and expenses
8. **February 25, 2026:** ACI responds with their own [audit of Aave Labs' work](https://x.com/AaveChan/status/2026570638941728850)

Currently, the DAO has passed the Aave Will Win Snapshot, and is set to move the proposal to an official onchain vote. When it surfaced, this proposal was a major point of contention, and its support from Aave Labs is what essentially led to the departure of BGD Labs and ACI. However, the proposal hasn't undergone an official onchain vote, and Aave Labs members are reportedly making amendments to the original proposal with plans to launch it in phases.

### Closing Thoughts

From a revenue standpoint, Aave (led by Aave V3) has performed exceptionally over the last few months, even with the delay of Aave V4. Aave grew its revenue 57% YoY in 2025 and maintained its position as the dominant lending venue.

However, the recent controversy has raised questions, and for good reason. Is a DAO structure sustainable? What are the downsides of decentralizing business operations? Specific to Aave: what is the fate of the protocol and its relationship with service providers?

These are all valid questions, but the most important thing to keep in mind is that Aave is making history, for better or for worse.

This is one of the first times we've seen a DAO and its service providers disagree on such a big stage. The outcome of this situation will set a precedent for other DAOs and onchain organizations, and the way they structure their operations.

In hindsight: it was a mistake to evaluate Aave as one entity, when the fragmented DAO and delegation structure complicates operations and is now posing a risk -- albeit short term -- to the outlook on the protocol.

Still, I believe Aave's distribution and liquidity to be its biggest moat, even with the likes of Morpho gaining traction. If you're interested in Aave, some key metrics to watch are:

Market share by outstanding loans

{{< chart src="/data/aave-six-months-later/outstanding-loans-marketshare.csv" type="area" title="Outstanding Loans Market Share" stacked="true" height="420px" ymin="0" ymax="100" >}}

Total Revenue by lending protocol

{{< chart src="/data/aave-six-months-later/lending-revenue-marketshare.csv" type="area" title="Lending Revenue (Daily, USD)" stacked="true" height="420px" >}}

Marketcap / Outstanding Loans

{{< chart src="/data/aave-six-months-later/mcap-to-outstanding-loans.csv" type="line" title="Mcap / Outstanding Loans" height="420px" >}}
