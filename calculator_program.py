from tkinter import *
import tkinter as tk
window=tk.Tk()                                               
window.geometry('300x260')
window.resizable(width = False, height = False)
window.title("Calculator")
entry=Entry(window, bg="white", width=32, font=("Times 13"),justify=RIGHT)               
entry.place(x=5, y=25)
entry.pack()
entry.grid(row=0,column = 0,columnspan = 5, stick = 'we')
def root():
    clear()
    rooted_result = result**0.5
    entry.insert(0,rooted_result)
def no_operator_value(value):
    array = list(value)
    x = 0
    for i in range(0,len(array)):
        if array[x] == '+' or array[x] == '-' or array[x] == '/' or array[x] == '*' or array[x] == 'r' or array[x] == '√':
            del array[x]
        elif array[x] == '**':
            del array[x]
            del array[x+1]           
        else:
            x+=1          
    s = [str(integer) for integer in array]
    a_string = "".join(s)
    res = float(a_string)
    return res
def calculate():
    global result
    clear()
    result = eval(value)
    if type(result) == int:
        int(result)
    elif type(result) == float:
        float(result)  
    total_value = str(result)
    entry.insert(0,total_value)
def rounding():
    clear()
    no_operator = no_operator_value(value)
    floated_value = float(no_operator)
    rounded_value = round(floated_value, 2)
    rounded_value_string = str(rounded_value)
    entry.insert(0,rounded_value_string)
def add_digit(name):
    global value
    value = entry.get() + str(name)
    clear()
    entry.insert(0, value) 
def get_number(name):
    if name != '=' and name != 'r' and name != '√' and name != 'C':
        add_digit(name)
    elif name == '=':
        calculate()
    elif name == '√':
        root()    
    if name == 'C':
        clear()
    if name == 'r':
        rounding()
def clear():
    entry.delete(0,END)
class button:
    def __init__(self,name,row1,column1):
        btn0 = Button(window,text = str(name),bd = 5,highlightbackground='black', activebackground="white", command = lambda:get_number(name)).grid(row = row1, column = column1, stick = 'wens',padx = 5,pady = 5)
button('0', 4, 0)
button('1', 1, 0)
button('2', 1, 1)
button('3', 1, 2)
button('4', 2, 0)
button('5', 2, 1)
button('6', 2, 2)
button('7', 3, 0)
button('8', 3, 1)
button('9', 3, 2)
button('=',4,1)
button('.',4,2)
button('/',4,3)
button('*',3,3)
button('-',2,3)
button('+',1,3)
button('C',1,4)
button('√',2,4)
button('**',3,4)
button('r',4,4)
window.grid_columnconfigure(0,minsize = 60)
window.grid_columnconfigure(1,minsize = 60)
window.grid_columnconfigure(2,minsize = 60)
window.grid_columnconfigure(3,minsize = 60)
window.grid_rowconfigure(1,minsize = 60)
window.grid_rowconfigure(2,minsize = 60)
window.grid_rowconfigure(3,minsize = 60)
window.grid_rowconfigure(4,minsize = 60)
window.mainloop()