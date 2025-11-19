-- SQL Queries for Marketing Campaign A/B Testing

-- 1. View Sample Data
SELECT * FROM marketing_data LIMIT 5;

-- 2. Count Total Customers per Campaign
SELECT campaign, COUNT(*) AS total_customers
FROM marketing_data
GROUP BY campaign;

-- 3. Calculate Click-Through Rate (CTR) per Campaign
SELECT campaign,
       SUM(clicked) * 1.0 / COUNT(*) AS CTR
FROM marketing_data
GROUP BY campaign
ORDER BY CTR DESC;

-- 4. Average Purchase Revenue per Campaign
SELECT campaign,
       AVG(purchase_amount) AS avg_revenue
FROM marketing_data
GROUP BY campaign
ORDER BY avg_revenue DESC;

-- 5. Revenue Lost from NON-clickers
SELECT campaign,
       SUM(CASE WHEN clicked = 0 THEN purchase_amount ELSE 0 END) AS lost_revenue
FROM marketing_data
GROUP BY campaign;

-- 6. Best Performing Customers (CTR + Revenue)
SELECT customer_id, campaign, purchase_amount
FROM marketing_data
WHERE clicked = 1 AND purchase_amount > 50
ORDER BY purchase_amount DESC;

-- 7. Segmented Recommendation Example
SELECT campaign,
       CASE
            WHEN purchase_amount >= 100 THEN 'High-Value'
            WHEN purchase_amount BETWEEN 50 AND 100 THEN 'Medium-Value'
            ELSE 'Low-Value'
       END AS customer_segment,
       COUNT(*) AS total_customers
FROM marketing_data
GROUP BY campaign, customer_segment
ORDER BY campaign, customer_segment;
