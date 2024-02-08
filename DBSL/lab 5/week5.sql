-- ER model lab

/* 1

*/
select bdate, address
from employee
where fname || ' ' || minit || ' ' || lname like 'John B Smith';

select E.fname || ' ' || E.minit || ' ' || E.lname, E.address
from employee E inner join department D 
    on E.dno = D.dnumber
where D.dname like 'Research';


/* 2

*/
select P.pnumber, D.dname, E.lname, E.address, E.bdate
from project P left join department D on P.dnum = D.dnumber
    left join employee E on D.mgr_ssn = E.ssn
where plocation like 'Stafford';

/* 3

*/
select E1.fname sub_fname, E1.lname sub_lname, E2.fname sup_fname, E2.lname sup_lname
from employee E1 left join employee E2
    on E1.super_ssn = E2.ssn;

/* 4

*/
select P.pnumber
from project P 
where exists (
    select *
    from employee E
    where E.dno = P.dnum and 
        E.lname like 'Smith'
);

/* 5

*/
with project_x_no(value) as (
    select pnumber 
    from project
    where pname like 'Project X'
),
project_x_employees(value) as (
    select W.essn
    from works_on W, project_x_no
    where W.pno = project_x_no.value
)
select case
    when E.ssn in (select * from project_x_employees) then salary * 1.1
    else salary
end as salary
from employee E;

/* 6

*/
select fname, minit, lname, dname, pname
from employee E, department D, works_on W, project P
where E.dno = D.dnumber and E.ssn = W.essn and P.dnum = D.dnumber
order by D.dname, E.lname, E.fname;

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

no rows selected
*/
WITH bigdept AS
        (
         SELECT dno, count(*) FROM employee
         GROUP BY dno
         HAVING COUNT(ssn) > 5
        )
SELECT dno, COUNT(ssn) FROM employee NATURAL JOIN bigdept
WHERE salary > 40000
GROUP BY dno;
