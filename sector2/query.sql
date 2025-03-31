SELECT customer_id, 
       SUM(amount) AS high_total_purchase
FROM orders
GROUP BY customer_id
ORDER BY high_total_purchase DESC
LIMIT 5;