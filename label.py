from tkinter import *
root = Tk()

#creating a label widget
myLabel1 = Label(root, text="Tkinter Program Beginning :")
myLabel2= Label(root, text="I am Mr Sampang")
myLabel3 = Label(root, text="This World shall know pain")

#Shoving it onto the sreen based upon x-axis and y-axis
#that does not move having a constant position
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=6)
myLabel3.grid(row=1, column= 1)

root.mainloop()