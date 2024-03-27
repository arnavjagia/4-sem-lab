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
create or replace procedure dept_info(v_dept_name department.dept_name%type) is
    cursor student_cursor is 
        select * from student where dept_name like v_dept_name;

    cursor course_cursor is
        select * from course where dept_name like v_dept_name;
begin
    dbms_output.put_line('== Department students ==');
    for s in student_cursor loop
        dbms_output.put_line(s.id || ' ' || s.name);
    end loop;

    dbms_output.put_line('== Department courses ==');
    for c in course_cursor loop
        dbms_output.put_line(c.course_id || ' ' || c.title);
    end loop;
end;
/

begin
    dept_info('&department');
end;
/

/* 3
Based on the University Database Schema in Lab 2, write a Pl/Sql block of code 
that lists the most popular course (highest number of students take it) for each of 
the departments. It should make use of a procedure course_popular which finds 
the most popular course in the given department.
*/
create or replace procedure course_popular(v_dept_name department.dept_name%type) is
    cursor course_frequency is
        select course_id, title, count(*) as enrollment
        from course
        where course.dept_name = v_dept_name
        group by course_id, title;

    v_max_enrollment int := 0;
begin
    for c in course_frequency loop
        if c.enrollment > v_max_enrollment then
            v_max_enrollment := c.enrollment;
        end if;
    end loop;

    dbms_output.put_line('Most popular courses for ' || v_dept_name);
    for c in course_frequency loop
        if c.enrollment = v_max_enrollment then
            dbms_output.put_line(c.course_id || ' ' || c.title);
        end if;
    end loop;
end;
/

begin
    for r in (select * from department) loop
        course_popular(r.dept_name);
    end loop;
end;
/

/* 4
Based on the University Database Schema in Lab 2, write a procedure which takes 
the dept-name as input parameter and lists all the students associated with the 
department as well as list all the courses offered by the department. Also, write an 
anonymous block with the procedure call.
*/
-- Same as Q2

/* 5
Write a function to return the Square of a given number and call it from an 
anonymous block.
*/
create or replace function square(x number) return number is
begin
    return x * x;
end;
/

begin
    dbms_output.put_line(square(5));
end;
/

/* 6
Based on the University Database Schema in Lab 2, write a Pl/Sql block of code 
that lists the highest paid Instructor in each of the Department. It should make use 
of a function department_highest which returns the highest paid Instructor for the 
given branch.
*/
create or replace function department_highest(v_dept_name department.dept_name%type) 
    return instructor.name%type is

    cursor instructor_cursor is
        select * from instructor where dept_name like v_dept_name;

    v_highest_salary instructor.salary%type := 0;
    v_name instructor.name%type;
begin
    for i in instructor_cursor loop
        if i.salary > v_highest_salary then
            v_name := i.name;
            v_highest_salary := i.salary;
        end if;
    end loop;

    return v_name;
end;
/

declare
    cursor dept_cursor is 
        select distinct dept_name from department;
begin
    for r in dept_cursor loop
        dbms_output.put_line(r.dept_name || ': ' || department_highest(r.dept_name));
    end loop;
end;
/

/* 7
Based on the University Database Schema in Lab 2, create a package to include 
the following:
 a) A named procedure to list the instructor_names of given department
 b) A function which returns the max salary for the given department
 c) Write a PL/SQL block to demonstrate the usage of above package components
*/
create or replace package department_operations is
    procedure list_instructors(v_dept_name department.dept_name%type);
    function max_salary(v_dept_name department.dept_name%type) return number;
end department_operations;
/

create or replace package body department_operations is 
    procedure list_instructors(v_dept_name department.dept_name%type) is
        cursor instructor_cursor is
            select name from instructor where dept_name like v_dept_name;
    begin
        dbms_output.put_line('== ' || v_dept_name || ' instructors ==');
        for i in instructor_cursor loop
            dbms_output.put_line(i.name);
        end loop;
    end;

    function max_salary(v_dept_name department.dept_name%type) return number is
        cursor salary_cursor is
            select salary from instructor where dept_name like v_dept_name;
        v_max_salary number := 0;
    begin
        for i in salary_cursor loop
            if i.salary > v_max_salary then
                v_max_salary := i.salary;
            end if;
        end loop;
        return v_max_salary;
    end;
end department_operations;
/

/* 8
Write a PL/SQL procedure to return simple and compound interest (OUT 
parameters) along with the Total Sum (IN OUT) i.e. Sum of Principle and Interest 
taking as input the principle, rate of interest and number of years (IN parameters). 
Call this procedure from an anonymous block.
*/
create or replace procedure compute_interest(
    principal number, roi number, years pls_integer,
    total_sum IN OUT number, 
    simple_interest OUT number, compound_interest OUT number
) is
begin
    total_sum := principal;
    for i in 1..years loop 
        total_sum := total_sum * (1 + roi);
    end loop;
    
    compound_interest := total_sum - principal;
    simple_interest := roi * years * principal;
end;
/

declare
    -- inputs
    principal number := 100;
    roi number := 0.09;
    years pls_integer := 8;

    -- outputs
    total_sum number;
    simple_interest number;
    compound_interest number;
begin
    compute_interest(principal, roi, years, 
        total_sum, simple_interest, compound_interest);

    dbms_output.put_line('Total sum: ' || total_sum);
    dbms_output.put_line('Simple interest: ' || simple_interest);
    dbms_output.put_line('Compound interest: ' || compound_interest);
end;
/
