from tkinter import *
import sqlite3 as sql
import turtle as t
from  tkinter import ttk
data = sql.connect("student_database.db")
comd=data.cursor()
###.....root destroy.....### >>>>>>>>>>>>>
def ex():
    root.destroy()

data_base = sql.connect("student_database.db")
comd= data_base.cursor()

def pr():
    display=Frame(root,padx=100,pady=10)
    display.grid(row=5,column=0,columnspan=9)
     
    fn=v[0][0]
    ln=v[0][1]
    gm=v[0][2]
    per=v[0][3]
    fth=v[0][4]
    par=v[0][5]
    adr=v[0][6]
    a="Name: "
    b="Gmail: "
    d="Contact(p,f): "
    e="Father's name: "
    f="Address: "
    d1=Label( display,text=a+fn+" "+ln)
    d1.pack()
    d3=Label( display,text=b+gm)
    d3.pack()
    d4=Label( display,text=d+str(per)+", "+str(par))
    d4.pack()
    d5=Label( display,text=e+fth)
    d5.pack()
    d7=Label( display,text=f+adr+".")
    d7.pack()

def fsearch():
    global entryy,v
    comd.execute("SELECT * FROM students WHERE f_name =:ln",{'ln': entryy.get()})
    v=comd.fetchall()
    pr()

def lsearch():
    global entryy,v
    comd.execute("SELECT * FROM students WHERE l_name=:ln", {'ln': entryy.get()})
    v=comd.fetchall()
    pr()

def esearch():
    global entryy,v
    comd.execute("SELECT * FROM students WHERE email=:ln", {'ln': entryy.get()})
    v=comd.fetchall()
    pr()

def csearch():
    global entryy,v
    comd.execute("SELECT * FROM students WHERE per_contact=:ln", {'ln': entryy.get()})
    v=comd.fetchall()
    pr()

def ftsearch():
    global entryy,v
    comd.execute("SELECT * FROM students WHERE l_name=:ln", {'ln': entryy.get()})
    v=comd.fetchall()
    pr()

def entr():
    global entryy
    global fr
    head=Label(fr, text="Search Entry", bg="pink", font="s 20")
    head.grid(row=2, column=1,pady=10,padx=14,columnspan=6)
    entryy=Entry(fr, font="r 12")
    entryy.grid(row=3, column=1, columnspan=6)
    
def clear(name) :
    for widgets in name.winfo_children():
        widgets.destroy()
           
def fname():
    
    entr()
    se=Button(fr, text="SEARCH(by f_name)", font="e 8",command=fsearch)
    se.grid(row=4, column=1,pady=10,padx=10,columnspan=6)
    
def lname():
    entr()
    se=Button(fr, text="SEARCH(by l_name)", font="e 8",command=lsearch)
    se.grid(row=4, column=1,pady=10,padx=10,columnspan=6)

def email():
    entr()
    se=Button(fr, text="SEARCH(by email)", font="e 8",command=esearch)
    se.grid(row=4, column=1,pady=10,padx=10,columnspan=6)

def contact():
    entr()
    se=Button(fr, text="SEARCH(by contact)", font="e 8",command=csearch)
    se.grid(row=4, column=1,pady=10,padx=10,columnspan=6)

def father_name():
    entr()
    se=Button(fr, text="SEARCH(by father_name)", font="e 8",command=fsearch)
    se.grid(row=4, column=1,pady=10,padx=10,columnspan=6)

def bk():  ### back button ###
    homepage()

def search():

    back=Button(fr, text="back",font="d 8",bg="white", fg="black",padx=254,command=bk)
    back.grid(row=0,column=0,columnspan=10,pady=4,padx=1)
    
    tag= Label(fr, text="SEARCH BY : ", font="Times 12", bg="yellow",pady=3)
    tag.grid(row=1, column=1,pady=6,padx=8)

    b1=Button(fr, text="f_name", font="e 10",command=fname,bg="yellow")
    b1.grid(row=1, column=2)

    b2=Button(fr, text="l_name", font="e 10",command=lname,bg="yellow")
    b2.grid(row=1, column=3)

    b3=Button(fr, text="email", font="e 10",command=email,bg="yellow")
    b3.grid(row=1, column=4)

    b4=Button(fr, text="personal contact", font="e 10",command=contact,bg="yellow")
    b4.grid(row=1, column=5)

    b5=Button(fr, text="father_name", font="e 10",command=father_name,bg="yellow")
    b5.grid(row=1, column=6)
    

def Iintodb():
    global root
    data=sql.connect("student_database.db")
    comd=data.cursor()
    comd.execute("INSERT INTO students VALUES (:f_name, :l_name, :email, :per_contact, :father_name, :par_contact, :address)",
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
    l=Label(root, text="entry estabilished", bg="red",fg="yellow")
    l.grid(row=12,column=1, columnspan=2)
    data.commit()


def entry():
    global root
    fr.destroy()
    global fn_e,ln_e,email_e,pec_e,ftn_e,pac_e,ad_e
    
    fr0=Frame(root,padx=170,pady=242,bg="white")
    fr0.grid(row=1,column=0,pady=10,padx=20,rowspan=2,columnspan=1)
    back=Button(fr0, text="back",font="d 8",bg="white", fg="black",padx=74,command=bk)
    back.grid(row=0,column=0,pady=4,padx=1,columnspan=2)

    h= Label(fr0, text="NEW STUDENT ENTRY", font="times 15",bg="yellow")
    h.grid(row=1, column=0, padx=1,pady=10,columnspan=2)

    fn= Label(fr0, text="FirstName", font="times 5",bg="pink",padx=3)
    fn.grid(row=2,column=0,pady=10)
    fn_e= Entry(fr0, font="j 12")
    fn_e.grid(row=2,column=1,pady=10) 

    ln= Label(fr0, text="LastName", font="times 5", bg="pink",padx=3)
    ln.grid(row=3,column=0,pady=10)
    ln_e= Entry(fr0, font="jh 12")
    ln_e.grid(row=3,column=1,pady=10)

    email= Label(fr0, text="Email", font="times 5", bg="pink",padx=5)     
    email.grid(row=4,column=0,pady=10)
    email_e=Entry(fr0, font="j 12")
    email_e.grid(row=4,column=1,pady=10)

    pec= Label(fr0, text="Personal contact", font="times 5", bg="pink",padx=6)
    pec.grid(row=5,column=0,pady=10)
    pec_e= Entry(fr0, font="jh 12")
    pec_e.grid(row=5,column=1,pady=10)

    ftn= Label(fr0, text="Father's name", font="times 5", bg="pink",padx=6)
    ftn.grid(row=6,column=0,pady=10)
    ftn_e= Entry(fr0, font="jh 12")
    ftn_e.grid(row=6,column=1,pady=10)

    pac= Label(fr0, text="Parent's contact", font="times 5", bg="pink",padx=6)
    pac.grid(row=7,column=0,pady=10)
    pac_e= Entry(fr0, font="J 12")
    pac_e.grid(row=7,column=1,pady=10)

    ad= Label(fr0, text="Address", font="times 5", bg="pink",padx=6)
    ad.grid(row=8,column=0,pady=10)
    ad_e= Entry(fr0, font="jh 12")
    ad_e.grid(row=8,column=1,pady=10)
    
    sv= Button(fr0, text="SAVE",bg="yellow", font="times 4", padx=6,command=Iintodb)   ## SAVE BUTTON
    sv.grid(row=11,column=1,pady=6,columnspan=2)


###.....homepage of databse system......### >>>>>>>>>>


def log():
    for widgets in root.winfo_children():
       widgets.destroy()

    global us_e, pwd_e
    root.configure(bg="pink")
    root.geometry("620x700")
    root.title("LogIn")
    h= Label(root, text="WELCOME USER", font="times 30", pady=10)
    h.grid(row=0,column=2,pady=10)

    us= Label(root, text="username", font="gd 15",bg="pink")
    us.grid(row=1,column=1,padx=30)

    us_e= Entry(root, font="j 13")
    us_e.grid(row=1, column=2)

    pwd=Label(root, text="password", font="de 15",bg="pink")
    pwd.grid(row=2, column=1,pady=5)

    pwd_e= Entry(root,font="j 13",show="*")
    pwd_e.grid(row=2, column=2)

    ln=Button(root, text="login", bg="orange", padx=50, font="de 12",command=check)
    ln.grid(row=3,column=2,pady=20)

def check():
    global a
    cred=sql.connect("credentials.db")
    cmd=cred.cursor()
    cmd.execute("SELECT * FROM user")
    val=cmd.fetchall()
    if us_e.get()==val[0][0]:
        if  pwd_e.get()==val[0][1]:
            homepage()
        
        else:
             q=Label(root, text="wrong password")
             q.grid(row=5, column=2 )
    else:
         r=Label(root, text="user doesn't exist")
         r.grid(row=5, column=2 )
    cred.commit()
    cred.close()

def con():

    canvas = t.Canvas(master = root, width = 440, height = 40, bg="pink")
    canvas.pack(padx=2, pady=2) 
    l=t.RawTurtle(canvas)
    l.speed("fastest")
    l.hideturtle()
    l.setheading(300)
    l.color("pink")
    l.pensize(2000)
    l.forward(410)
    l.goto(0,0)
    l.color("red")
    l.penup()
    l.setheading(0)
    l.setheading(180)
    l.forward(90)
    l.setheading(0)
    l.showturtle()
    l.pensize(12)
    l.shape("circle")
    l.speed("fastest")
    t1=0
    for __ in range (2):
        for _ in range(10):
             l.dot(8,"black")
             l.forward(20)
             t1+=1
        l.setheading(180)
        l.hideturtle()
        l.forward(200)
        l.setheading(0)
        l.showturtle()  
    if t1==20:
        log()

def port():
    global fr,fr2
    for widgets in root.winfo_children():
       widgets.destroy()
    jh=Label(root, text="STUDENT DATABASE MANAGEMENT SYSTEM", font="times 20",fg="red",bg="black" ,pady=10,padx=620)
    jh.grid(row=0,column=0,columnspan=3,pady=15,padx=20)

    fr=Frame(root,padx=170,pady=410,bg="pink")
    fr.grid(row=1,column=0,pady=10,padx=20,rowspan=2,columnspan=1)

    fr2=Frame(root,bg="pink")
    fr2.grid(row=1,column=1,pady=10,padx=20,rowspan=3,columnspan=2)

    inn=Button(fr, text="Newntry", bg="yellow",command=entry,padx=11)
    inn.grid(row=2, column=0,pady=2,)
    in2=Button(fr, text="SearchEntry", bg="yellow",command=search)
    in2.grid(row=3, column=0,padx=1)
    tab()




###.....homepage of databse system......### >>>>>>>>>>
def homepage():
    global root
    for widgets in root.winfo_children():
       widgets.destroy()
    root.geometry("1050x900")
    root.title("StudentDatabaseSystem")  
    root.configure(bg="grey")
    port()

  
def View():
    global trr,fr 
    comd.execute("SELECT * FROM students")
    rows = comd.fetchall()    
    button1.destroy()
    for row in rows: 
        trr.insert("", END, values=row)      
    data.close()


def tab():
    global trr,button1
    global fr2
    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=40)
    trr=ttk.Treeview(fr2, column=("c1", "c2", "c3","c4","c5","c6","c7"),show='headings',height=22)
    trr.column("#1", anchor=CENTER)
    trr.heading("#1", text="Fname")
    trr.column("#2", anchor=CENTER)
    trr.heading("#2", text="Lname")
    trr.column("#3", anchor=CENTER)
    trr.heading("#3", text="Gmail")
    trr.column("#4", anchor=CENTER)
    trr.heading("#4", text="Personal contact")
    trr.column("#5", anchor=CENTER)
    trr.heading("#5", text="Father's name")
    trr.column("#6", anchor=CENTER)
    trr.heading("#6", text="Parent contact")
    trr.column("#7", anchor=CENTER)
    trr.heading("#7", text="Address")
    trr.pack()
    button1 = Button(fr,text="Display data", command=View)
    button1.grid(row=5,column=0)


###....login call by root.....### >>>>>>>>
root=Tk()
root.configure(bg="pink")
root.geometry("500x500")
root.title("StudentDatabaseSystem")
h= Label(root, text="WELCOME USER", font="times 30", pady=10)
h.pack(pady=10)
s_up=Button(root, text="LOGIN", bg="pink", padx=30, font="de 12",command=homepage)
s_up.pack()
e_t=Button(root, text="exit", bg="red", padx=50, font="de 12",command=ex)
e_t.pack(pady=20)
root.mainloop()



###.........database insert.........##### >>>>>>>>>>>>>>>>>>>
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
    l=Label(root, text="entry estabilished", bg="red",fg="yellow")
    l.grid(row=12,column=1, columnspan=2)
    data.commit()
    data.close()

