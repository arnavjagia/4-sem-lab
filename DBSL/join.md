1. **JOIN (or INNER JOIN)**:
   - The `JOIN` keyword is used to combine rows from two or more tables based on a related column between them.
   - In Oracle SQL, `JOIN` and `INNER JOIN` are synonymous.
   - It returns only the rows where there is a match in both tables.

```sql
SELECT *
FROM table1
JOIN table2 ON table1.column_name = table2.column_name;
```

Example from the schema:

```sql
SELECT *
FROM instructor
JOIN department ON instructor.dept_name = department.dept_name;
```

2. **NATURAL JOIN**:
   - The `NATURAL JOIN` keyword performs a join by implicitly matching the columns with the same name in both tables.
   - It returns all columns from both tables with matching columns omitted.

```sql
SELECT *
FROM table1
NATURAL JOIN table2;
```

Example from the schema:

```sql
SELECT *
FROM instructor
NATURAL JOIN department;
```

3. **LEFT JOIN (or LEFT OUTER JOIN)**:
   - The `LEFT JOIN` keyword returns all rows from the left table (first table mentioned) and the matched rows from the right table. If there are no matches, NULL values are returned for the columns from the right table.
   - It ensures that all rows from the left table are included, even if there are no matches in the right table.

```sql
SELECT *
FROM table1
LEFT JOIN table2 ON table1.column_name = table2.column_name;
```

Example from the schema:

```sql
SELECT *
FROM course
LEFT JOIN teaches ON course.course_id = teaches.course_id;
```

4. **RIGHT JOIN (or RIGHT OUTER JOIN)**:
   - The `RIGHT JOIN` keyword returns all rows from the right table (second table mentioned) and the matched rows from the left table. If there are no matches, NULL values are returned for the columns from the left table.
   - It ensures that all rows from the right table are included, even if there are no matches in the left table.

```sql
SELECT *
FROM table1
RIGHT JOIN table2 ON table1.column_name = table2.column_name;
```

Example from the schema:

```sql
SELECT *
FROM teaches
RIGHT JOIN course ON teaches.course_id = course.course_id;
```

5. **OUTER JOIN (or FULL OUTER JOIN)**:
   - The `OUTER JOIN` keyword returns all rows when there is a match in either table. If there are no matches, NULL values are returned for the columns from the table without a match.
   - It combines the results of both `LEFT JOIN` and `RIGHT JOIN`.

```sql
SELECT *
FROM table1
FULL OUTER JOIN table2 ON table1.column_name = table2.column_name;
```

Example from the schema:

```sql
SELECT *
FROM teaches
FULL OUTER JOIN course ON teaches.course_id = course.course_id;
```

These are the various types of joins in Oracle SQL along with examples from the provided schema. They help in combining data from multiple tables based on related columns.
