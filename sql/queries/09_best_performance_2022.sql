SELECT 
    ticker,
    SUM(total_monthly_volume) AS total_volume_2022
FROM 
    trading_volume
WHERE 
    DATE_PART('year', month) = 2022
GROUP BY 
    ticker
ORDER BY 
    total_volume_2022 DESC;
