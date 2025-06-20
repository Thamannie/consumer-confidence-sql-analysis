import pandas as pd
import os

# --- Paths 
RAW_DIR = 'data/raw'
MERGED_DIR = 'data/merged'
OUTPUT_FILE = os.path.join(MERGED_DIR, 'merged_data.csv')

# --- CSV files and tickers ---
files = {
    'ADDYY.csv': 'ADDYY',
    'KO.csv': 'KO',
    'MCD.csv': 'MCD',
    'NKE.csv': 'NKE',
    'PEP.csv': 'PEP'
}

# --- Load, label, and collect DataFrames ---
all_data = []

for file, ticker in files.items():
    file_path = os.path.join(RAW_DIR, file)
    df = pd.read_csv(file_path)
    df['Ticker'] = ticker  # Add a column for ticker
    all_data.append(df)

# --- Combine all into a single DataFrame ---
merged_df = pd.concat(all_data, ignore_index=True)

# --- Ensure merged directory exists ---
os.makedirs(MERGED_DIR, exist_ok=True)

# --- Save to CSV ---
merged_df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Merged data saved to: {OUTPUT_FILE}")
