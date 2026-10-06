import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "rfm.csv"
OUTPUT_FILE = BASE_DIR / "data" / "rfm_scored.csv"

print("Loading RFM data...")

rfm = pd.read_csv(INPUT_FILE)

# ---------------------------------------------------------
# RFM QUARTILE SCORING
# ---------------------------------------------------------

# Recency:
# Lower recency = better customer activity
rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    q=4,
    labels=[4, 3, 2, 1],
    duplicates="drop"
).astype(int)

# Frequency:
# Higher frequency = better customer engagement
rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    q=4,
    labels=[1, 2, 3, 4]
).astype(int)

# Monetary:
# Higher monetary value = higher customer value
rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    q=4,
    labels=[1, 2, 3, 4]
).astype(int)

# Combined RFM score
rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)

# Overall numerical score
rfm["RFM_Total"] = (
    rfm["R_Score"]
    + rfm["F_Score"]
    + rfm["M_Score"]
)

# Save scored dataset
rfm.to_csv(OUTPUT_FILE, index=False)

print("\n" + "=" * 60)
print("RFM SCORING COMPLETED")
print("=" * 60)

print(f"Customers scored: {len(rfm):,}")

print("\nScore distribution:")
print(
    rfm[
        ["R_Score", "F_Score", "M_Score", "RFM_Total"]
    ].describe()
)

print("\nTop RFM profiles:")
print(
    rfm["RFM_Score"]
    .value_counts()
    .head(10)
)

print("\nAverage RFM score:")
print(f"{rfm['RFM_Total'].mean():.2f} / 12")

print(f"\nSaved to:")
print(OUTPUT_FILE)