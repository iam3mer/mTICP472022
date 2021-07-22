SELECT employee_id, last_name, job_id, hire_date STARTDATE
FROM employees
ORDER BY 3;

SELECT DISTINCT job_id
FROM employees;

SELECT employee_id 'Emp #', last_name Employee, job_id JOB, hire_date 'Hire Date'
FROM employees;

SELECT last_name, salary
FROM employees
WHERE salary > 12000;

SELECT last_name, department_id
FROM employees
WHERE employee_id = 176;

SELECT  last_name, salary
FROM employees
WHERE salary < 5000 OR salary > 12000;

SELECT last_name, salary
FROM employees
WHERE salary NOT BETWEEN 5000 AND 12000;

SELECT last_name, job_id, hire_date
FROM employees
WHERE last_name = 'Taylor' OR last_name = 'Matos';


SELECT last_name, job_id, hire_date
FROM employees
WHERE last_name LIKE 'Ta%' OR last_name LIKE 'Ma%';

SELECT last_name, department_id AS dept
FROM employees
WHERE dept = 10 OR dept = 8
ORDER BY first_name;

SELECT last_name Employee, salary 'Monthly Salary'
FROM employees
WHERE salary BETWEEN 5000 AND 12000 AND (department_id = 10 OR department_id= 8);

SELECT last_name, hire_date
FROM employees
WHERE hire_date LIKE '1994%';

SELECT  last_name, hire_date
FROM employees e 
WHERE manager_id IS NULL;

SELECT last_name, salary, salary*.1 commission
FROM employees e 
WHERE job_id = 16
ORDER BY 3;

SELECT last_name
FROM employees e 
WHERE last_name LIKE '__a%';

SELECT last_name
FROM employees e 
WHERE last_name LIKE '%a%' AND last_name LIKE '%e%';

SELECT
	employee_id,
	last_name,
	salary, salary + (salary * .155) 'New Salary'
FROM employees;

SELECT 
	last_name,
	UPPER(SUBSTR(last_name,1,1)) || LOWER(SUBSTR(last_name,2,LENGTH(last_name))) Apellido,
	LENGTH(last_name) Longitud
from employees e
WHERE first_name LIKE 'J%' OR first_name LIKE 'A%' OR first_name LIKE 'M%';

SELECT last_name, printf('$ %15.d ',salary) SALARY
from employees e;

SELECT max(salary)
from employees e ;

SELECT first_name, last_name, salary
from employees e
ORDER BY first_name, last_name, salary DESC;

SELECT first_name , count(last_name)
from employees e;

SELECT AVG(salary)
from employees e
where salary > 8060;

SELECT department_id, MAX(salary)
from employees e 
group by department_id
HAVING MAX(salary) > 10000; 

SELECT MAX(salary) 'Salario Máximo', MIN(salary) 'Salario Mínimo', SUM(salary) 'Total Pagado', AVG(salary) 'Promedio'
from employees e;

SELECT job_id, MAX(salary) 'Salario Máximo', MIN(salary) 'Salario Mínimo', SUM(salary) 'Total Pagado', AVG(salary) 'Promedio'
from employees e
group by job_id
ORDER by promedio DESC;

SELECT count(job_id)
from employees e 
WHERE job_id = 9;

SELECT job_id, count(job_id)
from employees e 
group by job_id ;

SELECT last_name , job_title, salary 
from employees e
natural join jobs;

SELECT last_name, job_title, salary
from employees e 
join jobs j on (e.job_id = j.job_id);

SELECT  last_name, job_title, salary
from employees e 
join jobs j 
using (job_id);

SELECT job_title, count(e.job_id)
from employees e
natural join jobs j
group by e.job_id;

SELECT job_title, first_name||' '||last_name
from jobs j, employees e
WHERE j.job_id = e.job_id;

SELECT department_name, COUNT(e.department_id) 
from employees e, departments d
WHERE d.department_id = e.department_id
GROUP BY e.department_id;

SELECT last_name, d.department_id, department_name
from employees e 
left outer join departments d on (e.department_id = d.department_id);

SELECT last_name, d.department_id, department_name
from  departments d
left outer join employees e on (e.department_id = d.department_id);

SELECT last_name, department_name
from employees e 
cross join departments d ;

select location_id, street_address, city, state_province, country_name
from locations l 
natural join countries c ;

select location_id, street_address, city, state_province, country_name
from locations l 
join countries c on (l.country_id = c.country_id);

select location_id, street_address, city, state_province, country_name
from locations l 
join countries c using (country_id);

SELECT last_name, d.department_id, department_name
from employees e 
join departments d using (department_id);

SELECT last_name
from employees e 
WHERE job_id in (17,18,19);

SELECT last_name
from employees e 
where job_id in (
	SELECT DISTINCT job_id 
	from employees e2 
	WHERE department_id = 5
);

SELECT round(salary_avg, 2)
from (
	SELECT AVG(salary) salary_avg
	from employees e 
	group by department_id );

SELECT last_name, salary
from employees e 
where manager_id = (
	SELECT employee_id 
	from employees e2 
	where last_name = 'King'
);

SELECT department_id, last_name, job_id
from employees e 
where department_id = (
	SELECT department_id 
	from departments d 
	where department_name = 'Executive'
);

SELECT last_name
from employees e 
union
select job_title
from jobs j ;

SELECT job_id
from employees e 
intersect
select job_id
from jobs j ;

INSERT into jobs (job_id,job_title,min_salary,max_salary)
values (20, 'New Job', 1000, 3000);

INSERT into job_grades (lowest_sal,highest_sal)
values (40001,60000);

insert into jobs 
values (21, 'Other New Salary', 2500, 5000);

CREATE TABLE sales_reps (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	salary REAL
);

INSERT into sales_reps 
select employee_id, first_name||' '||last_name, salary 
from employees 
WHERE job_id in (
	SELECT job_id
	from jobs 
	where job_title like '%Rep%'
);





