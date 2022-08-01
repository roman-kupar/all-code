from tkinter import *
import tkinter as tk
import tkinter as tkk
window=tk.Tk()                                               
window.geometry('200x250')
window.resizable(width = False, height = False)
window.title("Calculator")
entry=Entry(window, bg="white", width=20, font="Times 13")               
entry.place(x=5, y=25)
entry.configure(state=tk.DISABLED)
entry.pack()
class button:
    def __init__(self,name,coord_x,coord_y):
        btn0 = Button(window,text = str(name),height = 3, width = 3, command = button_action)
        btn0.place(x=int(coord_x), y=int(coord_y))
        global number
        number = int(name)
class button_operator:
    def __init__(self,name,coord_x,coord_y):
        btn0 = Button(window,text = str(name),height = 3, width = 3, command = button_action)
        btn0.place(x=int(coord_x), y=int(coord_y))
def button_action():
    print (number)        
button_operator('=',60,200)
button_operator(',',30,200)
button('0', 0, 200)
button('1', 0, 150)
button('2', 30, 150)
button('3', 60, 150)
button('4', 0, 100)
button('5', 30, 100)
button('6', 60, 100)
button('7', 0, 50)
button('8', 30, 50)
button('9', 60, 50)
button_operator('÷',90,200)
button_operator('x',90,150)
button_operator('-',90,100)
button_operator('+',90,50)
button_operator('C',120,50)
window.mainloop()