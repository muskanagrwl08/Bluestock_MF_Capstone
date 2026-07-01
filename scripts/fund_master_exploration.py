import pandas as pd
from pathlib import Path

# Locate project folder
project_path = Path(__file__).resolve().parent.parent

# Read fund master dataset
fund_master = pd.read_csv(project_path / "data" / "raw" / "01_fund_master.csv")

print("\n========== FUND HOUSES ==========")
print(fund_master["fund_house"].unique())

print("\n========== CATEGORIES ==========")
print(fund_master["category"].unique())

print("\n========== SUB CATEGORIES ==========")
print(fund_master["sub_category"].unique())

print("\n========== RISK CATEGORIES ==========")
print(fund_master["risk_category"].unique())