from Tkinter import *


root = Tk()

def printName():
    print("Hey people, My name is Tejas")

button1 = Button(root,text="Show me your name!",command=printName)  #Command=printName calls the function printName
                                                                    #This is binding the function to widget!!
button1.pack()



root.mainloop()