from Tkinter import *

''''' We have seen how to bind a function to gui(widget).
There's another method in which a function is called when a certain event is performe as programmed.
An event can be by keystrokes/doin normal click etc...'''''
root = Tk()

def printName(event):
    print("Hey people, My name is Tejas")

button1 = Button(root,text="Show me your name!")
button1.bind("button-1",printName)      #what event are u waiting for occur and what function is called when event occured is specified in the bind()
button1.pack()                          #here <button-1> is the event for left click event



root.mainloop()