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
        inp_roll := &roll; -- input roll number
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
        grade char(2);
BEGIN
        inp_roll := &roll;
        SELECT gpa INTO gpa_val FROM student WHERE roll = inp_roll;
        IF gpa_val >= 9 THEN
                grade := 'A+';
        ELSIF gpa_val >= 8 THEN
                grade := 'A';
        ELSIF gpa_val >= 7 THEN
                grade := 'B';
        ELSIF gpa_val >= 6 THEN
                grade := 'C';
        ELSIF gpa_val >= 5 THEN
                grade := 'D';
        ELSIF gpa_val >= 4 THEN
                grade := 'E';
        ELSE
                grade := 'F';
END IF;
DBMS_OUTPUT.PUT_LINE(grade);
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
        issue_date DATE; return_date DATE;
        days NUMBER; fine NUMBER;
BEGIN
        issue_date := TO_DATE('&issue_date', 'DDMMYYYY');
        return_date := TO_DATE('&return_date', 'DDMMYYYY');
        days := return_date - issue_date;
        fine := 0;
        
        IF days > 30 THEN
                fine := fine + ((days - 30) * 5); -- Fine for days after 30
                days := 30; -- Maximum fine applicable
        END IF;
        
        IF days > 15 THEN
                fine := fine + ((days - 15) * 2); -- Fine for days between 16 and 30
                days := 15; -- Maximum fine applicable
        END IF;
        
        IF days > 7 THEN
                fine := fine + ((days - 7) * 1); -- Fine for days between 8 and 15
                days := 7; -- Maximum fine applicable
        END IF;
        
        DBMS_OUTPUT.PUT_LINE('Fine: Rs. ' || fine);
END;
/
        
/* 4
Write a PL/SQL block to print the letter grade of all the students(RollNo: 1 - 5)
*/    
DECLARE
    gpa_val student.gpa%type;
    grade VARCHAR2(2);
BEGIN
    FOR i IN 1..5 LOOP
        SELECT gpa INTO gpa_val FROM student WHERE roll = i;
        
        IF gpa_val >= 9 THEN
            grade := 'A+';
        ELSIF gpa_val >= 8 THEN
            grade := 'A';
        ELSIF gpa_val >= 7 THEN
            grade := 'B';
        ELSIF gpa_val >= 6 THEN
            grade := 'C';
        ELSIF gpa_val >= 5 THEN
            grade := 'D';
        ELSIF gpa_val >= 4 THEN
            grade := 'E';
        ELSE
            grade := 'F';
        END IF;
        
        DBMS_OUTPUT.PUT_LINE('Student ' || i || ': ' || grade);
    END LOOP;
END;
/

/* 5
Usage of WHILE:
5. Alter StudentTable by appending an additional column LetterGrade Varchar2(2). 
Then write a PL/SQL block to update the table with letter grade of each student.
*/
-- Alter the table to add the LetterGrade column
ALTER TABLE student ADD (LetterGrade VARCHAR2(2));

-- PL/SQL block to update the table with letter grades
DECLARE
    gpa_val NUMBER;
    grade VARCHAR2(2);
    roll_num NUMBER := 1; -- Initialize the roll number
BEGIN
    -- Loop until all students are processed
    WHILE roll_num <= 5 LOOP
        -- Retrieve GPA for the current student
        SELECT gpa INTO gpa_val FROM student WHERE roll = roll_num;
        
        -- Determine the letter grade based on GPA
        IF gpa_val >= 9 THEN
            grade := 'A+';
        ELSIF gpa_val >= 8 THEN
            grade := 'A';
        ELSIF gpa_val >= 7 THEN
            grade := 'B';
        ELSIF gpa_val >= 6 THEN
            grade := 'C';
        ELSIF gpa_val >= 5 THEN
            grade := 'D';
        ELSIF gpa_val >= 4 THEN
            grade := 'E';
        ELSE
            grade := 'F';
        END IF;
        
        -- Update the LetterGrade column for the current student
        UPDATE student SET LetterGrade = grade WHERE roll = roll_num;
        
        -- Increment the roll number for the next iteration
        roll_num := roll_num + 1;
    END LOOP;
END;
/

/* 6

*/


/* 7

*/


/* 8

*/
