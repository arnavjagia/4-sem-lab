-- ER model lab

/* 1

*/


/* 2

*/


/* 3

*/


/* 4

*/


/* 5

*/


/* 6

*/


/* 7

*/


/* 8
Retrieve the names of employees who have no dependents
*/
SELECT fname, ssn FROM employee
WHERE ssn NOT IN (SELECT essn FROM dependent);

/* 9
List the names of managers who have at least one dependent

FNAME           SSN
--------------- ---------
Franklin        333445555
Jennifer        987654321
*/
SELECT fname, ssn FROM department NATURAL JOIN employee
WHERE ssn = mgr_ssn AND ssn IN
        (SELECT essn FROM dependent);

/* 10
Find the sum of the salaries of all employees, the maximum salary, the minimum 
salary, and the average salary

SUM(SALARY) MAX(SALARY) MIN(SALARY) AVG(SALARY)
----------- ----------- ----------- -----------
     318000       55000       25000  35333.3333

-- SELECT fname, ssn, salary FROM employee;
*/
SELECT sum(salary), max(salary), min(salary), avg(salary)
FROM employee;

/* 11
For each project, retrieve the project number, the project name, and the number 
of employees who work on that project.
*/


/* 12

*/


/* 13

*/


/* 14

*/


/* 15

*/

