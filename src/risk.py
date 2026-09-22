"""
Step 7: Portfolio-level risk reporting - Value-at-Risk and Conditional VaR.

Pseudocode:
    compute_var_cvar(portfolio_returns, confidence) ->
        sort returns ascending
        VaR = the loss at the (1 - confidence) percentile
        CVaR = average loss beyond that percentile
        return var, cvar
"""

import pandas as pd


def compute_var_cvar(portfolio_returns: pd.Series, confidence: float = 0.95) -> tuple[float, float]:
    """Return (VaR, CVaR) at the given confidence level for a return series."""
    raise NotImplementedError
