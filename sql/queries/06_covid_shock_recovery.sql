SELECT 
    ticker,
    TO_CHAR(month, 'YYYY-MM') AS month,
    ROUND(monthly_pct_change, 2) AS pct_change
FROM monthly_pct_change
WHERE month BETWEEN '2020-03-01' AND '2020-06-30'
ORDER BY ticker, month;
