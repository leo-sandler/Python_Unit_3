from tkinter import *
# This gives us all functionality from the Tkinter class

root = Tk()
# This is a class from Tkinter, which is blank creating a blank window
label_1 = Label(root, text="First Tkinter window")
# Labels are the same as text
# The first parameter is where it is displayed and then text.
label_1.pack()
# This places the label in the first possible place.
root.mainloop()
# This allows for the computer to display this for ever until it is ended
