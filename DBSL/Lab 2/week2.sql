/* 1.
Create Employee table with following constraints:
- Make EmpNo as Primary key.
- Do not allow EmpName, Gender, Salary and Address to have null values.
- Allow Gender to have one of the two values: ‘M’, ‘F’.
*/
CREATE TABLE employee
	(enum		number(3),
	 ename		varchar(15)	NOT NULL,
	 eadd		varchar(15)	NOT NULL,
	 gender		char(1)		NOT NULL,
	 salary		number(9,2)	NOT NULL,
	 PRIMARY KEY (enum),
	 CHECK (gender in ('M', 'F'))
	);

/* 2.
Create Department table with following:
- Make DeptNo as Primary key
- Make DeptName as candidate key
*/
CREATE TABLE department
	(deptno		number(3),
	 deptname	varchar(15)	NOT NULL,
	 PRIMARY KEY (deptno),
	 UNIQUE (deptname)
	);
