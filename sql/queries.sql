-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV Per Month
SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. Total Investment by State
SELECT
state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 4. Funds with Expense Ratio below 1%
SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Average 3-Year Return by Category
SELECT
category,
AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY category
ORDER BY avg_return DESC;

-- 6. Number of Transactions by Payment Mode
SELECT
payment_mode,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY payment_mode;

-- 7. Number of Investors by City Tier
SELECT
city_tier,
COUNT(*) AS investors
FROM fact_transactions
GROUP BY city_tier;

-- 8. Verified vs Pending KYC
SELECT
kyc_status,
COUNT(*) AS total
FROM fact_transactions
GROUP BY kyc_status;

-- 9. Highest 5-Year Return
SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 10. Average Investment Amount by Transaction Type
SELECT
transaction_type,
AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;