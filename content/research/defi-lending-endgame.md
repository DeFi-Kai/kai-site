+++
date = '2026-07-14T09:00:00-04:00'
draft = false
title = 'The DeFi Lending Endgame: Scale is the Only Lever Left'
slug = 'defi-lending-endgame'
+++

{{< img src="images/defi-lending-endgame/defi-lending-profit-pool-cover.png" alt="DeFi lending profit pool" >}}

## Intro

Lending is one of the oldest functions in finance. A lender lets a borrower turn $1 of collateral into more than $1 worth of financial exposure while charging interest for it. Homeowners do this with a home equity line of credit (HELOC), and options traders do this with margin. The modern economy relies on credit for various financial functions demonstrating a clear product-market fit.

Crypto performs the same function through lending protocols. A user deposits an asset, borrows against it, and pays interest on the loan. Aave, the leading lending venue, accepts USDC, EUR, and gold-pegged assets as collateral and intermediates ~$10 billion in active loans. The base primitive supports cash-and-carry trades and long and short positions, and it has grown into curated vault products through protocols like Morpho which recently integrated with Coinbase. In structure these venues now resemble global FX markets.

The industry is evolving and the competitive landscape is following suit. Specifically, the interest rate a borrower pays has converged into a narrow band across every major protocol, and the share of that interest each protocol keeps is converging with it. When both the price and the margin flatten this way, the only variable left to move is scale. The business becomes a contest for the largest loan book, and the question worth answering is which venue wins that contest, and whether its market price already reflects the answer.

### Key Takeaways

- Lending is a power law category. Aave holds 43% of DeFi active loans and the top three venues hold 66% of them.
- Borrow yields have converged into a 3.5–5.5% band across all eight major venues, and the take rate each protocol keeps is pinned. With price and capture both becoming static, the size of the loan book is the only active lever left.
- The take rate sorts venues into four buckets: Aave holds a defensible premium. Spark, Fluid and Euler lean on ancillary lines like liquidity provision and licensing. Morpho sets take to zero to buy scale. Compound, Kamino and Jupiter Lend run thin commodity reserve-factor take-rates that flatten as pricing power erodes.
- Only Aave, Kamino, Spark and Fluid clear their cost of capital, and Morpho sits below its cost of capital by choice.
- Aave is valued as a compounder and Morpho as an option. Aave is priced fair-to-rich at 12.6x earnings, a hold that turns long only when its V4 and GHO catalysts cross. Morpho's take is set to zero so it can only be valued on a future fee switch, and the take that would make it look fair would destroy its book. That makes $MORPHO a short at today's valuation.
- Flows are split by customer. Institutions route tokenized cash through the integrated model (Aave, Horizon) while retail flows to Morpho and the unbundled cohort.

## How we got here

Total active loans peaked at $52.3B in September 2025 at the height of the bull market but loans have since dropped to $24.4B as of July 2026. Since the majority of collateral on lending platforms are crypto-native assets, market prices and platform inventory are self-referential.

BTC and ETH (incl. LSTs and BTC wrappers) make up 76% of net total value locked (TVL) across Aave, Morpho, and SparkLend: 77% on Aave, 67% on Morpho, 87% on SparkLend.

{{< img src="images/defi-lending-endgame/lending-share-of-crypto-dual-axis.png" alt="DeFi lending vs BTC and ETH market cap" >}}

*Source: DefiLlama + CoinGecko*

Leverage often rises after spot peaks, as shown in August 2025. Following a peak, people borrow to re-enter, and inversely when spot prices fall loans decrease due to de-risking (repaid loans) and liquidations.

In its current state, lending is a power law category. Aave controls 34% of all DeFi lending TVL, and the top three protocols control 62%.

| Protocol     | Active Loans | Avg Loans (TTM) | % of Category | Fees TTM | Revenue TTM |
| ------------ | -----------: | --------------: | ------------: | -------: | ----------: |
| Aave         |      $10.50B |         $20.23B |         34.3% |    $927M |     $122.3M |
| Morpho       |       $3.69B |          $3.55B |         18.2% |    $209M |          $0 |
| Sparklend\*  |       $1.81B |          $1.71B |          9.5% |    $211M |      $24.9M |
| Kamino       |        $952M |          $1.32B |          2.7% |     $80M |      $12.1M |
| Jupiter Lend |        $859M |       $637M\*\* |          2.5% |     $26M |       $1.4M |
| Euler        |        $603M |          $1.08B |          0.8% |     $67M |       $3.8M |
| Fluid\*      |        $739M |          $1.24B |          1.6% |     $74M |      $12.6M |
| Compound     |        $569M |           $848M |          3.2% |     $38M |       $2.4M |

*Source: DefiLlama*

While the lending category is consolidating, the business of lending dollars against crypto collateral is becoming commoditized. With more competition, best practices diffuse across venues. And because the smart contracts are open source, rivals fork the winning design outright, making convergence mechanical.

Gross borrow yield is the interest (price) borrowers pay per dollar of active loans. It rose with rates into early 2025, then converged. By mid-2026 all eight venues sat in a tight 3.5% to 5.5% band.

{{< img src="images/defi-lending-endgame/defi-lending-borrow-yield.png" alt="Gross borrow yield across eight venues" >}}

*Source: DefiLlama*

Since capital is fungible, it can chase the best rates instantly. That means borrow-yield convergence is the base case. As pricing power erodes, venues defend their take rates in two ways: reducing costs and adding new business lines to increase revenue.

Lending protocols earn revenue from the interest borrowers pay. The interest is split according to a Reserve Factor which sets the protocol's share of interest. The remaining interest goes to depositors as supply yield. Reserve factor is the primary rate that influences costs and margin. Venues must balance the reserve factor to incentivize depositors while maintaining sizable margins. Secondary revenue comes from liquidation penalties, flash loans, and licensing deals.

Together, the reserve factor, and secondary sources control the take rate (revenue/fees). Over the past 12 months, reserve factors have tightened, causing Take Rates to converge into a band.

Defensibility of take is inversely proportional to how much of it comes from the reserve factor. Protocols with high reserve fees, like Kamino are reverting back to the mean. Meanwhile, venues like Sparklend, Fluid, and Euler are relying on additional sources like liquidations, liquidity provision and licensing agreements to reinforce take rates in anticipation of future reserve fee compression.

| Protocol     | Take Rate (Rev / Fees) | Reserve factor fee | Revenue margin (Rev / Avg Loans) | % of revenue from borrow interest | % of revenue from non-interest |
| ------------ | ---------------------: | -----------------: | -------------------------------: | --------------------------------: | -----------------------------: |
| Aave         |                  13.2% |              12.4% |                            0.60% |                               84% |                            16% |
| Morpho       |                     0% |                 0% |                            0.00% |                                 — |                              — |
| Sparklend    |                 11.8%† |               7.2% |                            1.46% |                               19% |                            81% |
| Kamino       |                  15.0% |              14.8% |                            1.01% |                               87% |                            13% |
| Jupiter Lend |                   5.3% |               5.3% |                            0.23% |                              100% |                             0% |
| Euler        |                   5.7% |               0.0% |                            0.35% |                                0% |         100% (a separate skim) |
| Fluid        |                 17.0%† |              12.0% |                            1.01% |                               54% |                            46% |
| Compound     |                   6.3% |               6.3% |                            0.28% |                              100% |                             0% |

*Source: DefiLlama*

Lifting take means raising the reserve factor, which taxes suppliers and bleeds the scale a venue is chasing, or building secondary lines like liquidations and licensing, which are slow and not open to everyone.

As a result, protocols are bucketed by where the capture comes from and whether it holds in a commoditizing market, which reveals 4 groups:

1. Defensible Premium - high reserve factor that deposits tolerate. Take is high and stable (Aave)
2. Ancillary take - High take rate that comes from lines that don't tax suppliers, including liquidations, flashloans, and licensing. Take rises without touching the reserve factor, so it doesn't impede scale (Sparklend, Fluid, and Euler)
3. Capture sacrificed for scale - Take set to zero on purpose (Morpho)
4. Commodity reserve-factor take - Low take drawn almost entirely from a thin reserve factor, with no premium or secondary lines to lean on. It is the least defensible take and the baseline the sector drifts toward as pricing power erodes (Compound, Kamino, and Jupiter Lend)

{{< img src="images/defi-lending-endgame/defi-lending-take-rate-ttm.png" alt="Take rate across eight venues" >}}

*Source: DefiLlama*

Kamino's take reverts to a higher floor because Solana has fewer lending protocols than EVM. The only other major competitor on Solana, Jupiter Lend, is the venue that caps it.

Morpho, the second largest venue on EVM chains, has conceded the price war, reducing take to 0% to drain market share from competitors. Euler is considering following suit, setting take to 0% in a pending governance vote.

Since price (gross borrow yields) is being largely competed away and capture (take rates) is converging to a banded range, revenue growth shows up in the only active lever left: scale (active loans).

Revenue expressed as a formula is:
{{< img src="images/defi-lending-endgame/formula-revenue.png" alt="Revenue formula" >}}

The market is essentially betting on whose loan book can compound over time and expand beyond the cyclicality of crypto. Scale is the active lever and distribution is the moat. And projects are approaching the scale issue with drastically different strategies.

## Where we are today: integrated vs. unbundled

Most lending protocols are moving on from monolithic architecture and adopting modular designs where markets are isolated by asset and risk. However, even as architecture converges, the market is still separated by two competing business models: integrated, and unbundled.

{{< img src="images/defi-lending-endgame/lending-integrated-unbundled.png" alt="Integrated versus unbundled lending models" >}}

*Source: protocol docs*

On one hand, Aave is modular but integrated. It recently launched modular markets with v4 in late March 2026. In v4, hubs (markets) hold liquidity which seed multiple spokes (vaults). Although Aave v4 is modular in architecture it remains an integrated stack: the protocol still approves and vets every spoke. The protocol is the curator. It sets every LTV, oracle, and listing, bears the risk decision, and takes the reserve factor on borrow interest plus secondary skims (liquidations, flash loans, licensing).

On the other hand, protocols like Morpho, Kamino, and Euler are modular but unbundled. These protocols maintain the base lending primitive, but hand over risk and curation to third parties. This surface area creates a market for traditional asset managers and DeFi native risk curators to productize vaults and earn from management fees. Curators select collateral, liquidity depth, and liquidation logic.

The key difference between integrated and unbundled business models is who manages the risk and who sets the spread/split.

Integrated protocols capture the full spread at the cost of having to build demand and curation themselves, while unbundled protocols outsource components at the cost of pricing power. For instance, Aave splits its earnings between two parties: depositors and the protocol. The split is set unilaterally by moving the reserve factor.

However, in the case of Morpho, third party claimants supply things Morpho doesn't own. Curators supply risk management and distribution is supplied by partners like Coinbase, which supply borrowers. As a result, the share must be split between four parties: depositors, curators, distribution, and eventually the protocol. Simply put, an unbundled protocol would have to garner ~2-3x more partnerships than an integrated protocol like Aave, to make the same impact on its earnings.

An integrated protocol like Aave can set its own price at the cost of having to build demand and curation itself, while an unbundled protocol can grow fast through third-party curators and integrations, but its economics must be negotiated.

Beyond economics, the two models contain risk differently. Even in modular form, an integrated protocol still pools liquidity through shared hubs, so a bad market in one place can draw down the wider book. An unbundled protocol isolates each vault, so a curator's mistake is capped at that vault and does not spread across the protocol.

They also differ in who eats the loss once it lands. Aave absorbs shortfall through a shared backstop (the Umbrella safety module), which pays out when a market goes bad and spreads the damage across the system. Morpho runs no such backstop, so the loss sits with the depositors of the vault that took it.

## The Lending Profit Pool

Morpho has set its take to zero and passes all yield to vault curators and depositors in an effort to acquire scale. By doing so, it puts off negotiations for a later time. This is a strategic move to penetrate the market, and attack the market leaders.

Calculating the Economic profit (EP) of each venue shows us where the real profit in lending actually sits. Economic profit (EP) is what a venue earns above its cost of capital. Specifically, the EP measures the profit the platform earned after subtracting the minimum profit that capital could have earned elsewhere.


{{< img src="images/defi-lending-endgame/formula-economic-profit.png" alt="Economic profit formula" >}}

| Protocol     | Earnings | Capital-at-risk | r × capital |      EP | Verdict |
| ------------ | -------: | --------------: | ----------: | ------: | :------ |
| Aave         |  $121.0M |         $660.8M |      $99.1M | +$21.9M | pass    |
| Kamino       |   $12.1M |          $33.1M |       $5.0M |  +$7.1M | pass    |
| Spark        |   $24.9M |          $82.1M |      $12.3M | +$12.6M | pass\*  |
| Compound     |    $2.4M |          $21.2M |       $3.2M |  −$0.8M | fail    |
| Jupiter Lend |    $1.4M |          $15.9M |       $2.4M |  −$1.0M | fail    |
| Fluid        |    $4.7M |          $30.9M |       $4.6M |  +$0.1M | pass    |
| Euler        |   −$1.1M |          $27.1M |       $4.1M |  −$5.2M | fail    |

*Source: DefiLlama + framework (assumptions above)*

Aave, Kamino, Spark and Fluid are the only protocols that generate revenue above their cost of capital. Notably, Aave earns $121.0M TTM and demonstrates the most economic profit. This also makes it the biggest target for modularized lending protocols to siphon scale.

This relationship can be visualized as a profit pool. Each venue is a bar. Width is the capital at risk. Height is its return above the cost of that capital, or ROIC minus WACC. And the area is the economic profit.

{{< img src="images/defi-lending-endgame/defi-lending-profit-pool.png" alt="Lending profit pool across eight venues" >}}

*Source: DefiLlama*

The flat line is the 15% hurdle (r). Above the line, projects are earning more than their cost of capital, and below the line, projects are earning less.

Among the profitable venues, Kamino runs a high spread on a thin book, so it stands tall and holds the third largest pool. However, it functions largely as a Solana beta, with a commoditizing take rate and a rich P/E (16.1x).

Sparklend posted +$12.6M in economic profit, but it's built on a fading peak with most revenue generated by the Spark Liquidity Layer (SLL), and not the loan book.

Fluid sits at +$0.1M in economic profit and barely clears the hurdle. While its lending business is the dominant business line, it relies on Jupiter Lend licensing fees to make up the remaining 46% of its earnings. In other words, a large share of Fluid's revenue comes from the secondary lending venue on Solana.

Aave makes up the entire profit pool with $21.9M in economic profit. Without Aave, total economic profit for the lending sector nets to -$0.5M. Aave's bar is short but it's also the widest, so it holds the largest pool in absolute dollars.

All other protocols including Morpho, Compound, Jupiter Lend, and Euler are in economic deficits with Euler being the least profitable at −$5.2M in EP.

Morpho is the only protocol that is deliberately operating beneath the hurdle. It purposely earns nothing on real capital at risk, which is the price it pays to buy scale. Its planning to expand its bar, and eventually flip it above the line once it enables fee share, to become the largest profit pool. As a second order effect of Morpho's zero-take, lenders will expect higher yields across the market which squeezes rivals' reserve fees.

## Valuing the market

Valuations for the lending sector have a wide dispersion; 10x P/E-multiple spread ranging from Sparklend at 7.0x to Compound at 70.4x. To understand comps we separate P/E into two parts: **P/S**, the market's value on gross fees, and **Take Rate**, the protocol's share of fees.

{{< img src="images/defi-lending-endgame/formula-pe-decomp.png" alt="P/E decomposition formula" >}}

Since P/E = P/S ÷ Take Rate, a high P/E is either from an inflated P/S, a low take rate, or both.

| Protocol       | Take rate (Rev / Fees) | P/S (FDV / Fees) | P/E (FDV / Rev) |
| -------------- | ---------------------: | ---------------: | --------------: |
| Aave           |                  13.2% |             1.7x |           12.6x |
| Morpho         |                   0.0% |            10.6x |             N/A |
| Sparklend      |                  11.8% |             0.8x |            7.0x |
| Kamino         |                  15.0% |             2.4x |           16.1x |
| Jupiter Lend\* |                   5.3% |              N/A |             N/A |
| Fluid\*        |                  17.0% |             1.4x |            8.0x |
| Euler          |                   5.7% |             0.4x |            7.2x |
| Compound       |                   6.3% |             4.5x |           70.4x |

*Source: DefiLlama + CoinGecko*

As an example, Compound has a thin take rate of 6%, and a relatively high P/S of 4.5x, trading at 70.4x P/E (highest P/E multiple in the set). However, Compound's loans decreased 47% over the last year, and revenue margin is among the lowest in the set (0.28%) suggesting that the market hasn't repriced on its declining revenue yet. If take rate were to decline further (as the data suggests), Compound would shift to the left, placing it in the ~100x P/E range prompting for a drastic re-rate downwards.

{{< img src="images/defi-lending-endgame/defi-lending-take-ps-scatter.png" alt="Take rate versus P/S scatter" >}}

*Source: DefiLlama + CoinGecko*

On the other hand, Euler also has a thin take rate of ~6%, but with a P/S of 0.4x it trades at 7.2x P/E. Both have similar take rates, but their P/E multiples are on opposite ends of the set. Compound with a low take and inflated P/S and Euler with a low take and depressed P/S.

---

## The trade: AAVE/MORPHO & Watchlist

### Aave: Compounder

Aave is a compounder so it's valued on earnings and the durability of its growth. Those earnings reach the token directly, since Aavenomics 3.0 routes protocol and GHO revenue into automated AAVE buybacks. We use the Gordon Growth Model to assess its growth in perpetuity.

{{< img src="images/defi-lending-endgame/formula-gordon-growth.png" alt="Gordon growth formula" >}}

where r is the discount rate (15%) and g is implied growth (what we're solving for). At 12.6x, the market is pricing ~7% perpetual earnings growth. Sensitized, the perpetual earnings spans ~7-17%.

| r (discount rate) | Implied perpetual g at 12.6x |
| ----------------- | ---------------------------: |
| 15% (base)        |                         7.1% |
| 20%               |                        12.1% |
| 25%               |                        17.1% |

*Source: author calculation (Gordon growth)*

{{< img src="images/defi-lending-endgame/defi-lending-aave-realized-g.png" alt="Aave realized growth versus the market-implied bar" >}}

*Source: DefiLlama*

The chart shows realized earnings growth (black) compared to loan book growth (blue). The gap between the two lines represents the margin. The green line represents the sensitized market implied perpetual growth (7.1% - 17.1%), the bar that Aave's growth must stay above.

The black above blue indicates that earnings grew faster than loan book, displaying a high margin. In mid 2025, the lines crossed indicating the growth of margin flipping negative. The book is now growing faster than earnings which shows that margin is compressing (0.99%-0.60%).

Realized growth is falling, but the two forces behind it are not the same. The loan book is shrinking because collateral and loans on Aave are crypto-native assets, so the book moves with the market and contracts in a downturn. That part is cyclical and recovers when the cycle turns.

The margin compression, however, is a different story. Base lending is commoditizing, so the spread Aave earns on each loan is structurally declining, and that does not come back on its own. This matters because the implied bar is a perpetual growth rate, a number the business has to hit through the entire cycle. A temporary cyclical dip does not threaten it, but a permanent decline in margin does because it's the sole piece that actually has to clear the bar. Presently, trailing earnings sits at +38.5%, however revenue has been flat at ~$122-$128M for seven months.

So, how does Aave grow from this point?

The answer is Aave v4, Aave's modular deployment and GHO, Aave's stablecoin.

Aave's V4 instance has been the genuine growth engine. V4 launched in late March 2026, and the loan book has grown to $85M, over the past 3 months. The book operates on a high take (12.4%), yet margins operate at a thin 0.34%. Presently, V4 makes up 0.2% of total Aave revenue which is too small to affect growth today.

{{< img src="images/defi-lending-endgame/defi-lending-aave-v4.png" alt="Aave V4 take and margin" >}}

*Source: DefiLlama*

So, what about GHO?

Aave's ability to set GHO rates gives it control over the borrowing price and the operating cost (GHO savings rate). However, GHO is still in its infancy and the subsidy to gain scale runs ~$22M a year against ~$4M of GHO revenue, a net ~$18M deficit.

{{< img src="images/defi-lending-endgame/defi-lending-aave-catalysts.png" alt="GHO fully-costed P&L" >}}

*Source: TokenLogic + DefiLlama*

As a result, GHO only becomes an active lever for growth once its revenue surpasses its expenses and maintains that relationship consistently.

At a 12.6x P/E multiple, Aave is fair-to-rich. Assuming a discount rate of 15% Aave is fair, and sensitized to 20%, Aave becomes rich. At that multiple the market already prices roughly 7% perpetual earnings growth, so the upside is not in the current price. Until the two catalysts are confirmed, Aave is a hold, and a long only on confirmation.

The re-rate runs on two triggers:

1. V4's gross borrow yield normalizes. The take is already 12.4% against core's 13.2%, so the entire margin gap is the yield. V4 borrows at 2.75% against core's 4.57%, which holds its revenue margin at 0.34% against core's 0.60%. The trigger is the yield climbing toward ~4.57% while the take stays intact, which pulls the margin to ~0.60% on its own. The second half is scale, V4 growing from 0.2% of Aave revenue past 5%, the point where it starts to move earnings.
2. GHO's borrow interest outgrows the savings-rate subsidy. GHO runs a ~$18M deficit today, ~$22M in subsidy against ~$4M in revenue. The trigger is that line crossing above zero and holding positive for two quarters.

If both confirm, Aave evolves from fair, to cheap and re-rates again.

The invalidation is revenue staying flat past its current seven-month plateau while core margin keeps sliding. That is margin declining permanently rather than dipping cyclically, and it means the business cannot make the ~7% growth the price already assumes. At that point a fair valuation turns expensive.

### Morpho: Expensive Option

Morpho takes 0% of fees to gain scale and operates in anticipation of a future fee switch. Since it can't currently be valued on earnings it must be valued on switching the fee switch on. This places the whole valuation on the 10.6x P/S, which is the richest in the cohort.

If we use the current P/S and plug in hypothetical take-rates we can find what the P/E might be when an eventual fee switch occurs.

P/E = P/S / take rate

{{< img src="images/defi-lending-endgame/defi-lending-morpho-option.png" alt="Morpho implied P/E at hypothetical take rates" >}}

*Source: DefiLlama + CoinGecko*

At a 10% take rate, Morpho's P/E comes to 106x. At 13% (Aave's current take), Morpho sits at an 81x, and at 15% (Kamino's current take), Morpho sits at a 70x. On today's fees, Morpho would have to assert a 53% take rate just to get to a 20x valuation, which is still wildly overvalued. Essentially, the take rate that makes the valuation fair would destroy Morpho's base and invite competitors to undercut it, similar to how it's doing now.

Even if we assume a full-float mcap, P/S would sit at 6.9x and the implied P/E at a 10-15% take is still 46-69x.

If we observe Morpho's price over the past year at a hypothetical 10% reserve factor, the P/E sits well above Aave's realized multiple over the entire period. The gap between the lines never closed and today Morpho's hypothetical multiple sits 8x above Aave's realized ~13x P/E. Although both have been compressing, the market has paid the "flip premium" for Morpho consistently.

{{< img src="images/defi-lending-endgame/defi-lending-morpho-option-vs-aave.png" alt="Morpho hypothetical P/E versus Aave actual P/E" >}}

*Source: CoinGecko + DefiLlama*

At a 10.6x P/S with zero earnings, Morpho is priced as an option with an unreachable strike. Morpho is a long trade at a fair valuation and a short trade at a rich valuation, which is where it sits currently.

However, size and timing matter here more than anything. Since Morpho's launch the option has remained expensive without reverting to the mean. Morpho's market sentiment has been overwhelmingly positive, allowing the price to hold within a ~$1-$2.50 range.

The largest supply cliff (Cohort 2, +193M) already fired in October 2025 and the range held, so the forward ~9M/mo vesting is roughly one day of volume and absorbable while demand remains steady.

Whether $MORPHO is a short is ultimately based on the demand-side and can be observed through 3 monitors:

- Price breaks the ~$1.18 band floor and holds below while circulating supply keeps climbing.
- Market cap flattens or rolls over while circulating supply keeps rising, so the price effect turns negative.
- Days-of-volume-to-absorb spikes, from a larger unlock or from volume thinning.

{{< img src="images/defi-lending-endgame/defi-lending-morpho-float.png" alt="Morpho float-absorption monitor" >}}

*Source: CoinGecko + Morpho docs*

Here's how to read the 3 panels:

1. **price vs the float.** Price with the $1.18–$2.50 band on the left axis, circulating supply on the right. This is the core absorption test. Supply doubled from 323M to 654M and the range held, so the float was absorbed. The one failure came after the October Cohort-2 cliff, when price bled to the ~$1.13 low by December before recovering. The short lives on the right edge: price losing the band floor while circulating keeps climbing.
2. **unlock intensity.** The orange bars are the monthly unlock in tokens. The teal line is the same unlock expressed in days of trading: the dollar value of the month's unlock divided by that month's average daily volume. It answers how many days of normal turnover it would take to absorb the new supply if it all sold. A reading of 1 means the unlock equals a single day of volume. It also rises for two reasons: a bigger unlock, or thinning volume.
3. **market-cap decomposition.** Each shaded band is one month and holds two bars: the supply effect, orange, and the price effect, green when price rose and red when it fell. The two bars sum to that month's mcap change. The signal is the price bar: A red bar means the float was not absorbed that month.

In the event that demand absorbs unlocks, the $MORPHO token will continue to be priced as an option in anticipation of a fee switch.

Invalidation criteria for a short:

- If Morpho turns on a small take (5-10%) and the book doesn't bleed then this proves that capture and scale can coexist and that Morpho's distribution moat is sturdy
- Morpho's fees outrun the take math and its hypothetical line falls towards Aave it demonstrates that the book is real and able to grow
- The market remains bullish on Morpho and the FDV/mcap gap closes gracefully. Essentially, as tokens vest the price holds.

### Watchlist

The lending sector consists of high-margin venues that clear their cost of capital but sit outside the trade. Each earns a long or a short under different conditions.

- **Kamino.** Solana's default money market, running the highest reserve-factor take of the majors near 15 percent. Kamino retains pricing power from being the largest venue on Solana. It is a levered bet on Solana activity, so it earns a place when Solana lending demand rises or its multiple compresses and becomes cheap.
- **Fluid.** Its design lets the same liquidity serve a DEX and a lending book at once, so it clears its cost of capital on a small balance sheet. About 46 percent of revenue now comes from licensing the engine to Jupiter Lend, so Fluid grows as the Jupiter Lend book grows. This also makes Fluid a bet against Kamino as well. Fluid is a bet on whether the capital-efficiency edge compounds into share.
- **Sparklend.** Its top earning line is the Spark Liquidity Layer, which deploys the Sky stablecoin balance sheet into outside venues, so most of the earnings come from allocating capital elsewhere rather than from its own book. Returns track where it routes the balance sheet more than its own lending margin.

## Category-wide Catalysts

DeFi lending presently has a finite ceiling and is mostly a beta-to-crypto product. The biggest unlock comes from private credit and RWA collateral. Moreover, pending regulations can lift demand for the entire sector.

### RWAs & Private Credit

RWA market cap sits at $31 billion with projections for $1 - 4 trillion by 2030 ([McKinsey, *From ripples to waves*, 2024](https://www.mckinsey.com/industries/financial-services/our-insights/from-ripples-to-waves-the-transformational-power-of-tokenizing-assets)).

With RWAs as collateral lending platforms stand to capture the $4 trillion RWA opportunity. Equities, commodities, and private credit are already being used as collateral in DeFi. According to DefiLlama, ~2.53b of RWAs are actively used in DeFi protocols.

Some notable examples include:

- Aave: Aave's Horizon platform lists money market funds like Bitwise Crypto Carry Fund ($10.49m), and VanEck Treasury Fund ($6.25m) as collateral
- Kamino: Kamino offers markets for equities via xStocks ($30.4m), HELOCs via Figure ($437.3m), and Bitwise Crypto Carry Fund ($34.5m)

Similarly, Private credit collateral can help make loan books more exogenous. Products like Maple, OnRe, and USDai intermediate loans offchain and pool capital using tokenized structured products. When venues list these products as collateral, depositors can deposit and take out loans against these products.

However, this also increases risks of contagion and liquidation cascades that flow throughout multiple protocols.

### Regulation

The GENIUS Act, signed in July 2025, already bars stablecoin issuers from paying yield to holders. The OCC's 2026 rulemaking goes further and moves to extend that ban from the issuer to its affiliates and third parties, with the full regime operational in January 2027.

The CLARITY Act is the market-structure bill that provides some hope for DeFi. It moves to exempt non-custodial DeFi activity from SEC and CFTC authority, adding a DeFi trading-protocol framework and an insolvency safe harbor. It also carries the Tillis-Alsobrooks compromise which bars rewards that are economically or functionally equivalent to interest on a bank deposit. But it preserves a carve-out for incentives tied to "bona fide activities" or transactions, which brings sanctioned activities closer to credit-card rewards. As of July 2026 it has advanced out of the Senate Banking Committee on a 15-9 vote and awaits a floor debate. Interestingly, prediction markets price 2026 signing odds near 72%.

If non-custodial lending sits outside the yield prohibition, then DeFi lending becomes the one compliant venue left where a dollar earns a yield that banks and CeFi are prohibited from paying. That would make lending platforms the primary venue for retail and third-party integrations to source stablecoin yield.

However, if the prohibition extends to the lending protocols themselves, the loophole closes.

## Closing Thoughts

Scale is the only lever left, but liquidity is the scarce input that scale is built from which places a spotlight on issuers like Sky.

Sky is the clearest example as it sets the savings rate it pays to hold USDS, and it also sets the base rate it charges to lend it. Since it controls both legs it can administer spread that stays relatively steady. So the durable position in the lending wars may not be a lender after all, and instead it may be the stablecoin franchise that supplies the liquidity.

Aave understands this, and is using GHO to move from renting the dollar to issuing it. But GHO still runs a roughly $18M deficit, and its growth depends on Aave's own loan demand, which is crypto-native and cyclical. Aave starts from lending and builds a dollar on top of that. Sky starts at the opposite end, from the dollar and builds lending on top of it with Spark. Essentially, Sky's bet is the easier one, which could make it the stronger long even though Aave is better known.

This also highlights another question: who is permissionless lending for?

Institutions are bringing tokenized cash and collateral onchain, and they're choosing not to route it through a permissionless vault with an anonymous curator. For instance, J.P. Morgan Asset Management has put tokenized money market funds on Ethereum, and it issues its JPMD deposit tokens on Base. This ultimately favors the integrated model, Aave and its Horizon arm, and it also favors the issuer that can offer a yield-bearing dollar inside the rules of the developing regulations.

Retail, however, is flowing towards Morpho and the unbundled cohort. So it's likely that flows split by customer rather than consolidate to a single winner. Still, the retail setup gives more power to the distributor because it owns the user.

While the trade is Aave and Morpho, the larger position is on who owns the dollar and who owns the user. Those two fights get settled on lending venues as the battlegrounds.

---

*This is research and personal opinion, not financial advice. The author may hold positions in the assets discussed. Figures are as of the dates noted and may be stale by the time you read this.*
