from Tkinter import *

root = Tk()
#grid configures the widget in a tabular format


label = Label(root,text="Name")
label2 = Label(root,text="Password")
entry_1 =Entry(root)    #textbox
entry_2 = Entry(root)

label.grid(row=0,sticky=E)
label2.grid(row=1,sticky=E)         #sticky is used for alligning the labels in East direction :D
                                    #perform the program without using sticky argument

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)        #row and column in grid

c = Checkbutton(root,text="Keep me logged in")
c.grid(columnspan=2)                                #Using columnspan we have allocated two column space for checkbutton
root.mainloop()