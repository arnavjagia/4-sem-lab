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
