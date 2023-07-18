###..............database select access.......###
import sqlite3 as sql


data_base = sql.connect("student_database.db")
comd= data_base.cursor()
comd.execute("SELECT * FROM students WHERE f_name='fbfb'")
v=comd.fetchall()


fn=v[0][0]
ln=v[0][1]
gm=v[0][2]
per=v[0][3]
fth=v[0][4]
par=v[0][5]
adr=v[0][6]

     

data_base.commit()
data_base.close()
