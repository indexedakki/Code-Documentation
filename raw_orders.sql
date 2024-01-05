-- models/raw_orders.sql

SELECT
  order_id,
  customer_id,
  order_date,
  total_amount
FROM
  your_data_source.raw_orders;
