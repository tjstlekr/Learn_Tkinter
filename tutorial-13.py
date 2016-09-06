from Tkinter import *

root = Tk()


canvas = Canvas(root,width=200,height=100)          #We need something to draw things on which cant be root
canvas.pack()                                       #so we specify canvas

blackline = canvas.create_line(0,0,200,50)           #creating a line using canvas

redline = canvas.create_line(0,100,200,50,fill="red")


bluebox =    canvas.create_rectangle(25,25,130,60,fill ="blue")         #(coordinatex,coordinatey,width,height)


canvas.delete(redline)                      #perform using this two delete function
canvas.delete(ALL)
root.mainloop()