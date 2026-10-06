import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "segment_summary.csv"
OUTPUT_FILE = BASE_DIR / "outputs" / "business_insights.txt"

print("Loading segment analysis...")

df = pd.read_csv(INPUT_FILE)

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------
# Key Segment Identification
# ---------------------------------------------------------

largest_segment = df.loc[df["Customers"].idxmax()]
highest_revenue_segment = df.loc[df["Revenue_Percentage"].idxmax()]
highest_value_segment = df.loc[df["Avg_Monetary"].idxmax()]

at_risk = df[df["Segment"] == "At Risk"]

if not at_risk.empty:
    at_risk_row = at_risk.iloc[0]
else:
    at_risk_row = None


# ---------------------------------------------------------
# Revenue Concentration
# ---------------------------------------------------------

priority_segments = df[
    df["Segment"].isin(
        ["Champions", "Loyal Customers"]
    )
]

priority_customers = priority_segments["Customers"].sum()
priority_revenue = priority_segments["Revenue_Percentage"].sum()

total_customers = df["Customers"].sum()

priority_customer_percentage = (
    priority_customers / total_customers * 100
)


# ---------------------------------------------------------
# Generate Business Insights
# ---------------------------------------------------------

insights = []

insights.append("RFM CUSTOMER SEGMENTATION - BUSINESS INSIGHTS")
insights.append("=" * 60)

insights.append(
    f"\n1. Revenue Concentration"
)

insights.append(
    f"Champions and Loyal Customers represent "
    f"{priority_customer_percentage:.2f}% of customers "
    f"and contribute {priority_revenue:.2f}% of total revenue."
)

insights.append(
    "\nBusiness implication: These customers should be prioritized "
    "for retention, loyalty programs, personalized offers and "
    "high-value engagement campaigns."
)


insights.append(
    f"\n2. Largest Customer Segment"
)

insights.append(
    f"{largest_segment['Segment']} is the largest segment with "
    f"{int(largest_segment['Customers']):,} customers "
    f"({largest_segment['Customer_Percentage']:.2f}% of the customer base)."
)

insights.append(
    "\nBusiness implication: This segment represents a major "
    "opportunity for targeted engagement and customer migration."
)


insights.append(
    f"\n3. Highest Revenue Segment"
)

insights.append(
    f"{highest_revenue_segment['Segment']} contributes "
    f"{highest_revenue_segment['Revenue_Percentage']:.2f}% "
    f"of total revenue."
)

insights.append(
    "\nBusiness implication: Protecting this segment should be "
    "a major customer retention priority."
)


insights.append(
    f"\n4. Highest Average Customer Value"
)

insights.append(
    f"{highest_value_segment['Segment']} has the highest "
    f"average monetary value at "
    f"£{highest_value_segment['Avg_Monetary']:,.2f} per customer."
)

insights.append(
    "\nBusiness implication: Customers in this segment can be "
    "targeted with premium experiences, cross-selling and "
    "high-value loyalty initiatives."
)


if at_risk_row is not None:

    insights.append(
        f"\n5. At-Risk Customer Opportunity"
    )

    insights.append(
        f"The At Risk segment contains "
        f"{int(at_risk_row['Customers']):,} customers "
        f"and represents {at_risk_row['Revenue_Percentage']:.2f}% "
        f"of total revenue."
    )

    insights.append(
        "\nBusiness implication: A targeted reactivation campaign "
        "could help recover customers showing declining engagement."
    )


# ---------------------------------------------------------
# Segment Strategy
# ---------------------------------------------------------

strategies = {
    "Champions":
        "Reward loyalty, provide VIP benefits, early access and personalized offers.",

    "Loyal Customers":
        "Strengthen retention through loyalty programs, cross-selling and personalized recommendations.",

    "Potential Loyalists":
        "Increase purchase frequency using targeted promotions, bundles and loyalty incentives.",

    "New Customers":
        "Focus on onboarding, second-purchase conversion and early engagement.",

    "At Risk":
        "Launch win-back campaigns, personalized offers and reactivation messaging.",

    "Need Attention":
        "Use targeted engagement campaigns to increase purchase frequency and recency.",

    "Hibernating / Lost":
        "Test low-cost reactivation campaigns while controlling marketing spend."
}


insights.append(
    "\n6. Recommended Marketing Strategy by Segment"
)

insights.append(
    "-" * 60
)

for segment in df["Segment"]:

    strategy = strategies.get(
        segment,
        "Develop a targeted customer engagement strategy."
    )

    insights.append(
        f"{segment}: {strategy}"
    )


# ---------------------------------------------------------
# Save Insights
# ---------------------------------------------------------

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

    file.write("\n".join(insights))


# ---------------------------------------------------------
# Terminal Output
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS GENERATED")
print("=" * 60)

print("\nKey Findings:")

print(
    f"\n• Champions + Loyal Customers:"
    f" {priority_customer_percentage:.2f}% of customers → "
    f"{priority_revenue:.2f}% of revenue"
)

print(
    f"• Largest segment:"
    f" {largest_segment['Segment']}"
)

print(
    f"• Highest revenue segment:"
    f" {highest_revenue_segment['Segment']}"
)

print(
    f"• Highest average customer value:"
    f" {highest_value_segment['Segment']}"
)

if at_risk_row is not None:
    print(
        f"• At-risk revenue:"
        f" {at_risk_row['Revenue_Percentage']:.2f}%"
    )

print(f"\nInsights saved to:")
print(OUTPUT_FILE)
