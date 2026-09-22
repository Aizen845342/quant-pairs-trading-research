"""
Step 5: Walk-forward validation - fit on a training window, evaluate on the next
untouched test window, roll forward through the full history. Guards against
overfitting the hedge ratio and thresholds to a single lucky sample.

Pseudocode:
    walk_forward_test(prices_a, prices_b, train_window, test_window) ->
        for each rolling (train, test) split:
            fit hedge ratio ONLY on train
            build signal and backtest ONLY on test
            record out-of-sample metrics
        return list of out-of-sample metrics
"""

import pandas as pd


def walk_forward_test(
    prices_a: pd.Series,
    prices_b: pd.Series,
    train_window: int,
    test_window: int,
) -> list[dict]:
    """Return a list of out-of-sample metric dicts, one per rolling window."""
    raise NotImplementedError
