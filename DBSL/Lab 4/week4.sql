/*
for i in range (1,17):
     print("/* "+str(i)+"\n\n*/\n")
*/

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
GROUP BY dept_name;

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
GROUP BY dept_name;

/* 5

*/

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

*/

/* 16

*/
