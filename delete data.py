import sqlite3 as sql

fn="zuby"

data_base = sql.connect("student_database.db")
comd= data_base.cursor()
comd.execute("DELETE FROM students WHERE f_name!='a'")

     

data_base.commit()
data_base.close()



