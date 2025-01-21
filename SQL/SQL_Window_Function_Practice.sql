select *
from employee;

/*A window function is just a way to apply a function to a specify group(window) of a column, 
for example apply the maximun salary on each group(window) of department*/

SELECT *, 
	MAX(salary) OVER(PARTITION BY dept_name) AS max_salary
FROM employee;

/*row_number() function, this is a window function that assign a number to each row*/
SELECT *,
	ROW_NUMBER() OVER (PARTITION BY dept_name) AS RowNumber
FROM Employee;

/*Fetch the first two employees that join the company by each depart, assumed that an emp_ID lower means that an employee joins the company first*/

/*So here we are going to use the row_number() funtion to idenitfy which emplooye joins the company early,
then we are going to use that query/table as a subquery that is going to limit the result by the first 2*/

select *
from (
	select *,
		row_number() over(partition by dept_name order by emp_id) as rowNumber
	from Employee
) as e
where e.rowNumber < 3;

/* RAN() Function ranks the result based on a column, for example rank the salary for each department*/

/* Fetch the top 3 in each department earning max salary*/

SELECT *
FROM (
	SELECT *,
		RANK() OVER(PARTITION BY dept_name ORDER BY salary DESC) as rankSalary
	FROM Employee e
) x
WHERE x.rankSalary <3;

SELECT *,
	ROW_NUMBER() OVER(PARTITION BY dept_name ORDER BY salary DESC) as numRow,
    RANK() OVER(PARTITION BY dept_name ORDER BY salary DESC) as rankSalary,
	DENSE_RANK() OVER(PARTITION BY dept_name ORDER BY salary DESC) as denseRankSalary
FROM Employee e;

/* lead() and lag() window functions returns the previous and next record of a specified column, for example the previous and next salary 
of each emplooye partation by department and sorted by id*/
SELECT *,
	LAG(salary) OVER(PARTITION BY dept_name ORDER BY emp_id) as previousSalary,
    LEAD(salary) OVER(PARTITION BY dept_name ORDER BY emp_id) as nextSalary
FROM Employee; 

/* feach the employees with higher salary compared to the previous one, return a column to tell if its higher, lower or eqaul */
SELECT *,
	LAG(salary) OVER(PARTITION BY dept_name ORDER BY emp_id) as prevSalary,
    CASE WHEN LAG(salary) OVER(PARTITION BY dept_name ORDER BY emp_id) > salary THEN 'Lower than prev'
		WHEN LAG(salary) OVER(PARTITION BY dept_name ORDER BY emp_id) < salary THEN 'Higher than prev'
        WHEN LAG(salary) OVER(PARTITION BY dept_name ORDER BY emp_id) = salary THEN 'Same as prev'
		END sal_range
FROM Employee;