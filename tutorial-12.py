from Tkinter import *
import tkMessageBox  #for python 3.x version import tkinter.messagebox


root = Tk()
tkMessageBox.showinfo('Window Title',"Gangadhar hi shaktiman hain!")        #for python 3.x use tkinter.messagebox.showinfo()

answer = tkMessageBox.askquestion('IQ Test',"If I told you that yes means no and no means yes, what would you say if I asked you if you wanted me to hit you?")

if answer == 'yes':
    print"Slap!"

root.mainloop()