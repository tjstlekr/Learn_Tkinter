from Tkinter import *
from tkFileDialog   import askopenfilename

def NewFile():
    print "New File!"
def OpenFile():
    name = askopenfilename()
    print name
def About():
    print "This is a simple example of a menu"

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu,tearoff=0)                 #try script without using tearoff to match the diff
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)



helpmenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)



#Creating the toolbar
def ahi():
    print("ahi")


toolbar = Frame(root,bg="blue")
button_1 = Button(toolbar,text="Insert Img",command=ahi)
button_1.pack(side=LEFT,padx=2,pady=2)
printbut = Button(toolbar,text="print ahi",command=ahi)
printbut.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)




mainloop()
