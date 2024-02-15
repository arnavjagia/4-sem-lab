SET SERVEROUTPUT ON        --display buffer work, basically shows output
SET DEFINE ON              --allows intput in sql *plus

https://www.oracletutorial.com/plsql-tutorial/

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
        inp_roll student.roll%type;
        gpa_val student.gpa%type;
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
        inp_roll student.roll%type;
        gpa_val student.gpa%type;
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
Input the date of issue and date of return for a book. Calculate and display the fine 
with the appropriate message using a PL/SQL block. The fine is charged as per 
the table 8.1:
Late period         Fine
7 days              NIL
8 – 15 days         Rs.1/day
16 - 30 days        Rs. 2/ day
After 30 days       Rs. 5.00
*/
DECLARE
        inp_date DATE;
BEGIN

END;
        

/* 4
Write a PL/SQL block to print the letter grade of all the students(RollNo: 1 - 5)
*/    
BEGIN
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

/* 5

*/


/* 6

*/


/* 7

*/


/* 8

*/
