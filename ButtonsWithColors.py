from tkinter import *
root = Tk()
def myClick():
    myLabel= Label(root, text="Button is Clicked!!")
    myLabel.pack()
myButton= Button(root, text="CLICK", command= myClick, fg="black", bg="white")
myButton.pack()

root.mainloop()