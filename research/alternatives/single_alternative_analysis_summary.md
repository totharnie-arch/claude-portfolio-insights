# Single Alternative Asset Selection: Analysis Summary
**Pension Fund Portfolio Enhancement — 60/40 Baseline**  
*Analysis Period: March 2011 – February 2026 (14.9 years) | Data: Public ETF Proxies via Yahoo Finance*

---

## Objective

Identify the **single best alternative asset class** to add to a traditional 60/40 portfolio, subject to a 10% allocation (reducing bonds from 40% → 30%).

**Candidates evaluated:**

| Alternative | Public Proxy | Nature |
|---|---|---|
| Infrastructure | IGF | Private (illiquid) |
| Private Credit | BKLN | Private (illiquid) |
| REITs | VNQ | Public (liquid) |
| Real Assets | DBA 40% / WOOD 40% / DBC 20% | Private (illiquid) |

---

## Methodology Note: Appraisal Smoothing

Private assets report quarterly appraisals, not daily marks. To simulate the experience of a private market investor, exponential smoothing was applied to illiquid proxies (Geltner 1991, 1993):

| Asset | Smoothing (α) | Vol Reduction |
|---|---|---|
| Infrastructure | 0.35 | −55% |
| Private Credit | 0.50 | −39% |
| Real Assets | 0.30 | −58% |
| REITs / Core | 1.00 | 0% |

Primary analysis uses **smoothed returns**. A sensitivity analysis with unadjusted (pessimistic) data is included.

---

## Performance Metrics — All Portfolios (Smoothed, Primary)

| Portfolio | Ann. Return | Volatility | Sharpe Ratio | Sortino Ratio | Max Drawdown | Total Return |
|---|---|---|---|---|---|---|
| **Baseline 60/40** | 9.46% | 10.54% | 0.769 | 0.94 | −21.72% | 285.2% |
| +Infrastructure | 10.06% | 10.92% | **0.796** | 0.96 | −25.17% | 317.9% |
| +Private Credit | 9.60% | 10.62% | 0.775 | 0.94 | −23.50% | 292.1% |
| +REITs | 10.00% | 12.04% | 0.728 | 0.88 | −25.71% | 314.3% |
| +Real Assets | 9.49% | 10.72% | 0.760 | 0.92 | −23.62% | 286.5% |

---

## Improvement vs. 60/40 Baseline

| Alternative | Return Improvement | Sharpe Improvement | Max DD Change | Vol Change |
|---|---|---|---|---|
| Infrastructure | **+60 bps** | **+0.027** | −3.46% | +0.38% |
| Private Credit | +13 bps | +0.006 | −1.78% | +0.08% |
| REITs | +54 bps | −0.041 | −3.99% | +1.50% |
| Real Assets | +3 bps | −0.009 | −1.90% | +0.18% |

> Infrastructure is the only alternative that improves **both** return (+60 bps) and Sharpe ratio (+0.027) over the baseline.

---

## Crisis Period Performance

### COVID-19 Shock (Feb–Apr 2020)

| Portfolio | Cumulative Return | Max Drawdown |
|---|---|---|
| Baseline 60/40 | −3.59% | −21.72% |
| +Infrastructure | −6.21% | −25.17% |
| +Private Credit | −4.45% | −23.50% |
| +REITs | −5.77% | −25.71% |
| +Real Assets | −5.66% | −23.62% |

*All alternatives underperformed baseline during COVID — equity selloff dominated.*

### 2022 Inflation Shock (Jan–Dec 2022)

| Portfolio | Cumulative Return | Max Drawdown | Volatility |
|---|---|---|---|
| **+Infrastructure** | **−14.36%** | −19.96% | 16.02% |
| +Real Assets | −14.56% | **−19.35%** | **15.74%** |
| +Private Credit | −14.61% | −19.37% | 15.74% |
| **Baseline 60/40** | −15.62% | −20.32% | 15.87% |
| +REITs | −17.02% | −22.12% | 17.62% |

> Infrastructure, Real Assets, and Private Credit all **outperformed the baseline** in the 2022 inflation regime. REITs significantly underperformed. This is the key stress test for inflation protection.

---

## Final Scoring Matrix (Weighted Multi-Criteria)

**Criteria weights:** Return 25% | Sharpe 25% | Max Drawdown 20% | Correlation 15% | Implementation 15%

| Alternative | Return | Sharpe | Max DD | Correlation | Implementation | **Total / 5** |
|---|---|---|---|---|---|---|
| **Infrastructure** | 5 | 5 | 2 | 4 | 3 | **3.95** |
| Private Credit | 3 | 4 | 4 | 5 | 4 | **3.90** |
| REITs | 4 | 1 | 1 | 4 | 5 | **2.80** |
| Real Assets | 2 | 2 | 3 | 5 | 2 | **2.65** |

---

## Sensitivity Analysis: Smoothing Assumption

| Scenario | Winner | Sharpe |
|---|---|---|
| Smoothed (primary / realistic) | **Infrastructure** | 0.796 |
| Unadjusted (pessimistic / public proxy) | **Private Credit** | 0.762 |

⚠️ **Sensitivity detected.** The winner changes depending on smoothing assumptions → **MODERATE CONFIDENCE** in Infrastructure recommendation. Private Credit is the conservative fallback.

| Alternative | Smoothed Sharpe | Unadjusted Sharpe | Benefit from Smoothing |
|---|---|---|---|
| Infrastructure | 0.796 | 0.735 | +0.061 |
| Real Assets | 0.760 | 0.716 | +0.044 |
| Private Credit | 0.775 | 0.762 | +0.013 |
| REITs | 0.728 | 0.728 | 0.000 |

---

## Final Recommendation

**Recommended:** Infrastructure (IGF proxy) — 10% allocation  
**New portfolio:** 60% Equity / 30% Bonds / 10% Infrastructure

| Metric | Baseline 60/40 | Enhanced Portfolio | Change |
|---|---|---|---|
| Annualized Return | 9.46% | 10.06% | **+60 bps** |
| Sharpe Ratio | 0.769 | 0.796 | **+0.027** |
| Max Drawdown | −21.72% | −25.17% | −3.46% |
| Volatility | 10.54% | 10.92% | +0.38% |

---

## Is This Conclusion Sensible? Critical Assessment

### ✅ What the Analysis Gets Right

**Infrastructure as the winner is directionally sound.** Academic and institutional literature broadly supports infrastructure's role in long-duration pension portfolios. Its inflation-linked revenues (regulated utilities, toll roads, airports), long-duration cash flows, and moderate equity-like returns align well with pension liability profiles. The +60 bps return improvement with only +38 bps additional volatility is a favourable trade-off.

**2022 stress test is the right lens.** Testing alternatives through the 2022 inflation-rate shock is exactly the right question for a pension fund — this was the precise regime where traditional 60/40 failed. Infrastructure's relative outperformance here (+1.26% vs baseline) is consistent with its real-asset, regulated-revenue characteristics.

**Smoothing adjustment is methodologically appropriate.** Applying Geltner-style smoothing to match private market experience is a well-established technique (Geltner 1991, 1993; NCREIF literature). Without it, public proxies would artificially penalise illiquid alternatives.

### ⚠️ Where the Analysis Has Limitations

**Public ETF proxies are imperfect substitutes for private infrastructure.** IGF holds listed infrastructure equities globally, not private unlisted infrastructure funds. Actual private infrastructure (brownfield assets, PPP projects) has meaningfully different characteristics — lower correlation to public equities, smoother cash flows, and higher illiquidity premium. The smoothing adjustment partially corrects for this, but structural differences remain.

**The analysis period (2011–2026) is dominated by a bull equity market.** Infrastructure's Sharpe advantage may be partly a function of beta to a rising equity cycle rather than genuine diversification. A longer data series including the 2000–2002 or 2007–2009 cycles would strengthen the case.

**The max drawdown trade-off is a real concern.** Infrastructure worsened max drawdown by −3.46% (−21.72% → −25.17%). For a pension fund with liability constraints, this is not a trivial caveat — it should be explicitly flagged to the board alongside the return improvement.

**Sensitivity analysis reveals fragility.** Infrastructure only wins under the smoothed (realistic private market) assumption. Under unadjusted public proxy volatility, Private Credit wins. This moderate confidence finding should inform how strongly the recommendation is presented.

**Private Credit's case is underappreciated.** At a scoring margin of only 0.05 points, Private Credit is effectively tied with Infrastructure. Its floating-rate structure, superior max drawdown profile, and consistent performance under both smoothed and unadjusted scenarios make it arguably the more conservative and implementable first alternative — especially given lower governance complexity.

### Bottom Line

The Infrastructure recommendation is **sensible but not unambiguous.** It is the right answer if the fund believes in private market smoothing, has the governance capacity for illiquid alternatives, and prioritises inflation protection and Sharpe improvement. If the fund is more conservative or implementation-constrained, **Private Credit at 3.90/5.00 is nearly equivalent and lower-risk to execute.** The two should be presented to the board as co-finalists, not a clear-cut single winner.

---

*Data sources: Yahoo Finance public ETFs (SPY, AGG, IGF, BKLN, VNQ, DBA, WOOD, DBC, BIL). Analysis period March 2011–February 2026. All results use appraisal-smoothed returns as primary scenario. This analysis uses public market proxies and should be validated against private market benchmarks (e.g., Preqin, MSCI Infrastructure) before a final allocation decision.*
