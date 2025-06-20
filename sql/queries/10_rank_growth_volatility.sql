-- Long-term growth and volatility per brand
SELECT
  ticker,
  ROUND(100.0 * (AVG(CASE WHEN EXTRACT(YEAR FROM month) >= 2023 THEN total_monthly_volume END)
              - AVG(CASE WHEN EXTRACT(YEAR FROM month) <= 2020 THEN total_monthly_volume END)) 
        / NULLIF(AVG(CASE WHEN EXTRACT(YEAR FROM month) <= 2020 THEN total_monthly_volume END), 0), 2) AS growth_percent,
  ROUND(STDDEV(total_monthly_volume), 2) AS volatility
FROM trading_volume
GROUP BY ticker
ORDER BY growth_percent DESC;
 