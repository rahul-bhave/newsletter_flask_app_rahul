This is an effort to develop CRUD applocation using flask.
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

![image](https://user-images.githubusercontent.com/55383777/120620489-a51b0e00-c47a-11eb-99f2-2112c17ff88f.png)

After submitting data

![image](https://user-images.githubusercontent.com/55383777/120620650-ced43500-c47a-11eb-9b2d-02478caa069a.png)

Data can be seen added in the database-

![image](https://user-images.githubusercontent.com/55383777/120620893-09d66880-c47b-11eb-9400-5b33ab3e5590.png)


