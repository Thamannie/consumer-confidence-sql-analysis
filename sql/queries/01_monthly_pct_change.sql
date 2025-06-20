SELECT
    ticker,
    DATE_TRUNC('month', date) AS month,
    ROUND(((close_price - LAG(close_price) OVER (PARTITION BY ticker ORDER BY DATE_TRUNC('month', date))) 
           / LAG(close_price) OVER (PARTITION BY ticker ORDER BY DATE_TRUNC('month', date))) * 100, 2) 
           AS monthly_pct_change
FROM brand_stock_data
GROUP BY ticker, month, close_price, date
ORDER BY ticker, month;
