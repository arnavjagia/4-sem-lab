/* 1.
Create Employee table with following constraints:
- Make EmpNo as Primary key.
- Do not allow EmpName, Gender, Salary and Address to have null values.
- Allow Gender to have one of the two values: ‘M’, ‘F’.
*/
CREATE TABLE employee
	(enum		number(3),
	 ename		varchar(15)	NOT NULL,
	 gender		char(1)		NOT NULL,
	 salary		number(9,2)	NOT NULL,
	 eadd		varchar(15)	NOT NULL,
	 dno		number(3),
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
	 location	varchar(15),
	 PRIMARY KEY (deptno),
	 UNIQUE (deptname)
	);

/* 3.
Make DNo of Employee as foreign key which refers to DeptNo of Department.
*/
ALTER TABLE employee
ADD CONSTRAINT dno_fk
	FOREIGN KEY (dno)
	REFERENCES department(deptno)
	ON DELETE CASCADE;

/* 4.
Insert few tuples into Employee and Department which satisfies the above constraints.
*/
INSERT INTO department VALUES(901, 'CSE', 'MANIPAL');
INSERT INTO department VALUES(902, 'ICT', 'MANIPAL');
INSERT INTO employee VALUES(101, 'firstperson', 'M', 1000, 'MANIPAL', 901);
INSERT INTO employee VALUES(102, 'secondperson', 'F', 2000, 'MANIPAL', 902);

/* 5.
Try to insert few tuples into Employee and Department which violates some of the above constraints
*/
-- ORA-00001: unique constraint (CSE50.SYS_C00146313) violated
INSERT INTO department VALUES(901, 'DSE','MANIPAL');
-- ORA-02290: check constraint (CSE50.SYS_C00146310) violated
INSERT INTO employee VALUES(103, 'thirdperson', 'G', 3000, 'MANIPAL', 901);

/* 6.
Try to modify/delete a tuple which violates a constraint.
(Ex: Drop a department tuple which has one or more employees)
*/
UPDATE department SET deptno = 903 WHERE deptname = 'CSE';
-- DELETE FROM department WHERE deptname = 'CSE';		-- doesn't violate

