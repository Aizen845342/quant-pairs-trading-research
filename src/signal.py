"""
Step 3: Build the hedge ratio, spread, rolling z-score, and entry/exit signal.

Pseudocode:
    compute_hedge_ratio(a, b) -> OLS regression: a = alpha + beta * b
    compute_spread(a, b, alpha, beta) -> a - (alpha + beta * b)
    compute_rolling_zscore(spread, window) -> (spread - rolling_mean) / rolling_std
    generate_signal(zscore, entry_threshold, exit_threshold) -> +1 / -1 / 0 position series
"""

import pandas as pd


def compute_hedge_ratio(series_a: pd.Series, series_b: pd.Series) -> tuple[float, float]:
    """Return (alpha, beta) from OLS regression of series_a on series_b."""
    raise NotImplementedError


def compute_spread(series_a: pd.Series, series_b: pd.Series, alpha: float, beta: float) -> pd.Series:
    """Return the regression residual spread."""
    raise NotImplementedError


def compute_rolling_zscore(spread: pd.Series, window: int) -> pd.Series:
    """Return the rolling z-score of the spread."""
    raise NotImplementedError


def generate_signal(zscore: pd.Series, entry_threshold: float = 2.0, exit_threshold: float = 0.0) -> pd.Series:
    """Return a position series: +1 (long spread), -1 (short spread), 0 (flat)."""
    raise NotImplementedError
