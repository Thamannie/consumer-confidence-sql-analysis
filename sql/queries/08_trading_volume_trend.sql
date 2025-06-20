SELECT 
    ticker,
    DATE_TRUNC('month', date) AS month,
    SUM(volume) AS total_monthly_volume
FROM 
    brand_stock_data
GROUP BY 
    ticker, month
ORDER BY 
    ticker, month;
