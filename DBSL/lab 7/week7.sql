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
Alter StudentTable by appending an additional column LetterGrade Varchar2(2). 
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
Usage of FOR:
Write a PL/SQL block to find the student with max. GPA without using aggregate 
function
*/
DECLARE
    max_gpa NUMBER := 0; -- Initialize maximum GPA
    max_roll NUMBER; -- Initialize roll number of the student with max GPA
BEGIN
    -- Iterate through each student's GPA
    FOR rec IN (SELECT roll, gpa FROM student) LOOP
        -- Check if the current GPA is greater than the current maximum GPA
        IF rec.gpa > max_gpa THEN
            max_gpa := rec.gpa; -- Update maximum GPA
            max_roll := rec.roll; -- Update roll number of the student with max GPA
        END IF;
    END LOOP;
    
    -- Display the student with the maximum GPA
    DBMS_OUTPUT.PUT_LINE('Student with maximum GPA:' || chr(10)
                      || 'Roll: ' || max_roll || chr(10)
                      || 'GPA: ' || max_gpa
    );
END;
/

/* 7
Usage of GOTO:
Implement lab exercise 4 using GOTO.
*/
DECLARE
    gpa_val NUMBER;
    grade VARCHAR2(2);
BEGIN
    FOR i IN 1..5 LOOP
        SELECT gpa INTO gpa_val FROM student WHERE roll = i;
        
        IF gpa_val >= 9 THEN
            grade := 'A+';
            GOTO print_grade;
        ELSIF gpa_val >= 8 THEN
            grade := 'A';
            GOTO print_grade;
        ELSIF gpa_val >= 7 THEN
            grade := 'B';
            GOTO print_grade;
        ELSIF gpa_val >= 6 THEN
            grade := 'C';
            GOTO print_grade;
        ELSIF gpa_val >= 5 THEN
            grade := 'D';
            GOTO print_grade;
        ELSIF gpa_val >= 4 THEN
            grade := 'E';
            GOTO print_grade;
        ELSE
            grade := 'F';
            GOTO print_grade;
        END IF;
        
        <<print_grade>>
        DBMS_OUTPUT.PUT_LINE('Student ' || i || ': ' || grade);
    END LOOP;
END;
/

/* 8
Exception Handling:
Based on the University database schema, write a PL/SQL block to display the 
details of the Instructor whose name is supplied by the user. Use exceptions to 
show appropriate error message for the following cases:
a. Multiple instructors with the same name
b. No instructor for the given name
*/
DECLARE
    v_instructor_name instructor.name%TYPE;
    v_instructor_id instructor.ID%TYPE;
    v_instructor_dept instructor.dept_name%TYPE;
    v_count_instructors INTEGER := 0; -- Initialize the count of instructors found
BEGIN
    -- Prompt the user to enter the instructor's name
    DBMS_OUTPUT.PUT('Enter the name of the Instructor: ');
    -- Accept the input from the user
    v_instructor_name := UPPER('&instructor_name');
    
    -- Retrieve the ID and department of the instructor
    SELECT ID, dept_name INTO v_instructor_id, v_instructor_dept 
    FROM instructor 
    WHERE UPPER(name) = v_instructor_name;
    
    -- Count the number of instructors found
    SELECT COUNT(*) INTO v_count_instructors 
    FROM instructor 
    WHERE UPPER(name) = v_instructor_name;
    
    -- Display appropriate message based on the number of instructors found
    IF v_count_instructors > 1 THEN
        DBMS_OUTPUT.PUT_LINE('Error: Multiple instructors found with the name ''' || v_instructor_name || '''');
    ELSIF v_count_instructors = 0 THEN
        DBMS_OUTPUT.PUT_LINE('Error: No instructor found with the name ''' || v_instructor_name || '''');
    ELSE
        -- Display the details of the instructor
        DBMS_OUTPUT.PUT_LINE('Instructor ID: ' || v_instructor_id);
        DBMS_OUTPUT.PUT_LINE('Department: ' || v_instructor_dept);
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Error: No instructor found with the name ''' || v_instructor_name || '''');
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('Error: Multiple instructors found with the name ''' || v_instructor_name || '''');
END;
/
