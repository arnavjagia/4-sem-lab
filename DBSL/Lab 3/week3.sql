-- 1.

SELECT title from course c,takes t where c.course_id=t.course_id and year=2010 and semester='Spring'
UNION
SELECT title from course c,takes t where c.course_id=t.course_id and year=2009 and semester='Fall';
-- 2.

SELECT title from course natural join takes where year=2010 and semester='Spring'
intersect
SELECT title from course natural join takes where year=2009 and semester='Fall';
-- 3.

SELECT title from course natural join takes where year=2009 and semester='Fall'
minus
SELECT title from course natural join takes where year=2010 and semester='Spring';
-- 4.

SELECT title FROM course
MINUS
SELECT c.title FROM course c, takes t WHERE t.course_id = c.course_id; 
-- 5.

SELECT title FROM course WHERE course_id IN 
(SELECT course_id FROM takes WHERE semester = 'Fall' AND year = 2009) 
AND course_id IN 
(SELECT course_id FROM takes WHERE semester = 'Spring' AND year = 2010);
-- 6.

SELECT COUNT(ID) FROM takes WHERE course_id IN 
(SELECT course_id FROM teaches WHERE ID = 10101);
-- 7.

SELECT course_id, title FROM course WHERE course_id 
IN (SELECT course_id FROM section WHERE semester = 'Fall'
 AND year = 2009) AND course_id NOT IN 
(SELECT course_id FROM section WHERE semester = 'Spring' AND year = 2010);

-- 8.
select name from student where name in (select name from instructor);

-- 9.
select name from instructor where salary > some(select salary from instructor where dept_name = 'Biology');

-- 10.
select name from instructor where salary > all(select salary from instructor where dept_name = 'Biology');

-- 11.
select * from (select dept_name, avg(salary) from instructor group by dept_name order by avg(salary) desc) where rownum = 1;

-- 12.
select dept_name from department where budget < all(select avg(salary) from instructor);

-- 13.
SELECT course_id, title FROM course WHERE EXISTS (SELECT course_id FROM section 
WHERE semester = 'Fall'  AND year = 2009 AND course.course_id = section.course_id)
INTERSECT
SELECT course_id, title FROM course WHERE EXISTS (SELECT course_id FROM section 
WHERE semester = 'Spring' AND year = 2010 AND course.course_id = section.course_id);

-- 14.
select name, ID from student where exists (select t.ID from takes t, course c where t.course_id = c.course_id and c.dept_name = 'Biology' and student.ID = t.ID);

-- 15.
select course_id, title form course where course_id in (select course_id from section where year = 2009 group by course_id having count(course_id) < 2);

-- 16.
select distinct id, name from student natural join takes where 2<=(select count(course_id) from course where dept_name = 'Comp. Sci');

-- 17.
select dept_name, avg(salary) from instructor group by dept_name having avg(salary) > 42000;

-- 18.
CREATE VIEW all_courses AS
SELECT section.course_id, section.sec_id, classroom.building, classroom.room_number
FROM section
JOIN course ON section.course_id = course.course_id
JOIN classroom ON section.building = classroom.building AND section.room_number = classroom.room_number
WHERE course.dept_name = 'Physics' AND section.semester = 'Fall' AND section.year = 2009;


-- 19.
SELECT *
FROM all_courses;


-- 20.
CREATE VIEW department_total_salary AS
SELECT dept_name, SUM(salary) AS total_salary
FROM instructor
GROUP BY dept_name;

