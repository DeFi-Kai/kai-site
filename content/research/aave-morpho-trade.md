+++
date = '2026-08-25T09:00:00-04:00'
draft = false
research_group = 'trade-ideas'
title = 'The AAVE/MORPHO Trade'
slug = 'aave-morpho-trade'
+++

_Originally published July 14, 2026 as part of the combined DeFi Lending Endgame report · Published as a standalone report August 25, 2026_

*This trade is built on the framework in [The DeFi Lending Endgame]({{< relref "/research/defi-lending-endgame" >}}), which covers the economics of onchain lending facilities and the evolving competition.*

---

Over the past year, Morpho has made headlines for its high-profile partnerships with exchanges like Coinbase and Kraken. The market believes Morpho will become the dominant lending platform, controlling RWA and stablecoin flows. The market prices Morpho according to that belief. I believe Morpho will capture a meaningful share of flows but its architecture keeps it from reliably taxing those flows and retaining durable earnings. In comparison, Aave captures similar flows through partnerships with EtherFi and Whop, but its terms let it tax that flow and retain durable earnings. For instance, the EtherFi Cash instance splits revenue 80/20 with the Aave DAO across the reserve factor, liquidations, and oracle recapture.

Aave runs at $122.3M TTM earnings, and a 13.2% take rate on a $20.23B TTM loan book. On current earnings, Aave is valued at a 12.6x P/E multiple on a $1.55B FDV (full-float), priced fair. Aave earns $22.5M above its cost of capital, accounting for nearly the entire sectors profit pool. Without Aave, the sectors profit pool nets to -$0.5M. Primary drivers for Aave's growth include Aave V4, a modular lending platform with increased capital efficiency, Aave Horizon, an RWA credit facility with access controls, and GHO, Aave's flagship stablecoin.

Morpho manages a TTM loan book of $3.55B with 0% take, trading at a $2.21B FDV (~60% float). It purposely operates at zero-take and emits ~$17M/year in MORPHO incentives to gain scale resulting in negative earnings. Morpho is priced as an option, valued on an eventual fee switch. At a 10-15% take rate (the market standard), Morpho's P/E becomes ~102x - 70x. For Morpho to operate at a fair valuation, it would have to flip on a 10-15% take rate on its loan book, and also generate 1.5-2x more loan volume than Aave ($30.34B - $40.46B in TTM loans).

Morpho splits revenue among 4 parties, making it difficult to generate durable earnings compared to Aave. Furthermore, it relies heavily on distribution partners which retain the relationship with the end user.

Aave becomes a long if it surpasses two catalysts: (1) V4's borrow yield normalizing toward V3's from 2.8% to 4.6% while take stays intact, and (2) GHO flipping cash-flow positive for two quarters. Morpho becomes a short if it's float trips one of three triggers: (1) Price losing the ~$1.18 band floor while circulating supply climbs, (2) market cap flattening while supply rises, turning the price effect negative, or (3) days-of-volume-to-absorb spiking.

### Key Takeaways

- Aave is valued as a compounder, priced fair at 12.6x earnings assuming r = 15%. The price already pays for both catalysts, so it turns long only when V4 accounts for 5% of total earnings and GHO becomes cash-flow positive.
- Morpho is valued as an option. Its take is set to zero, so it can only be valued on a future fee switch, and the take that would make it look fair would destroy its book. About a third of the token sits outside the float, and the vesting schedule adds roughly 9M a month into late 2027, so demand has to keep clearing new supply just to hold price. That makes $MORPHO a short if demand does not absorb token unlocks.

## Aave: The Compounder

Aave is the market leader with a growing line of products. Aave V4 increases capital efficiency and yield for lenders. GHO, Aave's stablecoin is positioned as the primary quote asset for loans. Aave issues GHO and offers interest on deposits through the GHO savings rate. This vantage point allows Aave to control both issuance and interest rates to stimulate demand or increase protocol spread when required.

Aave is a compounder so it's valued on earnings and the durability of its growth. It's earnings normally reach the token directly via buybacks but in April 2026 buybacks were paused amid the rsETH incident when Kelp's LayerZero rsETH bridge was exploited. [In a governance post](https://governance.aave.com/t/arfc-pause-aave-buybacks/24686), the team discussed resuming buybacks in the future when the incident was completely resolved.

In anticipation of buybacks resuming, we use the reverse Gordon Growth Model to assess Aave's growth in perpetuity.

g = r - p / (P/E)

{{< img src="images/aave-morpho-trade/formula-gordon-growth.png" alt="Implied growth formula" >}}

g is implied growth (what we're solving for). r is the discount rate (15%), and p represents the pass-through rate, the share of earnings that reaches token holders. We sensitize p using 25% as the floor, which represents Aave's previous $30M buyback budget, and 100% as the ceiling as the theoretical maximum.

At 12.6x, the market is pricing Aave at ~7-13% perpetual earnings growth.

| pass-through                              | Implied perpetual g at 12.6x |
| ----------------------------------------- | ---------------------------: |
| 100%                                      |                         7.1% |
| 50%                                       |                          11% |
| 25% (the $30M buyback budget vs. $122.3M) |                          13% |

*Source: author calculation (Gordon growth)*

{{< img src="images/aave-morpho-trade/defi-lending-aave-realized-g.png" alt="Aave realized growth versus the market-implied bar" >}}

*Source: DefiLlama*

The chart shows realized earnings growth (black) compared to loan book growth (blue). The gap between the two lines represents the margin. The green line represents the sensitized market implied perpetual growth (7.1% - 13%), the bar that Aave's growth must stay above.

The black above blue indicates that earnings grew faster than loan book, displaying a high margin. In mid 2025, the lines crossed indicating the growth of margin flipping negative. The book is now growing faster than earnings which shows that margin is compressing (0.99%-0.60%).

Realized growth is falling, but the three forces behind it are not the same. First, the loan book is shrinking because collateral and loans on Aave are crypto-native assets, so the book moves with the market and contracts in a downturn. That part is cyclical and recovers when the cycle turns. Secondly, $15B in TVL migrated away after the rsETH bridge exploit.

The third force, margin compression, is a different story. Base lending is commoditizing, so the spread Aave earns on each loan is structurally declining, and that does not come back on its own. This matters because the implied bar is a perpetual growth rate, a number the business has to hit through the entire cycle. A temporary cyclical dip does not threaten it, but a permanent decline in margin does because it's the sole piece that actually has to clear the bar. Presently, trailing earnings growth sits at +38.5%, however earnings have been flat at ~$122-$128M for seven months.

So, how does Aave grow from this point?

The answer is Aave v4, Aave's modular deployment and GHO, Aave's stablecoin.

Aave's V4 instance has been the genuine growth engine. V4 launched in late March 2026, and the loan book has grown to $85M, over the past 3 months. The book operates on a high take (12.4%), yet margins operate at a thin 0.34%. Presently, V4 makes up 0.2% of total Aave earnings which is too small to affect growth today.

{{< img src="images/aave-morpho-trade/defi-lending-aave-v4.png" alt="Aave V4 take and margin" >}}

*Source: DefiLlama*

So, what about GHO?

Aave's ability to set GHO rates gives it control over the borrowing price and the operating cost (GHO savings rate). However, GHO is still in its infancy and the subsidy to gain scale runs ~$22M a year against ~$4M of GHO revenue, a net ~$18M deficit.

{{< img src="images/aave-morpho-trade/defi-lending-aave-catalysts.png" alt="GHO fully-costed P&L" >}}

*Source: TokenLogic + DefiLlama*

As a result, GHO only becomes an active lever for growth once its revenue surpasses its expenses and maintains that relationship consistently.

At a 12.6x P/E multiple, Aave is fair. Assuming a discount rate of 15% Aave is fair. At that multiple the market already prices roughly 7% perpetual earnings growth, so the upside is not in the current price. Until the two catalysts are confirmed, the price already discounts them, making Aave a long on confirmation.

The re-rate runs on two triggers:

1. V4's gross borrow yield normalizes. The benchmark here is Aave across all versions, which is 97.7% Aave V3 by book. The take is already 12.4% against the 13.2% all-versions take, so the entire margin gap is the yield. V4 borrows at 2.75% against 4.57%, which holds its earnings margin at 0.34% against 0.60%. The trigger is the yield climbing toward ~4.57% while the take stays intact, which pulls the margin to ~0.60% on its own. The second half is scale, V4 growing from 0.2% of Aave earnings past 5%, the point where it starts to move the total.
2. GHO's borrow interest outgrows the savings-rate subsidy. GHO runs a ~$18M deficit today, ~$22M in subsidy against ~$4M in revenue. The trigger is that line crossing above zero and holding positive for two quarters.

If both confirm, Aave evolves from fair, to cheap and re-rates again.

The invalidation is the core margin (ex Aave V4) sliding below ~0.50% while the loan book grows quarter-over-quarter. Confirmed if TTM earnings also stays under ~$130M for two more quarters past the current seven-month plateau. This combination means the business cannot make the ~7% growth the price already assumes.

## Morpho: An Expensive Option

Morpho is an unbundled protocol whose token is priced for an economic model that does not yet exist. The protocol boasts major partnerships with Coinbase, Kraken, and Robinhood, but it does not actively earn revenue from any of them.

Morpho takes 0% of revenue to gain scale and operates in anticipation of a future fee switch. Since it can't currently be valued on earnings it must be valued on switching the fee switch on. This places the whole valuation on the 10.6x P/S, based on its gross revenue, which is the richest in the cohort.

If we use the current P/S and plug in hypothetical take-rates we can find what the P/E might be when an eventual fee switch occurs and Morpho begins to book earnings.

P/E = P/S / take rate

{{< img src="images/aave-morpho-trade/defi-lending-morpho-option.png" alt="Morpho implied P/E at hypothetical take rates" >}}

*Source: DefiLlama + CoinGecko*

At a 10% take rate, Morpho's P/E comes to 106x. At 13% (Aave's current take), Morpho sits at an 81x, and at 15% (Kamino's current take), Morpho sits at a 70x. On today's revenue, Morpho would have to assert a 53% take rate just to get to a 20x valuation, which is still wildly overvalued. Essentially, the take rate that makes the valuation fair would destroy Morpho's base and invite competitors to undercut it, similar to how it's doing now.

Even on circulating market cap rather than full float, P/S would sit at 6.9x and the implied P/E at a 10-15% take is still 46-69x.

If we observe Morpho's price over the past year at a hypothetical 10% reserve factor, the P/E sits well above Aave's realized multiple over the entire period. The gap between the lines never closed and today Morpho's hypothetical multiple sits 8x above Aave's realized ~13x P/E. Although both have been compressing, the market has paid the "flip premium" for Morpho consistently.

{{< img src="images/aave-morpho-trade/defi-lending-morpho-option-vs-aave.png" alt="Morpho hypothetical P/E versus Aave actual P/E" >}}

*Source: CoinGecko + DefiLlama*

At a 10.6x P/S with zero earnings, Morpho is priced as an option with an unreachable strike. Morpho is a long trade at a fair valuation and a short trade at a rich valuation, which is where it sits currently.

However, size and timing matter here more than anything. Since Morpho's launch the option has remained expensive without reverting to the mean. Morpho's market sentiment has been overwhelmingly positive, allowing the price to hold within a ~$1.18–$2.50 range.

The largest supply cliff (Cohort 2, +193M) already fired in October 2025 and the range held, so the forward ~9M/mo vesting is roughly one day of volume and absorbable while demand remains steady.

Whether $MORPHO is a short is ultimately based on the demand-side and can be observed through 3 monitors:

- Price breaks the ~$1.18 band floor and holds below while circulating supply keeps climbing.
- Market cap flattens or rolls over while circulating supply keeps rising, so the price effect turns negative.
- Days-of-volume-to-absorb spikes, from a larger unlock or from volume thinning.

{{< img src="images/aave-morpho-trade/defi-lending-morpho-float.png" alt="Morpho float-absorption monitor" >}}

*Source: CoinGecko + Morpho docs*

Here's how to read the 3 panels:

1. **price vs the float.** Price with the $1.18–$2.50 band on the left axis, circulating supply on the right. This is the core absorption test. Supply doubled from 323M to 654M and the band broadly held, so the float was absorbed. The one stress came after the October Cohort-2 cliff, when price wicked to a ~$1.13 low in December, just under the $1.18 floor, before reclaiming it. The short lives on the right edge: price losing the band floor while circulating keeps climbing.
2. **unlock intensity.** The orange bars are the monthly unlock in tokens. The teal line is the same unlock expressed in days of trading: the dollar value of the month's unlock divided by that month's average daily volume. It answers how many days of normal turnover it would take to absorb the new supply if it all sold. A reading of 1 means the unlock equals a single day of volume. It also rises for two reasons: a bigger unlock, or thinning volume.
3. **market-cap decomposition.** Each shaded band is one month and holds two bars: the supply effect, orange, and the price effect, green when price rose and red when it fell. The two bars sum to that month's mcap change. The signal is the price bar: A red bar means the float was not absorbed that month.

In the event that demand absorbs unlocks, the $MORPHO token will continue to be priced as an option in anticipation of a fee switch.

Invalidation criteria for a short:

- If Morpho turns on a small take (5-10%) and the book doesn't bleed then this proves that capture and scale can coexist and that Morpho's distribution moat is sturdy
- Morpho's revenue outruns the take math and its hypothetical line falls towards Aave it demonstrates that the book is real and able to grow
- The market remains bullish on Morpho and the FDV/mcap gap closes gracefully. Essentially, as tokens vest the price holds.

## Watchlist

The lending sector consists of high-margin venues that clear their cost of capital but sit outside the trade. Each earns a long or a short under different conditions.

- **Kamino.** Solana's default money market, running the highest reserve-factor take of the majors near 15%. Kamino retains pricing power from being the largest venue on Solana. It is a levered bet on Solana activity, so it earns a place when Solana lending demand rises or its multiple compresses and becomes cheap.
- **Fluid.** Its design lets the same liquidity serve a DEX and a lending book at once, so its take clears its cost of capital on a small balance sheet, though token incentives take almost all of that back and leave it near breakeven on economic profit. About 37% of earnings comes from that DEX and its Lite Vaults, and roughly 10% from licensing the engine to Jupiter Lend. It grows mainly as its own book compounds, with a smaller lift as Jupiter Lend grows on Solana. Fluid is a bet on whether the capital-efficiency edge compounds into share, and on emissions tapering as it does.
- **SparkLend.** Its top earning line is the Spark Liquidity Layer, which deploys the Sky stablecoin balance sheet into outside venues, so most of the earnings come from allocating capital elsewhere rather than from its own book. Returns track where it routes the balance sheet more than its own lending margin.

---

**Disclosure:** This report is provided for informational and research purposes only and does not constitute investment advice or a recommendation or solicitation to buy or sell any asset. I hold no position in AAVE or MORPHO as of publication. I may initiate, modify, or close positions discussed in this report after publication without notice. I received no compensation from Aave, Morpho, or their affiliates for producing this research. Any material commercial relationship with an entity discussed in my research will be disclosed.
