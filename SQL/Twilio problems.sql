USE prep_sql_test;
CREATE TABLE userst (
	user_id INT PRIMARY KEY,
    name VARCHAR(30)
);
INSERT INTO userst
VALUES	(1, 'John Doe'),
		(2, 'Jane Smith'),
        (3, 'Charlie Brown'),
        (4, 'Lucy Van Pelt');
CREATE TABLE sms (
	sms_id INT PRIMARY KEY,
    user_id INT,
    send_date DATETIME, 
    status VARCHAR(45)
);
		
INSERT INTO sms 
VALUES	(101, 1, '2024-10-01 00:00:00', 'Sent'),
		(102, 2, '2024-10-03 00:00:00', 'Sent'),
		(103, 1, '2024-10-03 00:00:00', 'Sent'),
		(104, 3, '2024-10-07 00:00:00', 'Sent'),
		(105, 4, '2024-10-08 00:00:00', 'Sent'),
		(106, 1, '2024-10-09 00:00:00', 'Sent'),
		(107, 4, '2024-10-09 00:00:00', 'Sent');

/*Let's say Twilio would like to identify its top users, focusing on the frequency of usage for their SMS service. 
The "power users" or "whale users" are defined as those who have sent out the most amount of SMS messages in the last 30 days*/
select *
from userst;
select *
from sms;

SELECT u.name, COUNT(s.user_id) AS top_users
FROM sms s 
LEFT JOIN userst u ON s.user_id = u.user_id
WHERE s.send_date > DATE_SUB(curdate(), INTERVAL 30 DAY) AND s.status = 'Sent'
GROUP BY u.name
ORDER BY top_users DESC;

CREATE TABLE call_records (
	call_id INT PRIMARY KEY,
    user_id INT,
    call_date DATE,
    call_durantion INT
);
INSERT INTO call_records 
VALUES	(1024, 1, '2021-01-04', 320),
		(1025, 2, '2021-01-04', 150),
        (1026, 1, '2021-02-04', 620),
        (1027, 2, '2021-02-04', 235),
        (1028, 1, '2021-02-04', 410);

SELECT user_id, call_date, ROUND(AVG(call_durantion)) AS avg_duration
FROM call_records
GROUP BY user_id, call_date