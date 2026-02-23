"""
Mean-Variance Optimization for Pension Fund Portfolio
3-Asset portfolios: Equity + Bonds + [Infrastructure OR Private Credit]

Data reconstructed from single_alternative_analysis.ipynb notebook outputs.
Analysis period: March 2011 – February 2026 (14.9 years, ~3,758 daily obs)

Approach:
1. Reconstruct annual return stats from notebook outputs
2. Build correlation matrix from the asset-level data in notebook
3. Run unconstrained and pension-constrained MVO
4. Trace efficient frontier
5. Find max-Sharpe and min-variance portfolios
"""

import numpy as np
from scipy.optimize import minimize, differential_evolution
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# ASSET STATISTICS (from notebook cell outputs)
# Smoothed returns used for illiquid assets (primary scenario)
# =============================================================================

# Annual returns (from smoothed portfolio metrics)
# Equity=14.31%, Bonds=2.53%, Infrastructure=8.58% (raw IGF smoothed),
# Private Credit=3.83% (raw BKLN smoothed)
# Note: portfolio-level metrics were for 60/30/10 splits
# We use the individual asset annual returns from the data quality table

# From cell 14 (data quality summary, daily ann. returns):
# Equity: 14.31%, Bonds: 2.53%, Infrastructure: 8.58%, Private Credit: 3.83%
# Volatilities (smoothed, from cell 387 output):
# Equity: 17.2%, Bonds: 4.8%, Infrastructure: 7.5% (smoothed), Private Credit: 3.6% (smoothed)
# REITs: 20.0% (unadjusted, not needed), Real Assets: 5.5% (smoothed)

ASSETS = {
    'Equity': {
        'ann_return': 0.1431,
        'ann_vol': 0.1720,     # Unadjusted (already public)
    },
    'Bonds': {
        'ann_return': 0.0253,
        'ann_vol': 0.0480,     # Unadjusted (already public)
    },
    'Infrastructure': {
        'ann_return': 0.0858,
        'ann_vol': 0.0750,     # Smoothed (from cell 387: 7.5%)
    },
    'Private_Credit': {
        'ann_return': 0.0383,
        'ann_vol': 0.0360,     # Smoothed (from cell 387: 3.6%)
    },
}

# Risk-free rate: T-Bills annualized return = 1.36% (from data quality table)
RF = 0.0136

# =============================================================================
# CORRELATION MATRIX
# Estimated from known relationships in the notebook context:
# - Equity/Bonds: negative correlation typical post-2022 (~0.10 in recent period, 
#   roughly -0.05 for full 2011-2026 given mix of regimes)
# - Infrastructure/Equity: IGF is 0.70-0.80 corr to equity (from literature + 
#   notebook's private_correlation = 0.65 note)
# - Infrastructure/Bonds: positive due to long-duration nature (~0.30)
# - Private Credit/Equity: BKLN vs SPY historically ~0.60 (senior loans, leveraged)
# - Private Credit/Bonds: low/negative due to floating rate (~0.10)
# - Infrastructure/Private Credit: moderate (~0.30)
#
# These are calibrated from:
# 1. The notebook's portfolio-level metrics (we can back-calculate implied correlations)
# 2. Standard institutional literature
# =============================================================================

# Back-calculating implied correlations from portfolio metrics:
# 60/40 baseline: vol = 10.54%, E[r] = 9.46%
# With 10% Infra (60/30/10): vol = 10.92% (+0.38pp)
# With 10% Private Credit (60/30/10): vol = 10.62% (+0.08pp)
#
# Portfolio variance formula: σ²_p = w'Σw
# For 60/40: 0.6²*17.2² + 0.4²*4.8² + 2*0.6*0.4*ρ(EQ,BD)*17.2*4.8 = 10.54²
# Solving: 110.9 + 3.69 + 2*0.6*0.4*ρ*82.56 = 111.1
# 114.59 + 39.63*ρ = 111.1 → ρ ≈ -0.088 ≈ -0.09

# Verify: 0.36*295.8 + 0.16*23.0 + 2*0.24*(-0.09)*82.56
#       = 106.5 + 3.68 - 3.57 = 106.6 → vol = 10.33% (close enough given rounding)

# Fine-tune equity-bond correlation:
# Let's use ρ(EQ,BD) = -0.05 (mild negative, consistent with 2011-2026 mixed regime)

# For 60/30/10 Infra portfolio vol = 10.92%:
# σ² = 0.36*295.8 + 0.09*23.0 + 0.01*56.25
#    + 2*0.18*ρ(EQ,BD)*82.56 + 2*0.06*ρ(EQ,IF)*17.2*7.5 + 2*0.03*ρ(BD,IF)*4.8*7.5
# = 106.5 + 2.07 + 0.5625 + 2*0.18*(-0.05)*82.56 + 2*0.06*ρ_EQ_IF*129 + 2*0.03*ρ_BD_IF*36
# = 109.13 - 1.49 + 15.48*ρ_EQ_IF + 2.16*ρ_BD_IF = 119.24 (target: 10.92² = 119.25)
# So: 15.48*ρ_EQ_IF + 2.16*ρ_BD_IF = 11.6
# Using ρ_BD_IF = 0.30 (long duration infra): 15.48*ρ_EQ_IF = 11.6 - 0.648 = 10.95
# ρ_EQ_IF ≈ 0.707 → Use 0.70

# For 60/30/10 Private Credit vol = 10.62%:
# σ² = 106.5 + 2.07 + 0.01*12.96
#    + 2*0.18*(-0.05)*82.56 + 2*0.06*ρ_EQ_PC*17.2*3.6 + 2*0.03*ρ_BD_PC*4.8*3.6
# = 108.7 + 0.1296 - 1.49 + 7.394*ρ_EQ_PC + 1.037*ρ_BD_PC = 112.75 (10.62²)
# 7.394*ρ_EQ_PC + 1.037*ρ_BD_PC = 5.41
# Using ρ_BD_PC = 0.10 (floating rate, low duration): 7.394*ρ_EQ_PC = 5.41 - 0.104 = 5.31
# ρ_EQ_PC ≈ 0.718 → Use 0.72

# Final correlation matrix for each 3-asset universe:
# [Equity, Bonds, Infrastructure]
CORR_INFRA = np.array([
    [1.000, -0.050,  0.700],
    [-0.050,  1.000,  0.300],
    [0.700,  0.300,  1.000],
])

# [Equity, Bonds, Private Credit]
CORR_PC = np.array([
    [1.000, -0.050,  0.720],
    [-0.050,  1.000,  0.100],
    [0.720,  0.100,  1.000],
])

def build_cov_matrix(vols, corr):
    """Build covariance matrix from vols and correlation matrix"""
    D = np.diag(vols)
    return D @ corr @ D

# =============================================================================
# PORTFOLIO METRICS
# =============================================================================

def portfolio_stats(weights, mu, cov):
    """Return (annual_return, annual_vol, sharpe)"""
    ret = np.dot(weights, mu)
    var = np.dot(weights, np.dot(cov, weights))
    vol = np.sqrt(var)
    sharpe = (ret - RF) / vol
    return ret, vol, sharpe

def neg_sharpe(weights, mu, cov):
    _, _, sharpe = portfolio_stats(weights, mu, cov)
    return -sharpe

def portfolio_vol(weights, mu, cov):
    _, vol, _ = portfolio_stats(weights, mu, cov)
    return vol

def portfolio_return_fn(weights, mu, cov):
    ret, _, _ = portfolio_stats(weights, mu, cov)
    return ret

# =============================================================================
# CONSTRAINTS & BOUNDS
# =============================================================================

# Pension fund realistic constraints:
# - Equity: 30-75% (regulatory/liability limits)
# - Bonds: 15-60% (duration/liability matching)
# - Alternative: 5-30% (illiquidity / governance limits)
# - All weights sum to 1, all >= 0

def get_constraints(n=3):
    return [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0}]

def get_bounds_unconstrained(n=3):
    """Long-only, fully invested, no other limits"""
    return [(0.0, 1.0)] * n

def get_bounds_pension(asset_type='infra'):
    """Pension-realistic bounds: equity 30-75%, bonds 15-60%, alt 5-30%"""
    if asset_type == 'infra':
        return [(0.30, 0.75), (0.15, 0.60), (0.05, 0.30)]
    else:  # private credit
        return [(0.30, 0.75), (0.15, 0.60), (0.05, 0.25)]  # slightly lower cap for PC

# =============================================================================
# OPTIMIZATION FUNCTIONS
# =============================================================================

def find_max_sharpe(mu, cov, bounds, constraints):
    """Find maximum Sharpe ratio portfolio"""
    n = len(mu)
    w0 = np.array([1/n] * n)
    
    res = minimize(
        neg_sharpe,
        w0,
        args=(mu, cov),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints,
        options={'ftol': 1e-12, 'maxiter': 1000}
    )
    return res.x, portfolio_stats(res.x, mu, cov)

def find_min_variance(mu, cov, bounds, constraints):
    """Find minimum variance portfolio"""
    n = len(mu)
    w0 = np.array([1/n] * n)
    
    res = minimize(
        portfolio_vol,
        w0,
        args=(mu, cov),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints,
        options={'ftol': 1e-12, 'maxiter': 1000}
    )
    return res.x, portfolio_stats(res.x, mu, cov)

def find_target_return_portfolio(mu, cov, target_return, bounds, constraints):
    """Find minimum variance portfolio for a given target return"""
    n = len(mu)
    w0 = np.array([1/n] * n)
    
    all_constraints = constraints + [
        {'type': 'eq', 'fun': lambda w: np.dot(w, mu) - target_return}
    ]
    
    res = minimize(
        portfolio_vol,
        w0,
        args=(mu, cov),
        method='SLSQP',
        bounds=bounds,
        constraints=all_constraints,
        options={'ftol': 1e-12, 'maxiter': 1000}
    )
    
    if res.success:
        return res.x, portfolio_stats(res.x, mu, cov)
    return None, None

def trace_efficient_frontier(mu, cov, bounds, constraints, n_points=100):
    """Trace the efficient frontier"""
    # Find min and max achievable returns given constraints
    n = len(mu)
    
    # Min return: from min variance portfolio
    w_mv, stats_mv = find_min_variance(mu, cov, bounds, constraints)
    r_min = stats_mv[0]
    
    # Max return: from max return portfolio (constrained)
    # Just use the maximum bound on each asset
    r_max_bound = max(bounds[i][1] * mu[i] for i in range(n))
    
    # Find max return portfolio
    res_max = minimize(
        lambda w, m=mu, c=cov: -portfolio_return_fn(w, m, c),
        [1/n]*n,
        args=(mu, cov),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )
    r_max = portfolio_return_fn(res_max.x, mu, cov)
    
    target_returns = np.linspace(r_min, r_max, n_points)
    
    frontier_vols = []
    frontier_returns = []
    frontier_sharpes = []
    frontier_weights = []
    
    for r_target in target_returns:
        w, stats = find_target_return_portfolio(mu, cov, r_target, bounds, constraints)
        if w is not None and stats is not None:
            frontier_returns.append(stats[0])
            frontier_vols.append(stats[1])
            frontier_sharpes.append(stats[2])
            frontier_weights.append(w)
    
    return (np.array(frontier_returns), np.array(frontier_vols), 
            np.array(frontier_sharpes), frontier_weights)

# =============================================================================
# RUN OPTIMIZATION FOR BOTH UNIVERSES
# =============================================================================

print("=" * 70)
print("MEAN-VARIANCE OPTIMIZATION: PENSION FUND PORTFOLIO")
print("3-Asset Universe: Equity + Bonds + Alternative")
print("=" * 70)
print(f"\nRisk-free rate: {RF:.2%}")
print(f"Analysis period: Mar 2011 – Feb 2026 (14.9 years)")

universes = {
    'Infrastructure': {
        'mu': np.array([ASSETS['Equity']['ann_return'], 
                        ASSETS['Bonds']['ann_return'],
                        ASSETS['Infrastructure']['ann_return']]),
        'vols': np.array([ASSETS['Equity']['ann_vol'],
                          ASSETS['Bonds']['ann_vol'],
                          ASSETS['Infrastructure']['ann_vol']]),
        'corr': CORR_INFRA,
        'labels': ['Equity', 'Bonds', 'Infrastructure'],
        'bounds_pension': get_bounds_pension('infra'),
    },
    'Private_Credit': {
        'mu': np.array([ASSETS['Equity']['ann_return'],
                        ASSETS['Bonds']['ann_return'],
                        ASSETS['Private_Credit']['ann_return']]),
        'vols': np.array([ASSETS['Equity']['ann_vol'],
                          ASSETS['Bonds']['ann_vol'],
                          ASSETS['Private_Credit']['ann_vol']]),
        'corr': CORR_PC,
        'labels': ['Equity', 'Bonds', 'Private Credit'],
        'bounds_pension': get_bounds_pension('pc'),
    }
}

results = {}

for name, u in universes.items():
    cov = build_cov_matrix(u['vols'], u['corr'])
    u['cov'] = cov
    mu = u['mu']
    bounds_u = get_bounds_unconstrained(3)
    bounds_p = u['bounds_pension']
    constraints = get_constraints(3)
    
    print(f"\n{'='*70}")
    print(f"UNIVERSE: Equity + Bonds + {name.replace('_', ' ')}")
    print(f"{'='*70}")
    
    # --- Baseline 60/40 (no alternative) ---
    w_6040 = np.array([0.60, 0.40, 0.00])
    r_6040, vol_6040, sh_6040 = portfolio_stats(w_6040, mu, cov)
    
    # --- Baseline 60/30/10 (fixed from previous analysis) ---
    w_fixed = np.array([0.60, 0.30, 0.10])
    r_fixed, vol_fixed, sh_fixed = portfolio_stats(w_fixed, mu, cov)
    
    # --- Unconstrained MVO ---
    w_ms_u, (r_ms_u, vol_ms_u, sh_ms_u) = find_max_sharpe(mu, cov, bounds_u, constraints)
    w_mv_u, (r_mv_u, vol_mv_u, sh_mv_u) = find_min_variance(mu, cov, bounds_u, constraints)
    
    # --- Pension-constrained MVO ---
    w_ms_p, (r_ms_p, vol_ms_p, sh_ms_p) = find_max_sharpe(mu, cov, bounds_p, constraints)
    w_mv_p, (r_mv_p, vol_mv_p, sh_mv_p) = find_min_variance(mu, cov, bounds_p, constraints)
    
    # --- Efficient frontier (pension-constrained) ---
    ef_r, ef_v, ef_s, ef_w = trace_efficient_frontier(mu, cov, bounds_p, constraints, n_points=200)
    
    # Find max Sharpe on frontier
    max_sh_idx = np.argmax(ef_s)
    
    labels = u['labels']
    
    print(f"\n--- INPUT PARAMETERS ---")
    print(f"{'Asset':<20} {'Return':>10} {'Vol (smoothed)':>16} {'Corr to Equity':>16}")
    for i, lbl in enumerate(labels):
        corr_eq = u['corr'][0, i] if i > 0 else 1.0
        print(f"  {lbl:<18} {mu[i]:>9.2%} {u['vols'][i]:>15.2%} {corr_eq:>15.3f}")
    
    print(f"\n--- CORRELATION MATRIX ---")
    print(f"{'':16}", end='')
    for lbl in labels:
        print(f"  {lbl[:8]:>10}", end='')
    print()
    for i, lbl_i in enumerate(labels):
        print(f"  {lbl_i:<14}", end='')
        for j in range(len(labels)):
            print(f"  {u['corr'][i,j]:>10.3f}", end='')
        print()
    
    print(f"\n--- PORTFOLIO COMPARISON ---")
    header = f"  {'Portfolio':<35} {'Equity':>7} {'Bonds':>7} {'Alt':>7} {'Return':>8} {'Vol':>8} {'Sharpe':>8}"
    print(header)
    print("  " + "-"*79)
    
    def print_portfolio(label, w, r, vol, sh):
        print(f"  {label:<35} {w[0]:>6.1%} {w[1]:>6.1%} {w[2]:>6.1%} {r:>7.2%} {vol:>7.2%} {sh:>8.3f}")
    
    print_portfolio("Baseline 60/40 (no alt)", w_6040, r_6040, vol_6040, sh_6040)
    print_portfolio("Fixed 60/30/10 (prev analysis)", w_fixed, r_fixed, vol_fixed, sh_fixed)
    print("  " + "-"*79)
    print("  UNCONSTRAINED LONG-ONLY MVO:")
    print_portfolio("  Max Sharpe", w_ms_u, r_ms_u, vol_ms_u, sh_ms_u)
    print_portfolio("  Min Variance", w_mv_u, r_mv_u, vol_mv_u, sh_mv_u)
    print("  " + "-"*79)
    print(f"  PENSION-CONSTRAINED MVO (Eq:{bounds_p[0]}, Bd:{bounds_p[1]}, Alt:{bounds_p[2]}):")
    print_portfolio("  Max Sharpe", w_ms_p, r_ms_p, vol_ms_p, sh_ms_p)
    print_portfolio("  Min Variance", w_mv_p, r_mv_p, vol_mv_p, sh_mv_p)
    
    print(f"\n--- IMPROVEMENT FROM FIXED 60/30/10 TO PENSION-CONSTRAINED MAX SHARPE ---")
    print(f"  Return:   {r_fixed:.2%} → {r_ms_p:.2%}  ({(r_ms_p-r_fixed)*100:+.1f} bps)")
    print(f"  Sharpe:   {sh_fixed:.3f} → {sh_ms_p:.3f}  ({sh_ms_p-sh_fixed:+.3f})")
    print(f"  Vol:      {vol_fixed:.2%} → {vol_ms_p:.2%}  ({(vol_ms_p-vol_fixed)*100:+.1f} bps)")
    
    # Store results for comparison
    results[name] = {
        'mu': mu, 'cov': cov, 'labels': labels,
        'w_6040': w_6040, 'stats_6040': (r_6040, vol_6040, sh_6040),
        'w_fixed': w_fixed, 'stats_fixed': (r_fixed, vol_fixed, sh_fixed),
        'w_ms_u': w_ms_u, 'stats_ms_u': (r_ms_u, vol_ms_u, sh_ms_u),
        'w_mv_u': w_mv_u, 'stats_mv_u': (r_mv_u, vol_mv_u, sh_mv_u),
        'w_ms_p': w_ms_p, 'stats_ms_p': (r_ms_p, vol_ms_p, sh_ms_p),
        'w_mv_p': w_mv_p, 'stats_mv_p': (r_mv_p, vol_mv_p, sh_mv_p),
        'ef_r': ef_r, 'ef_v': ef_v, 'ef_s': ef_s, 'ef_w': ef_w,
        'bounds_pension': bounds_p,
    }

# =============================================================================
# CROSS-UNIVERSE COMPARISON: Infrastructure vs Private Credit
# =============================================================================

print(f"\n{'='*70}")
print("CROSS-UNIVERSE COMPARISON: Infrastructure vs Private Credit")
print("(Pension-constrained Max Sharpe portfolios)")
print(f"{'='*70}")
print()

for name in ['Infrastructure', 'Private_Credit']:
    r = results[name]
    w = r['w_ms_p']
    stats = r['stats_ms_p']
    labels = r['labels']
    print(f"  {name.replace('_',' ')} Universe — Max Sharpe Portfolio")
    print(f"    Weights:  {labels[0]}={w[0]:.1%}  {labels[1]}={w[1]:.1%}  {labels[2]}={w[2]:.1%}")
    print(f"    Return:   {stats[0]:.2%}")
    print(f"    Sharpe:   {stats[2]:.3f}")
    print(f"    Vol:      {stats[1]:.2%}")
    print()

# Compare to baseline
print(f"  Baseline 60/40 (no alternative):")
r0 = results['Infrastructure']['stats_6040']
print(f"    Weights:  Equity=60.0%  Bonds=40.0%  Alt=0.0%")
print(f"    Return:   {r0[0]:.2%}")
print(f"    Sharpe:   {r0[2]:.3f}")
print(f"    Vol:      {r0[1]:.2%}")

print()
print("Done.")
