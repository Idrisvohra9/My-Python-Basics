from tkinter import *

# window create karne ke liye
w = Tk()

# window ki size
w.geometry("500x500")

# To create button
# b1 = Button(w, text="Button", activebackground="yellow", activeforeground="red")

# to set button
# b1.place(x=0, y=250)

l1=Label(text="First ")
l2=Label(text="Second")

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

w.mainloop()