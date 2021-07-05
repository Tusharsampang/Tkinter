from tkinter import *

top = Tk()
top.geometry("500x300")

name = Label(top, text = "Username :").place(x=50,y=70)
address= Label(top, text= "Address :").place(x=50,y=90)
email= Label(top, text= "Email :").place(x=50,y=130)
contact= Label(top, text= "Contact :").place(x= 50, y=150)
e1= Entry(top).place(x=115,y=70)
e2=Entry(top).place(x=105,y=90)
e3= Entry(top).place(x=90,y=130)
e4= Entry(top).place(x=105,y=150)

top.mainloop()