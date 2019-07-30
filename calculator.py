# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:52:15 2019

@author: USER
"""

import tkinter as tk
from tkinter import messagebox

mainWindow = tk.Tk()
mainWindow.title("Calculator")

heading_label = tk.Label(mainWindow,text="First number")
heading_label.pack()

name_field = tk.Entry(mainWindow)
name_field.pack()

heading_label2 = tk.Label(mainWindow,text="Second number")
heading_label2.pack()

name_field2 = tk.Entry(mainWindow)
name_field2.pack()


def takeValueInputplus():
    name , name2 = takeValueInput()
    s = name+name2
    result_label.config(text="Operations result is: " +str(s))


def takeValueInputminus():
    name , name2 = takeValueInput()
    s = name-name2
    result_label.config(text="Operations result is: "+ str(s))
    
def takeValueInputmul():
    name , name2 = takeValueInput()
    s = name*name2
    result_label.config(text="Operations result is: " +str(s))
    
def takeValueInputdivide():
    name , name2 = takeValueInput()
    if (name2 == 0):
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result = name / name2
        # print(first + second)
        result = round(result, 2)
        result_label.config(text="Operations result is: " +
                                 str(result))

def takeValueInput():
    first = name_field.get()
    second = name_field2.get()
    
    
    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(name_field.get()) == 0) or (len(name_field2.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)
    
    
    
    
button = tk.Button(mainWindow,text="+",fg="red",command = lambda:takeValueInputplus())
button.pack()
button = tk.Button(mainWindow,text="-",fg='blue',command = lambda:takeValueInputminus())
button.pack()

button = tk.Button(mainWindow,text="*",fg='purple',command = lambda:takeValueInputmul())
button.pack()

button = tk.Button(mainWindow,text="/",fg='green',command = lambda:takeValueInputdivide())
button.pack()

result_label = tk.Label(mainWindow, text="Operations result is:")
result_label.pack()




mainWindow.mainloop()