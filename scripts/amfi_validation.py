import pandas as pd
from pathlib import Path

# Project path
project_path = Path(__file__).resolve().parent.parent

# Read datasets
fund_master = pd.read_csv(project_path / "data" / "raw" / "01_fund_master.csv")
nav_history = pd.read_csv(project_path / "data" / "raw" / "02_nav_history.csv")

# Unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Missing codes
missing_codes = fund_codes - nav_codes

print("Total Fund Master Codes:", len(fund_codes))
print("Total NAV History Codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes are present in NAV History.")
else:
    print("\n❌ Missing AMFI Codes:")
    print(missing_codes)