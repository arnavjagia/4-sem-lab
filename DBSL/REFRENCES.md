- [SQL command to list all tables in Oracle](https://www.sqltutorial.org/sql-list-all-tables/#:~:text=SELECT%20%0A%20%20%20%20table_name%0AFROM%0A%20%20%20%20user_tables%3B)
  ```sql
  SELECT 
      table_name
  FROM
      user_tables;
  ```

- [Drop all tables in Oracle DB (scheme)](https://jochenhebbrecht.be/site/2010-05-10/database/drop-all-tables-in-oracle-db-scheme#:~:text=DROP%2Dsql%2Dscript%22%3A-,SELECT%20%27DROP%20TABLE%20%22%27%20%7C%7C%20TABLE_NAME%20%7C%7C%20%27%22%20CASCADE%20CONSTRAINTS%3B%27%20FROM%20user_tables%3B,-user_tables%20is%20a)  
copy and paste the output  
  ```sql
  SELECT 'DROP TABLE "' || TABLE_NAME || '" CASCADE CONSTRAINTS;' FROM user_tables;
  
  
  ```

- Comments in SQL
  ```sql
  -- single line commment
  /* multi line comment */
  ```

- 
