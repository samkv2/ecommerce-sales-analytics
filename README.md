# E-Commerce Sales Analytics — Python Portfolio Project

## Project Overview
End-to-end data analytics project on 1,000 e-commerce orders across 7 product categories and 15 Indian states for FY 2024.

## Key Findings
- Total Revenue  : Rs 74.0 Lakhs
- Total Profit   : Rs 21.0 Lakhs  
- Profit Margin  : 28.3%
- Top Category   : Electronics (highest revenue)
- Top State      : Uttar Pradesh
- Top Channel    : Paid Ad
- Return Rate    : 10.4%
- Avg Rating     : 4.05 / 5

## Skills Demonstrated
- **Data Generation** — Realistic synthetic dataset with Python
- **Data Cleaning** — Null checks, type conversion, duplicate detection
- **Exploratory Data Analysis (EDA)** — groupby, agg, describe, corr
- **Pandas** — DataFrame operations, multi-column aggregation, sorting
- **Matplotlib** — 8-chart dashboard with annotations
- **Business Insights** — KPIs, trend analysis, segment performance

## Files
| File | Description |
|------|-------------|
| `ecommerce_raw_data.csv` | 1,000 raw order records |
| `ecommerce_analysis.py` | Full Python analysis script |
| `ecommerce_analysis.xlsx` | Multi-sheet Excel output |
| `ecommerce_dashboard.png` | 8-chart visual dashboard |

## How to Run

### Windows
1. **Clone the repository:**
   ```cmd
   git clone https://github.com/sachanlabs/ecommerce-sales-analytics.git
   cd ecommerce-sales-analytics
   ```
2. **Create a virtual environment:**
   ```cmd
   python -m venv venv
   ```
3. **Activate the virtual environment:**
   ```cmd
   venv\Scripts\activate
   ```
4. **Install dependencies:**
   ```cmd
   pip install pandas matplotlib openpyxl streamlit
   ```
5. **Run the analysis script (generates output files):**
   ```cmd
   python ecommerce_analysis.py
   ```
6. **Run the interactive Streamlit dashboard:**
   ```cmd
   streamlit run app.py
   ```

### Linux / macOS
1. **Clone the repository:**
   ```bash
   git clone https://github.com/sachanlabs/ecommerce-sales-analytics.git
   cd ecommerce-sales-analytics
   ```
2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```
3. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```
4. **Install dependencies:**
   ```bash
   pip install pandas matplotlib openpyxl streamlit
   ```
5. **Run the analysis script (generates output files):**
   ```bash
   python3 ecommerce_analysis.py
   ```
6. **Run the interactive Streamlit dashboard:**
   ```bash
   streamlit run app.py
   ```

## Tools Used
Python 3 · Pandas · Matplotlib · OpenPyXL

## Resume Description
> Built an end-to-end E-Commerce Sales Analytics project in Python analyzing 1,000 orders across 7 categories and 15 Indian states. Performed EDA using Pandas (groupby, agg, corr), computed KPIs (revenue, margin, return rate), and visualized insights with an 8-chart Matplotlib dashboard.
