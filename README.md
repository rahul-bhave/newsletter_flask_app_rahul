Steps fo application setup:

1. Clone the repo.
2. Create virtual environment.
3. Setup sqlite db and tables using following steps:

Steps to create database tables:

import sqlite3

conn = sqlite3.connect('newsletter.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Employee")

cursor.execute("DROP TABLE IF EXISTS Department")

query = """CREATE TABLE Department (
	    id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
	    department_name NVARCHAR(50)  NULL
		 )"""
		 
cursor.execute(query)

conn.commit()

query = """CREATE TABLE Employee(
        employee_id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name NVARCHAR(50)  NOT NULL, 
        email NVARCHAR(50)  NOT NULL, 
        department_id INTEGER  NOT NULL,
		FOREIGN KEY(department_id) REFERENCES Department(id)
         )"""
		 
cursor.execute(query)

conn.commit()

conn.execute("INSERT INTO Department (id, department_name ) "
             "VALUES (01, 'QA')")
	     
conn.execute("INSERT INTO Department (id, department_name ) "
             "VALUES (02, 'Dev')")
		 
conn.commit()

conn.close()

4. Run python app.python
5. Add Record please select Department name as QA or Dev only.
