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
SELECT dept_name
FROM instructor 
GROUP BY dept_name
HAVING avg(salary) >= ALL (
        SELECT avg(salary)
        FROM instructor
        GROUP BY  dept_name
        );

-- 12.
select dept_name from department where budget < all(select avg(salary) from instructor);

-- 13.
select course_id
from section as S
where semester = 'Fall' and year= 2009 and
        exists (select *
                from section as T
                where semester = 'Spring' and year= 2010 and
                S.course_id= T.course_id);

-- 14.
select distinct S.ID, S.name
from student S
where not exists (
        from course
        where dept_name = 'Biology')
        minus
        (select T.course_id
        from takes T
        where S.ID = T.ID)
        );

-- 15.
select course_id, title form course where course_id in (select course_id from section where year = 2009 group by course_id having count(course_id) < 2);

-- 16.
select distinct S.ID, S.name
from student S
where 1 < (
    select count(*)
    from takes T
    where T.ID = S.ID and 
        T.course_id in (
            select course_id 
            from course
            where dept_name = 'Comp. Sci.'
        )
); 

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

