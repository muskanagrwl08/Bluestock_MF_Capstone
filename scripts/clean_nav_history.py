import pandas as pd
from pathlib import Path

# Project folder path
project_path = Path(__file__).resolve().parent.parent

# Read the NAV history dataset
nav_history = pd.read_csv(project_path / "data" / "raw" / "02_nav_history.csv")

# Convert date column to datetime
nav_history["date"] = pd.to_datetime(nav_history["date"])

# Sort by AMFI code and date
nav_history = nav_history.sort_values(by=["amfi_code", "date"])

# Forward-fill missing NAV values for each AMFI code
nav_history["nav"] = nav_history.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
nav_history = nav_history.drop_duplicates()

# Keep only rows where NAV is greater than 0
nav_history = nav_history[nav_history["nav"] > 0]

# Save cleaned dataset
output_path = project_path / "data" / "processed" / "02_nav_history_cleaned.csv"

nav_history.to_csv(output_path, index=False)

print("✅ NAV History cleaned successfully!")
print(f"Rows: {len(nav_history)}")
print(f"Saved to: {output_path}")