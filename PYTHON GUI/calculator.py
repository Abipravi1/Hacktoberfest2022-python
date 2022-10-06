from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Calculator")

title = Label(root, text="Calculator", fg="purple",  font=("serif", 30))

def add():
    x = float(input_one.get())
    y = float(input_two.get())
    result["text"] = x+y

def subtract():
    x = float(input_one.get())
    y = float(input_two.get())
    result["text"] = x-y

def divide():
    x = float(input_one.get())
    y = float(input_two.get())
    result["text"] = x/y

def multiply():
    x = float(input_one.get())
    y = float(input_two.get())
    result["text"] = x*y

text_one = Label(root, text="The first number", width=20, bd=10, font=("serif", 20), bg="purple", fg="white")
input_one = Entry(root, width=30, bg="purple", fg="white", font=("serif", 20), bd=10)
text_two = Label(root, text="The second number", width=20, bd=10, font=("serif", 20), bg="purple", fg="white")
input_two = Entry(root, width=30, bg="purple", fg="white", font=("serif", 20), bd=10)

result = Label(root, text="Result", width=20, bd=10, font=("serif", 20), bg="brown", fg="white")

add = Button(root, text="Add", width=15, height=3, bd=25, bg="pink", font=("serif", 28), relief=SUNKEN, command=add)
subtract = Button(root, text="Subtract", width=15, height=3, bd=25, bg="pink", font=("serif", 28), relief=RAISED, command=subtract)
divide = Button(root, text="Divide", width=15, height=3, bd=25, bg="pink", font=("serif", 28), relief=GROOVE, command=divide)
multiply = Button(root, text="Multiply", width=15, height=3, bd=25, bg="pink", font=("serif", 28), relief=RIDGE, command=multiply)



title.grid(column=1)

text_one.grid(row=1, column=0)
input_one.grid(row=1, column=1)

text_two.grid(row=2, column=0)
input_two.grid(row=2, column=1)

result.grid(row=3,column=1)

add.grid(row=4, column=0)
subtract.grid(row=4, column=1)
divide.grid(row=5, column=0)
multiply.grid(row=5, column=1)

root.mainloop()