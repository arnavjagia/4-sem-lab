- [Create a new user in SQL *Plus](https://library.netapp.com/ecmdocs/ECMP12471543/html/GUID-287BC8BA-B8B6-4D67-804E-880B65D30B68.html)

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

- [Display names of all constraints for a table in Oracle SQL](https://stackoverflow.com/questions/11879217/display-names-of-all-constraints-for-a-table-in-oracle-sql#:~:text=SELECT%20*%0A%20%20FROM%20user_constraints%0A%20WHERE%20table_name%20%3D%20%27%3Cyour%20table%20name%3E%27%0A%20%20%20AND%20constraint_name%20%3D%20%27%3Cyour%20constraint%20name%3E%27%3B)
  ```sql
  SELECT *
    FROM user_constraints
   WHERE table_name = '<your table name>'
     AND constraint_name = '<your constraint name>';
  ```

- Never put `AS` in `FROM` clause in Oracle SQL
- `EXCEPT` clause doesn't work, instead use `MINUS` instead
- use `ROLLBACK TO <savpoint name>` to go to a savepoint  
  NOTE: savepoints are created for the current session only
- `UNIQUE` doesn't work in Oracle SQL so use `count(*)` method like in book
