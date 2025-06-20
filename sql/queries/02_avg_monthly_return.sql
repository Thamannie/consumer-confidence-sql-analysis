SELECT ticker,
    ROUND(AVG(monthly_pct_change), 2) AS avg_monthly_return
FROM monthly_pct_change
GROUP BY ticker
ORDER BY avg_monthly_return DESC;