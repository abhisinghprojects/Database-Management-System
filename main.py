import tkinter.messagebox as mb
from tkinter import *
import sqlite3 as sql
import turtle as t
from  tkinter import ttk
data = sql.connect("student_database.db")
comd=data.cursor()
###.....root destroy.....### >>>>>>>>>>>>>
def ex():
    a=False
    a=mb.askokcancel("exit","You want to exit?")
    if a==True:
       root.destroy()

data_base = sql.connect("student_database.db")
comd= data_base.cursor()

def clean():
    p= " "
    comd.execute( " ")

def bk():
    clear(fr)
    lab1=Label(fr, text="OPTIONS", bg="green", font="times 14")
    lab1.pack(fill=X)
    inn=Button(fr, text="New Entry", bg="yellow",command=entry,padx=180)
    inn.place(x=60,y=70)
    in2=Button(fr, text="Search Entry", bg="yellow",command=search,padx=173)
    in2.place(x=60,y=110)
    in3=Button(fr, text="Delete Database", bg="orange",padx=161)
    in3.place(x=60,y=150)
    in7=Button(fr, text=" Modify Database", bg="orange",command=md,padx=157)
    in7.place(x=60,y=190)
    in5=Button(fr, text=" Settings", bg="blue",command=setting,padx=145)
    in5.place(x=100,y=230)
    in6=Button(fr, text="Exit", bg="grey",command=exit,padx=60)
    in6.place(x=195,y=270)

def acs():
    data=sql.connect("student_database.db")
    comd=data.cursor()
    comd.execute("ALTER TABLE ADD COLUMN (:'value')",
    {'value':inn.get()+" "+ int})

def ac():
    global inn
    clear(fr)
    inn=Entry(fr,bg="black",fg="white",border=2)
    inn.place(x=20,y=120)
    i=Button(fr,text="Done", fg="yellow",command=acs, bg="black")
    i.place(x=20,y=140)
    
def md():
    clear(fr)
    al=Label(fr, text="Modify Database",bg="blue", fg="black",font="times 14")
    al.pack(fill=X)
    al=Button(fr, text="Add Column",bg="green", fg="white",font="times 10", command=ac,padx=140)
    al.place(x=100, y=60)
    al=Button(fr, text="Remove Column",bg="red", fg="black",font="times 10", padx=128)
    al.place(x=100, y=100)
    al=Button(fr, text="<<",bg="blue", fg="black",font="j 11",border=0, command=bk)
    al.place(x=0, y=0)

def setting():
    clear(fr)
    al=Label(fr, text="SETTING",bg="blue", fg="black",font="times 14")
    al.pack(fill=X)
    al=Button(fr, text="Add Login",bg="green", fg="white",font="times 10", padx=140,command=uentry)
    al.place(x=100, y=60)
    al=Button(fr, text="Remove Login",bg="red", fg="black",font="times 10", padx=128)
    al.place(x=100, y=100)
    al=Button(fr, text="View Registered Users",bg="green", fg="white",font="times 10", padx=102)
    al.place(x=100, y=140)
    al=Button(fr, text="<<",bg="blue", fg="black",font="j 11",border=0, command=bk)
    al.place(x=0, y=0)

def pr():
    clear(fr)
    search()
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
    d1=Label( fr,text=a+fn+" "+ln,bg="black", fg="red")
    d1.place(x=100,y=200)
    d3=Label( fr,text=b+gm,bg="black", fg="red")
    d3.place(x=100,y=250)
    d4=Label( fr,text=d+str(per)+", "+str(par),bg="black", fg="red")
    d4.place(x=100,y=300)
    d5=Label( fr,text=e+fth,bg="black", fg="red")
    d5.place(x=100,y=350)
    d7=Label( fr,text=f+adr+".",bg="black", fg="red")
    d7.place(x=100,y=400)

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
    clear(fr)
    search()
    head=Label(fr, text="Search Entry", bg="green", font="s 15",padx=140)
    head.place(x=67,y=120)
    
    entryy=Entry(fr, font="r 13", border=2, bg="white", fg="blue")
    entryy.place(x=160,y=160)
    
def clear(name) :
    for widgets in name.winfo_children():
        widgets.destroy()
 

def fname():
    
    entr()
    se=Button(fr, text="SEARCH(by f_name)", font="e 8",command=fsearch)
    se.place(x=208,y=200)
    
def lname():
    global se
    entr()
    se=Button(fr, text="SEARCH(by l_name)", font="e 8",command=lsearch)
    se.place(x=208,y=200)

def email():
    entr()
    se=Button(fr, text="SEARCH(by email)", font="e 8",command=esearch)
    se.place(x=208,y=200)

def contact():
    entr()
    se=Button(fr, text="SEARCH(by contact)", font="e 8",command=csearch)
    se.place(x=208,y=200)

def father_name():
    entr()
    se=Button(fr, text="SEARCH(by father_name)", font="e 8",command=fsearch)
    se.place(x=208,y=200)

    

def search():
    clear(fr)
    

    tag1= Label(fr, text="SEARCH STUDENT RECORD", font="Times 12", bg="yellow",pady=3)
    tag1.pack(fill=X)

    tag= Label(fr, text="SEARCH BY : ", font="Times 9", bg="black",fg="white")
    tag.place(relx=0.04,rely=0.06)

    b1=Button(fr, text="f_name", font="e 8",command=fname,bg="yellow")
    b1.place(relx=0.2,rely=0.06)

    b2=Button(fr, text="l_name", font="e 8",command=lname,bg="yellow")
    b2.place(relx=0.3,rely=0.06)

    b3=Button(fr, text="email", font="e 8",command=email,bg="yellow")
    b3.place(relx=0.4,rely=0.06)

    b4=Button(fr, text="personal contact", font="e 8",command=contact,bg="yellow")
    b4.place(relx=0.479,rely=0.06)

    b5=Button(fr, text="father_name", font="e 8",command=father_name,bg="yellow")
    b5.place(relx=0.67,rely=0.06)
    al=Button(fr, text="<<",bg="yellow", fg="black",font="j 11",border=0, command=bk)
    al.place(x=0, y=0)
    

def iintoaccess():
    if P2_E.get()==P_E.get():
       daata=sql.connect("credentials.db")
       coomd=daata.cursor()
       coomd.execute("INSERT INTO user VALUES (:USERNAME, :PWD)",
                      {
                          'USERNAME':U_E.get(),
                          'PWD':P_E.get()
                      }
                      )
       l=Label(fr, text="estabilished", bg="red",fg="yellow")
       l.place(x=400,y=5)
       daata.commit()
    else : 
       l=Label(fr, text="password not matched", bg="red",fg="yellow")
       l.place(x=400,y=5)
       

def uentry():
    global U_E, P_E, P2_E
    clear(fr)

    h= Label(fr, text="NEW USER ENTRY", font="times 15",bg="yellow")
    h.pack(fill=X)

    U= Label(fr, text="Username :",font="times 13",fg="white", bg="black",padx=3)
    U.place(relx=0.12,rely=0.1)
    U_E= Entry(fr, font="jh 12",bg="black",fg="blue",borderwidth="4")
    U_E.place(relx=0.40,rely=0.1)

    P= Label(fr, text="Password", font="times 13",fg="white", bg="black",padx=3)
    P.place(relx=0.12,rely=0.14)
    P_E= Entry(fr, font="jh 12",bg="black",fg="blue",borderwidth="4", show="*")
    P_E.place(relx=0.40,rely=0.14)

    P2= Label(fr, text="Confirm Password", font="times 13",fg="white", bg="black",padx=3)
    P2.place(relx=0.12,rely=0.18)
    P2_E= Entry(fr, font="jh 12",bg="black",fg="blue",borderwidth="4", )
    P2_E.place(relx=0.40,rely=0.18)

    sv= Button(fr, text="REGISTER",bg="yellow", font="times 9", padx=6,command=iintoaccess)   ## SAVE BUTTON
    sv.place(relx=0.51,rely=0.39)
    al=Button(fr, text="<<",bg="yellow", fg="black",font="j 11",border=0, command=bk)
    al.place(x=0, y=0)

def Iintodb():
    global root
    if not fn_e.get() or not email_e.get() or not pec_e.get() or not ftn_e.get() or not pac_e.get() or not ad_e.get():
       mb.showerror('Error!', "Please fill all the missing fields!!")
    else:    
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
        l=Label(fr, text="estabilished", bg="red",fg="yellow")
        l.place(x=400,y=5)
        data.commit()
        mb.showinfo('Done',f'The record of {fn_e.get().upper()} is successfully added.')


def entry():
    global root
    
    global fn_e,ln_e,email_e,pec_e,ftn_e,pac_e,ad_e
    clear(fr)

    h= Label(fr, text="NEW STUDENT ENTRY", font="times 15",bg="yellow")
    h.pack(fill=X)

    fn= Label(fr, text="FirstName",font="times 13",fg="white", bg="black",padx=3)
    fn.place(relx=0.12,rely=0.1)
    fn_e= Entry(fr, font="jh 12",bg="black",fg="blue",borderwidth="4")
    fn_e.place(relx=0.38,rely=0.1)

    ln= Label(fr, text="LastName", font="times 13",fg="white", bg="black",padx=3)
    ln.place(relx=0.12,rely=0.14)
    ln_e= Entry(fr, font="jh 12",bg="black",fg="blue",borderwidth="4")
    ln_e.place(relx=0.38,rely=0.14)

    email= Label(fr, text="Email",font="times 13",fg="white", bg="black",padx=3)     
    email.place(relx=0.12,rely=0.18)
    email_e=Entry(fr,  font="jh 12",bg="black",fg="blue",borderwidth="4")
    email_e.place(relx=0.38,rely=0.18)

    pec= Label(fr, text="Personal contact",font="times 13",fg="white", bg="black",padx=3)
    pec.place(relx=0.12,rely=0.22)
    pec_e= Entry(fr,  font="jh 12",bg="black",fg="blue",borderwidth="4")
    pec_e.place(relx=0.38,rely=0.22)

    ftn= Label(fr, text="Father's name",font="times 13",fg="white", bg="black",padx=3)
    ftn.place(relx=0.12,rely=0.26)
    ftn_e= Entry(fr,  font="jh 12",bg="black",fg="blue",borderwidth="4")
    ftn_e.place(relx=0.38,rely=0.26)

    pac= Label(fr, text="Parent's contact",font="times 13",fg="white", bg="black",padx=3)
    pac.place(relx=0.12,rely=0.30)
    pac_e= Entry(fr, font="jh 12",bg="black",fg="blue",borderwidth="4")
    pac_e.place(relx=0.38,rely=0.30)

    ad= Label(fr, text="Address", font="times 13",fg="white", bg="black",padx=3)
    ad.place(relx=0.12,rely=0.34)
    ad_e= Entry(fr, font="jh 12",bg="black",fg="blue",borderwidth="4")
    ad_e.place(relx=0.38,rely=0.34)

    sv= Button(fr, text="SAVE",bg="yellow", font="times 9", padx=6,command=Iintodb)   ## SAVE BUTTON
    sv.place(relx=0.51,rely=0.39)
    al=Button(fr, text="<<",bg="yellow", fg="black",font="j 11",border=0, command=bk)
    al.place(x=0, y=0)

   


###.....homepage of databse system......### >>>>>>>>>>


def log():
    for widgets in root.winfo_children():
       widgets.destroy()

    global us_e, pwd_e
    root.configure(bg="pink")
    root.geometry("620x700")
    root.title("LogIn")

    h= Label(root, text="WELCOME USER", font="times 30", pady=10)
    h.pack(fill=X,pady=10)
    f1=Frame(root, bg="red")
    f1.pack(pady=40)

    us= Label(f1, text="Username :", font="gd 15",bg="pink")
    us.grid(row=0, column=0,padx=5,pady=5)
    us_e= Entry(f1, font="j 13")
    us_e.grid(row=0,column=1,padx=5,pady=5)

    pwd=Label(f1, text="Password :", font="de 15",bg="pink")
    pwd.grid(row=1,column=0,padx=5,pady=5)
    pwd_e= Entry(f1,font="j 13",show="*")
    pwd_e.grid(row=1, column=1,padx=5,pady=5)

    ln=Button(root, text="Log in", bg="orange", padx=10, font="de 12",command=check,)
    ln.pack()

def check():
    global a
    if not us_e.get() or not pwd_e.get():
       mb.showerror('Error!', "Please fill all the fields !!")
    else:   
       cred=sql.connect("credentials.db")
       cmd=cred.cursor()
       cmd.execute("SELECT * FROM user")
       val=cmd.fetchall()
       for i in range(0,4):
         if us_e.get()==val[i][0]:
           if  pwd_e.get()==val[i][1]:
               homepage()
           else: 
               q=Label(root, text="(x) username/password")
               q.grid(row=5, column=2 )
    
         else:
            q=Label(root, text="(x) username/password")
            q.grid(row=5, column=2 )
    
    cred.close()

def con():

    canvas = t.Canvas(master = root, width = 440, height = 40, bg="red")
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
        homepage()

def View():
    global trr,fr 
    comd.execute("SELECT * FROM students")
    rows = comd.fetchall()    
    button1.destroy()
    for row in rows: 
        trr.insert("", END, values=row)      
    data.close()


def port():
    global fr,fr2,button1
    for widgets in root.winfo_children():
       widgets.destroy()
    jh=Label(root, text="STUDENT DATABASE MANAGEMENT SYSTEM", font="times 20",fg="red",bg="black" ,pady=10,padx=565)
    jh.grid(row=0,column=0,columnspan=3,pady=15,padx=20)

    fr=Frame(root,bg="black")
    fr.place(x=20, y=80, relheight=0.9, relwidth=0.3)

    fr2=Frame(root,bg="black")
    fr2.place(relx=0.314, y=80, relheight=0.9, relwidth=0.677)
    
    lab=Label(fr2, text="STUDENT DATABASE",font=" times 15 " ,bg="red")
    lab.pack(fill=X)
    lab1=Label(fr, text="OPTIONS", bg="green", font="times 14")
    lab1.pack(fill=X)
    inn=Button(fr, text="New Entry", bg="yellow",command=entry,padx=180)
    inn.place(x=60,y=70)
    in2=Button(fr, text="Search Entry", bg="yellow",command=search,padx=173)
    in2.place(x=60,y=110)
    in3=Button(fr, text="Delete Database", bg="orange",padx=161)
    in3.place(x=60,y=150)
    in7=Button(fr, text=" Modify Database", bg="orange",command=md,padx=157)
    in7.place(x=60,y=190)
    in5=Button(fr, text=" Settings", bg="blue",command=setting,padx=145)
    in5.place(x=100,y=230)
    in6=Button(fr, text="Exit", bg="grey",command=ex,padx=60)
    in6.place(x=195,y=270)

    
    button1 = Button(fr2,text="Display data", command=View)
    button1.place(x=12,y=728)
    bbutton1 = Button(fr2,text="Clean Database", command=clean)
    bbutton1.place(relx=0.08,y=728)

    




###.....homepage of databse system......### >>>>>>>>>>
def homepage():
    global root
    for widgets in root.winfo_children():
       widgets.destroy()
    root.geometry("1800x1000")
    root.resizable(0, 0)
    root.title("StudentDatabaseSystem")  
    root.configure(bg="pink")
    port()
    tab()

  


def tab():
    global trr,button1
    global fr2
    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=40,bg="red")
    trr=ttk.Treeview(fr2, column=("c1", "c2", "c3","c4","c5","c6","c7"),show='headings',height=22)
    X_scroller = Scrollbar(trr, orient=HORIZONTAL, command=trr.xview)
    Y_scroller = Scrollbar(trr, orient=VERTICAL, command=trr.yview)

    X_scroller.pack(side=BOTTOM, fill=X)
    Y_scroller.pack(side=RIGHT, fill=Y)

    trr.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
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
    trr.place(y=38, relwidth=0.98, relheight=0.76, x=12)



###....login call by root.....### >>>>>>>>
root=Tk()
root.configure(bg="pink")
root.geometry("500x500")
root.title("StudentDatabaseSystem")
h= Label(root, text="WELCOME USER", font="times 30", pady=10)
h.pack(pady=10)
s_up=Button(root, text="LOGIN", bg="pink", padx=30, font="de 12",command=con)
s_up.pack()
e_t=Button(root, text="exit", bg="red", padx=50, font="de 12",command=ex)
e_t.pack(pady=20)
root.mainloop()





