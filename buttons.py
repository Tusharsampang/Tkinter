from tkinter import*
root = Tk()
# Button without  any function
myButton = Button(root, text="Click Me")
myButton.pack()

# State disabled button
myButton1 = Button(root, text="Click", state=DISABLED)
myButton1.pack()

#button x and padding

myButton2 = Button(root, text="Click", padx=20)
myButton2.pack()
myButton3 = Button(root, text="Click", padx=10,pady=15)
myButton3.pack()

root.mainloop()