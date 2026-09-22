"""
Step 1: Fetch and clean historical price data for candidate tickers.

Pseudocode:
    fetch_prices(tickers, start, end) -> download daily closes, drop empty rows
    clean_prices(prices) -> forward-fill small gaps, drop tickers with too much missing data
"""

import pandas as pd
import yfinance as yf


def fetch_prices(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    """Download daily adjusted close prices for the given tickers."""
    raise NotImplementedError


def clean_prices(prices: pd.DataFrame) -> pd.DataFrame:
    """Forward-fill small gaps and drop tickers with excessive missing data."""
    raise NotImplementedError
