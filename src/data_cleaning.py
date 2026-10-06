import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"
OUTPUT_FILE = BASE_DIR / "data" / "clean_retail_transactions.csv"

print("Loading dataset...")

df = pd.read_excel(INPUT_FILE)

original_rows = len(df)

# 1. Remove transactions without CustomerID
df = df.dropna(subset=["CustomerID"])

# 2. Remove cancelled invoices
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# 3. Keep only valid purchases
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# 4. Remove duplicate transactions
df = df.drop_duplicates()

# 5. Calculate transaction revenue
df["TransactionValue"] = df["Quantity"] * df["UnitPrice"]

# Create output directory if required
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# Save cleaned dataset
df.to_csv(OUTPUT_FILE, index=False)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)

print(f"Original rows:       {original_rows:,}")
print(f"Clean rows:          {len(df):,}")
print(f"Rows removed:        {original_rows - len(df):,}")
print(f"Customers:           {df['CustomerID'].nunique():,}")
print(f"Transactions:        {df['InvoiceNo'].nunique():,}")
print(f"Countries:           {df['Country'].nunique():,}")
print(f"Total revenue:       £{df['TransactionValue'].sum():,.2f}")

print(f"\nSaved to:")
print(OUTPUT_FILE)