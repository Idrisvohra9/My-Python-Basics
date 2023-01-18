<<<<<<< HEAD
# To import the entire library and all the things in it:
from tkinter import *

def Main():
    # Initialize the window object:
    w = Tk()

    # To set the window size:
    # The parameter is in string and in the format of widthxheight
    w.geometry("500x500")

    # Set the title of the window:
    w.title("Testing")

    # The function if called will destroy the window:

    def CreateWindow():
        Main()
    def DestroyWindow():
        w.destroy()

    # A button object with properties:
    CWBtn = Button(
        w,
        text="Create Window",
        command=CreateWindow,
        activeforeground="Blue",
        activebackground="darkgreen",
        background= "Green",
        borderwidth=2,
        width=10,
        height=10,
    )

    DesBtn = Button(
        w,
        text="Destroy Window",
        command=DestroyWindow,
        activeforeground="Blue",
        activebackground="darkgreen",
        background= "Green",
        borderwidth=2,
        width=10,
        height=10,
    )
    # Placing the button in x and y coordinates:
    CWBtn.place(relx=0.3,rely=0.3)
    DesBtn.place(relx=0.6,rely=0.3)
    # We need a mainloop to keep the tkinter window running.
    w.mainloop()

Main()
=======
def give(n):
    n+10
    raise ValueError

print(give(10))
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
