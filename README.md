# Quant Pairs Trading & Portfolio Risk Research

A statistical arbitrage research pipeline: find cointegrated equity pairs, build a mean-reversion trading signal, backtest it honestly (with costs and walk-forward validation), then combine multiple pairs into a risk-managed portfolio.

**Status: in progress.** This repo currently holds the project scaffold and stub modules. Implementation is being built module by module, in the order below.

## Why this project

Built as hands-on preparation for quantitative research roles (e.g. Junior Quant Researcher at a systematic trading firm). The goal isn't just "a strategy that looks profitable" — it's demonstrating the full research discipline: statistically validating a hypothesis, testing it out-of-sample, being honest about costs and overfitting, and reporting risk properly at the portfolio level.

## Pipeline overview

```
fetch prices --> screen for cointegrated pairs --> build spread + z-score signal
    --> backtest with costs --> walk-forward validate --> combine into portfolio
    --> optimize weights (Markowitz) --> report risk (VaR / CVaR)
```

## Project structure

```
quant-pairs-trading-research/
├── data/                     # downloaded price data (gitignored, generated locally)
├── notebooks/                # exploratory analysis, plots, scratch work
├── src/
│   ├── data.py               # fetch and clean price data
│   ├── cointegration.py      # pairwise cointegration screening
│   ├── signal.py             # hedge ratio, spread, rolling z-score, entry/exit signal
│   ├── backtest.py           # walk-through-time backtest engine with transaction costs
│   ├── validation.py         # walk-forward (rolling train/test) validation
│   ├── portfolio.py          # combine strategies, Markowitz mean-variance optimization
│   ├── risk.py               # Value-at-Risk and Conditional VaR reporting
│   └── main.py               # ties every stage together end to end
├── tests/                    # unit tests for each module
├── requirements.txt
├── .gitignore
└── README.md
```

## Build order (and why)

| Step | Module | Depends on | Why this order |
|---|---|---|---|
| 1 | `data.py` | — | Nothing else works without clean price data |
| 2 | `cointegration.py` | data | Must prove a pair is statistically mean-reverting before trading it |
| 3 | `signal.py` | cointegration | The z-score signal only makes sense once the spread is trustworthy |
| 4 | `backtest.py` | signal | Confirm the trading mechanics work before worrying about realism |
| 5 | `validation.py` | backtest | Walk-forward testing to catch overfitting — the most important honesty check |
| 6 | `portfolio.py` | validation (multiple pairs) | Combine several validated strategies via Markowitz optimization |
| 7 | `risk.py` | portfolio | Risk reporting only makes sense once the combined portfolio exists |

## Methodology notes

- **Cointegration, not correlation.** Two stocks can be highly correlated and never cointegrated (both trend up forever) or lowly correlated and cointegrated (they mean-revert around each other). Screening uses the Engle-Granger test (`statsmodels.tsa.stattools.coint`).
- **Costs are never ignored.** Every simulated trade deducts an assumed transaction cost (basis points per trade) — a strategy that only looks good before costs isn't a strategy.
- **Walk-forward validation is mandatory, not optional.** Parameters (hedge ratio, entry/exit thresholds) are fit only on a training window and evaluated only on a subsequent, untouched test window, rolled forward through the full history. In-sample and out-of-sample performance are both reported — including when they diverge.
- **Risk is reported at the portfolio level.** Value-at-Risk and Conditional VaR are computed on the combined, optimized portfolio, not per-pair, since that's what actually matters for capital allocation.

## Results

_To be filled in as the pipeline is built — will include cointegration screening results, backtest performance (Sharpe, max drawdown, turnover), walk-forward in-sample vs out-of-sample comparison, optimized portfolio weights, and VaR/CVaR figures._
