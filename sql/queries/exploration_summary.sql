-- View sample of the data
SELECT * FROM brand_stock_data
LIMIT 20;

-- Check date range
SELECT 
  MIN(date) AS earliest_date, 
  MAX(date) AS latest_date 
FROM brand_stock_data;

-- Check for missing values
SELECT 
  COUNT(*) AS total_rows,
  COUNT(*) FILTER (WHERE close_price IS NULL) AS missing_close,
  COUNT(*) FILTER (WHERE high_price IS NULL) AS missing_high,
  COUNT(*) FILTER (WHERE low_price IS NULL) AS missing_low,
  COUNT(*) FILTER (WHERE open_price IS NULL) AS missing_open,
  COUNT(*) FILTER (WHERE volume IS NULL) AS missing_volume
FROM brand_stock_data;

-- Check unique tickers
SELECT DISTINCT ticker
FROM brand_stock_data;

-- Summary stats for each brand
SELECT 
  ticker,
  COUNT(*) AS records,
  ROUND(AVG(close_price), 2) AS avg_close,
  ROUND(MIN(close_price), 2) AS min_close,
  ROUND(MAX(close_price), 2) AS max_close,
  ROUND(STDDEV(close_price), 2) AS std_dev_close
FROM brand_stock_data
GROUP BY ticker
ORDER BY ticker;

