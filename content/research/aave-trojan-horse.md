+++
date = '2025-08-02T09:00:00-04:00'
draft = false
title = 'Aave: The Bank of DeFi'
slug = 'aave-the-bank-of-defi'
aliases = ['/research/aave-trojan-horse/']
+++

*This report was originally published on [Blocmates](https://x.com/blocmates/status/1951422453734953348).*

---
Aave has grown to become DeFi’s Trojan Horse, reaching a scale comparable to traditional banks. With $35 billion in TVL and $57 billion in net deposits, it now controls 25% of DeFi TVL and ranks among the 50 largest US banks by assets under management (AUM).
{{< img src="images/aave-the-bank-of-defi/image11.jpg" alt="Aave chart" >}}

In 2024, the protocol made $86M in revenue (a 280% YoY increase). As of July 2025, annualized revenue is ~ $100M, but with upcoming catalysts like Aave V4, Chainlink SVR's full rollout, Horizon adoption, and improving U.S. regulation, they have the **potential to reach $150M+ in ARR by year-end.**   
{{< img src="images/aave-the-bank-of-defi/image19.jpg" alt="Aave chart" >}}

Here's how Aave plans to scale:

1. **Aave V4** will enable markets for RWA and long-tail assets with increased capital efficiency through network-specific liquidity hubs.   
2. **Chainlink SVR** on all V3 markets will allow Aave to capture a percentage of multi-million dollar liquidations every month.   
3. **Horizon** gives Aave the regulatory arm to tokenize RWAs and issue loans in **GHO**, further boosting revenue.   
4. **The Stablecoin Act** and **CLARITY Act** will ease the regulatory landscape and promote stablecoin adoption, reducing friction for Aave V4 market deployments and GHO minting. 

{{< img src="images/aave-the-bank-of-defi/image12.jpg" alt="Aave chart" >}}

As attention slowly shifts back to revenue-generating protocols, Aave is a top contender as **the bank of DeFi**. 

This report outlines the roadmap that could bring Aave to $150M+ in annual revenue within the next year, and potentially 5x revenue growth within three years. 

## The Aave Vision

Aave has emerged as the most trusted protocol to earn yield on idle capital. As of July 2025, they've captured $35B in TVL, a 96% YoY increase. That deep liquidity attracts integrations and asset listings which drive more deposits and strengthen Aave's flywheel. 

{{< img src="images/aave-the-bank-of-defi/image17.png" alt="Aave chart" >}}
[source](https://defillama.com/protocol/aave)

When developers and asset issuers build on Aave, they tap into its infrastructure, active users, and deep liquidity. In return, Aave collects fees and expands its footprint across DeFi.

For developers, aTokens function as interest-bearing ERC-4626 vaults that are easy to integrate into external products. Protocols like Morpho, Beefy Finance, and Balancer use these vaults to support millions in user deposits through their own interfaces.

For asset issuers, listing on Aave extends utility for token holders by giving them a place to borrow against their assets. For example, in May 2025, Pendle listed PT-sUSDe on Aave V3 (Ethereum) and attracted $1.47B in deposits in under two months.

{{< img src="images/aave-the-bank-of-defi/image25.jpg" alt="Aave chart" >}}

Additionally, these kinds of listings continually position Aave as a global money market. Particularly, each new asset listing enhances rate differentials which presents FX-like trading opportunities. Here are a few examples: 

- **USDC, DAI, PYUSD, USDe, EURC:** Enables synthetic FX trades between USD-pegged and euro-denominated stablecoins.  
- **Pendle ptTokens:** Integrate rate markets with Aave by letting users post future yield as collateral.  
- **Staked Ethereum & Restaked Bitcoin:** Offer carry trade opportunities based on staking and restaking yield differentials.  
- **SyrupUSDC (TBA):** Unlocks arbitrage opportunities across decentralized lending venues.

{{< img src="images/aave-the-bank-of-defi/image14.png" alt="Aave chart" >}}
[source](https://app.aave.com/markets/?marketName=proto_mainnet_v3)

With over 40 listed assets on Ethereum Core and $35B in TVL, each addition strengthens Aave's network effect. This dynamic attracts builders, helping Aave stay at the center of DeFi's economic activity. Today, it accounts for over 64% of lending market share by TVL.

{{< img src="images/aave-the-bank-of-defi/image24.png" alt="Aave chart" >}}
[source](https://tokenterminal.com/explorer/projects/aave/metrics/tvl)

In the past 90 days, Aave has been generating revenue at an annualized rate of roughly $100M, coming from the following sources:

- **Aave V2 & V3 (~88%):** Around $88M from lending and borrowing markets across EVM chains.  
- **GHO (~10%):** About $10.4M from borrowing demand for Aave's overcollateralized stablecoin.  
- **Other (~3%):** A mix of liquidation fees, treasury yield from aTokens, and smaller revenue streams.

Marc Zeller, founder of the [Aave Chan Initiative (ACI)](https://www.aavechan.com/#shaping) an Aave DAO delegate, has proposed a roadmap targeting 5× revenue growth, led by GHO and RWAs. Based on current traction, I estimate that roughly 20% of that plan could be achieved by year-end, **bringing ARR to $150M+.**  

{{< img src="images/aave-the-bank-of-defi/image16.jpg" alt="Aave chart" >}}
Source: Token Terminal

To complement its growth strategy, the Aave DAO has also launched a buyback program starting with $24M over six months. If they maintain this pace it could scale to $48M, potentially removing ~1% AAVE supply from circulation. As of now, the DAO has already bought back $14M (65k $AAVE).

{{< img src="images/aave-the-bank-of-defi/image9.png" alt="Aave chart" >}}
[Source](https://aave.tokenlogic.xyz/buybacks)

To drive revenue expansion and support initiatives like ongoing buybacks, several catalysts are in play:

- **Aave v4:** A major upgrade designed to increase capital efficiency and risk modularity.  
- **Chainlink SVR full rollout:** Captures MEV from liquidations across all V3 markets.  
- **Horizon adoption:** Accelerates GHO issuance through real-world asset integration.  
- **Regulatory clarity:** Tailwinds from legislation like the Stablecoin Act and CLARITY Act could unlock new participation from institutional capital.

## Aave V4 upgrade

Aave V4 allows multiple markets to exist on the same network. Each market can be tailored to specific asset types, including long-tail tokens, RWAs, and assets that trade at parity. This improves capital efficiency and makes it easier to support novel lending structures and a wider range of collateral.

{{< img src="images/aave-the-bank-of-defi/image13.png" alt="Aave chart" >}}

[source](https://www.youtube.com/watch?v=veoALQrKOkE)

Currently, in Aave V3, each blockchain is limited to a single market (with the exception of Ethereum Prime and Core) with its own isolated liquidity pool and asset mix. This makes it harder to support novel assets or implement unique borrow configurations.  

{{< img src="images/aave-the-bank-of-defi/image5.png" alt="Aave chart" >}}
[source](https://aave.com/blog/understanding-aave-v4s-architecture)

**Aave V4 solves this through a new architecture built around Spokes and Liquidity Hubs.**

**Spokes** are individual markets with their own risk parameters that connect to a shared **Liquidity Hub** on each chain. This structure results in higher loan-to-value ratios and tighter spreads. New Spokes can be deployed using existing liquidity from the hub, with the option to introduce new assets, removing the friction of seeding new markets. 

{{< img src="images/aave-the-bank-of-defi/image18.png" alt="Aave chart" >}}
[source](https://aave.com/blog/understanding-aave-v4s-architecture)

V4 also introduces Vault Spokes, which allow users to borrow from isolated vaults without supplying collateral directly to Aave. Instead, users can connect a [Gnosis Safe](https://www.youtube.com/watch?v=veoALQrKOkE) to an Aave Smart account, which locks funds for the duration of the loan. This makes it possible for a DAO to keep its treasury assets in a Gnosis Safe and still borrow stablecoins from Aave without moving those assets into the protocol.

The Spoke-and-Hub model has the potential to significantly increase Aave's TVL and lending activity. By enabling more flexible risk parameters, it could support a wider range of asset listings, including riskier tokens like memecoins, for example. If Aave were to capture even 15% of the memecoin market, currently valued at around $73B, that would add ~$10B in additional supply. This could push active loans to roughly ~$33B, generating an estimated $125M in annual lending revenue.

Aave V4 also benefits from existing development upgrades aimed at protecting and growing protocol revenue. **Chainlink's Secure Value Relay (SVR)** integration returns liquidation auction revenue back to the protocol, while **Aave Umbrella** provides a safety buffer for bad debt and insolvency. 

### Chainlink SVR: Capturing liquidation MEV as revenue 

Over the past few years, Aave has generated several million dollars annually from liquidations. When a position is liquidated, the protocol applies a [liquidation bonus](https://governance.aave.com/t/arfc-aave-chainlink-svr-v1-phase-1-activation/21247/6?u=chaoslabs) allowing it to retain a small percentage of the collateral as revenue.

 {{< img src="images/aave-the-bank-of-defi/image20.png" alt="Aave chart" >}}
 [Source](https://aave.com/docs/resources/parameters)

In August 2024, massive ETH selloffs triggered $234M in liquidations. Aave retained $2.1M from this event ( ~1% of the liquidated capital).

With Chainlink SVR now live, Aave could capture an additional ~2 % of every liquidation. SVR enables Aave to capture a share of Oracle Extractable Value (OEV), the MEV that arises when liquidations are triggered based on lending markets.

SVR introduces an auction mechanism where searchers compete for the right to execute the liquidation. Instead of leaking to external arbitrageurs, this value is routed back to the protocol.

Aave now receives 64% of the auction proceeds. In the August 2024 example, this would have turned a $2.1M revenue event into $6.6M, nearly tripling the earnings from the same liquidation activity.  

{{< img src="images/aave-the-bank-of-defi/image15.jpg" alt="Aave chart" >}}
[source](https://blog.chain.link/chainlink-smart-value-recapture-svr/)

Currently, SVR is enabled for only 6 assets on Aave V3 limiting its impact. For instance, over the last 90 days, Aave captured just $88K from $4.4M in liquidations (about 2%).

{{< img src="images/aave-the-bank-of-defi/image8.png" alt="Aave chart" >}}
[Source](https://community.chaoslabs.xyz/aave/risk/svr/liquidations)

If SVR had been enabled across all Ethereum V3 markets during the same 90-day period (which saw $24M in liquidations) Aave would have earned $560K in OEV revenue. Annualized, that's $2.2M. When combined with standard liquidation bonus fees, total liquidation revenue could reach $6-8 million per year.  

{{< img src="images/aave-the-bank-of-defi/image10.png" alt="Aave chart" >}}
[Source](https://dune.com/KARTOD/AAVE-Liquidations)

As discussed in [Aave's phase 1 Chainlink SVR proposal](https://governance.aave.com/t/arfc-aave-chainlink-svr-v1-phase-1-activation/21247?u=chaoslabs) in March 2025, a full rollout across Ethereum V3 is expected if the test deployment performs well.

### Umbrella Safety Module: yield and risk management

Lending markets face handling shortfall events like bad debt. Aave's Umbrella safety module addresses this by creating protection pools that support risk management while offering yield.

Users can supply GHO or aTokens for boosted yield. Each pool includes a deficit offset buffer, which reduces the likelihood of slashing user funds. For instance, USDT staking has a 100k USDT offset, which means events must exceed $100K in USDT for user funds to be slashed.   

{{< img src="images/aave-the-bank-of-defi/image6.jpg" alt="Aave chart" >}}

As Aave brings in more institutional capital, the Umbrella module adds a scalable way to manage risk and protect user confidence during market stress.

## Horizon: bridging RWA markets with GHO

Aave Labs' Horizon is a real-world asset (RWA) issuance platform that allows institutions to tokenize RWAs and borrow stablecoins like GHO or USDC on Aave.

Aave's earlier attempt to onboard institutions, Aave Arc, fell short due to its permissioned structure, which restricted access from the liquidity of Aave's main markets. While forward-thinking firms such as [New Silver](https://newsilver.com/the-lender/new-silver-expands-financial-offerings-by-partnering-with-aave/) (real estate), [Sygnum](https://www.sygnum.com/news/sygnum-launches-first-phase-of-institutional-grade-access-to-decentralised-finance/) (Swiss bank), and [Wintermute](http://binance.com/en/square/post/25244375559562) (market maker) have used Aave, overall institutional adoption has remained limited.

In response, Aave Labs introduced Horizon, a more flexible framework that enables institutional access with offchain legal structure, regulatory coordination, and whitelisted liquidations.   

{{< img src="images/aave-the-bank-of-defi/image23.jpg" alt="Aave chart" >}}
Through Horizon, institutions can tokenize RWAs such as money market funds (MMFs) or real estate and tap into Aave to borrow stablecoins with configurable access controls.

{{< img src="images/aave-the-bank-of-defi/image4.png" alt="Aave chart" >}}
[Source](https://governance.aave.com/t/temp-check-horizon-s-rwa-instance/21740)

Horizon will support two facilitators for stablecoin lending:

1. **USDC and GHO:** Loans for qualified users, gated by the RWA issuer.  
2. **GHO Facilitator:** Allows institutions to mint GHO using RWA collateral.

The GHO facilitator will launch with an initial cap of 1 million GHO, offering institutions access to stablecoin loans at near-fixed rates.

Aave's latest proposal also includes 50% profit-sharing with the Aave DAO for Year 1 of Horizon revenue. If Institutions mint $700M in GHO through Horizon (raising total GHO supply to $1B), Aave could generate $28M in revenue. The DAO would receive half ($14M), adding to its existing $10M in GHO revenue, bringing total GHO revenue for the DAO to $24M.

### GHO: the stablecoin wrapper for RWAs

GHO is Aave's overcollateralized stablecoin. Users can deposit assets into Aave and borrow (mint) GHO, with the protocol collecting interest fees. 

As of now, GHO has a market cap of $313M, generating $12M in ARR. While still a fraction of Aave's total, each GHO minted brings in 10× more revenue than $1 borrowed on Aave. In other words, Aave has a strong incentive to scale GHO.  

{{< img src="images/aave-the-bank-of-defi/image2.png" alt="Aave chart" >}}
[source](https://community.chaoslabs.xyz/aave/risk/GHO/overview)

With Aave V4 and the Horizon RWA initiative, institutions will be able to mint GHO against tokenized RWAs. This positions GHO as a settlement layer that bridges permissioned collateral with permissionless liquidity.

To accelerate growth, the Aave DAO is working with Aave Labs to deploy $1M in incentives (in $AAVE), likely aimed at kickstarting GHO borrowing.

These incentives, combined with discounted rates, are expected to attract early institutional demand, but native yield options will give them reasons to hold GHO, not just borrow it. 

Unlike stablecoins like USDS (formerly DAI), GHO users earn interest on their deposited collateral. GHO can also be lent into permissionless pools or staked as sGHO, allowing institutions to earn yield while helping backstop GHO's solvency.

Today, GHO is backed primarily by ETH and BTC, with a collateralization ratio above 150% throughout 2025.   

{{< img src="images/aave-the-bank-of-defi/image1.png" alt="Aave chart" >}}
[source](https://community.chaoslabs.xyz/aave/risk/GHO/overview)

As Horizon expands, RWA collateral like U.S. Treasury bonds will diversify that backing, bringing GHO structurally closer to stablecoins like USDC or USDT.

Yet, GHO has better economics. For example, with a $10B market cap, USDC generates around $260M annually for Circle. In comparison, GHO could generate $400M at the same scale.

{{< img src="images/aave-the-bank-of-defi/image26.png" alt="Aave chart" >}}

This revenue efficiency gives Aave a path to scale faster. If GHO reaches multi-billion scale, it could emerge as a "global money market dollar": a stablecoin backed by crypto and RWAs, offering institutions access to permissionless, yield-bearing liquidity.

## Regulatory tailwinds

Under President Trump, U.S. policy toward crypto has become more supportive. Upcoming legislation such as the Stablecoin Act and the CLARITY Act will provide regulatory... umm, clarity... for stablecoins potentially leading to increased use of Aave. 

The **Stablecoin Act** formalizes reserve requirements for stablecoin issuers. This could drive broader adoption and deeper stablecoin liquidity positioning Aave as the venue for depositing stablecoins to earn yield.

However, the stablecoin act prohibits stablecoin issuers from paying interest directly to holders. As written, this presents a challenge for sGHO, since Aave DAO is both the issuer of GHO and the source of its savings rate. This could potentially prevent U.S. users from using sGHO. 

**The CLARITY Act** offers a possible workaround. It exempts permitted stablecoins and digital commodities from SEC oversight and provides safe harbor for DeFi protocols. This gives Aave the flexibility to route yield through a third-party wrapper or facilitator vault that pays out protocol fees without triggering a broker registration. 

It's important to note, the Stablecoin Act's interest ban will not be enforced until regulators complete the rulemaking process, which is expected in late 2026. This gives Aave an 18-month window to launch, and test a compliant sGHO structure before penalties kick in.

The bottom line: with favorable regulation and the launch of Aave Horizon, it **removes the main regulatory blocker** allowing Aave to onboard institutions directly into its core markets. This regulatory shift could help unlock the path to Aave's projected 5× growth, bringing protocol revenue to an estimated $500M over the next three years.

## Aave's Bear Case

Aave remains the largest lending protocol by TVL, but it faces growing pressure from smaller, faster-moving competitors like Morpho, Euler, and Maple.

Some of these competitors, like Morpho, are building directly on top of Aave's infrastructure. While this may seem symbiotic, it introduces a structural risk:  
Aave increasingly becomes a wrapper layer for execution. If these external protocols capture more fees than Aave itself, it may affect the protocols bottom line.

At the same time, Aave's absence from sectors like RWAs adds to the pressure. Private credit grew by 77% YoY, from $8.5B in July 2024 to $15.1B in July 2025, without Aave horizon's participation.   

{{< img src="images/aave-the-bank-of-defi/image3.png" alt="Aave chart" >}}
[source](https://app.rwa.xyz/private-credit)

To catch up, the success of Aave Horizon is critical. It must meaningfully drive GHO adoption and encourage institutions to mint GHO over alternatives like USDC. If not, Aave risks missing out on a more lucrative source of revenue compared to borrowing interest.

Another concern is Aave's correlation with Ethereum. Roughly 40% of Aave's TVL is held in ETH, and 90% of its TVL resides on the Ethereum network. Could lead to sharp drops in Aave's TVL when ETH's price declines. 

{{< img src="images/aave-the-bank-of-defi/image7.png" alt="Aave chart" >}}
[Source](https://portfolioslab.com/tools/stock-comparison/AAVE-USD/ETH-USD)

From a price performance perspective, ETH has consistently outperformed AAVE, raising the question of whether holding ETH is a more efficient way to gain exposure to Aave's ecosystem. Unless Aave can capture value from assets outside of ETH, it may remain overshadowed by the asset it relies on most.

In a bear case scenario, these dynamics may not collapse Aave's core business, but they could cap upside and slow growth. 

## Closing Thoughts

Aave's deep liquidity and composable infrastructure have created a self-reinforcing flywheel that strengthens its role as the Bank of DeFi.

Peer protocols increasingly seek asset listings or integrations with Aave to access its liquidity, ensuring that Aave continues to capture value from economic activity across the broader DeFi ecosystem.

The $AAVE token is already listed via [a 21Shares ETP](https://global.morningstar.com/en-gb/investments/etfs/0P0001OI9B/quote) and could become a candidate for a crypto ETF as regulatory clarity improves.

To stay ahead of competitors and outperform broader networks like Ethereum, Aave will need to:

- Activate Chainlink SVR across all V3 markets  
- Launch Aave V4, enabling modular and capital-efficient market design  
- Scale Horizon, bringing institutional flows into GHO

With $100M ARR, and $4.4B market cap, Aave currently trades at a ~44× EV/Revenue multiple, a premium valuation that reflects its strong fundamentals and position in DeFi. 

**If Aave scales to $150M+ in ARR, even with a multiple compression to ~37× a $5.5B valuation is possible.**

If Aave executes across GHO, SVR, and Horizon, revenue could surpass $250M by 2026. With moderate multiple compression (32×), this would support a valuation of $8B.
