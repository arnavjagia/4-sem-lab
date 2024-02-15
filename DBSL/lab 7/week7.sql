SET SERVEROUTPUT ON

DECLARE
        grade CHAR(1);
BEGIN
        grade := '&g';
IF grade = 'A' THEN
        DBMS_OUTPUT.PUT_LINE('Excellent');
ELSIF grade = 'B' THEN
        DBMS_OUTPUT.PUT_LINE('Very Good');
ELSIF grade = 'C' THEN
        DBMS_OUTPUT.PUT_LINE('Good');
ELSIF grade = 'D' THEN
        DBMS_OUTPUT. PUT_LINE('Fair');
ELSIF grade = 'F' THEN
        DBMS_OUTPUT.PUT_LINE('Poor');
ELSE
        DBMS_OUTPUT.PUT_LINE('No such grade');
END IF;
END;
/


        
/*
Use a table StudentTable(RollNo, GPA) and populate the table with {(1, 5.8), (2, 6.5),
(3, 3.4), (4,7.8), (5, 9.5)} unless a different DB schema is explicitly specified
*/
CREATE TABLE student (roll number(3), gpa number(2));

INSERT INTO student VALUES (1, 5.8);
INSERT INTO student VALUES (2, 6.5);
INSERT INTO student VALUES (3, 3.4);
INSERT INTO student VALUES (4, 7.8);
INSERT INTO student VALUES (5, 9.5);

/* 1
Write a PL/SQL block to display the GPA of given student.
*/
DECLARE
        inp_roll number(3);
        gpa_val number(2);
BEGIN
        inp_roll := &g; -- input roll number
        SELECT gpa INTO gpa_val FROM student WHERE roll = inp_roll;
        DBMS_OUTPUT.PUT_LINE('GPA of student with roll number ' || inp_roll || ' is ' || gpa_val);
END;
/

/* 2
Write a PL/SQL block to display the letter grade(0-4: F; 4-5: E; 5-6: D; 6-7: C; 
7-8: B; 8-9: A; 9-10: A+} of given student
*/
DECLARE
        inp_roll number(3);
        gpa_val number(2);
BEGIN
        inp_roll := &g;
        SELECT gpa INTO gpa_val FROM student WHERE roll = inp_roll;
        IF gpa_val >= 9 THEN
                DBMS_OUTPUT.PUT_LINE('A+');
        ELSIF gpa_val >= 8 THEN
                DBMS_OUTPUT.PUT_LINE('A');
        ELSIF gpa_val >= 7 THEN
                DBMS_OUTPUT.PUT_LINE('B');
        ELSIF gpa_val >= 6 THEN
                DBMS_OUTPUT.PUT_LINE('C');
        ELSIF gpa_val >= 5 THEN
                DBMS_OUTPUT.PUT_LINE('D');
        ELSIF gpa_val >= 4 THEN
                DBMS_OUTPUT.PUT_LINE('E');
        ELSE
                DBMS_OUTPUT.PUT_LINE('F');
END IF;
END;
/

/* 3

*/


/* 4

*/


/* 5

*/


/* 6

*/


/* 7

*/


/* 8

*/
