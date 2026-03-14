import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ── PAGE CONFIG ──────────────────────────────────────────
st.set_page_config(page_title="E-Commerce Sales Analytics", page_icon="🛒", layout="wide")

# ── LOAD DATA ──────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("ecommerce_raw_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = pd.to_numeric(df["revenue"])
    df["profit"] = pd.to_numeric(df["profit"])
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file 'ecommerce_raw_data.csv' not found. Please ensure it is in the same directory.")
    st.stop()

# ── CUSTOM CSS ────────────────────────────────────────────
st.markdown("""
<style>
    div[data-testid="stMetricValue"] {
        font-size: 28px;
        color: #1F7872;
    }
</style>
""", unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────────
st.title("🛒 E-Commerce Sales Analytics Dashboard")
st.markdown("Interactive dashboard analyzing 1,000 e-commerce orders across 7 product categories and 15 Indian states for FY 2024.")
st.divider()

# ── SIDEBAR FILTERS ───────────────────────────────────────
st.sidebar.header("Filters")
selected_category = st.sidebar.multiselect("Select Category", df["category"].unique(), default=df["category"].unique())
selected_state = st.sidebar.multiselect("Select State", df["state"].unique(), default=df["state"].unique())

# Filter the dataframe based on selection
filtered_df = df[df["category"].isin(selected_category) & df["state"].isin(selected_state)]

# ── KPIs ──────────────────────────────────────────────────
if not filtered_df.empty:
    total_revenue = filtered_df["revenue"].sum()
    total_profit  = filtered_df["profit"].sum()
    total_orders  = len(filtered_df)
    avg_order_val = filtered_df["revenue"].mean()
    profit_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
    return_rate   = filtered_df["returned"].mean() * 100

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Total Revenue", f"₹ {total_revenue/100000:.2f} L")
    col2.metric("Total Profit", f"₹ {total_profit/100000:.2f} L")
    col3.metric("Profit Margin", f"{profit_margin:.1f}%")
    col4.metric("Total Orders", f"{total_orders:,}")
    col5.metric("Avg Order Value", f"₹ {avg_order_val:,.0f}")
    col6.metric("Return Rate", f"{return_rate:.1f}%")
    st.divider()

    # ── CHARTS ────────────────────────────────────────────────
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("Monthly Revenue Trend")
        monthly_sorted = filtered_df.groupby("month_num")["revenue"].sum().reset_index()
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        ax1.plot(monthly_sorted["month_num"], monthly_sorted["revenue"]/1000, marker="o", color="#2E75B6", linewidth=2)
        ax1.set_xlabel("Month (1-12)")
        ax1.set_ylabel("Revenue (₹ K)")
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig1)

        st.subheader("Payment Method Distribution")
        pay_counts = filtered_df["payment"].value_counts()
        fig3, ax3 = plt.subplots(figsize=(6, 4))
        ax3.pie(pay_counts.values, labels=pay_counts.index, autopct="%1.0f%%", startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
        st.pyplot(fig3)

    with col_chart2:
        st.subheader("Revenue by Category")
        cat_rev = filtered_df.groupby("category")["revenue"].sum().sort_values(ascending=True)
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.barh(cat_rev.index, cat_rev.values/1000, color="#1F7872")
        ax2.set_xlabel("Revenue (₹ K)")
        st.pyplot(fig2)

        st.subheader("Customer Rating Distribution")
        rating_counts = filtered_df["rating"].value_counts().sort_index()
        fig4, ax4 = plt.subplots(figsize=(6, 4))
        rating_counts.plot(kind="bar", ax=ax4, color="#C55A11")
        ax4.set_xlabel("Rating (1-5)")
        ax4.set_ylabel("Count")
        st.pyplot(fig4)

    st.divider()

    # ── DATA TABLE ────────────────────────────────────────────
    st.subheader("Raw Data View")
    st.dataframe(filtered_df.head(100), use_container_width=True)

else:
    st.warning("No data available for the selected filters.")

