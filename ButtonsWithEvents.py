from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root, text="Yamete OniSan!!")
    myLabel.pack()

myButton=Button(root, text="Click Me!", command=myClick)
myButton.pack()

root.mainloop()