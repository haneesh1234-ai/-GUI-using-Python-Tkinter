from tkinter import *


root = Tk()
root.title('Number Pad')
root.geometry('300x300')

frame = Frame(master=root, height=50, width=50, bg="#55c4fb", relief=RIDGE, borderwidth=5)
frame.pack()

root.mainloop()