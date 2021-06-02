# newsletter_flask_app_rahul
newsletter project experiment flask CRUD app

DB Scripts for table creation:

import sqlite3
# Connect to sqlite database
conn = sqlite3.connect('newsletter.db')
# cursor object
cursor = conn.cursor()
# drop query
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# create query
query = """CREATE TABLE Employee(
        employee_id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name NVARCHAR(50)  NOT NULL, 
        email NVARCHAR(50)  NOT NULL, 
        department_id INTEGER  NOT NULL,
		FOREIGN KEY(department_id) REFERENCES Department(department_id)
         )"""
		 
query = """CREATE TABLE Department (
	    department_id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
	    department_name NVARCHAR(50)  NULL
		 )"""
cursor.execute(query)
# commit and close
conn.commit()
conn.close()
