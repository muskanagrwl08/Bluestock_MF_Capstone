import pandas as pd
from pathlib import Path

# Project folder
project_path = Path(__file__).resolve().parent.parent

# Read dataset
df = pd.read_csv(project_path / "data" / "raw" / "07_scheme_performance.csv")

# ---------------------------------
# Convert return columns to numeric
# ---------------------------------

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ---------------------------------
# Flag rows having missing return values
# ---------------------------------

anomalies = df[df[return_columns].isnull().any(axis=1)]

print("Number of anomalous rows:", len(anomalies))

# ---------------------------------
# Validate expense ratio
# Keep only values between 0.1% and 2.5%
# ---------------------------------

df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

# ---------------------------------
# Remove duplicate rows
# ---------------------------------

df = df.drop_duplicates()

# ---------------------------------
# Save cleaned dataset
# ---------------------------------

output_path = project_path / "data" / "processed" / "07_scheme_performance_cleaned.csv"

df.to_csv(output_path, index=False)

print("✅ Scheme Performance cleaned successfully!")
print("Rows:", len(df))
print("Saved to:", output_path)