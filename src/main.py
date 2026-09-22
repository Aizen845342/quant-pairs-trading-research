"""
Ties the full pipeline together end to end:

    fetch/clean prices
    -> screen candidate pairs for cointegration
    -> for each selected pair: build signal, backtest, walk-forward validate
    -> combine validated strategies into an optimized portfolio
    -> report portfolio-level VaR / CVaR

Run with: python src/main.py
"""

from data import fetch_prices, clean_prices
from cointegration import find_best_pairs
from signal import compute_hedge_ratio, compute_spread, compute_rolling_zscore, generate_signal
from backtest import run_backtest, compute_metrics
from validation import walk_forward_test
from portfolio import build_portfolio
from risk import compute_var_cvar

TICKERS = ["JPM", "BAC", "WFC", "C", "GS", "MS"]
START, END = "2019-01-01", "2026-09-12"
ZSCORE_WINDOW = 30
TRAIN_WINDOW, TEST_WINDOW = 252 * 2, 126  # ~2 years train, ~6 months test
COST_BPS = 5.0
TOP_N_PAIRS = 3


def main():
    prices = clean_prices(fetch_prices(TICKERS, START, END))

    ranked_pairs = find_best_pairs(prices)
    selected_pairs = ranked_pairs.head(TOP_N_PAIRS)

    strategy_returns = []
    for _, row in selected_pairs.iterrows():
        a, b = row["asset_a"], row["asset_b"]

        alpha, beta = compute_hedge_ratio(prices[a], prices[b])
        spread = compute_spread(prices[a], prices[b], alpha, beta)
        zscore = compute_rolling_zscore(spread, ZSCORE_WINDOW)
        signal = generate_signal(zscore)

        returns = run_backtest(prices[a], prices[b], signal, beta, COST_BPS)
        metrics = compute_metrics(returns)
        print(f"{a}/{b} full-sample metrics: {metrics}")

        wf_results = walk_forward_test(prices[a], prices[b], TRAIN_WINDOW, TEST_WINDOW)
        print(f"{a}/{b} walk-forward out-of-sample results: {wf_results}")

        strategy_returns.append(returns)

    weights, portfolio_returns = build_portfolio(strategy_returns)
    print(f"Optimal portfolio weights: {weights}")

    var, cvar = compute_var_cvar(portfolio_returns)
    print(f"Portfolio VaR (95%): {var:.4f}, CVaR (95%): {cvar:.4f}")


if __name__ == "__main__":
    main()
