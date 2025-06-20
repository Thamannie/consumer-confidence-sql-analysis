SELECT
  ticker,
  ROUND(STDDEV(monthly_pct_change), 2) AS holiday_season_volatility
FROM
  monthly_pct_change
WHERE
  TO_CHAR(month, 'MM') IN ('11', '12')
GROUP BY
  ticker
ORDER BY
  holiday_season_volatility ASC;

