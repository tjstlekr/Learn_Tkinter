from Tkinter import *




class Ahi:

    def __init__(self, master):  # this function doesnt needs to be called explicitly
        self.printmessage = []      #for people using python 3.x version u dont need to add this line

        frame = Frame(master)
        frame.pack()


        self.printButton = Button(frame, text="Print- Message", command=self.printmessage)
        self.printButton.pack(side=LEFT)


        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)


root = Tk()
a = Ahi(root)
root.mainloop()
