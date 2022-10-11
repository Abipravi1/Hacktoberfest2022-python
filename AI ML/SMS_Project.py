
##Student Management System with database

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from sqlalchemy import update
from tkcalendar import *
from tkcalendar import DateEntry
import mysql.connector


root=Tk()

######## ALL VARIABLES ############
NAME=StringVar()
PRN=StringVar()
ROLL=StringVar()
CAL=StringVar()
BRANCH=StringVar()
GENDER=StringVar()

SCH1=StringVar()
SCH2=StringVar()
##############___________________####################################

bg1 = PhotoImage(file="C:\\Users\\Rutikwakchaure\\Pictures\\BG.png") #inserted background image
lb = Label(root, image=bg1)
lb.place(height=750, width=1400)

root.title("PROJECT  BY  SARTHAK")
root.geometry("1200x1000")


title = Label(root, text='Student  Management System  ', bd=10, relief=GROOVE, font=('Arial black', 30))
title.place(x=0.3, y=20, width=1350)

f1 = Frame(root, bg='lightblue3', relief=RIDGE, bd=10.5)
f1.place(x=-1, y=96, height=600, width=560)

f2 = Frame(root, bg='lightblue3', relief=RIDGE, bd=10.5)
f2.place(x=554, y=96, height=599, width=795)



Name = Label(f1, text="Student Name", font=('Arial Rounded MT Bold', 19), bg='lightblue3').place(x=70, y=55)
prn = Label(f1, text="PRN", font=('Arial Rounded MT Bold', 17), bg='lightblue3').place(x=70, y=135)
rno = Label(f1, text="Roll No", font=('Arial Rounded MT Bold', 17), bg='lightblue3').place(x=70, y=210)
dob = Label(f1, text="D.O.B", font=('Arial Rounded MT Bold', 17), bg='lightblue3').place(x=70, y=287)
br = Label(f1, text="Branch", font=('Arial Rounded MT Bold', 17), bg='lightblue3').place(x=70, y=365)
Gen = Label(f1, text='Gender', font=('Arial Rounded MT Bold', 17), bg='lightblue3').place(x=70, y=435)

name = Entry(f1, font=('bold', 16), bd=2, relief=SOLID,textvariable=NAME)
name.place(x=265, y=63, height=25, width=250)
prn = Entry(f1, font=('bold', 16), bd=2, relief=SOLID,textvariable=PRN)
prn.place(x=265, y=140, height=25, width=200)
rno = Entry(f1, font=('bold', 16), bd=2, relief=SOLID,textvariable=ROLL)
rno.place(x=265, y=215, height=25, width=130)


br = ttk.Combobox(f1, textvariable=BRANCH, state='readonly', font=('Arial', 12))
br['value'] = (
            'Computer Enginnering', 'IT', 'ENTC', "Chemical", 'Civil Engineering', "Mechanical Engineering", 'Robotics')
br.place(x=265, y=371, height=25, width=200)


gn = ttk.Combobox(f1, textvariable=GENDER, state='readonly', font=('Arial', 12))
gn['value'] = ('Male', 'Female', 'Others')
gn.place(x=265, y=441, height=23, width=120)

cal = DateEntry(f1, textvariable=CAL,state='readonly',height=10, width=10, year=2021, month=9, day=3, font=('bold', 15), background='darkblue',foreground='white', borderwidth=2)
cal.place(x=265, y=290, height=30, width=150)

        #########        Frame 2     ###########

f3 = Frame(root, bg='white', relief=RIDGE, bd=10.5)
f3.place(x=7, y=625, height=60, width=540)


######################  Functions  #################


def add():
    a=NAME.get()
    b=PRN.get()
    c=ROLL.get()
    d=BRANCH.get()
    e=GENDER.get()
    f=CAL.get()


    if a=="" or b=="" or c=="" or d=="" or e=="" or f=="":
        messagebox.showerror("Student Management System","Sorry!!! All fields are required")

    else:
        conn = mysql.connector.connect(user='root', password='12345',
                                       host='localhost', database='sarthak',
                                       auth_plugin='mysql_native_password')
        cur=conn.cursor()
        cur.execute('insert into data values(%s,%s,%s,%s,%s,%s)',(NAME.get(),
                                                                      PRN.get(),
                                                                      ROLL.get(),
                                                                      CAL.get(),
                                                                      BRANCH.get(),
                                                                      GENDER.get()))

        conn.commit()
        display()
        conn.close()

        messagebox.showinfo("Student Management System","Your Data has beeen recorded Successfully!!!\n Thankyou!!!")



###Display record ##########

def display():
    conn = mysql.connector.connect(user='root', password='12345',
                                   host='localhost', database='sarthak',
                                   auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute("select * from data")
    dis=cur.fetchall()

    if len(dis)!=0:
        tree.delete(*tree.get_children())
        for i in dis:
            tree.insert("",END,values=i)
        conn.commit()
    conn.close()

########## Update ###########


def select_data(event):
    data=tree.focus()
    cursor=tree.item(data)
    row=cursor['values']
    NAME.set(row[0])
    PRN.set(row[1])
    ROLL.set(row[2])
    CAL.set(row[3])
    BRANCH.set(row[4])
    GENDER.set(row[5])

def update_data():
    a = NAME.get()
    b = PRN.get()
    c = ROLL.get()
    d = BRANCH.get()
    e = GENDER.get()
    f = CAL.get()
    if a == "" or b == "" or c == "" or d == "" or e == "" or f == "":
        messagebox.showerror("Student Management System", "Sorry!!! All fields are required")

    else:

        conn = mysql.connector.connect(user='root', password='12345',
                                       host='localhost', database='sarthak',
                                       auth_plugin='mysql_native_password')
        cur = conn.cursor()
        cur.execute("update data set Name=%s, Roll_No=%s, D_O_B=%s, BRANCH=%s, Gender=%s where PRN=%s ", (NAME.get(),
                                                                                                          ROLL.get(),
                                                                                                          CAL.get(),
                                                                                                          BRANCH.get(),
                                                                                                          GENDER.get(),
                                                                                                          PRN.get()))

        conn.commit()
        display()
        conn.close()
        messagebox.showinfo('Student Management System','Record has been Updated Successfully !!!')
        #### Except PRN all parameters can change PRN is a primary key
        #### for updatation of data atleast one parameter should be constant

### Delete record ##########

def delete():
    a = NAME.get()
    b = PRN.get()
    c = ROLL.get()
    d = BRANCH.get()
    e = GENDER.get()
    f = CAL.get()

    if a == "" or b == "" or c == "" or d == "" or e == "" or f == "":
        messagebox.showerror("Student Management System", "Sorry!!! All fields are required")

    else:
        conn = mysql.connector.connect(user='root', password='12345',
                                       host='localhost', database='sarthak',
                                       auth_plugin='mysql_native_password')
        cur = conn.cursor()
        cur.execute("delete from data where PRN=%s",(PRN.get(),))  ##Only one parameter is required from particular record to delete
        conn.commit()
        display()
        conn.close()
        messagebox.showinfo('Student Management System', 'Record has been Deleted Successfully !!!')


##### Search Record ###############

def search_rec():
    s1=SCH1.get()
    s2=SCH2.get()

    if s1 == "" or s2 == "":
        messagebox.showerror("Student Management System", "Please select option to search Record")

    else:
        conn = mysql.connector.connect(user='root', password='12345',
                                       host='localhost', database='sarthak',
                                       auth_plugin='mysql_native_password')
        cur = conn.cursor()
        cur.execute("SELECT * from data where " +str(SCH1.get())+" LIKE '%"+str(SCH2.get())+"%'")
        dis = cur.fetchall()

        if len(dis) != 0:
            tree.delete(*tree.get_children())
            for i in dis:
                tree.insert("", END, values=i)
            conn.commit()
        conn.close()




#########Show All ############

def show_all():
    conn = mysql.connector.connect(user='root', password='12345',
                                   host='localhost', database='sarthak',
                                   auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute("SELECT * from data")
    dis = cur.fetchall()

    if len(dis) != 0:
        tree.delete(*tree.get_children())
        for i in dis:
            tree.insert("", END, values=i)
        conn.commit()
    conn.close()


#######Buttons###############


add = Button(f3, text='Add', cursor='hand2', borderwidth=6, bg='blue',command=add, fg='white', font=('arial', 16)).place(x=0,y=1,height=40,width=100)  # Submit Button

delete = Button(f3, text='Delete', cursor='hand2', borderwidth=6,command=delete, bg='blue', fg='white',font=('arial', 16)).place(x=140, y=1, height=40, width=100)  # Exit Button

upd = Button(f3, text='Update', cursor='hand2', borderwidth=6, bg='blue',command=update_data,fg='white', font=('arial', 16)).place(x=280, y=1, height=40, width=100)

exit = Button(f3, text='Exit', cursor='hand2', borderwidth=6, bg='blue',command=root.destroy, fg='white',font=('arial', 16)).place(x=422, y=1, height=40, width=100)

show=Button(root,text='Show All',borderwidth=6, bg='blue',command=show_all, fg='white',font=('arial', 16),cursor='hand2')
show.place(x=1200,y=119,height=40,width=120)

################========================DATABASE FRAME==============================###############



#############____________________++++++++++++++++++++++@##################################

ser = Label(root, text="Search:", font=('Arial Rounded MT Bold', 20), bg='lightblue3',fg='black')
ser.place(x=580, y=119)

sch1 = ttk.Combobox(root,  state='readonly', font=('Arial', 15),textvariable=SCH1)
sch1['value'] = ('Name', 'Roll_No')
sch1.place(x=700, y=125, height=28, width=130)

sch2= Entry(root, font=('bold', 15), bd=2, relief=SOLID,textvariable=SCH2)
sch2.place(x=849, y=126, height=27, width=150)
        ##########__________________##########

sch=Button(root,text='Search',borderwidth=6, bg='blue', fg='white',command=search_rec,font=('arial', 16),cursor='hand2')
sch.place(x=1030,y=119,height=40,width=120)


###################################################################

f4 = Frame(root, bg='white', relief=RIDGE, bd=10.5)
f4.place(x=557, y=173, height=520, width=787)


ys = Scrollbar(root, orient=VERTICAL)

tree=ttk.Treeview(f4,columns=('Name','PRN','Roll No','DOB','Branch','Gender'), yscrollcommand=ys.set)
tree.pack(fill=BOTH,expand=TRUE)


ys.config(command=tree.yview)


ys.pack(side=RIGHT, fill=Y)

tree.heading('Name',text='Name')
tree.heading('PRN',text='PRN')
tree.heading('Roll No',text='Roll No')
tree.heading('DOB',text='D.O.B (MM/DD/YY)')
tree.heading('Branch',text='Branch')
tree.heading('Gender',text='Gender')

tree.column('Name',width=80)
tree.column('PRN',width=80)
tree.column('Roll No',width=80)
tree.column('DOB',width=80)
tree.column('Branch',width=100)
tree.column('Gender',width=70)


tree['show']='headings'

display()
tree.bind('<ButtonRelease-1>',select_data)   #####   EVENT ############

root.mainloop()
