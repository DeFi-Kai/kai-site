+++
date = '2026-05-19T12:30:00-04:00'
draft = false
title = 'Unpacking the Superapp Stack'
+++

{{< img src="images/superapp-stack/robinhood-vs-hyperliquid-1.png" alt="Robinhood vs Hyperliquid chart 1" >}}

Over the past year, trading platforms like Robinhood, Bybit, and Kraken have rolled out onchain protocols to extend their product offerings. By tapping into decentralized protocols they're able to deliver new services at scale, ranging from tokenized equities to non-custodial trading.

As this trend continues, the competition between Web2 and Web3 is converging into a race to build **Superapps**: platforms that combine mobile-first distribution with blockchain infrastructure.

{{< img src="images/superapp-stack/robinhood-vs-hyperliquid-2.png" alt="Robinhood vs Hyperliquid chart 2" >}}

Mobile-first apps like **Robinhood** start from the top down: It already commands retail distribution and is now building on Arbitrum rails underneath to extend its product suite onchain. In contrast, **Hyperliquid** runs the opposite playbook: It specializes in perp infrastructure and lets other frontends - mobile or web - plug in through Builder Codes.

The projects that win will dominate at least one layer of the stack. The strongest will capture value from both.

{{< img src="images/superapp-stack/robinhood-vs-hyperliquid-3.png" alt="Robinhood vs Hyperliquid chart 3" >}}

This report compares how Robinhood and Hyperliquid are approaching this challenge and building on the Superapp stack.

## The Superapp stack

Today's marketplace of DeFi protocols gives app developers access to plug-and-play financial primitives.

Phantom wallet routes user swaps through Jupiter aggregator. It offers in-app perps trading via Hyperliquid. Binance Exchange packages yield products using BNB Chain protocols like Solv.

As a result, it's becoming useful to identify projects by what they own:

- **Distribution.** Mobile-first apps that own the user. Examples: Binance Exchange, Robinhood, Phantom.
- **Composable rails.** Blockchain infrastructure that apps plug into. Examples: Uniswap Hooks, Hyperliquid Builder Codes, Aave API, Pendle SDK.

{{< img src="images/superapp-stack/Drawing-2026-05-19-12.35.55.excalidraw.png" alt="Superapp stack diagram" >}}

Teams competing for the Superapp opportunity choose from three strategic positions:

1. **Build the full stack.** Own distribution and build the rails beneath it. Robinhood is the cleanest example. High control, high execution risk.
2. **Specialize in infrastructure.** Run the rails and let other apps compose. Hyperliquid is the cleanest example. No mobile app burden. Growth depends on builder adoption.
3. **Specialize in distribution.** Own the user and aggregate whatever infrastructure wins. Phantom is the cleanest example. No protocol risk. Margin depends on what's composable.

This report covers all three. The thesis is that the middle position, owning some of the stack but not all, is where companies get squeezed.

## The case for Robinhood

As a mobile-first app, Robinhood has become the most active trading venue for U.S. retail. As of May 2025, it serves 25.8 million funded accounts and manages $255 billion in platform assets across equities, options, crypto, and cash.

{{< img src="images/superapp-stack/robinhood-vs-hyperliquid-5.png" alt="Robinhood accounts and assets chart" >}}

[Source](https://investors.robinhood.com/static-files/da19a20a-8e88-445e-8c71-3a1029ac0c51)

Before Robinhood, public trading was dominated by brokerages charging per-trade commissions.

Robinhood restructured the model by removing commissions entirely and monetizing through payment for order flow (PFOF), a system where trades are routed to market makers who pay Robinhood for the volume. This shifted transaction costs away from the user and enabled Robinhood to scale rapidly and rival brokerages like TD Ameritrade.

In this model, Robinhood doesn't provide liquidity directly. It originates retail flow and sells it to wholesale market makers, who quote spreads and pocket the difference.

Lately, they're moving to meet the demand for crypto among retail traders. In Q1 2025, the leading source of transaction-based revenue were crypto transactions, which produced $252 million in revenue. For context, Robinhood's options revenue was $240 million and equities revenue was $56 million for the same period.

{{< img src="images/superapp-stack/robinhood-vs-hyperliquid-6.png" alt="Robinhood revenue mix chart" >}}

To expand liquidity Robinhood acquired Bitstamp, giving it control of the 15th largest CEX. Most recently, they've deployed an L2 on Arbitrum and announced plans to eventually migrate to a standalone L1. The chain hosts tokenized US equities for EU customers.

But this enables much more. By using blockchain infrastructure behind a permissioned frontend, Robinhood can integrate with open protocols while maintaining control, similar to JPMorgan's integration with Ondo.

This improves their already robust product suite, which now includes:

- Strategies (automated hedge-fund strategies)
- Options (equities)
- Equities perps and spot
- Crypto perps and spot
- Prediction markets

Robinhood may not appeal to the cyberpunk / decentralization maxi, but its distribution edge gives it a realistic shot at onboarding millions before they reach DeFi-native frontends like Phantom.

By owning both layers, distribution and infrastructure, Robinhood is positioning itself as a financial Superapp: a platform offering access to multiple markets and tools for yield generation and wealth management.

**The bear case?**

If Robinhood fails to create meaningful DeFi-integrated products that resonate with users, it risks being outpaced by protocols with stronger offerings or a better understanding of user behavior.

In the age of Superapps, companies will either integrate crypto meaningfully, or be left behind.

## The case for Hyperliquid

Hyperliquid, the leading perp DEX, has set itself apart with faster asset listings, deeper leverage, and an aggressive approach to developer integrations. By mid-2025, the protocol was processing over $150 billion in monthly volume, translating to $908 million in annualized revenue.

{{< img src="images/superapp-stack/robinhood-vs-hyperliquid-7.png" alt="Hyperliquid growth chart" >}}

[Source](https://defillama.com/protocol/perps/hyperliquid)

This performance has also helped drive growth for DEXes, with DEX perp volume now running at roughly 8% of CEX perp volume, as of July 2025.

{{< img src="images/superapp-stack/robinhood-vs-hyperliquid-8.png" alt="DEX to CEX perp volume chart" >}}

[Source](https://www.theblock.co/data/decentralized-finance/derivatives/dex-to-cex-futures-trade-volume)

Liquidity on Hyperliquid is provided by HLP, a public vault that pools user capital into the protocol's market-making strategies. HLP depositors take the operating profit from this activity. Trading fees flow separately to the Assistance Fund, which buys back HYPE on the open market. The split means HLP holders take market-making risk, while HYPE holders take fee exposure.

**What's behind this growth?**

Hyperliquid's frontend drives most volume today. But the Builder Code system is what scales distribution from here.

Builder codes let developers embed Hyperliquid's perps into their own apps and share in order fill fees. As of July 2025, 181 builders have integrated Hyperliquid via Builder Codes, generating $11 million in protocol revenue.

{{< img src="images/superapp-stack/robinhood-vs-hyperliquid-9.png" alt="Hyperliquid builder code chart" >}}

[Source](https://www.hypeburn.fun/builders)

One of the most impactful recent integrations was with Phantom, which went live on July 9th 2025. In just 10 days, Phantom drove over 16K new users and facilitated $1.9 billion in volume on Hyperliquid.

{{< img src="images/superapp-stack/robinhood-vs-hyperliquid-10.png" alt="Phantom integration chart" >}}

[Source](https://www.flowscan.xyz/builders?builder=phantom)

Builder codes allow Hyperliquid to distribute trading infrastructure without owning the frontend, making it a scalable backend for emerging Superapps. As more builders integrate Hyperliquid, it generates more fees, positioning it as a kingmaker for onchain perps.

Furthermore, with Hyperliquid's recent [HIP-3 proposal](https://www.blocmates.com/articles/hip-3-explained-why-hyperliquid-will-flip-binance), they are addressing new markets. HIP-3 will let developers spin up perp markets for virtually any asset, including:

- Commodities
- Global equities
- FX (EUR/USD, GBP/USD)
- Prediction markets
- Custom baskets

Launching an HIP-3 market requires staking 1 million HYPE, valued at $40 million at current prices. While steep, this grants access to the full HyperCore infrastructure including matching engine, onchain order books, oracles, and settlement layer.

If builder adoption continues, whether through new Builder Code integrations or HIP-3 market launches, Hyperliquid could surpass Robinhood on revenue even without matching its retail distribution.

Today, Hyperliquid already outpaces Robinhood on core product specs: offering up to 50x leverage (vs. 3x on Robinhood) and access to over 100 perp markets, compared to a much narrower set on Robinhood Crypto Perps.

**The bear case?**

Centralized platforms like Robinhood benefit from full regulatory licensing. This will matter if Hyperliquid, or its frontend partners like Phantom want to enable fiat off-ramps across multiple countries.

Lack of regulatory clarity already presents friction: Hyperliquid is currently inaccessible to U.S. users, limiting its reach and revenue potential.

## The case for Phantom

Phantom is the third archetype: a mobile-first wallet that owns distribution and composes with whatever infrastructure wins. It does not run its own AMM, perps engine, or chain. It routes swaps through Jupiter, perps through Hyperliquid, and earns fees on volume across both. The product is a UX layer over the existing DeFi stack. The bet is that whoever owns the user can rent the rails.

The Hyperliquid integration shows the model in motion. Phantom drove $1.9 billion in volume and 16K new users to Hyperliquid in the 10 days after the July 2025 launch ([Source](https://www.flowscan.xyz/builders?builder=phantom)). Builder Code revenue from the perp integration came to $458K in that window ([Source](https://defillama.com/protocol/phantom-perps)). Total Phantom revenue across all wallet activity in the same 10 days was $7.9 million ([Source](https://defillama.com/protocol/phantom)).

The bigger number is the cumulative one. Phantom has produced $559 million in lifetime revenue from the aggregation model, without owning a single piece of infrastructure ([Source](https://defillama.com/protocol/phantom)). The Hyperliquid integration is one line in a diversified revenue stack.

**Why this matters for the Robinhood comparison.**

Phantom and Robinhood compete for the same prize: retail attention. Hyperliquid does not. Robinhood's full-stack bet rests on the premise that building the rails is necessary to control UX and capture margin. Phantom shows the rails are increasingly commodity. If users can switch between infrastructure providers without leaving the wallet, the value of owning rails collapses to whatever margin the wallet negotiates with each rail.

That makes Phantom, not Hyperliquid, the structural threat to Robinhood. Robinhood's edge is regulated distribution to US retail. Phantom's wedge is mobile-first distribution to users who do not need a US brokerage. If onchain off-ramps mature, that cohort widens.

**The bear case?**

Phantom's margin depends on the composability of the ecosystem around it. If a dominant infrastructure provider like Hyperliquid moves up the stack and launches its own wallet, the aggregation model loses leverage. The current revenue mix is diversified across swaps and Builder Codes, but a single rail capturing too much volume share would compress Phantom's negotiating position.

## Closing thoughts

Three strategic positions emerge from the analysis. Full-stack ownership (Robinhood). Infrastructure specialization (Hyperliquid). Distribution specialization (Phantom).

The middle is where companies get squeezed. Owning some of the stack but not all means competing with full-stack players on one side and pure-play specialists on the other.

Historically, centralized exchanges have had a clear edge due to off-ramp access and regulatory compliance. As crypto embeds deeper into financial apps and consumer platforms, off-ramps abstract away. That weakens the CEX model's biggest moat and opens room for both full-stack incumbents like Robinhood and distribution-only aggregators like Phantom to capture displaced users.

At present, Hyperliquid's HIP-3 framework gives it the broadest product scope among the three. Robinhood will need to move faster on onchain features like strategy vaults and synthetic assets to keep pace. Phantom benefits regardless of which infrastructure provider wins, as long as the aggregation model remains composable.

{{< img src="images/superapp-stack/robinhood-vs-hyperliquid-11.png" alt="Superapp stack closing chart" >}}

### How the three are priced today

- **Robinhood (NASDAQ: HOOD).** ~$85B market cap on $2.9B annual revenue, ~29x multiple. Premium reflects regulated distribution at scale and optionality on tokenized assets via the new chain.
- **Hyperliquid (HYPE).** $40B FDV on $908M annualized revenue, ~44x multiple. Premium reflects the infra-as-primitive thesis and HIP-3 expansion path. Revenue routes to HYPE holders through the Assistance Fund, which buys back HYPE on the open market. Closer to a buyback than a dividend, but a tighter holder-to-fee link than most governance tokens.
- **Phantom.** Private. $559M in lifetime revenue from the aggregation model alone. The run rate provides a floor on what distribution-only specialization can sustain without owning infrastructure.

### Where the investable wedges sit

1. **Regulated frontends for HIP-3 markets.** HIP-3 lets anyone spin up a perp market. The wedge is jurisdiction-specific or asset-class-specific frontends with compliance built in.
2. **Regional distribution specialists.** Phantom owns Western mobile-first crypto users. The regional analogs in LATAM, SEA, and MENA are still open.
3. **B2B onchain settlement infrastructure for incumbent brokerages.** Robinhood builds this internally. The opportunity for new entrants is providing it as a primitive to traditional brokerages and fintechs that want tokenization without owning the chain.
4. **Routing and aggregation layers.** As more rails compete, the abstraction layer that picks the best route per trade becomes valuable on its own.

### What we're watching

- **The regulatory clock on Hyperliquid US access.** A US license unlocks the largest retail pool and changes the Robinhood comparison directly.
- **Whether Robinhood licenses or partners on infra rather than building it.** A pure-build path is expensive. A partnership signal would be different.
- **Take rate compression in Builder Codes.** As more wallets compete for the same protocols, Builder Code fees may compress.
- **Phantom's product roadmap.** Does it stay pure distribution or move into infra. Either is a strong signal for the broader thesis.
- **HIP-3 adoption velocity.** Number of markets, builder concentration, and which asset classes attract real volume.
