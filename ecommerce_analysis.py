# ═══════════════════════════════════════════════════════════
# E-COMMERCE SALES ANALYTICS — Python Portfolio Project
# Author : [Your Name]
# Tools  : Python, Pandas, Matplotlib
# Dataset: 1,000 e-commerce orders | FY 2024
# GitHub : github.com/[your-username]/ecommerce-analytics
# ═══════════════════════════════════════════════════════════

import pandas as pd
import matplotlib.pyplot as plt

# ── STEP 1: LOAD DATA ──────────────────────────────────────
df = pd.read_csv("ecommerce_raw_data.csv")
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(df.head())
print(df.info())

# ── STEP 2: DATA CLEANING ─────────────────────────────────
# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicates
print(f"\nDuplicate rows: {df.duplicated().sum()}")

# Data types
df["date"] = pd.to_datetime(df["date"])
df["revenue"] = pd.to_numeric(df["revenue"])
df["profit"] = pd.to_numeric(df["profit"])

# ── STEP 3: EXPLORATORY DATA ANALYSIS (EDA) ───────────────

# KPIs
total_revenue = df["revenue"].sum()
total_profit  = df["profit"].sum()
total_orders  = len(df)
avg_order_val = df["revenue"].mean()
profit_margin = total_profit / total_revenue * 100
return_rate   = df["returned"].mean() * 100

print(f"\n── KEY PERFORMANCE INDICATORS ──")
print(f"Total Revenue   : Rs {total_revenue:,.0f}")
print(f"Total Profit    : Rs {total_profit:,.0f}")
print(f"Profit Margin   : {profit_margin:.1f}%")
print(f"Total Orders    : {total_orders:,}")
print(f"Avg Order Value : Rs {avg_order_val:,.0f}")
print(f"Return Rate     : {return_rate:.1f}%")

# Category-wise analysis using groupby + agg
cat_analysis = df.groupby("category").agg(
    Revenue=("revenue", "sum"),
    Orders=("order_id", "count"),
    Profit=("profit", "sum"),
    Avg_Rating=("rating", "mean")
).round(2).sort_values("Revenue", ascending=False)
cat_analysis["Margin_%"] = (cat_analysis["Profit"] / cat_analysis["Revenue"] * 100).round(1)
print("\n── CATEGORY ANALYSIS ──")
print(cat_analysis)

# Monthly trend
monthly = df.groupby("month_num").agg(
    Revenue=("revenue", "sum"),
    Orders=("order_id", "count")
).reset_index()
print("\n── MONTHLY REVENUE ──")
print(monthly)

# Channel performance
channel = df.groupby("channel").agg(
    Revenue=("revenue", "sum"),
    Orders=("order_id", "count"),
    Avg_Order=("revenue", "mean")
).sort_values("Revenue", ascending=False)
print("\n── CHANNEL PERFORMANCE ──")
print(channel)

# State-wise top 5
state_top = df.groupby("state")["revenue"].sum().sort_values(ascending=False).head(5)
print("\n── TOP 5 STATES ──")
print(state_top)

# Correlation analysis
numeric_cols = ["quantity", "unit_price", "discount_pct", "revenue", "profit", "rating"]
print("\n── CORRELATION MATRIX ──")
print(df[numeric_cols].corr().round(2))

# ── STEP 4: VISUALISATION ─────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("E-Commerce Sales Analytics", fontsize=16, fontweight="bold")

# 1. Monthly Revenue
monthly_sorted = df.groupby("month_num")["revenue"].sum().reset_index()
axes[0,0].plot(monthly_sorted["month_num"], monthly_sorted["revenue"]/1000,
               marker="o", color="#2E75B6", linewidth=2)
axes[0,0].set_title("Monthly Revenue Trend")
axes[0,0].set_xlabel("Month"); axes[0,0].set_ylabel("Revenue (Rs K)")

# 2. Category Revenue
cat_rev = df.groupby("category")["revenue"].sum().sort_values()
axes[0,1].barh(cat_rev.index, cat_rev.values/1000, color="#1F7872")
axes[0,1].set_title("Revenue by Category")
axes[0,1].set_xlabel("Revenue (Rs K)")

# 3. Payment Methods
pay_counts = df["payment"].value_counts()
axes[1,0].pie(pay_counts.values, labels=pay_counts.index, autopct="%1.0f%%", startangle=90)
axes[1,0].set_title("Payment Method Distribution")

# 4. Rating Distribution
df["rating"].value_counts().sort_index().plot(kind="bar", ax=axes[1,1], color="#C55A11")
axes[1,1].set_title("Customer Rating Distribution")
axes[1,1].set_xlabel("Rating"); axes[1,1].set_ylabel("Count")

plt.tight_layout()
plt.savefig("ecommerce_dashboard.png", dpi=120, bbox_inches="tight")
plt.show()
print("\nAnalysis complete! Chart saved as ecommerce_dashboard.png")

# ── STEP 5: EXPORT RESULTS ────────────────────────────────
with pd.ExcelWriter("ecommerce_analysis.xlsx") as writer:
    df.to_excel(writer, sheet_name="Raw Data", index=False)
    cat_analysis.to_excel(writer, sheet_name="Category Analysis")
    monthly.to_excel(writer, sheet_name="Monthly Trend", index=False)
    channel.to_excel(writer, sheet_name="Channel Analysis")

print("Results exported to ecommerce_analysis.xlsx")
