-- 1. Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS monthly_pct_change (
    ticker TEXT,
    month DATE,
    monthly_pct_change NUMERIC
);

-- 2. Insert calculated monthly percentage change into the table
INSERT INTO monthly_pct_change (ticker, month, monthly_pct_change)
SELECT
    ticker,
    DATE_TRUNC('month', date) AS month,
    ROUND(((close_price - LAG(close_price) OVER (PARTITION BY ticker ORDER BY DATE_TRUNC('month', date))) 
           / LAG(close_price) OVER (PARTITION BY ticker ORDER BY DATE_TRUNC('month', date))) * 100, 2) 
           AS monthly_pct_change
FROM brand_stock_data
GROUP BY ticker, month, close_price, date
ORDER BY ticker, month;
