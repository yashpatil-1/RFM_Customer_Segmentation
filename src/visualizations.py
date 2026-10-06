import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "customer_segments.csv"
SUMMARY_FILE = BASE_DIR / "data" / "segment_summary.csv"
OUTPUT_DIR = BASE_DIR / "visuals"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Loading segmented customer data...")

df = pd.read_csv(INPUT_FILE)
segment_summary = pd.read_csv(SUMMARY_FILE)

sns.set_theme(style="whitegrid")


# ---------------------------------------------------------
# 1. Customer Distribution by Segment
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

customer_order = (
    segment_summary
    .sort_values("Customers", ascending=False)["Segment"]
)

sns.barplot(
    data=segment_summary,
    x="Customers",
    y="Segment",
    order=customer_order
)

plt.title("Customer Distribution by Segment")
plt.xlabel("Number of Customers")
plt.ylabel("Customer Segment")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "customer_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ---------------------------------------------------------
# 2. Revenue Contribution by Segment
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

revenue_order = (
    segment_summary
    .sort_values("Revenue_Percentage", ascending=False)["Segment"]
)

sns.barplot(
    data=segment_summary,
    x="Revenue_Percentage",
    y="Segment",
    order=revenue_order
)

plt.title("Revenue Contribution by Customer Segment")
plt.xlabel("Revenue Contribution (%)")
plt.ylabel("Customer Segment")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_contribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ---------------------------------------------------------
# 3. RFM Score Distribution
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="RFM_Total"
)

plt.title("Distribution of Overall RFM Scores")
plt.xlabel("RFM Total Score")
plt.ylabel("Number of Customers")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "rfm_score_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ---------------------------------------------------------
# 4. Recency vs Monetary Value
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Recency",
    y="Monetary",
    hue="Segment",
    alpha=0.65
)

plt.title("Recency vs Monetary Value")
plt.xlabel("Recency (Days)")
plt.ylabel("Monetary Value (£)")
plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "recency_vs_monetary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ---------------------------------------------------------
# 5. Frequency vs Monetary Value
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Frequency",
    y="Monetary",
    hue="Segment",
    alpha=0.65
)

plt.title("Frequency vs Monetary Value")
plt.xlabel("Purchase Frequency")
plt.ylabel("Monetary Value (£)")
plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "frequency_vs_monetary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ---------------------------------------------------------
# 6. Segment RFM Profile
# ---------------------------------------------------------

segment_rfm = (
    df.groupby("Segment")
    .agg(
        Recency=("Recency", "mean"),
        Frequency=("Frequency", "mean"),
        Monetary=("Monetary", "mean")
    )
    .reset_index()
)

segment_rfm_melted = segment_rfm.melt(
    id_vars="Segment",
    var_name="Metric",
    value_name="Average_Value"
)

plt.figure(figsize=(12, 7))

sns.barplot(
    data=segment_rfm_melted,
    x="Segment",
    y="Average_Value",
    hue="Metric"
)

plt.title("Average RFM Metrics by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Average Value")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "segment_rfm_profile.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print("\n" + "=" * 60)
print("VISUALIZATION GENERATION COMPLETED")
print("=" * 60)

print("\nGenerated visualizations:")

for file in sorted(OUTPUT_DIR.glob("*.png")):
    print(f"✓ {file.name}")

print(f"\nSaved to:")
print(OUTPUT_DIR)
