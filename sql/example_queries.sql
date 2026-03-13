-- Example analytics queries for the Urban Mobility Data Lakehouse

-- Total trips per day
SELECT
    pickup_date,
    SUM(trip_count) AS trips
FROM daily_trip_summary_silver_bronze_yellow_tripdata_2024_01
GROUP BY pickup_date
ORDER BY pickup_date;


-- Total revenue per day
SELECT
    pickup_date,
    SUM(total_revenue) AS revenue
FROM daily_trip_summary_silver_bronze_yellow_tripdata_2024_01
GROUP BY pickup_date
ORDER BY pickup_date;


-- Hourly demand
SELECT
    pickup_hour,
    SUM(trip_count) AS trips
FROM hourly_demand_summary_silver_bronze_yellow_tripdata_2024_01
GROUP BY pickup_hour
ORDER BY pickup_hour;


-- Revenue by payment type
SELECT
    payment_type,
    SUM(total_revenue) AS revenue
FROM payment_type_revenue_silver_bronze_yellow_tripdata_2024_01
GROUP BY payment_type
ORDER BY revenue DESC;