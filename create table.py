from dataclasses import dataclass
import sqlite3 as sql

data=sql.connect("student_database.db")
cmd=data.cursor()
cmd.execute("create table students(f_name varchar, l_name varchar,email primary_key email, per_contact number, father_name varchar, par_contact number, address varchar)")
data.commit()
