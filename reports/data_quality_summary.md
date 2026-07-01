# Data Quality Summary

## Project
Bluestock Mutual Fund Capstone - Day 1

## Dataset Overview

A total of **10 CSV datasets** were successfully loaded into Python using the Pandas library.

## Data Validation Results

- All 10 datasets were successfully read without any loading errors.
- Column names were correctly recognized for every dataset.
- The datasets were readable and displayed correctly using the `head()` function.
- Data types for all columns were successfully identified using the `dtypes` attribute.
- Dataset dimensions were verified using the `shape` attribute.
- Live NAV data was successfully fetched from the MFAPI and saved as `live_nav.csv`.
- AMFI code validation was successfully completed.
- All AMFI codes present in `01_fund_master.csv` were found in `02_nav_history.csv`.
- No missing AMFI codes were detected.
- No major structural issues were observed during the initial data ingestion process.

## Conclusion

The datasets have been successfully ingested and validated for the initial phase of the project. The data is ready for further cleaning, preprocessing, and analysis in Day 2.