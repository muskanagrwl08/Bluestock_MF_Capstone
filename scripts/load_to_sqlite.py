import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# Project folder
project_path = Path(__file__).resolve().parent.parent

# Database
engine = create_engine(f"sqlite:///{project_path/'bluestock_mf.db'}")

# -------------------------
# Read cleaned datasets
# -------------------------

fund_master = pd.read_csv(project_path / "data" / "raw" / "01_fund_master.csv")

nav = pd.read_csv(project_path / "data" / "processed" / "02_nav_history_cleaned.csv")

transactions = pd.read_csv(project_path / "data" / "processed" / "08_investor_transactions_cleaned.csv")

performance = pd.read_csv(project_path / "data" / "processed" / "07_scheme_performance_cleaned.csv")

# -------------------------
# Create dim_fund
# -------------------------

dim_fund = fund_master[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "sub_category",
        "plan",
        "risk_category",
    ]
]

# -------------------------
# Create dim_date
# -------------------------

nav["date"] = pd.to_datetime(nav["date"])

dim_date = pd.DataFrame({
    "date": nav["date"].dt.strftime("%Y-%m-%d"),
    "year": nav["date"].dt.year,
    "month": nav["date"].dt.month,
    "day": nav["date"].dt.day,
}).drop_duplicates()

# -------------------------
# Load tables
# -------------------------
# Load tables

dim_fund.to_sql("dim_fund", engine, if_exists="replace", index=False)

dim_date.to_sql("dim_date", engine, if_exists="replace", index=False)

nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)

performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

# Create fact_aum from performance dataset
fact_aum = performance[["amfi_code", "aum_crore"]]

fact_aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

print("✅ Data loaded successfully into SQLite!")

print("\nRow Counts")
print("dim_fund:", len(dim_fund))
print("dim_date:", len(dim_date))
print("fact_nav:", len(nav))
print("fact_transactions:", len(transactions))
print("fact_performance:", len(performance))
print("fact_aum:", len(fact_aum))