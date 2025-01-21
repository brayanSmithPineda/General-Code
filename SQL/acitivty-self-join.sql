CREATE TABLE Activity(
	machine_id INT,
    process_id INT, 
    activity_type ENUM('start','end'),
    timestamp FLOAT,
    PRIMARY KEY (machine_id, process_id, activity_type)
);

INSERT INTO Activity
VALUES	(0, 0, 'start', 0.712),
		(0, 0, 'end', 1.520),
        (0, 1, 'start', 3.140),
        (0, 1, 'end', 4.120),
        (1, 0, 'start', 0.550),
        (1, 0, 'end', 1.550),
        (1, 1, 'start', 0.430),
        (1, 1, 'end', 1.420);
        
SELECT *
FROM Activity a1
JOIN Activity a2
ON a1.machine_id = a2.machine_id;


SELECT * 
FROM Activity a1
LEFT JOIN Activity a2
ON a1.machine_id = a2.machine_id AND a1.process_id = a2.process_id
WHERE a1.activity_type = 'start' AND a2.activity_type = 'end';