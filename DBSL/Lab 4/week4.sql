/* 1
Find the number of students in each course
*/
SELECT course_id, count(*) 
FROM takes
GROUP BY course_id;

/* 2
Find those departments where the average number of students are greater than 10.
*/
SELECT dept_name, count(*) n_students
FROM department NATURAL JOIN student
GROUP BY dept_name
HAVING count(*)>10;

/* 3
Find the total number of courses in each department.
*/
SELECT dept_name, count(*) n_courses 
FROM course
GROUP BY dept_name;

/* 4
Find the names and average salaries of all departments whose average salary is 
greater than 42000.
*/
SELECT dept_name, avg(salary)
FROM instructor
GROUP BY dept_name
HAVING avg(salary)>42000;

/* 5
Find the enrolment of each section that was offered in Spring 2009.
*/
SELECT course_id, sec_id, count(*) n_enrolments
FROM takes
GROUP BY course_id, sec_id, semester, year
HAVING semester = 'Spring' and year = '2009';

/* 6

*/

/* 7

*/

/* 8

*/

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
Transfer all the students from CSE department to IT department.
*/
SAVEPOINT s1;
UPDATE student SET dept_name = 'IT' 
WHERE dept_name = 'Comp. Sci.';
ROLLBACK TO s1;

/* 16
Increase salaries of instructors whose salary is over $100,000 by 3%, and all 
others receive a 5% raise
*/
SAVEPOINT s2;
UPDATE instructor SET salary = CASE
                WHEN salary <= 100000 THEN salary * 1.05
                ELSE salary * 1.03
        END
ROLLBACK TO s2;
