"""
Step 2: Screen all candidate pairs for cointegration (Engle-Granger test).

Pseudocode:
    test_cointegration(series_a, series_b) -> p_value, score via statsmodels.tsa.stattools.coint
    find_best_pairs(prices) -> test every pair, rank by p_value ascending
"""

import pandas as pd


def test_cointegration(series_a: pd.Series, series_b: pd.Series) -> tuple[float, float]:
    """Return (p_value, test_score) for the cointegration test between two price series."""
    raise NotImplementedError


def find_best_pairs(prices: pd.DataFrame) -> pd.DataFrame:
    """Test every ticker pair for cointegration; return a table sorted by p_value."""
    raise NotImplementedError
