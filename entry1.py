from tkinter import *
root = Tk()

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
def button_click(number):
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current)+ str(number))
root.mainloop()
