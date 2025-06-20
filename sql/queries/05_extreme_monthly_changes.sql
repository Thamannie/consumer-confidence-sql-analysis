-- Steepest gains
SELECT
    ticker,
    month,
    ROUND(monthly_pct_change, 2) AS pct_change,
    'Max Gain' AS type
FROM monthly_pct_change AS a
WHERE monthly_pct_change = (
    SELECT MAX(monthly_pct_change)
    FROM monthly_pct_change AS b
    WHERE a.ticker = b.ticker
)

UNION

-- Steepest losses
SELECT
    ticker,
    month,
    ROUND(monthly_pct_change, 2) AS pct_change,
    'Max Loss' AS type
FROM monthly_pct_change AS a
WHERE monthly_pct_change = (
    SELECT MIN(monthly_pct_change)
    FROM monthly_pct_change AS b
    WHERE a.ticker = b.ticker
)
ORDER BY ticker, type;
