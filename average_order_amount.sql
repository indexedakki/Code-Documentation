-- models/average_order_amount.sql

WITH customer_order_totals AS (
  SELECT
    customer_id,
    AVG(total_amount) AS avg_order_amount
  FROM
    {{ ref('raw_orders') }}
  GROUP BY
    customer_id
)

SELECT
  customer_id,
  avg_order_amount
FROM
  customer_order_totals;
