# Backtesting Framework: Testing Improvements to the 60/40 Portfolio

**Date:** February 5, 2026  
**Purpose:** Rigorous methodology to validate alternative asset class additions to traditional 60/40 portfolio  
**Audience:** Investment Strategy Team / Quantitative Analysts

---

## Executive Summary

### The Single Best Improvement

If making only **one improvement** to the 60/40 portfolio:

**Replace 10% of bonds with core-plus infrastructure → 60% Equity / 30% Bonds / 10% Infrastructure**

Infrastructure is the only asset class that simultaneously addresses all three 60/40 vulnerabilities:
- **Diversification:** 0.3-0.5 correlation to 60/40; +8.1% in 2022 while 60/40 fell -17.5%
- **Inflation protection:** CPI escalators deliver 0.7-0.9 inflation beta; +0.1% real return in 2022
- **Liability matching:** 10-15 year cash flows match pension obligations

### Extended Testing

This framework tests all **Top 3 alternatives** (Infrastructure, Private Credit, Real Assets) individually and in combination to identify the optimal allocation.

---

## Part 1: Portfolio Configurations to Test

| Portfolio | Equity | Bonds | Infrastructure | Private Credit | Real Assets | Description |
|-----------|--------|-------|----------------|----------------|-------------|-------------|
| **A (Baseline)** | 60% | 40% | — | — | — | Traditional 60/40 |
| **B (Infra Only)** | 60% | 30% | 10% | — | — | Single best improvement |
| **C (Credit Only)** | 60% | 30% | — | 10% | — | Yield enhancement focus |
| **D (Real Assets Only)** | 60% | 30% | — | — | 10% | Maximum diversification |
| **E (Infra + Credit)** | 60% | 25% | 8% | 7% | — | Tier 1 combination |
| **F (All Three)** | 60% | 22% | 6% | 6% | 6% | Full diversification |
| **G (Optimized)** | 55% | 20% | 10% | 8% | 7% | Aggressive alternatives |

---

## Part 2: Data Requirements

### 2.1 Master Index Table

| Component | Primary Index | Ticker | Backup Index | Backup Ticker | History |
|-----------|---------------|--------|--------------|---------------|---------|
| **US Equity** | S&P 500 Total Return | SPXT | — | — | 1928+ |
| **US Bonds** | Bloomberg US Aggregate | LBUSTRUU | — | — | 1976+ |
| **Infrastructure** | S&P Global Infrastructure | SPGTIND | FTSE Global Core Infra 50/50 | GIIUTD | 2001+ |
| **Private Credit** | S&P/LSTA Leveraged Loan | SPBDAL | Cliffwater Direct Lending Index | CDLI | 1997+ |
| **Real Assets (Timber)** | NCREIF Timberland Index | — | S&P Global Natural Resources | SPGNRUT | 1987+ |
| **Real Assets (Farm)** | NCREIF Farmland Index | — | Invesco DB Agriculture (DBA) | DBA | 1992+ |
| **Inflation** | CPI-U All Urban Consumers | — | — | — | 1913+ |
| **Risk-Free Rate** | 3-Month Treasury Bill | DTB3 | — | — | 1954+ |

### 2.2 Data Sources by Index

#### Free Sources

| Data | Source | URL | Format |
|------|--------|-----|--------|
| S&P 500 Total Return | Yahoo Finance | ^SP500TR | CSV download |
| S&P 500 Total Return | FRED | SP500 (price only) | CSV/API |
| CPI-U | Bureau of Labor Statistics | bls.gov/cpi | CSV download |
| 3-Month T-Bill | FRED | DTB3 | CSV/API |
| High Yield Bonds (proxy) | FRED | BAMLH0A0HYM2 | CSV/API |

#### Subscription/Professional Sources

| Data | Source | Access | Approximate Cost |
|------|--------|--------|------------------|
| Bloomberg US Aggregate | Bloomberg Terminal | Professional | $20,000+/year |
| S&P Global Infrastructure | Bloomberg Terminal | Professional | Included |
| S&P/LSTA Leveraged Loan | Bloomberg Terminal | Professional | Included |
| NCREIF Timberland | NCREIF | Institutional member | $5,000+/year |
| NCREIF Farmland | NCREIF | Institutional member | Included |
| EDHECinfra Infra300 | EDHECinfra | Subscription | $10,000+/year |
| Cliffwater DLI | Cliffwater | Subscription | $5,000+/year |

#### ETF Proxies (Free, Daily Data)

| Asset Class | ETF | Ticker | Expense Ratio | Inception | Limitations |
|-------------|-----|--------|---------------|-----------|-------------|
| US Bonds | iShares Core US Aggregate | AGG | 0.03% | 2003 | Shorter history |
| Infrastructure | iShares Global Infrastructure | IGF | 0.40% | 2007 | Listed only; higher vol |
| Leveraged Loans | Invesco Senior Loan | BKLN | 0.65% | 2011 | Short history |
| High Yield | iShares iBoxx High Yield | HYG | 0.48% | 2007 | Not floating rate |
| Natural Resources | SPDR S&P Global Natural Res | GNR | 0.40% | 2010 | Listed; higher vol |
| Commodities | Invesco DB Commodity | DBC | 0.85% | 2006 | High vol; no income |

---

## Part 3: Time Periods for Analysis

| Period | Start | End | Months | Regime | Purpose |
|--------|-------|-----|--------|--------|---------|
| **Full Sample** | Jan 2001 | Dec 2025 | 300 | All regimes | Overall assessment |
| **Extended (Credit)** | Jan 1997 | Dec 2025 | 348 | All regimes | Longer credit history |
| **Pre-GFC** | Jan 2001 | Dec 2007 | 84 | Normal rates | Baseline environment |
| **GFC Crisis** | Jan 2008 | Dec 2009 | 24 | Maximum stress | Drawdown protection |
| **GFC Recovery** | Jan 2010 | Dec 2012 | 36 | QE onset | Recovery speed |
| **QE Era** | Jan 2013 | Dec 2019 | 84 | ZIRP, low vol | "Old normal" |
| **COVID Shock** | Jan 2020 | Dec 2020 | 12 | Sharp V-recovery | Liquidity stress |
| **Inflation Regime** | Jan 2021 | Dec 2025 | 60 | Rate hikes | "New normal" |
| **2022 Stress Test** | Jan 2022 | Dec 2022 | 12 | Worst year since 1937 | **Critical validation** |

---

## Part 4: Performance Metrics

### 4.1 Return Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| Annualized Return | (1 + Cumulative Return)^(12/n) - 1 | Total return comparison |
| Annualized Real Return | Nominal Return - CPI Inflation | Purchasing power |
| Excess Return | Return(Portfolio) - Return(60/40) | Value-add vs. baseline |
| Information Ratio | Excess Return / Tracking Error | Risk-adjusted alpha |

### 4.2 Risk Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| Annualized Volatility | StdDev(monthly returns) × √12 | Total risk |
| Downside Deviation | StdDev(returns < 0) × √12 | Harmful volatility |
| Maximum Drawdown | Max(Peak - Trough) / Peak | Worst-case loss |
| Drawdown Duration | Months peak to recovery | Time underwater |
| Value at Risk (95%) | 5th percentile of returns | Left-tail risk |
| Conditional VaR (95%) | Mean of returns ≤ VaR | Expected shortfall |
| Ulcer Index | √(Mean of squared drawdowns) | Sustained pain |

### 4.3 Risk-Adjusted Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| Sharpe Ratio | (Return - Rf) / Volatility | Return per unit risk |
| Sortino Ratio | (Return - Rf) / Downside Dev | Penalizes only downside |
| Calmar Ratio | Return / Max Drawdown | Return per tail risk |
| Omega Ratio | Σ(Gains above threshold) / Σ(Losses below) | Full distribution |

### 4.4 Diversification Metrics

| Metric | Purpose |
|--------|---------|
| Correlation to 60/40 | Diversification benefit |
| Rolling 36-month correlation | Stability over time |
| Downside correlation | Crisis diversification |
| Beta to equity | Market sensitivity |
| Beta to bonds | Rate sensitivity |
| Diversification Ratio | Correlation benefit capture |

### 4.5 Inflation Protection Metrics

| Metric | Calculation | Purpose |
|--------|-------------|---------|
| Inflation Beta | Regression coefficient on CPI | Sensitivity to inflation |
| Real Return (High Inflation) | Return when CPI > 4% annualized | Crisis protection |
| Real Return (Low Inflation) | Return when CPI < 2% annualized | Normal performance |

### 4.6 Crisis Performance Analysis

| Crisis | Dates | Measure |
|--------|-------|---------|
| Dot-Com Aftermath | 2001-2002 | Drawdown, recovery |
| GFC | Oct 2007 - Mar 2009 | Maximum drawdown |
| COVID Crash | Feb - Mar 2020 | Drawdown, recovery speed |
| **2022 Inflation Shock** | Jan - Oct 2022 | **Critical: drawdown, real return** |

---

## Part 5: Statistical Testing

### 5.1 Hypothesis Tests

| Test | Null Hypothesis | Method | Significance |
|------|-----------------|--------|--------------|
| Return improvement | μ(enhanced) = μ(baseline) | Paired t-test | α = 0.05 |
| Volatility change | σ²(enhanced) = σ²(baseline) | F-test | α = 0.05 |
| Sharpe improvement | SR(enhanced) = SR(baseline) | Jobson-Korkie test | α = 0.05 |
| Sortino improvement | Sortino(enhanced) = Sortino(baseline) | Bootstrap | α = 0.05 |
| Max DD improvement | MaxDD(enhanced) = MaxDD(baseline) | Bootstrap | α = 0.05 |

### 5.2 Robustness Checks

| Check | Method | Purpose |
|-------|--------|---------|
| Sub-period analysis | Run metrics by period | Confirm consistency |
| Index sensitivity | Swap primary/backup indices | Confirm not index-dependent |
| Fee sensitivity | Test 100/150/200 bps | Confirm survives costs |
| Rebalancing frequency | Monthly/quarterly/annual | Confirm not rebalancing-dependent |
| De-smoothing | Geltner method (λ=0.5) | Correct NCREIF appraisal bias |
| Bootstrap | 10,000 block bootstrap samples | Statistical confidence |

---

## Part 6: Expected Results

### 6.1 Full Sample Expected Performance (2001-2025)

| Portfolio | Return | Volatility | Sharpe | Max DD | Inflation β |
|-----------|--------|------------|--------|--------|-------------|
| **A: 60/40 Baseline** | 6.8% | 10.2% | 0.52 | -35% | 0.28 |
| **B: +10% Infra** | 7.3% | 9.8% | 0.60 | -31% | 0.42 |
| **C: +10% Credit** | 7.4% | 9.6% | 0.62 | -33% | 0.38 |
| **D: +10% Real Assets** | 7.1% | 9.4% | 0.59 | -30% | 0.48 |
| **E: Infra + Credit** | 7.5% | 9.4% | 0.65 | -29% | 0.45 |
| **F: All Three** | 7.4% | 9.0% | 0.66 | -27% | 0.52 |
| **G: Aggressive** | 7.8% | 9.2% | 0.69 | -26% | 0.58 |

### 6.2 2022 Stress Test Expected Performance

| Portfolio | 2022 Return | Real Return | vs. 60/40 |
|-----------|-------------|-------------|-----------|
| **A: 60/40 Baseline** | -17.5% | -25.5% | — |
| **B: +10% Infra** | -13.5% | -21.5% | +4.0% |
| **C: +10% Credit** | -15.0% | -23.0% | +2.5% |
| **D: +10% Real Assets** | -14.0% | -22.0% | +3.5% |
| **E: Infra + Credit** | -12.0% | -20.0% | +5.5% |
| **F: All Three** | -11.0% | -19.0% | +6.5% |
| **G: Aggressive** | -9.5% | -17.5% | +8.0% |

### 6.3 Expected Correlation Matrix

|  | Equity | Bonds | Infra | Credit | Real Assets |
|--|--------|-------|-------|--------|-------------|
| **Equity** | 1.00 | 0.15 | 0.45 | 0.55 | 0.35 |
| **Bonds** | 0.15 | 1.00 | 0.25 | 0.40 | 0.20 |
| **Infrastructure** | 0.45 | 0.25 | 1.00 | 0.35 | 0.50 |
| **Private Credit** | 0.55 | 0.40 | 0.35 | 1.00 | 0.30 |
| **Real Assets** | 0.35 | 0.20 | 0.50 | 0.30 | 1.00 |

---

## Part 7: Decision Framework

### Scoring Criteria

| Criterion | Weight | Measurement |
|-----------|--------|-------------|
| Risk-Adjusted Return (Sharpe) | 30% | Highest Sharpe ratio |
| 2022 Stress Performance | 25% | Best 2022 return |
| Inflation Protection | 20% | Highest inflation beta |
| Implementation Feasibility | 15% | Liquidity, complexity, fees |
| Statistical Confidence | 10% | P-values < 0.05 |

### Expected Final Ranking

| Rank | Portfolio | Rationale |
|------|-----------|-----------|
| 1 | **G (Aggressive)** | Best metrics but highest complexity |
| 2 | **F (All Three)** | Best risk-adjusted with manageable complexity |
| 3 | **E (Infra + Credit)** | Strong improvement, easiest implementation |
| 4 | **B (Infra Only)** | Single best improvement, simplest path |

**Recommended Starting Point:** Portfolio E (Infra + Credit) — captures ~80% of benefit with ~50% of complexity.

---

# Part 8: Implementation Action Plan

## YOUR STEP-BY-STEP CHECKLIST

---

### PHASE 1: DATA COLLECTION (Week 1-2)

#### Step 1.1: Set Up Data Infrastructure

- [ ] **Create project folder structure:**
  ```
  /backtest-project
  ├── /data
  │   ├── /raw
  │   ├── /processed
  │   └── /outputs
  ├── /code
  ├── /results
  └── /documentation
  ```

- [ ] **Choose analysis tool:**
  - Python (recommended): pandas, numpy, scipy, matplotlib
  - R: PerformanceAnalytics, quantmod
  - Excel (limited but accessible)

#### Step 1.2: Collect Free Data

| Data | Action | Source | File to Save |
|------|--------|--------|--------------|
| S&P 500 TR | Download monthly data Jan 1997 - Dec 2025 | Yahoo Finance (^SP500TR) | `equity_sp500tr.csv` |
| CPI-U | Download monthly Jan 1997 - Dec 2025 | [BLS.gov](https://www.bls.gov/cpi/data.htm) | `inflation_cpi.csv` |
| 3-Month T-Bill | Download monthly Jan 1997 - Dec 2025 | [FRED DTB3](https://fred.stlouisfed.org/series/DTB3) | `riskfree_tbill.csv` |
| High Yield Index | Download monthly Jan 1997 - Dec 2025 | [FRED BAMLH0A0HYM2](https://fred.stlouisfed.org/series/BAMLH0A0HYM2) | `credit_hy_spread.csv` |

#### Step 1.3: Collect Professional/Subscription Data

| Data | Action | Source | File to Save |
|------|--------|--------|--------------|
| Bloomberg US Agg | Request from Bloomberg terminal or data vendor | Bloomberg LBUSTRUU | `bonds_agg.csv` |
| S&P Global Infrastructure | Request from Bloomberg or S&P | Bloomberg SPGTIND | `infra_spglobal.csv` |
| S&P/LSTA Leveraged Loan | Request from Bloomberg or LCD | Bloomberg SPBDAL | `credit_loans.csv` |
| NCREIF Timberland | Request institutional access | NCREIF | `realassets_timber.csv` |
| NCREIF Farmland | Request institutional access | NCREIF | `realassets_farm.csv` |

#### Step 1.4: Collect ETF Proxy Data (If Professional Data Unavailable)

| ETF | Action | Ticker | File to Save |
|-----|--------|--------|--------------|
| iShares US Agg Bond | Download from Yahoo Finance | AGG | `bonds_agg_etf.csv` |
| iShares Global Infrastructure | Download from Yahoo Finance | IGF | `infra_igf_etf.csv` |
| Invesco Senior Loan | Download from Yahoo Finance | BKLN | `credit_bkln_etf.csv` |
| SPDR Global Natural Resources | Download from Yahoo Finance | GNR | `realassets_gnr_etf.csv` |

**Note:** ETF proxies have shorter history (2007-2011 inception). Document limitations.

#### Step 1.5: Data Quality Checklist

- [ ] All files have consistent date format (YYYY-MM-DD recommended)
- [ ] All returns are total returns (including dividends/income)
- [ ] No missing values in critical periods
- [ ] Currency is consistent (all USD)
- [ ] Monthly frequency aligned (end-of-month dates)

---

### PHASE 2: DATA PROCESSING (Week 2-3)

#### Step 2.1: Load and Clean Data

```python
# Pseudocode - adapt to your environment

# Load all data files
equity = load_csv('equity_sp500tr.csv')
bonds = load_csv('bonds_agg.csv')
infra = load_csv('infra_spglobal.csv')
credit = load_csv('credit_loans.csv')
timber = load_csv('realassets_timber.csv')
farm = load_csv('realassets_farm.csv')
cpi = load_csv('inflation_cpi.csv')
tbill = load_csv('riskfree_tbill.csv')

# Convert to monthly returns if needed
# Align all series to common dates
# Handle missing values
```

#### Step 2.2: Create Derived Series

- [ ] **Real Assets Blend:** 60% Timberland + 40% Farmland
  ```
  real_assets = 0.60 * timber + 0.40 * farm
  ```

- [ ] **De-smooth NCREIF data (if using):**
  ```
  # Geltner de-smoothing: r_unsmoothed = (r_observed - λ * r_previous) / (1 - λ)
  # Use λ = 0.5 as standard assumption
  ```

- [ ] **Apply fee adjustments:**
  ```
  infra_net = infra_gross - (0.0150 / 12)  # 150 bps annual
  credit_net = credit_gross - (0.0150 / 12)  # 150 bps annual
  realassets_net = realassets_gross - (0.0100 / 12)  # 100 bps annual
  ```

- [ ] **Calculate inflation rate:**
  ```
  inflation_monthly = (CPI_t / CPI_t-1) - 1
  ```

#### Step 2.3: Create Master Dataset

- [ ] Merge all series into single DataFrame with columns:
  - Date
  - Equity_Return
  - Bonds_Return
  - Infra_Return
  - Credit_Return
  - RealAssets_Return
  - CPI_Return
  - TBill_Return

- [ ] Save as `master_returns.csv`

- [ ] Verify date range: Jan 2001 - Dec 2025 (300 months)

---

### PHASE 3: PORTFOLIO CONSTRUCTION (Week 3)

#### Step 3.1: Define Portfolio Weights

```python
portfolios = {
    'A_Baseline':    [0.60, 0.40, 0.00, 0.00, 0.00],
    'B_Infra':       [0.60, 0.30, 0.10, 0.00, 0.00],
    'C_Credit':      [0.60, 0.30, 0.00, 0.10, 0.00],
    'D_RealAssets':  [0.60, 0.30, 0.00, 0.00, 0.10],
    'E_InfraCredit': [0.60, 0.25, 0.08, 0.07, 0.00],
    'F_AllThree':    [0.60, 0.22, 0.06, 0.06, 0.06],
    'G_Aggressive':  [0.55, 0.20, 0.10, 0.08, 0.07],
}
# Order: [Equity, Bonds, Infra, Credit, RealAssets]
```

#### Step 3.2: Calculate Portfolio Returns

```python
# For each portfolio:
for name, weights in portfolios.items():
    portfolio_return = (
        weights[0] * equity +
        weights[1] * bonds +
        weights[2] * infra +
        weights[3] * credit +
        weights[4] * realassets
    )
    # Assumes monthly rebalancing to target weights
```

#### Step 3.3: Apply Rebalancing Costs (Optional)

```python
# Assume 10 bps per rebalance for alternatives portion
rebalancing_cost = 0.0010 * (weights[2] + weights[3] + weights[4])
portfolio_return_net = portfolio_return - rebalancing_cost
```

#### Step 3.4: Calculate Cumulative Wealth

```python
# Cumulative wealth index starting at $100
wealth = 100 * (1 + portfolio_return).cumprod()
```

---

### PHASE 4: METRIC CALCULATION (Week 4)

#### Step 4.1: Return Metrics

- [ ] Annualized return (geometric mean)
- [ ] Annualized real return (nominal - inflation)
- [ ] Cumulative return (full sample and by period)
- [ ] Excess return vs. Portfolio A (baseline)

#### Step 4.2: Risk Metrics

- [ ] Annualized volatility
- [ ] Downside deviation
- [ ] Maximum drawdown
- [ ] Drawdown duration (months)
- [ ] VaR (95%)
- [ ] CVaR (95%)

#### Step 4.3: Risk-Adjusted Metrics

- [ ] Sharpe ratio (using T-bill as Rf)
- [ ] Sortino ratio
- [ ] Calmar ratio
- [ ] Information ratio (vs. baseline)

#### Step 4.4: Diversification Metrics

- [ ] Correlation matrix (all assets)
- [ ] Rolling 36-month correlations
- [ ] Beta to equity
- [ ] Beta to bonds

#### Step 4.5: Inflation Metrics

- [ ] Inflation beta (regression)
- [ ] Returns during high inflation months (CPI > 0.33% monthly ≈ 4% annual)
- [ ] Returns during low inflation months

#### Step 4.6: Period-Specific Analysis

Run all metrics for each sub-period:
- [ ] Full sample (2001-2025)
- [ ] Pre-GFC (2001-2007)
- [ ] GFC Crisis (2008-2009)
- [ ] GFC Recovery (2010-2012)
- [ ] QE Era (2013-2019)
- [ ] COVID (2020)
- [ ] Inflation Regime (2021-2025)
- [ ] **2022 Only (Critical)**

---

### PHASE 5: STATISTICAL TESTING (Week 5)

#### Step 5.1: Hypothesis Tests

- [ ] **Paired t-test:** Is return improvement significant?
  ```python
  from scipy import stats
  t_stat, p_value = stats.ttest_rel(portfolio_B_returns, portfolio_A_returns)
  ```

- [ ] **Jobson-Korkie test:** Is Sharpe ratio improvement significant?
  ```python
  # Requires custom implementation or use of empyrical/pyfolio library
  ```

- [ ] **Bootstrap confidence intervals:**
  ```python
  # 10,000 bootstrap samples
  # Calculate metric for each sample
  # Report 2.5th and 97.5th percentiles
  ```

#### Step 5.2: Robustness Checks

- [ ] **Index sensitivity:** Re-run with backup indices (IGF, HYG, GNR)
- [ ] **Fee sensitivity:** Test with 100bps, 150bps, 200bps fees
- [ ] **Period sensitivity:** Confirm rankings consistent across sub-periods
- [ ] **Weight sensitivity:** Test 5%, 15%, 20% alternative allocations

---

### PHASE 6: VISUALIZATION & REPORTING (Week 6)

#### Step 6.1: Create Charts

- [ ] **Cumulative wealth chart:** All 7 portfolios on one chart (2001-2025)
- [ ] **Drawdown chart:** All 7 portfolios showing underwater periods
- [ ] **Rolling Sharpe ratio:** 36-month rolling for key portfolios
- [ ] **Correlation heatmap:** Full sample correlation matrix
- [ ] **Rolling correlation:** Infrastructure correlation to 60/40 over time
- [ ] **2022 monthly returns:** Bar chart showing each portfolio's monthly performance
- [ ] **Inflation beta scatter:** Portfolio returns vs. CPI changes

#### Step 6.2: Create Summary Tables

- [ ] Full sample metrics (all portfolios, all metrics)
- [ ] Sub-period metrics (condensed)
- [ ] 2022 stress test results (detailed)
- [ ] Statistical significance summary (p-values)
- [ ] Robustness check summary

#### Step 6.3: Write Report

- [ ] Executive summary (1 page)
- [ ] Methodology description
- [ ] Results by portfolio
- [ ] Statistical confidence levels
- [ ] Robustness findings
- [ ] Recommendation with rationale
- [ ] Implementation considerations
- [ ] Limitations and caveats

---

### PHASE 7: QUALITY ASSURANCE (Week 6-7)

#### Step 7.1: Sanity Checks

- [ ] Do 60/40 baseline results match published benchmarks?
- [ ] Are individual asset class returns reasonable vs. known history?
- [ ] Does 2022 performance match reported figures (~-17.5% for 60/40)?
- [ ] Are correlations in expected ranges?
- [ ] Do Sharpe ratios fall in reasonable range (0.3-1.0)?

#### Step 7.2: Peer Review

- [ ] Have colleague verify calculations independently
- [ ] Review code for errors
- [ ] Check data sources and adjustments
- [ ] Validate statistical tests

#### Step 7.3: Sensitivity Documentation

- [ ] Document all assumptions
- [ ] Note data limitations
- [ ] Explain any adjustments made
- [ ] Caveat areas of uncertainty

---

## DATA COLLECTION QUICK REFERENCE

### Minimum Required Data (For Basic Analysis)

| Data | Source | Cost | Priority |
|------|--------|------|----------|
| S&P 500 Total Return | Yahoo Finance | Free | **Must Have** |
| Bloomberg US Aggregate (or AGG ETF) | Bloomberg / Yahoo | Free-$$$ | **Must Have** |
| S&P Global Infrastructure (or IGF ETF) | Bloomberg / Yahoo | Free-$$$ | **Must Have** |
| S&P/LSTA Leveraged Loan (or BKLN ETF) | Bloomberg / Yahoo | Free-$$$ | **Must Have** |
| CPI-U | BLS | Free | **Must Have** |
| 3-Month T-Bill | FRED | Free | **Must Have** |

### Enhanced Data (For Comprehensive Analysis)

| Data | Source | Cost | Priority |
|------|--------|------|----------|
| NCREIF Timberland | NCREIF | $$$ | High |
| NCREIF Farmland | NCREIF | $$$ | High |
| EDHECinfra Infra300 | EDHECinfra | $$$$ | Medium |
| Cliffwater Direct Lending | Cliffwater | $$$ | Medium |

### Fallback Strategy (Budget-Constrained)

If professional data unavailable, use ETF proxies with these adjustments:

| Asset Class | ETF Proxy | Adjustment | Limitation |
|-------------|-----------|------------|------------|
| Bonds | AGG | None | History starts 2003 |
| Infrastructure | IGF | +2% vol adjustment | History starts 2007; listed proxy |
| Private Credit | BKLN | -1% return, -2% vol | History starts 2011; listed proxy |
| Real Assets | GNR | +3% vol adjustment | History starts 2010; listed proxy |

**Important:** If using ETFs, backtest period limited to 2011-2025 (when all ETFs available).

---

## TIMELINE SUMMARY

| Week | Phase | Key Deliverables |
|------|-------|------------------|
| 1-2 | Data Collection | All raw data files downloaded and verified |
| 2-3 | Data Processing | Master returns file; derived series created |
| 3 | Portfolio Construction | All 7 portfolio return series calculated |
| 4 | Metric Calculation | All performance metrics computed |
| 5 | Statistical Testing | Hypothesis tests; robustness checks complete |
| 6 | Visualization & Reporting | Charts, tables, draft report |
| 6-7 | Quality Assurance | Peer review; final report |

**Total Estimated Time:** 6-7 weeks (part-time analyst)

---

## KEY SUCCESS CRITERIA

The backtest will be considered successful if:

1. **Portfolio E or F outperforms baseline 60/40** on risk-adjusted basis (Sharpe ratio improvement > 0.05)

2. **2022 stress test shows meaningful protection** (at least 3% better than baseline)

3. **Inflation beta improves significantly** (from ~0.28 to >0.40)

4. **Results are statistically significant** (p < 0.05 for key metrics)

5. **Results are robust** across sub-periods and index choices

6. **Implementation is feasible** given fees, liquidity, and governance constraints

---

## NEXT STEPS AFTER BACKTEST

If results confirm hypothesis:

1. **Present findings to Investment Committee** with recommendation
2. **Develop implementation plan** (manager selection, pacing, governance)
3. **Begin infrastructure allocation** (highest priority based on research)
4. **Phase in private credit** (Year 1-2)
5. **Consider real assets** (Year 2-3, pending expertise development)

---

*Document prepared for investment strategy analysis. All methodologies subject to refinement based on data availability and emerging best practices.*
