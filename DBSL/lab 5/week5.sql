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

*/


/* 11

*/


/* 12

*/


/* 13

*/


/* 14

*/


/* 15

*/

