import requests
import pandas as pd
from pathlib import Path

# Project folder
project_path = Path(__file__).resolve().parent.parent

# Save folder
save_folder = project_path / "data" / "raw"

# AMFI Codes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, amfi_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        file_name = f"{scheme_name}_NAV.csv"

        df.to_csv(save_folder / file_name, index=False)

        print(f"✅ {scheme_name} saved successfully.")

    else:
        print(f"❌ Failed to fetch {scheme_name}")