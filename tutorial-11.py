from Tkinter import *

#when you hover over some buttons you can see what do they do in status bar maybe. just help text ..
# following program can guide you to make status bar!
root = Tk()


status = Label(root,text = "status bar completed", relief = SUNKEN, anchor = W)
status.pack(side=BOTTOM,fill = X)

root.mainloop()