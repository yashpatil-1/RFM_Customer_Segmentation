import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "rfm_scored.csv"
OUTPUT_FILE = BASE_DIR / "data" / "customer_segments.csv"

print("Loading scored RFM data...")

rfm = pd.read_csv(INPUT_FILE)


def assign_segment(row):
    r = row["R_Score"]
    f = row["F_Score"]
    m = row["M_Score"]

    # 1. Champions
    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"

    # 2. Loyal Customers
    elif r >= 3 and f >= 3 and m >= 3:
        return "Loyal Customers"

    # 3. Potential Loyalists
    elif r >= 3 and f >= 2 and m >= 2:
        return "Potential Loyalists"

    # 4. New Customers
    elif r >= 4 and f <= 2:
        return "New Customers"

    # 5. At Risk
    elif r <= 2 and f >= 3 and m >= 3:
        return "At Risk"

    # 6. Need Attention
    elif r <= 2 and f >= 2:
        return "Need Attention"

    # 7. Hibernating / Lost
    else:
        return "Hibernating / Lost"


rfm["Segment"] = rfm.apply(assign_segment, axis=1)


# Segment summary
segment_summary = (
    rfm.groupby("Segment")
    .agg(
        Customers=("CustomerID", "count"),
        Avg_Recency=("Recency", "mean"),
        Avg_Frequency=("Frequency", "mean"),
        Avg_Monetary=("Monetary", "mean"),
        Total_Revenue=("Monetary", "sum")
    )
    .reset_index()
)

# Customer percentage
segment_summary["Customer_Percentage"] = (
    segment_summary["Customers"]
    / len(rfm)
    * 100
)

# Revenue percentage
segment_summary["Revenue_Percentage"] = (
    segment_summary["Total_Revenue"]
    / rfm["Monetary"].sum()
    * 100
)

# Sort by revenue contribution
segment_summary = segment_summary.sort_values(
    "Revenue_Percentage",
    ascending=False
)

# Save customer-level segmentation
rfm.to_csv(OUTPUT_FILE, index=False)

# Save segment summary
SUMMARY_FILE = BASE_DIR / "data" / "segment_summary.csv"
segment_summary.to_csv(SUMMARY_FILE, index=False)


print("\n" + "=" * 60)
print("CUSTOMER SEGMENTATION COMPLETED")
print("=" * 60)

print(f"\nCustomers segmented: {len(rfm):,}")
print(f"Number of segments: {rfm['Segment'].nunique()}")

print("\nSegment Distribution:")
print(
    rfm["Segment"]
    .value_counts()
)

print("\nSegment Summary:")
print(
    segment_summary.to_string(index=False)
)

print(f"\nCustomer segments saved to:")
print(OUTPUT_FILE)

print(f"\nSegment summary saved to:")
print(SUMMARY_FILE)