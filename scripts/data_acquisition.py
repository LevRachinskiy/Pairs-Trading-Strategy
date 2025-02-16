import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Create data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Define parameters
tickers = ["JPM", "BAC"]  # Example candidate pair
end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)  # Past 5 years

def download_data(ticker):
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def main():
    for ticker in tickers:
        data = download_data(ticker)
        file_name = f"data/{ticker}_historical.csv"
        data.to_csv(file_name)
        print(f"Data for {ticker} saved to {file_name}")

if __name__ == "__main__":
    main()
