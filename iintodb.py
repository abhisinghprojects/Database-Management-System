from tkinter import *
import sqlite3 as sql
####..........databse data insert.........### >>>>>>>>>>>>>>>
def Iintodb():

    data=sql.connect("student_database.db")
    cmd=data.cursor()
    cmd.execute("INSERT INTO students VALUES (:f_name, :l_name, :email, :per_contact, :father_name, :par_contact, :address)",
               {
                   'f_name':fn_e.get(),
                   'l_name':ln_e.get(),
                   'email':email_e.get() ,
                   'per_contact': pec_e.get(),
                   'father_name':ftn_e.get(),
                   'par_contact':pac_e.get(),
                   'address':ad_e.get()
               }
               )
    l=Label(form, text="entry estabilished", bg="red",fg="yellow")
    l.grid(row=12,column=1, columnspan=2)
    data.commit()
    data.close()


global form
global fn_e,ln_e,email_e,pec_e,ftn_e,pac_e,ad_e
form=Tk()
form.geometry("600x900")
form.title("StudentDatabaseSystem")
form.configure(bg="red")

h= Label(form, text="NEW STUDENT ENTRY", font="times 35",bg="yellow")
h.grid(row=0, column=0, padx=10,pady=35, columnspan=2)

fn= Label(form, text="FirstName", font="times 15",bg="pink",padx=35)
fn.grid(row=2,column=0,pady=10)
fn_e= Entry(form, font="j 12")
fn_e.grid(row=2,column=1,pady=10) 

ln= Label(form, text="LastName", font="times 15", bg="pink",padx=36)
ln.grid(row=3,column=0,pady=10)
ln_e= Entry(form, font="jh 12")
ln_e.grid(row=3,column=1,pady=10)

email= Label(form, text="Email", font="times 15", bg="pink",padx=56)     
email.grid(row=4,column=0,pady=10)
email_e=Entry(form, font="j 12")
email_e.grid(row=4,column=1,pady=10)

pec= Label(form, text="Personal contact", font="times 15", bg="pink",padx=9)
pec.grid(row=5,column=0,pady=10)
pec_e= Entry(form, font="jh 12")
pec_e.grid(row=5,column=1,pady=10)

ftn= Label(form, text="Father's name", font="times 15", bg="pink",padx=21)
ftn.grid(row=6,column=0,pady=10)
ftn_e= Entry(form, font="jh 12")
ftn_e.grid(row=6,column=1,pady=10)

pac= Label(form, text="Parent's contact", font="times 15", bg="pink",padx=19)
pac.grid(row=7,column=0,pady=10)
pac_e= Entry(form, font="J 12")
pac_e.grid(row=7,column=1,pady=10)

ad= Label(form, text="Address", font="times 15", bg="pink",padx=45)
ad.grid(row=8,column=0,pady=10)
ad_e= Entry(form, font="jh 12")
ad_e.grid(row=8,column=1,pady=10)
    
sv= Button(form, text="SAVE",bg="yellow", font="times 11", padx=12,command=Iintodb)   ## SAVE BUTTON
sv.grid(row=10,column=1,pady=20,columnspan=3)
 
form.mainloop()



