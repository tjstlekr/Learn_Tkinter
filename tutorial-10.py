from Tkinter import *

#Creating the toolbar
def ahi():
    print("ahi")

root = Tk()
toolbar = Frame(root,bg="blue")
button_1 = Button(toolbar,text="Insert Img",command=ahi)
button_1.pack(side=LEFT,padx=2,pady=2)
printbut = Button(toolbar,text="print ahi",command=ahi)
printbut.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)


root.mainloop()