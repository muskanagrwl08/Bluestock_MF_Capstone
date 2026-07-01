import pandas as pd
from pathlib import Path

print("Bluestock Mutual Fund Capstone - Day 1")

# Project folder
project_path = Path(__file__).resolve().parent.parent

# Raw data folder
raw_data = project_path / "data" / "raw"

# Get all CSV files
csv_files = list(raw_data.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files.\n")

# Read each CSV
for file in csv_files:

    print("=" * 60)
    print(f"Dataset : {file.name}")

    df = pd.read_csv(file)

    print("\nShape")
    print(df.shape)

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\n")