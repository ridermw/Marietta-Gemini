import yfinance as yf
import pandas as pd
import os
from src import config

def fetch_crypto_data(ticker, start_date, end_date):
    """
    Fetches historical cryptocurrency data from Yahoo Finance.

    Args:
        ticker (str): The ticker symbol of the cryptocurrency (e.g., 'BTC-USD').
        start_date (str): The start date for the data (e.g., '2022-01-01').
        end_date (str): The end date for the data (e.g., '2023-01-01').

    Returns:
        pandas.DataFrame: A DataFrame containing the historical data, or None if the request fails.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            print(f"No data found for {ticker} from {start_date} to {end_date}")
            return None
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def fetch_multiple_crypto_data(tickers, start_date, end_date):
    """
    Fetches historical data for multiple cryptocurrencies.

    Args:
        tickers (list): A list of ticker symbols.
        start_date (str): The start date for the data.
        end_date (str): The end date for the data.

    Returns:
        dict: A dictionary of DataFrames, with tickers as keys.
    """
    all_data = {}
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        data = fetch_crypto_data(ticker, start_date, end_date)
        if data is not None:
            all_data[ticker] = data
    return all_data

if __name__ == '__main__':
    # Create the data directory if it doesn't exist
    if not os.path.exists(config.DATA_DIR):
        os.makedirs(config.DATA_DIR)

    # Fetch data using parameters from the config file
    crypto_data = fetch_multiple_crypto_data(
        tickers=config.TICKERS, start_date=config.START_DATE, end_date=config.END_DATE
    )

    # Save the data to CSV files
    for ticker, data in crypto_data.items():
        file_path = os.path.join(config.DATA_DIR, f'{ticker.lower()}.csv')
        data.to_csv(file_path)
        print(f"{ticker} data saved to {file_path}")
