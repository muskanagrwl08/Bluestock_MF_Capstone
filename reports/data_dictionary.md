# BlueStock Mutual Fund Data Dictionary

## dim_fund
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| scheme_name | Text | Mutual Fund Scheme Name |
| fund_house | Text | AMC Name |
| category | Text | Fund Category |
| sub_category | Text | Fund Sub Category |
| plan | Text | Direct/Regular |
| risk_category | Text | Risk Classification |

---

## dim_date
| Column | Data Type | Description |
|--------|-----------|-------------|
| date | Date | NAV Date |
| year | Integer | Year |
| month | Integer | Month |
| day | Integer | Day |

---

## fact_nav
Stores daily NAV values.

---

## fact_transactions
Stores investor transaction records.

---

## fact_performance
Stores mutual fund performance metrics.

---

## fact_aum
Stores Assets Under Management.

---

### Data Sources

- AMFI India
- mfapi.in
- Public Mutual Fund Datasets