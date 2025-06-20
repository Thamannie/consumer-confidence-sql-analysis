SELECT
    ticker,
    ROUND(
        (MAX(close_price) - MIN(close_price)) / MIN(close_price) * 100, 2
    ) AS cumulative_return
FROM
    brand_stock_data
GROUP BY
    ticker
ORDER BY
    cumulative_return DESC;
