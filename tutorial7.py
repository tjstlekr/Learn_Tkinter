from Tkinter import *
# Let's bind multiple Functions to single widget
root = Tk()


def leftclick(event):


    print"Left Click Captured"


def rightclick(event):
    print "right click captured"


def middleclick(event):
    print"right"


frame = Frame(root, width=300, height=300)

frame.bind("<button-1>",leftclick)
frame.bind("<button-2>",middleclick)
frame.bind("<button-3>",rightclick)
frame.pack()

root.mainloop()
