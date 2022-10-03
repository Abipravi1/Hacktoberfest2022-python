#Name:Ashish Ramesh
#Github ID : AshishRamesh

from tkinter import *

window= Tk(className='Database_GUI')

L1=Label(window,text='Title')
L1.grid(row=0,column=0)
L2=Label(window,text='Name')
L2.grid(row=0,column=2)
L3=Label(window,text='Year')
L3.grid(row=1,column=0)
L4=Label(window,text='Phone No.')
L4.grid(row=1,column=2)

title_val = StringVar()
E1=Entry(window,textvariable=title_val)
Author_val = StringVar()
E1.grid(row=0,column=1)
E2=Entry(window,textvariable=Author_val)
E2.grid(row=0,column=3)
year_val = StringVar()
E3=Entry(window,textvariable=year_val)
E3.grid(row=1,column=1)
ISBN_val=StringVar()
E4=Entry(window,textvariable=ISBN_val)
E4.grid(row=1,column=3)

T1= Text(window,height=10,width=15)
T1.grid(row=2,column=1,rowspan=5)

B1=Button(window,text='View All',width=12)
B1.grid(row=2,column=3)
B2=Button(window,text='Search Entry',width=12)
B2.grid(row=3,column=3)
B3=Button(window,text='Add Entry',width=12)
B3.grid(row=4,column=3)
B4=Button(window,text='Update Selected',width=12)
B4.grid(row=5,column=3)
B5=Button(window,text='Delete Selected',width=12)
B5.grid(row=6,column=3)
B6=Button(window,text='Close',width=12)
B6.grid(row=7,column=3)

window.mainloop()