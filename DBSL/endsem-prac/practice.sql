SET SERVEROUTPUT ON        -- turning on output
SET DEFINE ON              -- allows input in SQL*Plus

-- testing excepting ZERO_DIVIDE
DECLARE
        res NUMBER(4);
BEGIN
        res := 23/0;
        DBMS_OUTPUT.PUT_LINE(res);
EXCEPTION
        WHEN ZERO_DIVIDE THEN
                DBMS_OUTPUT.PUT_LINE('zero divide exception handled');
END;
/

-- student gpa fetch
DROP TABLE student CASCADE CONSTRAINTS;
CREATE TABLE student (roll number(3), gpa number(2));

INSERT INTO student VALUES (1, 5.8);
INSERT INTO student VALUES (2, 6.5);
INSERT INTO student VALUES (3, 3.4);
INSERT INTO student VALUES (4, 7.8);
INSERT INTO student VALUES (5, 9.5);

DECLARE
        gpa student.gpa%type;
        rec student%rowtype;
BEGIN
        SELECT * INTO rec
        FROM student
        WHERE roll = '&roll_number';
        DBMS_OUTPUT.PUT_LINE(rec.roll || '|' || rec.gpa);
END;
/

-- letter grade of student
DECLARE
        REC STUDENT%ROWTYPE;
        GRADE VARCHAR2(10);
BEGIN
        SELECT * INTO REC FROM STUDENT WHERE STUDENT.ROLL = '&ROLL_NUMBER';
        CASE 
        WHEN REC.GPA >= 9 THEN
                GRADE:='A+';
        WHEN REC.GPA >= 8 THEN
                GRADE:='A';
        WHEN REC.GPA >= 7 THEN
                GRADE:='B';
        WHEN REC.GPA >= 6 THEN
                GRADE:='C';
        WHEN REC.GPA >= 5 THEN
                GRADE:='D';
        WHEN REC.GPA >= 4 THEN
                GRADE:='E';
        ELSE
                GRADE:='F';
        END CASE;
        DBMS_OUTPUT.PUT_LINE(REC.ROLL || ' ' || REC.GPA || ' ' || GRADE);
END;
/

-- letter grade all students
DECLARE
        REC STUDENT%ROWTYPE;
        GRADE VARCHAR2(10);
        i NUMBER;
BEGIN
        i:=0;
        LOOP 
        i:=i+1;
        SELECT * INTO REC FROM STUDENT WHERE STUDENT.ROLL = i;
        CASE 
        WHEN REC.GPA >= 9 THEN
                GRADE:='A+';
        WHEN REC.GPA >= 8 THEN
                GRADE:='A';
        WHEN REC.GPA >= 7 THEN
                GRADE:='B';
        WHEN REC.GPA >= 6 THEN
                GRADE:='C';
        WHEN REC.GPA >= 5 THEN
                GRADE:='D';
        WHEN REC.GPA >= 4 THEN
                GRADE:='E';
        ELSE
                GRADE:='F';
        END CASE;
        DBMS_OUTPUT.PUT_LINE(REC.ROLL || ' ' || REC.GPA || ' ' || GRADE);
        EXIT WHEN i=5;
        END LOOP;
END;
/

/*
Usage of WHILE:
5. Alter StudentTable by appending an additional column LetterGrade Varchar2(2). 
Then write a PL/SQL block to update the table with letter grade of each student
*/
ALTER TABLE STUDENT ADD LETTERGRADE VARCHAR(2);
DECLARE
        REC STUDENT%ROWTYPE;
        GRADE VARCHAR(2);
        i NUMBER;
BEGIN
        i:=0;
        WHILE i<5
        LOOP
                i:=i+1;
                SELECT * INTO REC FROM STUDENT WHERE STUDENT.ROLL = i;
                CASE 
                WHEN REC.GPA >= 9 THEN
                        GRADE:='A+';
                WHEN REC.GPA >= 8 THEN
                        GRADE:='A';
                WHEN REC.GPA >= 7 THEN
                        GRADE:='B';
                WHEN REC.GPA >= 6 THEN
                        GRADE:='C';
                WHEN REC.GPA >= 5 THEN
                        GRADE:='D';
                WHEN REC.GPA >= 4 THEN
                        GRADE:='E';
                ELSE
                        GRADE:='F';
                END CASE; 
                UPDATE STUDENT
                SET STUDENT.LETTERGRADE = GRADE
                WHERE STUDENT.ROLL = i;
        END LOOP;
END;
/

-- hello world procedure
CREATE OR REPLACE PROCEDURE DISP_HELLO IS
BEGIN
        DBMS_OUTPUT.PUT_LINE('hello world');
END;
/

EXEC DISP_HELLO;
/
