# 📊 Mutual Fund Analytics Platform

**Bluestock Fintech – Individual Capstone Project**

---

# 📌 Project Overview

The Mutual Fund Analytics Platform is an end-to-end data analytics project that demonstrates the complete lifecycle of a mutual fund analytics system.

The project performs:

- Data ingestion
- Data cleaning
- SQL database creation
- Exploratory Data Analysis (EDA)
- Performance analytics
- Advanced risk analytics
- Interactive Power BI dashboard

The project is developed using Python, Pandas, SQLite, SQL, Jupyter Notebook, and Microsoft Power BI.

---

# 🎯 Objectives

- Import and process multiple mutual fund datasets
- Clean and validate financial data
- Store datasets in SQLite database
- Perform SQL-based analysis
- Calculate mutual fund performance metrics
- Build advanced risk analytics
- Create an interactive Power BI dashboard
- Generate reports for investment analysis

---

# 🛠️ Tech Stack

- Python 3.12
- Pandas
- NumPy
- Matplotlib
- SciPy
- SQLite
- SQLAlchemy
- Jupyter Notebook
- Microsoft Power BI
- VS Code

---

# 📂 Project Structure

```
BLUESTOCK_MF_ANALYTICS/
│
├── dashboard/
│   └── bluestock_mf.pbix
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│       └── bluestock_mf.db
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── reports/
│   ├── alpha_beta.csv
│   ├── cagr_table.csv
│   ├── fund_scorecard.csv
│   ├── max_drawdown.csv
│   ├── sharpe_ratio.csv
│   ├── sortino_ratio.csv
│   ├── tracking_error.csv
│   ├── var_cvar_report.csv
│   ├── sip_continuity_report.csv
│   ├── Dashboard.pdf
│   ├── Page1.png
│   ├── Page2.png
│   ├── Page3.png
│   ├── Page4.png
│   └── rolling_sharpe_chart.png
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── compute_metrics.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── README.md
└── requirements.txt
```

---

# 📥 Data Sources

The project uses cleaned mutual fund datasets including:

- Fund Master
- NAV History
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Category Inflows
- SIP Inflows
- Industry Folio Count
- Benchmark Indices

---

# ⚙️ Project Workflow

## Step 1 — Data Ingestion

- Import CSV datasets
- Validate schema
- Handle missing values
- Load into Pandas DataFrames

Notebook:

```
01_data_ingestion.ipynb
```

---

## Step 2 — Data Cleaning

Performed:

- Duplicate removal
- Missing value handling
- Data type conversion
- Date formatting
- Column standardization

Notebook:

```
02_data_cleaning.ipynb
```

---

## Step 3 — Exploratory Data Analysis

Performed:

- Category distribution
- Fund house analysis
- Return analysis
- AUM analysis
- Investor transaction analysis

Notebook:

```
03_eda_analysis.ipynb
```

---

## Step 4 — Performance Analytics

Calculated:

- Daily Returns
- CAGR (1Y, 3Y, 5Y)
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Tracking Error
- Fund Scorecard

Notebook:

```
04_performance_analytics.ipynb
```

Generated Reports:

- alpha_beta.csv
- sharpe_ratio.csv
- sortino_ratio.csv
- cagr_table.csv
- tracking_error.csv
- max_drawdown.csv
- fund_scorecard.csv

---

## Step 5 — Advanced Analytics

Implemented:

- Historical VaR (95%)
- Conditional VaR (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Simple Fund Recommender
- Advanced Insights

Notebook:

```
05_advanced_analytics.ipynb
```

Generated Reports:

- var_cvar_report.csv
- sip_continuity_report.csv
- rolling_sharpe_chart.png

---

# 💻 Python Scripts

## etl_pipeline.py

Automates:

- Data loading
- Data cleaning
- SQLite storage

---

## compute_metrics.py

Computes:

- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown

---

## live_nav_fetch.py

Fetches latest NAV data for selected mutual funds.

---

## recommender.py

Simple recommendation engine based on:

- Risk Grade
- Sharpe Ratio

Returns Top 3 recommended mutual funds.

---

# 🗄 Database

Database:

```
bluestock_mf.db
```

Contains cleaned mutual fund datasets stored in SQLite.

SQL files:

- schema.sql
- queries.sql

---

# 📈 Power BI Dashboard

The dashboard consists of four pages:

## Page 1 – Industry Overview

- KPI Cards
- Total AUM
- SIP Inflows
- Folios
- Schemes
- Industry AUM Trend
- AUM by Fund House

---

## Page 2 – Fund Performance

- Risk vs Return Scatter Plot
- Top Mutual Fund Table
- NAV Analysis
- Performance Comparison
- Interactive Slicers

---

## Page 3 – Investor Analytics

- Transaction Amount by State
- Transaction Type Distribution
- Average SIP by Age Group
- Monthly Transaction Volume
- State Filters
- Age Group Filters
- City Tier Filters

---

## Page 4 – SIP & Market Trends

- SIP Inflow vs YoY Growth
- Category Inflow Analysis
- Heatmap
- Top Categories by Inflow

---

# 📊 Performance Metrics

Implemented metrics include:

- CAGR
- Daily Returns
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Tracking Error
- VaR
- CVaR
- Rolling Sharpe Ratio

---

# 📁 Deliverables

- Power BI Dashboard (.pbix)
- Dashboard PDF
- Dashboard PNG Images
- SQLite Database
- SQL Scripts
- Python Scripts
- Jupyter Notebooks
- Analytics Reports

---

# 🚀 Future Enhancements

- Live AMFI API Integration
- Machine Learning Fund Recommendation
- Portfolio Optimization
- Web Dashboard using Streamlit
- Real-time NAV Updates
- Automated ETL Scheduling

---

# 👨‍💻 Author

** M Hari Sreenivas**

B.Tech – Artificial Intelligence & Data Science

Amrita Vishwa Vidyapeetham

Bluestock Fintech Capstone Project

---

# 📜 License

This project was developed for educational and internship purposes as part of the Bluestock Fintech Individual Capstone Project.

---