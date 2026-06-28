-- Top 5 Funds by 5Y Return

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Average NAV

SELECT AVG(nav)
FROM fact_nav;

-- Transaction Count

SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- State Wise Investments

SELECT
state,
SUM(amount_inr)
FROM fact_transactions
GROUP BY state;

-- Gender Wise Investments

SELECT
gender,
SUM(amount_inr)
FROM fact_transactions
GROUP BY gender;