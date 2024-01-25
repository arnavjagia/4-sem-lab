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
