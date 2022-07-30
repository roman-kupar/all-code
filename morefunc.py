import tkinter as tk
window=tk.Tk()
test_file = open('c:\\Users\\Roma\\test.txt')
a = (test_file.read())
b = tk.Label(text = str(a), width=320,
    height=320)
b.pack()
window.mainloop()
