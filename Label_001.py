from Tkinter import *

root = Tk() #creates a window in which we work our gui

label_1 = Label(root,text="Hello World!!",bg="red",fg="yellow") #enters a text in the window bg
label_1.pack(fill=X) #.pack is allows  the widget to see in the window else/also for positioning our widgets

root.mainloop()#its like a return 0 in c Holds the window