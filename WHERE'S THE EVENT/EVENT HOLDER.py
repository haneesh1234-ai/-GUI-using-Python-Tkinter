from tkinter import *

screen = Tk()
screen.geometry("1222x10200")
screen.title("Event Handler")

def buttonClick():
    print("\n Button is clicked")

button = Button(text="click me", fg="black", bg="pink", command=buttonClick)
button.pack()

def keyPressed(event):
    print(event.char)

screen.bind("<Key>", keyPressed)

screen.mainloop()