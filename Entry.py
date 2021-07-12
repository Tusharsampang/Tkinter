from tkinter import *

root = Tk()

e1 = Entry(root, width=50, fg="black", bg="white", borderwidth=5)
e1.pack()


def myClick():
    textoutput = "Hello " + e1.get()
    myLabel = Label(root, text=textoutput)
    myLabel.pack()
    myButton1 = Button(root, text="Click")
    myButton1.pack()

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()

root.mainloop()
