from tkinter import *
from tkinter import ttk


screen = Tk()
screen.geometry("1000x1000")
screen.title("Formulare")

a = Label(screen ,text = "First Name").grid(row = 0,column = 0)
a1 = Entry(screen).grid(row = 0,column = 1)
a = 1
screen.mainloop()