from tkinter import *

# creating the application main window
root = Tk()

#creating a button widgett
redbutton = Button(root, text = "LEFT" ,fg = "green")
#shoving it onto the sreen
redbutton.pack( side = LEFT)

greenbutton = Button(root, text = "RIGHT", fg = "black")
greenbutton.pack( side = RIGHT)
bluebutton = Button(root, text = "TOP" , fg ="blue")
bluebutton.pack( side = TOP)
blackbutton = Button(root, text = "BOTTOM" , fg = "red")
blackbutton.pack( side = BOTTOM)

root.mainloop()