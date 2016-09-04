from Tkinter import *

root = Tk()
one = Label(root,text="ahi",bg="red",fg="yellow")
one.pack()
two = Label(root,text="two",bg="green",fg="white")


#compare the output OF label one and other two labels :fill=X parameter
two.pack(fill=X)
three = Label(root,text="three",bg="magenta",fg="brown")
three.pack(side=LEFT,fill=Y)

root.mainloop()