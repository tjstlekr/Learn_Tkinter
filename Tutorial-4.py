from Tkinter import *

root = Tk()
#grid configures the widget in a tabular format


label = Label(root,text="Name")
label2 = Label(root,text="Password")
entry_1 =Entry(root)    #textbox
entry_2 = Entry(root)

label.grid(row=0)
label2.grid(row=1)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)        #row and column in grid


root.mainloop()