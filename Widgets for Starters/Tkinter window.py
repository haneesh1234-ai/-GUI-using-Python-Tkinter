from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Test window")

label1 = Label(text="Welcome !!!", fg="black", bg="pink", height=1, width=200)

label1.pack()

label2 = Label(text="Enter your name below : ", fg="black", bg="yellow", height=1, width=100)

label2.pack()

name = Entry()

name.pack()

text = Text(height=5)

text.pack()

def display():

    n = name.get()

    message1 = "Hello " + n + "\n"

    text.insert(END, message1)

    message2 = "Welcome to the Application"

    text.insert(END, message2)

button = Button(text="Click Me", fg="white", bg="blue", command = display)

button.pack()


window.mainloop()
