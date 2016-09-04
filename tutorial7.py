from Tkinter import *
# Let's bind multiple Functions to single widget
root = Tk()


def leftClick(self,event):
    print("Left Click Captured")


def middleClick(self,event):
    print("right")


def rightClick(self,event):
    print ("right click captured")


frame = Frame(root, width=300, height=300)
frame.bind("<button-1>",'',leftClick)
frame.bind("<button-2>",'',middleClick)
frame.bind("<button-3>",'',rightClick)           #'' is there just so that binding doesnt get replaced by next bind()
frame.pack()

root.mainloop()
