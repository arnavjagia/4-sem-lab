-- problem 9
select name, dept_name from student;
-- problem 10
select * from instructor where dept_name = 'Comp. Sci.';
-- problem 11
select title from course where dept_name = 'Comp. Sci.' and credits = 3;
-- problem 12
select course_id, title from takes natural join course where id = 12345;
-- problem 13
select * from instructor where salary between 40000 and 90000;
-- problem 14
select * from instructor where id not in (select id from teaches);
/* 15
Find the student names, course names, and the year, for all students those who have 
attended classes in room-number 303
*/
select * from student natural join takes natural join section where room_number = 303;
/* 16
 For all students who have opted courses in 2015, find their names and course id’s 
with the attribute course title replaced by c-name.
*/
select name, course_id as "c-name" from student natural join takes where year = 2015;
/* 17
Find the names of all instructors whose salary is greater than the salary of at least 
one instructor of CSE department and salary replaced by inst-salary.
*/
select name, salary as "inst-salary"
    from instructor
    where salary > (
        select min(salary)
        from instructor
        where dept_name = 'Comp. Sci.'
    );
/* 18
Find the names of all instructors whose department name includes the substring ‘ch’
*/
select * from instructor where dept_name like '%ch%';
/* 19
List the student names along with the length of the student names.
*/
select name, length(name) from student;
/* 20
List the department names and 3 characters from 3rd position of each department name
*/
select dept_name, substr(dept_name, 3, 3) from department;
/* 21
List the instructor names in upper case.
*/
select name, upper(name) from instructor;
/* 22
Replace NULL with value1(say 0) for a column in any of the table 
*/

/* 23 
Display the salary and salary/3 rounded to nearest hundred from Instructor.
*/
select salary, round(salary, -2) from instructor;
/* 24
Display the birth date of all the employees in the following format:
 ‘DD-MON-YYYY’
 ‘DD-MON-YY’
 ‘DD-MM-YY’
*/
CREATE TABLE employee
	(enum		number(3),
	 ename		varchar(15),
	 gender		char(1)	,
	 salary		number(9,2),
	 eadd		varchar(15),
	 dno		number(3),
	 dob		char(8),
	 PRIMARY KEY (enum),
	 CHECK (gender in ('M', 'F'))
	);
INSERT INTO employee (enum, dob) values (101, '25012024');
INSERT INTO employee (enum, dob) values (102, '05122004');
select enum, dob, to_date(dob, 'DDMMYYYY'), to_date(dob, 'DDMMYY'), to_date(dob, 'DDMMYY') from employee;
/* 25
List the employee names and the year (fully spelled out) in which they are born
 ‘YEAR’
 ‘Year’
 ‘year’
*/
