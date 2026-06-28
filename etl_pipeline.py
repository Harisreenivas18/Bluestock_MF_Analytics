import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/processed/nav_history_clean.csv")
transactions = pd.read_csv("data/processed/investor_transactions_clean.csv")
performance = pd.read_csv("data/processed/scheme_performance_clean.csv")


aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category = pd.read_csv("data/raw/05_category_inflows.csv")
folio = pd.read_csv("data/raw/06_industry_folio_count.csv")
holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")


fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

aum.to_sql("fact_aum", engine, if_exists="replace", index=False)
sip.to_sql("fact_sip", engine, if_exists="replace", index=False)
category.to_sql("fact_category_inflows", engine, if_exists="replace", index=False)
folio.to_sql("fact_folio", engine, if_exists="replace", index=False)
holdings.to_sql("fact_holdings", engine, if_exists="replace", index=False)
benchmark.to_sql("fact_benchmark", engine, if_exists="replace", index=False)

print("Fund Master:", len(fund_master))
print("NAV:", len(nav))
print("Transactions:", len(transactions))
print("Performance:", len(performance))
print("AUM:", len(aum))
print("SIP:", len(sip))
print("Category:", len(category))
print("Folio:", len(folio))
print("Holdings:", len(holdings))
print("Benchmark:", len(benchmark))

print("Database Created Successfully")