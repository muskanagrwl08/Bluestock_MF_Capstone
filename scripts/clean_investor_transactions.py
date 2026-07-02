import pandas as pd
from pathlib import Path

# Project folder
project_path = Path(__file__).resolve().parent.parent

# Read dataset
df = pd.read_csv(project_path / "data" / "raw" / "08_investor_transactions.csv")

# -------------------------------
# 1. Convert transaction date
# -------------------------------
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

# -------------------------------
# 2. Standardize transaction type
# -------------------------------
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.lower()
)

mapping = {
    "sip": "SIP",
    "systematic investment plan": "SIP",
    "lumpsum": "Lumpsum",
    "lump sum": "Lumpsum",
    "redemption": "Redemption",
    "redeem": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(mapping)

# -------------------------------
# 3. Remove invalid amountck
# -------------------------------
df = df[df["amount_inr"] > 0]

# -------------------------------
# 4. Standardize KYC status
# -------------------------------
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending"]

invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print("Invalid KYC records:", len(invalid_kyc))

# -------------------------------
# 5. Remove duplicates
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# Save cleaned dataset
# -------------------------------
output_path = project_path / "data" / "processed" / "08_investor_transactions_cleaned.csv"

df.to_csv(output_path, index=False)

print("✅ Investor Transactions cleaned successfully!")
print("Rows:", len(df))
print("Saved to:", output_path)