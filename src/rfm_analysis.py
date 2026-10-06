import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "clean_retail_transactions.csv"
OUTPUT_FILE = BASE_DIR / "data" / "rfm.csv"

print("Loading cleaned transaction data...")

df = pd.read_csv(
    INPUT_FILE,
    parse_dates=["InvoiceDate"]
)

# RFM reference date
snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Calculate RFM metrics
rfm = (
    df.groupby("CustomerID")
    .agg(
        Recency=(
            "InvoiceDate",
            lambda x: (snapshot_date - x.max()).days
        ),
        Frequency=(
            "InvoiceNo",
            "nunique"
        ),
        Monetary=(
            "TransactionValue",
            "sum"
        )
    )
    .reset_index()
)

# Save RFM dataset
rfm.to_csv(OUTPUT_FILE, index=False)

print("\n" + "=" * 60)
print("RFM ANALYSIS COMPLETED")
print("=" * 60)

print(f"Snapshot date:       {snapshot_date}")
print(f"Customers analyzed:  {len(rfm):,}")

print(f"\nAverage Recency:     {rfm['Recency'].mean():.2f} days")
print(f"Median Recency:      {rfm['Recency'].median():.2f} days")

print(f"\nAverage Frequency:   {rfm['Frequency'].mean():.2f} orders")
print(f"Median Frequency:    {rfm['Frequency'].median():.2f} orders")

print(f"\nAverage Monetary:    £{rfm['Monetary'].mean():,.2f}")
print(f"Median Monetary:     £{rfm['Monetary'].median():,.2f}")

print("\nRFM Summary:")
print(rfm[["Recency", "Frequency", "Monetary"]].describe())

print(f"\nSaved to:")
print(OUTPUT_FILE)