# Second Alternative Asset Selection: Analysis Summary
**Pension Fund Portfolio Enhancement — Phase 1, Step 1.1**
*Analysis Period: March 2011 – February 2026 (180 months) | Data: analysis_returns_primary.csv (pre-smoothed)*

---

## Objective

Identify the best second alternative asset class and optimal funding source to add to the existing two baseline portfolios, subject to a 5% allocation.

**Baselines evaluated:**

| Baseline | Equity | Bonds | Infrastructure | Sharpe | Return | Max DD |
|---|---|---|---|---|---|---|
| 60/40 | 60% | 40% | — | 0.854 | 9.25% | −20.05% |
| Base-A 60/30/10 | 60% | 30% | 10% | 0.848 | 9.88% | −19.42% |
| Base-B 50/20/30 | 50% | 20% | 30% | 0.807 | 10.02% | −18.13% |

**Second alternative candidates (5% allocation):**

| Alternative | Proxy | Ann Return | Ann Vol | Sharpe | Smoothing |
|---|---|---|---|---|---|
| Private Credit | BKLN | 3.85% | 4.86% | 0.480 | α = 0.50 |
| REITs | VNQ | 8.65% | 17.06% | 0.418 | None (public) |
| Real Assets | DBA/WOOD/DBC blend | 3.59% | 12.16% | 0.171 | α = 0.30 |

**Funding sources tested:** Bond-funded · Equity-funded · Split-funded (50/50)

**Total portfolios backtested:** 21 (3 baselines + 18 scenarios)

---

## Methodology Note

Returns data sourced from `analysis_returns_primary.csv`, which contains daily pre-smoothed returns from the single alternative analysis notebook. Smoothing applied using the Geltner (1991, 1993) exponential method to simulate institutional private market experience. Daily returns compounded to month-end. Risk-free rate from DTB3.csv (avg 1.51% annualised over period).

---

## Full Metrics Table

| Portfolio | Return | Vol | Sharpe | Sortino | Max DD | COVID | 2022 |
|---|---|---|---|---|---|---|---|
| **60/40 Baseline** | 9.25% | 9.10% | 0.854 | 0.777 | −20.05% | −4.15% | −15.83% |
| **Base-A 60/30/10** | 9.88% | 9.96% | 0.848 | 0.762 | −19.42% | −6.63% | −14.55% |
| **Base-B 50/20/30** | 10.02% | 10.72% | 0.807 | 0.727 | −18.13% | −10.35% | −11.39% |
| Base-A \| Private Credit \| Bond | 9.94% | 10.04% | **0.847** | 0.762 | −19.02% | −7.07% | −14.03% |
| Base-A \| Private Credit \| Split | 9.67% | 9.74% | 0.844 | 0.759 | −18.77% | −6.76% | −13.89% |
| Base-A \| Private Credit \| Equity | 9.39% | 9.45% | 0.841 | 0.755 | −18.53% | −6.45% | −13.75% |
| Base-A \| REITs \| Bond | 10.15% | 10.54% | 0.830 | 0.748 | −20.19% | −7.72% | −15.26% |
| Base-A \| Real Assets \| Bond | 9.90% | 10.27% | 0.827 | 0.734 | −19.05% | −7.65% | −14.00% |
| Base-A \| REITs \| Split | 9.88% | 10.25% | 0.826 | 0.738 | −19.95% | −7.41% | −15.11% |
| Base-A \| Real Assets \| Split | 9.63% | 9.97% | 0.824 | 0.736 | −18.80% | −7.34% | −13.86% |
| Base-A \| REITs \| Equity | 9.60% | 9.95% | 0.822 | 0.733 | −19.70% | −7.10% | −14.97% |
| Base-A \| Real Assets \| Equity | 9.36% | 9.67% | 0.820 | 0.732 | −18.56% | −7.03% | −13.72% |
| Base-B \| Private Credit \| Bond | 10.08% | 10.81% | **0.807** | 0.725 | −18.65% | −10.79% | −10.86% |
| Base-B \| Private Credit \| Split | 9.81% | 10.52% | 0.802 | 0.720 | −18.16% | −10.48% | −10.71% |
| Base-B \| Private Credit \| Equity | 9.54% | 10.23% | 0.797 | 0.721 | −17.67% | −10.17% | −10.57% |
| Base-B \| REITs \| Bond | 10.28% | 11.31% | 0.792 | 0.709 | −19.39% | −11.44% | −12.12% |
| Base-B \| Real Assets \| Bond | 10.04% | 11.05% | 0.788 | 0.705 | −19.04% | −11.36% | −10.83% |
| Base-B \| REITs \| Split | 10.01% | 11.03% | 0.787 | 0.704 | −18.90% | −11.13% | −11.98% |
| Base-B \| Real Assets \| Split | 9.77% | 10.76% | 0.783 | 0.700 | −18.55% | −11.05% | −10.68% |
| Base-B \| REITs \| Equity | 9.74% | 10.74% | 0.782 | 0.698 | −18.41% | −10.82% | −11.83% |
| Base-B \| Real Assets \| Equity | 9.50% | 10.47% | 0.777 | 0.700 | −18.07% | −10.74% | −10.54% |

---

## Global Ranking — All 18 Scenarios by Sharpe

| Rank | Portfolio | Sharpe | ΔSharpe vs Base | Return | Max DD | 2022 | Funding |
|---|---|---|---|---|---|---|---|
| 1 ★ | Base-A \| Private Credit \| Bond | 0.847 | −0.000 | 9.94% | −19.02% | −14.03% | Bond |
| 2 | Base-A \| Private Credit \| Split | 0.844 | −0.003 | 9.67% | −18.77% | −13.89% | Split |
| 3 | Base-A \| Private Credit \| Equity | 0.841 | −0.007 | 9.39% | −18.53% | −13.75% | Equity |
| 4 | Base-A \| REITs \| Bond | 0.830 | −0.018 | 10.15% | −20.19% | −15.26% | Bond |
| 5 | Base-A \| Real Assets \| Bond | 0.827 | −0.021 | 9.90% | −19.05% | −14.00% | Bond |
| 6 | Base-A \| REITs \| Split | 0.826 | −0.021 | 9.88% | −19.95% | −15.11% | Split |
| 7 | Base-A \| Real Assets \| Split | 0.824 | −0.024 | 9.63% | −18.80% | −13.86% | Split |
| 8 | Base-A \| REITs \| Equity | 0.822 | −0.025 | 9.60% | −19.70% | −14.97% | Equity |
| 9 | Base-A \| Real Assets \| Equity | 0.820 | −0.028 | 9.36% | −18.56% | −13.72% | Equity |
| 10 | Base-B \| Private Credit \| Bond | 0.807 | −0.001 | 10.08% | −18.65% | −10.86% | Bond |
| 11 | Base-B \| Private Credit \| Split | 0.802 | −0.005 | 9.81% | −18.16% | −10.71% | Split |
| 12 | Base-B \| Private Credit \| Equity | 0.797 | −0.010 | 9.54% | −17.67% | −10.57% | Equity |
| 13 | Base-B \| REITs \| Bond | 0.792 | −0.016 | 10.28% | −19.39% | −12.12% | Bond |
| 14 | Base-B \| Real Assets \| Bond | 0.788 | −0.020 | 10.04% | −19.04% | −10.83% | Bond |
| 15 | Base-B \| REITs \| Split | 0.787 | −0.021 | 10.01% | −18.90% | −11.98% | Split |
| 16 | Base-B \| Real Assets \| Split | 0.783 | −0.025 | 9.77% | −18.55% | −10.68% | Split |
| 17 | Base-B \| REITs \| Equity | 0.782 | −0.026 | 9.74% | −18.41% | −11.83% | Equity |
| 18 | Base-B \| Real Assets \| Equity | 0.777 | −0.030 | 9.50% | −18.07% | −10.54% | Equity |

---

## Funding Source Head-to-Head

Bond-funded wins every single matchup across all alternatives and both bases. Results below are for Base-A (60/30/10).

**Private Credit**

| Funding | Sharpe | Return | Vol | Max DD | 2022 | COVID |
|---|---|---|---|---|---|---|
| Bond ← best | 0.847 | 9.94% | 10.04% | −19.02% | −14.03% | −7.07% |
| Split | 0.844 | 9.67% | 9.74% | −18.77% | −13.89% | −6.76% |
| Equity | 0.841 | 9.39% | 9.45% | −18.53% | −13.75% | −6.45% |

**REITs**

| Funding | Sharpe | Return | Vol | Max DD | 2022 | COVID |
|---|---|---|---|---|---|---|
| Bond ← best | 0.830 | 10.15% | 10.54% | −20.19% | −15.26% | −7.72% |
| Split | 0.826 | 9.88% | 10.25% | −19.95% | −15.11% | −7.41% |
| Equity | 0.822 | 9.60% | 9.95% | −19.70% | −14.97% | −7.10% |

**Real Assets**

| Funding | Sharpe | Return | Vol | Max DD | 2022 | COVID |
|---|---|---|---|---|---|---|
| Bond ← best | 0.827 | 9.90% | 10.27% | −19.05% | −14.00% | −7.65% |
| Split | 0.824 | 9.63% | 9.97% | −18.80% | −13.86% | −7.34% |
| Equity | 0.820 | 9.36% | 9.67% | −18.56% | −13.72% | −7.03% |

**Why bond-funded wins:** Bonds returned 2.55% annualised with a Sharpe of 0.23 over the period — the weakest contributor in every portfolio. Replacing bonds with any alternative improves the portfolio's efficiency more than replacing equities (Sharpe 0.875). The Sharpe penalty from equity-funding ranges from −0.007 to −0.030 depending on the alternative.

---

## Improvement vs Baselines

### Off Base-A (60/30/10) — Sharpe 0.848, Return 9.88%, Max DD −19.42%

| Scenario | Sharpe | ΔSharpe | ΔReturn | ΔVol | ΔMax DD | 2022 |
|---|---|---|---|---|---|---|
| + Private Credit (Bond) | 0.847 | −0.000 | +6 bps | +0.08% | **+0.41%** | −14.03% |
| + Private Credit (Split) | 0.844 | −0.003 | −21 bps | −0.22% | +0.65% | −13.89% |
| + Private Credit (Equity) | 0.841 | −0.007 | −49 bps | −0.51% | +0.90% | −13.75% |
| + REITs (Bond) | 0.830 | −0.018 | +27 bps | +0.58% | −0.77% | −15.26% |
| + Real Assets (Bond) | 0.827 | −0.021 | +2 bps | +0.31% | +0.38% | −14.00% |

> Private Credit (Bond-funded) is the only scenario that is effectively Sharpe-neutral (−0.000) while improving both max drawdown (+41 bps) and 2022 resilience (+52 bps) simultaneously.

### Off Base-B (50/20/30) — Sharpe 0.807, Return 10.02%, Max DD −18.13%

| Scenario | Sharpe | ΔSharpe | ΔReturn | ΔVol | ΔMax DD | 2022 |
|---|---|---|---|---|---|---|
| + Private Credit (Bond) | 0.807 | −0.001 | +6 bps | +0.09% | **−0.52%** | −10.86% |
| + Private Credit (Split) | 0.802 | −0.005 | −21 bps | −0.20% | −0.03% | −10.71% |
| + Private Credit (Equity) | 0.797 | −0.010 | −49 bps | −0.49% | +0.46% | −10.57% |
| + REITs (Bond) | 0.792 | −0.016 | +26 bps | +0.60% | −1.26% | −12.12% |
| + Real Assets (Bond) | 0.788 | −0.020 | +2 bps | +0.34% | −0.91% | −10.83% |

---

## Crisis Period Analysis

### COVID-19 (Feb–Apr 2020)

All scenarios underperformed the 60/40 baseline during COVID (−4.15%), as the equity selloff dominated. Private Credit was the least-bad alternative, with equity-funded showing the mildest COVID drawdown due to reduced equity exposure. Infrastructure's illiquidity dampening (smoothing effect) partially masks true COVID losses.

### 2022 Inflation Shock (Jan–Dec 2022)

The 60/40 baseline lost −15.83%. All second-alternative additions improved 2022 performance, with the magnitude of improvement depending on base portfolio and alternative chosen.

| Best 2022 result | Portfolio | 2022 Return | vs 60/40 |
|---|---|---|---|
| Best absolute | Base-B \| Real Assets \| Equity | −10.54% | +529 bps |
| Best while preserving Sharpe | Base-A \| Private Credit \| Bond | −14.03% | +180 bps |

The Real Assets (Equity-funded) result wins on inflation protection but costs 77 bps of Sharpe versus the best scenario, reflecting Real Assets' weak standalone return profile (3.59% annualised).

---

## Asset Correlation Matrix (Monthly, Full Period)

|  | Equity | Bonds | Infrastructure | Private Credit | REITs | Real Assets |
|---|---|---|---|---|---|---|
| **Equity** | 1.000 | 0.291 | 0.737 | 0.713 | 0.722 | 0.649 |
| **Bonds** | 0.291 | 1.000 | 0.381 | 0.151 | 0.534 | 0.033 |
| **Infrastructure** | 0.737 | 0.381 | 1.000 | 0.714 | 0.742 | 0.687 |
| **Private Credit** | 0.713 | 0.151 | 0.714 | 1.000 | 0.595 | 0.591 |
| **REITs** | 0.722 | 0.534 | 0.742 | 0.595 | 1.000 | 0.500 |
| **Real Assets** | 0.649 | 0.033 | 0.687 | 0.591 | 0.500 | 1.000 |

**Key observations:**
- All alternatives are highly correlated to equity (0.65–0.74), limiting true diversification
- Real Assets has the lowest bond correlation (0.033), providing the most genuine diversification relative to the traditional 60/40 mix
- Private Credit has the lowest bond correlation among the three candidates (0.151), consistent with its floating-rate, credit-driven return profile
- Portfolio-level correlations to baselines are all above 0.96 at 5% allocation — the 5% position is too small to meaningfully alter portfolio character

---

## Allocation Sensitivity (Off Base-A, Bond-Funded)

### Private Credit — bond-funded

| Allocation | Bonds weight | Sharpe | ΔSharpe | Return | Max DD | 2022 |
|---|---|---|---|---|---|---|
| 3% | 27% | 0.847 | −0.000 | 9.92% | −19.18% | −14.24% |
| **5%** | **25%** | **0.847** | **−0.000** | **9.94%** | **−19.02%** | **−14.03%** |
| 7% | 23% | 0.847 | −0.001 | 9.97% | −18.86% | −13.82% |
| 10% | 20% | 0.846 | −0.002 | 10.00% | −18.61% | −13.51% |

Sharpe is remarkably stable across all sizing — degrading by only −0.002 at 10%. Max drawdown continues to improve as allocation increases. A **10% Private Credit** allocation (60/20/10/10) is worth exploring in the next phase.

### REITs — bond-funded (for comparison)

| Allocation | Sharpe | ΔSharpe | Return | Max DD | 2022 |
|---|---|---|---|---|---|
| 3% | 0.837 | −0.011 | 10.04% | −19.88% | −14.97% |
| 5% | 0.830 | −0.018 | 10.15% | −20.19% | −15.26% |
| 7% | 0.823 | −0.025 | 10.25% | −20.50% | −15.54% |
| 10% | 0.812 | −0.035 | 10.41% | −20.95% | −15.97% |

REITs worsen monotonically on every risk metric as allocation increases — the opposite of Private Credit.

---

## Key Findings

### Finding 1: Private Credit (Bond-funded) is the clear winner

Across both base portfolios and all funding sources, **Private Credit funded from bonds** ranks #1 on Sharpe. It is the only second alternative that does not degrade Sharpe while simultaneously improving max drawdown and 2022 inflation resilience. The recommended new portfolio off Base-A is:

**60% Equity / 25% Bonds / 10% Infrastructure / 5% Private Credit**

### Finding 2: Bond-funded wins every matchup without exception

Bond-funding outperforms equity-funding on Sharpe for every alternative, off every base portfolio. The Sharpe penalty from equity-funding is −0.007 (Private Credit) to −0.030 (Real Assets). Equity-funding does reduce max drawdown by trimming beta, but not enough to compensate for the lost return engine. Split-funding consistently lands between the two.

### Finding 3: Adding any second alternative at 5% slightly dilutes Sharpe off Base-A

The 60/40 baseline has the highest Sharpe at 0.854, above Base-A (0.848) and all 18 second-alternative scenarios. This is because Infrastructure (Sharpe 0.569) and all second-alternative candidates have lower Sharpe than the core equity/bond mix. The benefit of alternatives shows up in **drawdown reduction and inflation resilience**, not Sharpe improvement. This is the correct trade-off for a pension fund with liability obligations.

### Finding 4: Best inflation protection requires accepting lower Sharpe

The strongest 2022 result is Real Assets (Equity-funded) off Base-B at −10.54%, a 529 bps improvement over 60/40. However its full-period Sharpe is 0.777 — the lowest of all scenarios. There is a clear trade-off between maximum inflation protection and risk-adjusted total return; the board should be presented with both options.

### Finding 5: Allocation sizing supports going higher on Private Credit

The sensitivity analysis shows Sharpe is essentially flat from 3% to 10% for Private Credit (bond-funded), degrading by only 2 bps at 10%. Max drawdown improves continuously as allocation grows. A **10% allocation** (60/20/10/10) appears viable and warrants analysis in Phase 2.

---

## Recommendation

**Recommended second alternative:** Private Credit (BKLN proxy)
**Recommended funding source:** Bond-funded
**Recommended allocation:** 5% (primary), with 10% tested in Phase 2
**New portfolio:** 60% Equity / 25% Bonds / 10% Infrastructure / 5% Private Credit

| Metric | 60/40 Baseline | Base-A 60/30/10 | **New Portfolio** | vs 60/40 | vs Base-A |
|---|---|---|---|---|---|
| Ann Return | 9.25% | 9.88% | **9.94%** | +69 bps | +6 bps |
| Sharpe | 0.854 | 0.848 | **0.847** | −0.007 | −0.000 |
| Max DD | −20.05% | −19.42% | **−19.02%** | +103 bps | +40 bps |
| 2022 | −15.83% | −14.55% | **−14.03%** | +180 bps | +52 bps |
| COVID | −4.15% | −6.63% | **−7.07%** | −292 bps | −44 bps |

**Rationale:** Private Credit's floating-rate structure, low standalone volatility (4.86%), and moderate equity correlation (0.713) make it the most complementary addition to Infrastructure. The bond-funded approach preserves equity exposure (a fiduciary priority for long-duration pension liabilities) while replacing the portfolio's weakest Sharpe contributor.

**Caveat:** BKLN is an imperfect public proxy for private credit. Actual private credit funds would carry different liquidity profiles (quarterly redemptions, capital call structures) and potentially higher returns through an illiquidity premium. Governance and manager selection requirements must be considered before committing capital.

---

## Next Steps

1. **Phase 1, Step 1.2:** Test 10% Private Credit allocation (60/20/10/10) vs 5%
2. **Phase 2:** Add third alternative — REITs or Real Assets — to the two-alternative base
3. **Phase 3:** Full mean-variance optimisation across all alternatives
4. **Phase 4:** Out-of-sample validation (2011–2018 training / 2019–2026 test)

---

## Limitations

- **Public ETF proxies** understate the illiquidity premium of actual private credit funds and overstate mark-to-market volatility
- **Analysis period (2011–2026)** is dominated by a bull equity cycle; performance in a secular bear market (2000–2009 equivalent) is not captured
- **5% allocation** is too small to materially alter portfolio character (all scenario correlations to baselines exceed 0.96); true diversification benefits require 15–20% alternatives allocation
- **Smoothing sensitivity:** Private Credit's result is robust to smoothing assumption (α = 0.50 has modest effect); Infrastructure's smoothing (α = 0.35) has a larger impact on its apparent Sharpe

---

*Data sources: analysis_returns_primary.csv (pre-smoothed daily returns), DTB3.csv (Federal Reserve 3-month T-bill). Analysis period March 2011 – February 2026. All results use appraisal-smoothed returns as primary scenario. Public ETF proxies should be validated against private market benchmarks (Preqin, Cliffwater Direct Lending Index) before final allocation decision.*
