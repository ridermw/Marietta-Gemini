"""
Configuration file for the backtesting project.
"""
import os

# --- Data Configuration ---
DATA_DIR = "data"
START_DATE = "2018-01-01"
END_DATE = "2023-12-31"

# Top 20 liquid cryptocurrencies as of late 2023 / early 2024
TICKERS = [
    'BTC-USD', 'ETH-USD', 'XRP-USD', 'BCH-USD', 'LTC-USD', 'EOS-USD',
    'SOL-USD', 'UNI1-USD', 'PEPE-USD', 'NEAR-USD', 'AAVE-USD', 'VET-USD',
    'XMR-USD', 'FTM-USD', 'ALGO-USD', 'OMG-USD', 'CRV-USD', 'YFI-USD',
    'OKB-USD', 'RUNE-USD'
]