import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"

df = pd.read_excel(DATA_FILE)

print("=" * 60)
print("DATA QUALITY ANALYSIS")
print("=" * 60)

print(f"\nTotal rows: {len(df):,}")

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Cancelled invoices
cancelled = df["InvoiceNo"].astype(str).str.startswith("C")
print(f"\nCancelled invoice rows: {cancelled.sum():,}")

# Negative quantities
negative_qty = df["Quantity"] < 0
print(f"Negative quantity rows: {negative_qty.sum():,}")

# Zero quantities
zero_qty = df["Quantity"] == 0
print(f"Zero quantity rows: {zero_qty.sum():,}")

# Zero prices
zero_price = df["UnitPrice"] == 0
print(f"Zero price rows: {zero_price.sum():,}")

# Negative prices
negative_price = df["UnitPrice"] < 0
print(f"Negative price rows: {negative_price.sum():,}")

# Missing customers
missing_customer = df["CustomerID"].isnull()
print(f"Missing CustomerID rows: {missing_customer.sum():,}")

# Duplicate rows
duplicates = df.duplicated()
print(f"Duplicate rows: {duplicates.sum():,}")

# Date range
print("\nDate range:")
print(f"Earliest: {df['InvoiceDate'].min()}")
print(f"Latest:   {df['InvoiceDate'].max()}")

# Countries
print(f"\nUnique countries: {df['Country'].nunique()}")

# Customers
print(f"Unique customers: {df['CustomerID'].nunique():,}")

print("\nData quality analysis completed.")
