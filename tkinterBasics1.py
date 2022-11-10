# To import the entire library and all the things in it:
from tkinter import *

# Initialize the window object:
w = Tk()

# To set the window size:
# The parameter is in string and in the format of widthxheight
w.geometry("1000x1000")

# Set the title of the window:
w.title("Testing")

# The function if called will destroy the window:
def DestroyWindow():
    w.__init__()

# A button object with properties:
Btn = Button(
    w,
    text="Red Button",
    command=DestroyWindow,
    activeforeground="red",
    activebackground="maroon",
    background= "RED",
    borderwidth=0,
    width=10,
    height=10
    )

# Placing the button in x and y coordinates:
Btn.place(x=500,y=300)
# We need a mainloop to keep the tkinter window running.
w.mainloop()