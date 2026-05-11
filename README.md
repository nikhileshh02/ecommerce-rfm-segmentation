# 🛒 E-Commerce Customer Segmentation — RFM Analysis

> **Python → SQLite → Power BI** | Full End-to-End Data Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 📌 Problem Statement

E-commerce businesses struggle to identify which customers are likely to churn, which are their most valuable, and how to prioritise marketing spend across a large customer base. Without a structured segmentation model, businesses treat all customers the same — wasting budget on already-loyal customers and losing at-risk high-spenders with no targeted intervention.

---

## 🎯 Objective

- Score 10,000 customers using the RFM (Recency, Frequency, Monetary) framework
- Segment customers into 5 actionable business tiers
- Quantify churn risk in dollar terms to make the business case for retention
- Deliver an interactive Power BI dashboard for non-technical stakeholders

---

## 🔄 Approach

1. **Generate** 50,000 synthetic transactions for 10,000 customers using Python + NumPy (seed=42 for reproducibility)
2. **Calculate** R, F, M scores (1–5 each) using quantile-based scoring via pandas `qcut()`
3. **Store** results in a SQLite database and apply segment labels using a SQL `CASE` statement
4. **Export** final labeled data to CSV and visualise in Power BI with DAX measures and interactive slicers

---

## 🗂️ Project Files

```
ecommerce-rfm-segmentation/
│
├── step1_rfm.py                # Phase 1 — Generate data + calculate RFM scores
├── step2_sql.py                # Phase 2 — Load into SQLite database
├── step3_segmentation.py       # Phase 3 — Segment customers + export CSV
│
├── ecommerce.db                # SQLite database (9,924 customers)
├── final_segmented_data.csv    # RFM scores (no segment labels)
├── final_for_powerbi.csv       # Final labeled data → feeds Power BI
│
└── E_Commerce_RFM_Dashboard.pbix  # Power BI dashboard
```

---

## ⚙️ Setup & Run

```bash
pip install pandas numpy
python step1_rfm.py           # Creates final_segmented_data.csv
python step2_sql.py           # Creates ecommerce.db
python step3_segmentation.py  # Creates final_for_powerbi.csv
```
Open `E_Commerce_RFM_Dashboard.pbix` in Power BI Desktop and connect to `final_for_powerbi.csv` if prompted.

---

## 👥 Customer Segments & Results

| Segment | Customers | Avg Spend | Revenue Share | Action |
|---|---|---|---|---|
| 🏆 Champions | 1,900 | $4,165 | 31.5% | Reward & retain |
| 💛 Loyal Customers | 2,671 | $3,058 | 32.5% | Upsell & grow |
| 🌱 Potential Loyalists | 2,719 | $2,089 | 22.6% | Nurture with offers |
| ⚠️ At Risk | 1,985 | $1,422 | 11.2% | Re-engagement campaign |
| ❌ Lost | 649 | $789 | 2.0% | Win-back or accept loss |

> **Key Insight:** 26.5% of customers are at churn risk, representing **$3.33M in revenue at stake**. Champions and Loyal Customers make up only 46% of the base but drive **64% of total revenue**.

---

## 📈 Dashboard Visuals

| Visual | Insight |
|---|---|
| 5 KPI Cards | Total Customers, Revenue, Avg Spend, Revenue at Risk, Churn Risk % |
| Donut Chart | Segment distribution across all 5 tiers |
| Bar Chart | Revenue by segment |
| Bar Chart | Customers by RFM Score Band |
| Scatter Chart | Spend vs Recency — segments visible as distinct clusters |
| 3 Slicers | Filter by Segment, Churn Flag, Spend Tier |

---

## 🧠 Technical Highlights

- `pd.qcut()` for quantile-based scoring — avoids bias from outliers
- `rank(method='first')` on Frequency — handles duplicate order counts fairly
- SQL `CASE` statement for segmentation — business logic stays in the database layer
- Fully reproducible — `np.random.seed(42)` gives identical results every run

---

## 📁 Data Schema

```sql
CREATE TABLE customer_segments (
    Customer_ID              INTEGER,
    Days_Since_Last_Purchase INTEGER,
    Total_Orders             INTEGER,
    Total_Spent              REAL,
    R_Score                  INTEGER,
    F_Score                  INTEGER,
    M_Score                  INTEGER,
    Final_RFM_Score          INTEGER,
    Segment                  TEXT
);
```

---

## 📝 Data Note

Synthetic dataset generated with NumPy (seed=42) for reproducibility. Pipeline and methodology are fully applicable to real-world transaction data.

---

## 👤 Author

**Nikhilesh** — [GitHub](https://github.com/nikhileshh02)

*Open to Data Analyst / Business Analyst roles. Feel free to connect!*
