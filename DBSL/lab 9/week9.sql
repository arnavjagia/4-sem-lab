/*
PROCEDURES, FUNCTIONS & PACKAGES
*/
SET SERVEROUTPUT ON;
SET DEFINE ON;

/* 1
Write a procedure to display a message “Good Day to You”.
*/
CREATE OR REPLACE PROCEDURE good_msg IS
BEGIN
        DBMS_OUTPUT.PUT_LINE('Good Day to You.');
END;
/

EXEC good_msg;

/* 2
Based on the University Database Schema in Lab 2, write a procedure which takes 
the dept_name as input parameter and lists all the instructors associated with the 
department as well as list all the courses offered by the department. Also, write an 
anonymous block with the procedure call.
*/


/* 3
Based on the University Database Schema in Lab 2, write a Pl/Sql block of code 
that lists the most popular course (highest number of students take it) for each of 
the departments. It should make use of a procedure course_popular which finds 
the most popular course in the given department.
*/


/* 4
Based on the University Database Schema in Lab 2, write a procedure which takes 
the dept-name as input parameter and lists all the students associated with the 
department as well as list all the courses offered by the department. Also, write an 
anonymous block with the procedure call.
*/


/* 5
Write a function to return the Square of a given number and call it from an 
anonymous block.
*/


/* 6
Based on the University Database Schema in Lab 2, write a Pl/Sql block of code 
that lists the highest paid Instructor in each of the Department. It should make use 
of a function department_highest which returns the highest paid Instructor for the 
given branch.
*/


/* 7
Based on the University Database Schema in Lab 2, create a package to include 
the following:
 a) A named procedure to list the instructor_names of given department
 b) A function which returns the max salary for the given department
 c) Write a PL/SQL block to demonstrate the usage of above package components
*/


/* 8
Write a PL/SQL procedure to return simple and compound interest (OUT 
parameters) along with the Total Sum (IN OUT) i.e. Sum of Principle and Interest 
taking as input the principle, rate of interest and number of years (IN parameters). 
Call this procedure from an anonymous block.
*/

