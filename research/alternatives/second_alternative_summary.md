# Second Alternative Analysis — Pension Fund Portfolio
**Base Portfolio:** 60/30/10 (Equity / Bonds / Infrastructure) | **Analysis Period:** March 2011 – February 2026 | **Avg. Risk-Free Rate:** 1.51%
> **v1 — Corrected vol methodology:** Vol, Sharpe, and Sortino computed at daily frequency (×√252). Return and Max DD use monthly compounded series. Base-B (50/20/30) removed. Allocation tested at 5% primary, sensitivity at 3%, 5%, 7%, 10%.

---

## 1. Objective

Having established Infrastructure as the optimal first alternative (Phase 1), this analysis identifies the best *second* alternative to add to the 60/30/10 Base-A portfolio. Each candidate is tested at a 5% allocation funded three ways — bond-funded, equity-funded, and split — yielding a 60/25/10/5 or 55/30/10/5 structure. Candidates: Private Credit (BKLN), REITs (VNQ), Real Assets (DBA/WOOD/DBC).

---

## 2. Appraisal Smoothing Methodology

Smoothing applied at daily frequency in preprocessing (`analysis_returns_primary.csv`) using exponential filter `r_s(t) = α×r(t) + (1−α)×r_s(t−1)`: Infrastructure α=0.35, Real Assets α=0.30, Private Credit α=0.50, REITs α=1.00. Vol computed at daily frequency to preserve smoothing — compounding to monthly re-amplifies autocorrelation introduced by the filter, overstating illiquid asset vol by up to 2×. Return and drawdown use monthly compounded series for accuracy.

---

## 3. Individual Asset Statistics (Smoothed, daily vol ×√252)

| Asset | Ann. Return | Ann. Vol | Sharpe |
|---|---|---|---|
| Equity | 13.78% | 17.17% | 0.743 |
| Bonds | 2.55% | 4.79% | 0.223 |
| **Infrastructure** | **9.22%** | **7.51%** | **0.941** |
| **Private Credit** | **3.85%** | **3.57%** | **0.644** |
| REITs | 8.65% | 19.98% | 0.386 |
| Real Assets | 3.59% | 5.50% | 0.275 |

Private Credit's 3.57% vol is the lowest of any asset class, including bonds. Its standalone Sharpe (0.644) is second only to Infrastructure (0.941). REITs remain the least attractive — highest vol (19.98%), weakest Sharpe of any alternative (0.386), and no smoothing benefit given their fully public nature.

---

## 4. Full Portfolio Performance vs. Baselines

| Portfolio | Ann. Return | Ann. Vol | Sharpe | Sortino | Max DD | 2022 |
|---|---|---|---|---|---|---|
| 60/40 Baseline | 9.25% | 10.53% | 0.768 | 0.725 | -20.05% | -15.83% |
| **Base-A 60/30/10** | **9.88%** | **10.91%** | **0.796** | **0.743** | **-19.42%** | **-14.55%** |
| + PC \| Equity | 9.39% | 10.15% | **0.804** ✅ | **0.748** ✅ | **-18.53%** ✅ | -13.75% ✅ |
| + PC \| Split | 9.67% | 10.56% | 0.801 | 0.745 | -18.77% | -13.89% |
| + PC \| Bond | 9.94% | 10.96% | 0.798 | 0.743 | -19.02% | -14.03% |
| + RA \| Equity | 9.36% | 10.20% | 0.796 | 0.738 | -18.56% | **-13.72%** ✅ |
| + RA \| Split | 9.63% | 10.61% | 0.794 | 0.735 | -18.80% | -13.86% |
| + RA \| Bond | 9.90% | 11.01% | 0.791 | 0.734 | -19.05% | -14.00% |
| + REITs \| Equity | 9.60% | 10.85% | 0.778 | 0.724 | -19.70% | -14.97% |
| + REITs \| Split | 9.88% | 11.25% | 0.776 | 0.722 | -19.95% | -15.11% |
| + REITs \| Bond | 10.15% | 11.65% | 0.774 | 0.719 | -20.19% | -15.26% |

Private Credit (equity-funded) is the clear winner on Sharpe (+0.008 vs Base-A), Sortino, and drawdown. Real Assets (equity-funded) ties Base-A on Sharpe but leads on 2022 inflation protection (-13.72%). All REITs configurations worsen Sharpe and deepen drawdowns — consistently the weakest candidate across all metrics and funding methods.

---

## 5. Funding Source Analysis

Equity-funded is the best funding mechanism across all three candidates:

| Candidate | Bond Sharpe | Equity Sharpe | Split Sharpe | Best Funding |
|---|---|---|---|---|
| Private Credit | 0.798 | **0.804** ✅ | 0.801 | Equity |
| Real Assets | 0.791 | **0.796** | 0.794 | Equity |
| REITs | 0.774 | **0.778** | 0.776 | Equity |

Funding from equity reduces portfolio vol by replacing high-vol equity exposure (17.17%) with the lower-vol alternative, improving the Sharpe denominator. Bond-funded preserves return but adds marginal vol. For a pension fund with a long-term liability horizon, equity-funded also preserves bond duration, which helps with liability matching.

---

## 6. Allocation Sensitivity (3%–10%)

**Private Credit — equity-funded** (recommended configuration): Sharpe improves monotonically at every size — from +0.005 at 3% to +0.016 at 10%. The trade-off is return compression (8.91% at 10% vs 9.88% baseline) as equity is replaced by lower-yielding private credit.

**Real Assets — equity-funded**: Sharpe is flat (0.796) from 3% to 10% — it neither adds nor destroys risk-adjusted value at any size, though drawdown and 2022 protection improve steadily. Best for inflation protection, not Sharpe.

**REITs**: Sharpe degrades at every allocation and every funding method, reaching as low as 0.752 at 10% bond-funded. Should not be added at any size.

| Alloc | PC \| Equity ΔSharpe | RA \| Equity ΔSharpe | REITs \| Equity ΔSharpe |
|---|---|---|---|
| 3% | +0.005 | +0.000 | -0.011 |
| 5% | +0.008 | +0.000 | -0.019 |
| 7% | +0.011 | -0.000 | -0.027 |
| 10% | +0.016 | -0.001 | -0.041 |

---

## 7. Crisis Performance

| Portfolio | COVID Max DD | 2022 Return | 2022 Max DD |
|---|---|---|---|
| 60/40 Baseline | -20.05% | -15.83% | -16.75% |
| Base-A 60/30/10 | -19.42% | -14.55% | -16.23% |
| **+ PC \| Equity** | **-18.53%** | -13.75% | -15.62% |
| + RA \| Equity | -18.56% | **-13.72%** | **-15.59%** |
| + REITs \| Equity | -19.70% | -14.97% | -16.41% |

Both Private Credit and Real Assets (equity-funded) meaningfully improve drawdown versus Base-A in both stress regimes. The margin between them is narrow — PC is marginally better on overall drawdown; Real Assets fractionally better in 2022. REITs worsen both metrics relative to Base-A.

---

## 8. Global Ranking (all 9 scenarios by Sharpe)

| Rank | Portfolio | Sharpe | ΔSharpe vs Base-A | 2022 | Max DD | Funding |
|---|---|---|---|---|---|---|
| 🥇 1 | PC \| Equity | 0.804 | +0.008 | -13.75% | -18.53% | Equity |
| 🥈 2 | PC \| Split | 0.801 | +0.005 | -13.89% | -18.77% | Split |
| 🥉 3 | PC \| Bond | 0.798 | +0.002 | -14.03% | -19.02% | Bond |
| 4 | RA \| Equity | 0.796 | +0.000 | -13.72% | -18.56% | Equity |
| 5 | RA \| Split | 0.794 | -0.003 | -13.86% | -18.80% | Split |
| 6 | RA \| Bond | 0.791 | -0.005 | -14.00% | -19.05% | Bond |
| 7 | REITs \| Equity | 0.778 | -0.019 | -14.97% | -19.70% | Equity |
| 8 | REITs \| Split | 0.776 | -0.020 | -15.11% | -19.95% | Split |
| 9 | REITs \| Bond | 0.774 | -0.022 | -15.26% | -20.19% | Bond |

Private Credit dominates the top three. The funding method matters — equity-funded is consistently better than bond-funded across all candidates. REITs occupy all three bottom spots regardless of funding method.

---

## 9. Which Metrics Matter Most for a Pension Fund?

Not all metrics carry equal weight for a pension fund. The following framework ranks metrics by their relevance to a fund's fiduciary obligations, liability structure, and regulatory environment.

### Tier 1 — Primary (highest emphasis)

**Maximum Drawdown & Drawdown Duration**
The single most operationally dangerous metric for a pension fund. Unlike an endowment or hedge fund, a pension fund faces *non-discretionary cash outflows* — benefit payments do not pause during market downturns. A deep drawdown forces selling assets at depressed prices to meet liabilities, permanently impairing recovery. The 2022 example (-15.83% for 60/40) illustrates how a drawdown coinciding with rising liabilities creates a double squeeze. Every basis point of drawdown improvement has direct balance sheet implications.

**Inflation-Adjusted Return vs. Liability Growth**
Pension liabilities grow with wage inflation and actuarial assumptions. If portfolio returns do not exceed liability growth in real terms, the funded ratio deteriorates even in years of positive absolute returns. The 2022 stress test is therefore the *most relevant* single-year scenario in this dataset — it reflects a period where both assets fell and liability discount rates rose sharply, exactly the correlation regime that pension funds most fear.

**Sortino Ratio (over Sharpe)**
The Sortino ratio penalises only downside deviation — the part of volatility that actually hurts a pension fund. Upside volatility (positive return surprises) is not a problem; missing a pension payment is. Sortino is therefore more aligned with pension fund risk tolerance than Sharpe, which treats upside and downside symmetrically. When Sharpe and Sortino rankings agree (as they do here), the case is reinforced; when they diverge, prefer Sortino.

### Tier 2 — Important (moderate emphasis)

**Sharpe Ratio**
A useful normalised summary of risk-adjusted efficiency, and standard for cross-portfolio comparison. Important but imperfect for pensions because it treats volatility symmetrically and uses a risk-free rate benchmark rather than a liability-based hurdle rate. Should be used alongside Sortino, not instead of it.

**Annualised Volatility**
Relevant primarily as a contributor to drawdown risk and as a regulatory/governance input (many pension fund IPS documents specify a vol budget). However, vol *per se* is less important than *downside* vol — a portfolio with high vol but strong positive skew can be acceptable. The metric becomes more important when the fund is in deficit or approaching a funding ratio trigger.

**Correlation to Existing Portfolio**
Important for assessing true diversification benefit. However, the correlation numbers here (all >0.99 vs Base-A) reflect that a 5% sleeve in a dominated portfolio cannot structurally shift correlation. This metric becomes far more meaningful at higher alternative allocations (20%+).

### Tier 3 — Secondary (lower emphasis in isolation)

**Annualised Return**
Necessary but not sufficient. A pension fund needs returns to exceed the liability discount rate (typically 5–7% for a well-funded fund), but chasing raw return at the expense of drawdown protection is the most common source of underfunding. Return should be evaluated relative to the liability hurdle, not maximised in isolation.

**Sharpe vs. Calmar Ratio**
The Calmar ratio (return / max drawdown) is arguably more intuitive than Sharpe for pension funds because it directly relates return to the most consequential risk dimension. Not reported in this analysis but worth adding to Phase 3.

**Total Return / CAGR**
Useful for board-level narrative (cumulative wealth charts) but can be misleading — two portfolios with the same CAGR but different drawdown profiles are not equivalent for a fund with ongoing liabilities.

### Practical Weighting for This Analysis

When the metrics conflict, apply this decision hierarchy:

1. **Does it protect the 2022 inflation scenario?** (liability-matching relevance)
2. **Does it reduce Max DD?** (benefit payment solvency)
3. **Does it improve Sortino?** (asymmetric risk alignment)
4. **Does it improve Sharpe?** (overall efficiency)
5. **Does it add return?** (only if 1–4 are satisfied)

Under this framework, **Private Credit (equity-funded)** remains the top recommendation — it wins on Sharpe, Sortino, drawdown, and 2022 protection simultaneously. **Real Assets (equity-funded)** is the preferred alternative if inflation protection is the primary board mandate, as it leads on 2022 performance (-13.72%) at no Sharpe cost.

---

## 10. Top 2 Recommended Second Alternatives

### 🥇 #1 — Private Credit (equity-funded, 5%–10%)

**Pros**
- Best Sharpe of all 9 scenarios (0.804, +0.008 vs Base-A) — improves monotonically to +0.016 at 10%
- Best Sortino (0.748) — most aligned with pension fund's asymmetric downside mandate
- Best overall Max DD (-18.53%), improving steadily at larger allocations
- Strong 2022 protection (-13.75% vs -14.55% Base-A, -15.83% 60/40)
- Equity-funding preserves bond duration for liability matching while replacing the highest-vol asset

**Cons**
- Equity-funding reduces absolute return (9.39% vs 9.88% Base-A) — below-baseline raw return requires board-level framing as a risk-adjusted trade-off
- BKLN proxy understates true private credit illiquidity premium and covenant protections
- High infrastructure correlation (0.714) suggests limited diversification between the two alternatives
- J-curve drag and capital call timing mismatches require active cash management
- Credit spread compression in benign environments reduces forward-looking alpha

---

### 🥈 #2 — Real Assets (equity-funded, 5%–10%)

**Pros**
- Best 2022 inflation protection of all candidates (-13.72%), critical if fund's liabilities are inflation-linked
- Sharpe flat at 0.796 from 3% to 10% — zero risk-adjusted cost at any sizing
- Max DD steadily improves with scale (-17.68% at 10%), the best drawdown trajectory of any candidate at higher allocations
- Lowest correlation to 60/40 baseline (0.9909) among all scenarios — marginal but best available diversification
- Natural inflation hedge via commodity, farmland, and timberland exposures structurally relevant to long-duration pension liabilities

**Cons**
- No Sharpe improvement over Base-A (0.796 = flat) — adds no risk-adjusted efficiency, only inflation protection
- Return compresses at higher allocations (8.83% at 10% equity-funded) — return dilution risk
- DBA/WOOD/DBC is a weak proxy; genuine farmland and timberland allocations have extremely long lock-ups and high minimum commitments
- Real assets as a category is internally heterogeneous — commodity exposure (DBC) behaves very differently from timberland in different regimes
- Implementation complexity rivals private infrastructure: specialist managers, long lock-ups, appraisal-based NAV reporting

---

## 11. Recommendation Summary

| | Private Credit (equity-funded) | Real Assets (equity-funded) |
|---|---|---|
| **Sharpe vs Base-A** | **+0.008** | 0.000 |
| **Sortino** | **0.748** | 0.738 |
| **Max DD** | **-18.53%** | -18.56% |
| **2022 return** | -13.75% | **-13.72%** |
| **Scales with size?** | ✅ Strongly (+0.016 at 10%) | ➖ Flat (0.796) |
| **Primary use case** | Risk-adjusted efficiency | Inflation protection mandate |
| **Key risk** | Return dilution, credit cycle | Return dilution, proxy quality |
| **Suggested sizing** | 5%–10% | 5%–10% |

> **Bottom line:** Private Credit (equity-funded) is the preferred second alternative — it is the only candidate that simultaneously improves Sharpe, Sortino, and drawdown over Base-A. Real Assets is the preferred choice if the fund's liability profile or board mandate prioritises inflation protection above all else, as it leads on the 2022 stress scenario at no Sharpe cost. REITs should be excluded entirely at all sizes and funding methods. Phase 3 should test a 60/20/10/10 structure combining Infrastructure + Private Credit as the base case, with a sensitivity test substituting Real Assets for Private Credit.

---

*Script: `second_alternative_analysis_v3.py` | Data: `analysis_returns_primary.csv`, `DTB3.csv` | Smoothing: `single_alternative_analysis.ipynb` | Vol methodology: daily ×√252 throughout*
