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

   PNUMBER PNAME               NUMEMP
---------- --------------- ----------
         1 ProductX                 2
         2 ProductY                 3
         3 ProductZ                 2
        10 Computerization          3
        20 Reorganization           3
        30 Newbenefits              3
*/
WITH projemp AS
        (
         SELECT pno pnumber, COUNT(essn) numemp FROM works_on
         GROUP BY pno
        )
SELECT pnumber, pname, numemp FROM project NATURAL JOIN projemp;

/* 12
For each project on which more than two employees work, retrieve the project 
number, the project name, and the number of employees who work on the 
project.

   PNUMBER PNAME               NUMEMP
---------- --------------- ----------
         2 ProductY                 3
        10 Computerization          3
        20 Reorganization           3
        30 Newbenefits              3
*/
WITH projemp AS
        (
         SELECT pno pnumber, COUNT(essn) numemp FROM works_on
         GROUP BY pno
         HAVING COUNT(essn) > 2
        )
SELECT pnumber, pname, numemp FROM project NATURAL JOIN projemp;

/* 13
For each department that has more than five employees, retrieve the department 
number and the number of its employees who are making more than 40,000.
*/
WITH highpay AS
        (
         SELECT ssn, fname FROM employee
         WHERE 
SELECT dno, richemp

