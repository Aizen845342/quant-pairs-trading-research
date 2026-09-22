"""
Step 6: Combine multiple validated pair strategies into a single portfolio using
Markowitz mean-variance optimization.

Pseudocode:
    build_portfolio(list_of_strategy_return_series) ->
        combine into a returns matrix
        compute covariance matrix and expected returns
        solve for optimal weights (cvxpy) that maximize return for a target risk
        return optimal_weights, portfolio_returns
"""

import pandas as pd


def build_portfolio(strategy_returns: list[pd.Series]) -> tuple[dict, pd.Series]:
    """Return (optimal_weights, portfolio_returns) from a set of strategy return series."""
    raise NotImplementedError
