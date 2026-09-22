"""
Step 4: Walk-through-time backtest engine with transaction costs and performance metrics.

Pseudocode:
    run_backtest(prices_a, prices_b, signal, hedge_ratio, cost_bps) -> daily P&L series
    compute_metrics(daily_returns) -> Sharpe ratio, max drawdown, turnover
"""

import pandas as pd


def run_backtest(
    prices_a: pd.Series,
    prices_b: pd.Series,
    signal: pd.Series,
    hedge_ratio: float,
    cost_bps: float = 5.0,
) -> pd.Series:
    """Simulate trading the signal day by day; return the daily P&L series net of costs."""
    raise NotImplementedError


def compute_metrics(daily_returns: pd.Series) -> dict:
    """Return {sharpe, max_drawdown, turnover} for a daily return series."""
    raise NotImplementedError
