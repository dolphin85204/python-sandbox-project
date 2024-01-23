# This is direct from the "Hello World" tutorial at https://docs.python.org/3/library/tkinter.html#a-hello-world-program
# experiment with changing values to see behavior

from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

ttk.Label(frame, text="Hello World").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()

