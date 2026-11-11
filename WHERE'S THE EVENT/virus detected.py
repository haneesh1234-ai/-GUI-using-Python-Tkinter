from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def buttonClick():
    messagebox.showwarning("warning", "Stop! Virus Found.", icon="info")

button = Button(root, text="Scan for Virus", command=buttonClick)
button.place(x=50, y=80)

root.mainloop()
