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

*/


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

