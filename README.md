# 🛒 Customer Segmentation Using RFM Analysis

An end-to-end customer analytics project that uses **RFM (Recency, Frequency, Monetary)** analysis to segment customers, evaluate customer lifetime value, and generate actionable, data-driven marketing strategies.

This project converts raw e-commerce transaction data into customer-level business insights through automated data cleaning, metric scoring, segment profiling, visualization, and strategic reporting.

---

## 📌 Project Overview

Analyzing thousands of individual transaction logs makes it difficult for businesses to pinpoint high-value customers, identify churn risk, or target marketing budgets effectively.

This pipeline solves that challenge by transforming transaction logs into three core dimensions:

- **Recency ($R$)**: How recently a customer made a purchase (days since last order).
- **Frequency ($F$)**: How often a customer purchased (total unique orders).
- **Monetary ($M$)**: How much money a customer spent in total transaction value.

Customers are scored on a scale of 1–4 across each metric, combined into an RFM profile, and categorized into distinct business segments.

---

## 🎯 Business Objectives

- **Identify High-Value Customers**: Isolate top-tier revenue drivers for VIP retention.
- **Analyze Purchasing Patterns**: Measure customer engagement through recency and order frequency.
- **Mitigate Customer Churn**: Detect slipping customers early to run targeted re-engagement campaigns.
- **Quantify Revenue Concentration**: Determine segment contribution to overall gross revenue.
- **Automate Business Intelligence**: Provide an end-to-end executable pipeline from raw input to generated figures and reports.

---

## 📊 Dataset Overview

The project utilizes the **Online Retail** dataset sourced from
[ the UCI Machine Learning Repository.](https://archive.ics.uci.edu/dataset/352/online+retail)

### Dataset Summary

| Attribute | Value |
| :--- | :--- |
| **Original Transactions** | 541,909 rows |
| **Cleaned Transactions** | 392,692 rows |
| **Unique Customers** | 4,338 |
| **Unique Invoices** | 18,532 |
| **Countries Covered** | 37 |
| **Total Revenue Processed** | £8.89 Million |
| **Date Range** | Dec 2010 – Dec 2011 |

### Attributes
- `InvoiceNo`: Unique order identifier (prefixed with "C" if cancelled).
- `StockCode`: Product/item code.
- `Description`: Item name.
- `Quantity`: Quantities per transaction.
- `InvoiceDate`: Timestamp of order creation.
- `UnitPrice`: Product price per unit in GBP (£).
- `CustomerID`: Unique customer identifier.
- `Country`: Customer location.

---

## 🧹 Data Cleaning & Preprocessing

To ensure statistical integrity, raw transactions undergo automated cleaning steps:

1. **Missing Data Handling**: Removed rows without valid `CustomerID` values.
2. **Cancellation Filtering**: Removed cancelled invoices (invoices prefixed with 'C').
3. **Invalid Transaction Removal**: Filtered out non-positive quantities ($Quantity \le 0$) and unit prices ($UnitPrice \le 0$).
4. **Deduplication**: Stripped identical duplicate records.
5. **Feature Engineering**: Generated total transaction value per line item:
   $$\text{TransactionValue} = \text{Quantity} \times \text{UnitPrice}$$

---

## 📐 RFM Analysis & Scoring

### Metrics Snapshot

| Metric | Average | Median |
| :--- | :---: | :---: |
| **Recency** | 92.54 days | 51.00 days |
| **Frequency** | 4.27 orders | 2.00 orders |
| **Monetary** | £2,048.69 | £668.57 |

> **Key Insight**: The significant variance between the average (£2,048.69) and median (£668.57) monetary values indicates a heavily right-skewed spend distribution.

### Scoring Logic
Customers are assigned a score from 1 to 4 across each dimension based on quartile boundaries:

- **Recency**: Lower number of days $\rightarrow$ **Higher Score (4)**
- **Frequency**: Higher order counts $\rightarrow$ **Higher Score (4)**
- **Monetary**: Higher spending amount $\rightarrow$ **Higher Score (4)**

Scores are aggregated into an RFM Profile (e.g., `444` represents maximum engagement across all three vectors). Out of **4,338** scored customers, the most frequent individual profile was **444** (489 customers).

---

## 👥 Customer Segments & Business Impact

| Segment | Customers | Customer % | Revenue % | Core Definition |
| :--- | :---: | :---: | :---: | :--- |
| **🏆 Champions** | 489 | 11.27% | 49.78% | High recency, high frequency, highest spenders. |
| **💛 Loyal Customers** | 828 | 19.09% | 23.23% | Regular buyers with high monetary contribution. |
| **⚠️ At Risk** | 449 | 10.35% | 10.75% | Previously high spenders who haven't bought recently. |
| **😴 Hibernating / Lost** | 1,135 | 26.16% | 5.48% | Low recency, low frequency, low overall spend. |
| **🌟 Potential Loyalists** | 442 | 10.19% | 5.29% | Recent buyers with average purchasing frequency. |
| **🔔 Need Attention** | 875 | 20.17% | 5.09% | Above-average recency and frequency, but at risk of dropping off. |
| **🆕 New Customers** | 120 | 2.77% | 0.38% | Recent buyers with low overall transaction counts. |

---

## 🔥 Key Business Findings

1. **Extreme Revenue Concentration**: **30.36%** of the customer base (*Champions* + *Loyal Customers*) accounts for **73.01%** of total revenue.
2. **Champions dominate profitability**: The *Champions* segment alone drives nearly **50% of revenue** while representing only **11.27%** of the total customer base.
3. **Significant Inactive Footprint**: Over **26%** of customers fall into *Hibernating / Lost*, bringing in under **6%** of gross revenue.
4. **Reactivation Opportunity**: The *At Risk* segment controls **10.75%** of historical revenue, representing a primary focus area for win-back campaigns.

---

## 🎯 Strategic Recommendations

| Segment | Recommended Action Plan |
| :--- | :--- |
| **Champions** | VIP rewards programs, early access to product launches, personalized perks, and review requests. |
| **Loyal Customers** | Upselling, cross-selling high-margin items, and tier-based loyalty incentives. |
| **Potential Loyalists** | Targeted product bundles, personalized recommendations, and membership invitations. |
| **New Customers** | Dedicated onboarding flows, welcome discount codes for second purchases. |
| **At Risk** | Personalized re-engagement emails, high-value discount vouchers, and feedback surveys. |
| **Need Attention** | Time-limited promotions, re-activation offers, and targeted feature recommendations. |
| **Hibernating / Lost** | Low-cost automated email sequences, win-back discounts, or minimal marketing spend focus. |

---

## 📈 Generated Visual Analytics

Running the pipeline automatically saves the following plots to the `visuals/` directory:

- `customer_distribution.png`: Bar chart of customer volume per segment.
- `revenue_contribution.png`: Pareto breakdown of total monetary contribution by segment.
- `rfm_score_distribution.png`: Histogram detailing overall RFM score distribution.
- `recency_vs_monetary.png`: Scatter plot comparing days since last purchase against spend.
- `frequency_vs_monetary.png`: Relationship between total order count and lifetime value.
- `segment_rfm_profile.png`: Heatmap/Bar summary of mean $R, F, M$ values per segment.

---

## ⚙️ Project Architecture

```text
RFM Customer Segmentation/
│
├── data/
│   ├── online_retail_II.xlsx        # Raw input transaction dataset
│   ├── clean_retail_transactions.csv# Filtered dataset post cleaning
│   ├── rfm.csv                      # Raw RFM metric values per customer
│   ├── rfm_scored.csv               # Customer RFM scores (1-4 scale)
│   ├── customer_segments.csv        # Final dataset with assigned segments
│   └── segment_summary.csv          # Aggregate metrics per segment
│
├── notebooks/                       # Exploratory analysis and scratchpads
│
├── src/
│   ├── data_inspection.py           # Initial data structure and schema evaluation
│   ├── data_quality.py              # Anomaly and missing value check routines
│   ├── data_cleaning.py             # Preprocessing & cleaning pipeline
│   ├── rfm_analysis.py              # RFM metric calculation algorithms
│   ├── rfm_scoring.py               # Scoring logic implementation
│   ├── customer_segmentation.py     # Segment mapping logic
│   ├── visualizations.py            # Chart generation scripts
│   └── business_insights.py         # Automated summary and report generator
│
├── outputs/
│   └── business_insights.txt        # Text summary of generated insights
│
├── visuals/                         # Saved figures and visualizations
│   ├── customer_distribution.png
│   ├── revenue_contribution.png
│   ├── rfm_score_distribution.png
│   ├── recency_vs_monetary.png
│   ├── frequency_vs_monetary.png
│   └── segment_rfm_profile.png
│
├── main.py                          # Full end-to-end pipeline launcher
├── requirements.txt                 # Python dependencies
├── README.md                        # Documentation
└── .gitignore
```

---

## 🚀 Execution & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/RFM-Customer-Segmentation.git
cd RFM-Customer-Segmentation
```

### 2. Set Up Virtual Environment

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Execute the Automated Pipeline
```bash
python main.py
```

#### Executed Stages:
$$\text{Data Inspection} \longrightarrow \text{Quality Check} \longrightarrow \text{Cleaning} \longrightarrow \text{RFM Computation} \longrightarrow \text{Scoring} \longrightarrow \text{Segmentation} \longrightarrow \text{Visualization} \longrightarrow \text{Report Generation}$$

---

## 🛠️ Tools & Technologies

- **Language**: Python 3.8+
- **Data Manipulation**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
- **Excel Processing**: OpenPyXL
- **Environment**: Jupyter Notebook, VS Code
- **Version Control**: Git, GitHub

---

## 👤 Author

**Yash Patil**  
*MBA Tech – Computer Engineering*  
NMIMS

---

## 📄 License

This project is open-source and intended for educational, analytical, and portfolio presentation purposes.