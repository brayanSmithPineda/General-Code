USE prep_sql_test;

CREATE TABLE Prices (
	product_id INT,
    start_date DATE,
    end_date DATE,
    price INT
);

INSERT INTO Prices 
VALUES	(1, '2019-02-17', '2019-02-28', 5),
		(1, '2019-03-01', '2019-03-22', 20),
        (2, '2019-02-01', '2019-02-20', 15),
        (2, '2019-02-21', '2019-03-31', 30);
		

CREATE TABLE UnitsSold (
	product_id INT, 
    purchase_date DATE,
    units INT
);

INSERT INTO UnitsSold
VALUES	(1, '2019-02-25', 100),
		(1, '2019-03-01', 15),
		(2, '2019-02-10', 200),
        (2, '2019-03-22', 30);
        
SELECT *
FROM Prices;

SELECT *
FROM UnitsSold;

/* Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. */
INSERT INTO Prices
VALUES (3, '2019-02-27', '2019-02-28', 5);

SELECT p.product_id, COALESCE(ROUND(SUM(us.units*p.price) / SUM(us.units),2),0) AS average_price
FROM Prices p 
LEFT JOIN UnitsSold us ON p.product_id = us.product_id
WHERE us.purchase_date BETWEEN p.start_date AND p.end_date OR us.purchase_date IS NULL
GROUP BY p.product_id;


/*
Write a solution to find the percentage of the users registered in each contest rounded to two decimals.
Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.
*/

CREATE TABLE Users (
	user_id INT,
    name VARCHAR(50)
);

INSERT INTO Users
VALUES	(6, 'Alice'),
		(2, 'Bob'),
        (7, 'Alex');
        
CREATE TABLE Register (
	contest_id INT,
    user_id INT
);

INSERT INTO Register
VALUES	(215, 6),
		(209, 2),
        (208, 2),
        (210, 6),
        (208, 6),
        (209, 7),
        (209, 6),
        (215, 7),
        (208, 7),
        (210, 2),
        (207, 2),
        (210, 7);

WITH cte_user AS (
	SELECT COUNT(*) AS userCount
    FROM Users
)
        
SELECT r.contest_id, ROUND(COUNT(DISTINCT r.user_id)*100/ cu.userCount,2) AS percentage 
FROM Register r
LEFT JOIN Users s ON r.user_id = s.user_id
CROSS JOIN cte_user cu
GROUP BY r.contest_id, cu.userCount
ORDER BY percentage DESC, r.contest_id ASC;


CREATE TABLE Queries (
	query_name VARCHAR(30),
    result VARCHAR(50),
    position INT,
    rating INT
);

INSERT INTO Queries
VALUES	('Dog','Golden Retriever', 1, 5),
		('Dog','German Shepherd', 2, 5),
        ('Dog','Mule', 200, 1),
        ('Cat','Shirazi', 5, 2),
        ('Cat','Siamese', 3, 3),
        ('Cat','Sphynx', 7, 4);

/*
We define query quality as:
     The average of the ratio between query rating and its position.
We also define poor query percentage as:
     The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and poor_query_percentage.
Both quality and poor_query_percentage should be rounded to 2 decimal places.
Return the result table in any order.
The result format is in the following example.
*/
WITH PoorQueryPercentage AS (
SELECT query_name, ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END )*100 / COUNT(*),2) AS poor_query_percentage
FROM Queries
GROUP BY query_name
)

SELECT q.query_name, ROUND(AVG(q.rating/q.position),2) AS quality, p.poor_query_percentage
FROM Queries q
LEFT JOIN PoorQueryPercentage p ON q.query_name = p.query_name
GROUP BY q.query_name, p.poor_query_percentage;

/*-------------------------------------------------------------------------------------------------- */
USE prep_sql_test;
CREATE TABLE Transactions (
	id INT,
    country VARCHAR(50),
    state ENUM('approved', 'declined'),
    amount INT,
    trans_date DATE
);

INSERT INTO Transactions
VALUES	(121, 'US', 'approved', 1000, '2018-12-18'),
		(122, 'US', 'declined', 2000, '2018-12-19'),
        (123, 'US', 'approved', 2000, '2019-01-01'),
        (124, 'DE', 'approved', 2000, '2019-01-07');
        
SELECT *
FROM Transactions;

/*
Write an SQL query to find for each month and country, the number of transactions and their total amount, 
the number of approved transactions and their total amount.
*/


SELECT 
	DATE_FORMAT(t.trans_date, '%Y-%m') AS month, 
    t.country, 
    COUNT(t.id) AS trans_count,
    SUM(CASE WHEN t.state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(t.amount) AS trans_total_amount,
    SUM(CASE WHEN t.state = 'approved' THEN t.amount ELSE 0 END) AS approved_total_amount
FROM Transactions t
GROUP BY month, country;

/*----------------------------1174. Immediate Food Delivery II------------------------------------------------ */
USE prep_sql_test;
CREATE TABLE Delivery (
	delivery_id INT, 
    customer_id INT,
    order_date DATE,
    customer_pref_delivery_date DATE
);
INSERT INTO Delivery
VALUES	(1, 1, "2019-08-01", "2019-08-02"),
		(2, 2, "2019-08-02", "2019-08-02"),
        (3, 1, "2019-08-11", "2019-08-12"),
        (4, 3, "2019-08-24", "2019-08-24"),
        (5, 3, "2019-08-21", "2019-08-22"),
        (6, 2, "2019-08-11", "2019-08-13"),
        (7, 4, "2019-08-09", "2019-08-09");
/* 
1- get only the records of the first order, we can do that with the MIN function an use a subquery or a CTE to then INNER JOIN with the original table
that way we can have all the columns that are associated with the MIN order date
)
*/
WITH cte AS (
SELECT customer_id, MIN(order_date) AS earliest_date
FROM Delivery
GROUP BY customer_id)

SELECT ROUND(SUM(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 END)/COUNT(d.delivery_id)*100,2) AS immediate_percentage
FROM Delivery d
INNER JOIN cte dd ON d.customer_id = dd.customer_id AND d.order_date = dd.earliest_date;