USE prep_sql_test;

CREATE TABLE Weather(
	id INT PRIMARY KEY,
    recordDate DATE,
    temperature INT
);

INSERT INTO Weather
VALUES 	(1, "2015-01-01", 10),
		(2, "2015-01-02", 25),
        (3, "2015-01-03", 20),
        (4, "2015-01-04", 30),
        (5, "2015-01-06", 40);
        
SELECT *
FROM Weather w1
LEFT JOIN Weather w2
ON w1.recordDate = date_add(W2.recordDate, INTERVAL 1 DAY)
