# scripts/fetch_data.py

import yfinance as yf
import pandas as pd
import os

# ----------- SETTINGS -----------
tickers = ['KO', 'PEP', 'NKE', 'ADDYY', 'MCD']  # Coca-Cola, PepsiCo, Nike, Adidas, McDonald's
start_date = '2020-01-01'
end_date = '2024-12-31'
output_folder = 'data/raw'

# ----------- CREATE OUTPUT FOLDER -----------
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ----------- FETCH AND SAVE DATA -----------
for ticker in tickers:
    print(f"📥 Fetching data for {ticker}...")
    stock = yf.download(ticker, start=start_date, end=end_date, progress=False)

    if not stock.empty:
        stock.reset_index(inplace=True)
        stock['Ticker'] = ticker
        output_path = os.path.join(output_folder, f"{ticker}.csv")
        stock.to_csv(output_path, index=False)
        print(f"✅ Saved to {output_path}")
    else:
        print(f"⚠️ No data found for {ticker}")

print("\n🚀 All stock data fetched and saved.")
