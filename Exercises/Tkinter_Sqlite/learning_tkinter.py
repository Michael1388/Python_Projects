# Python 3.10.9
#
# Michael LaRocca
# 
# TKINTER VIDEOS    
# Steps 251, 253, 255, 257, 259
# 

import tkinter
from tkinter import * 

# these first top three lines are fundamental, you will be using this 'template' 
# often, it's good to just copy and paste until you completely understand 
# its' purposes and uses.

class ParentWindow(Frame):          #1
    def __init__ (self, master):    #2
        Frame.__init__ (self)       #3           

        self.master = master   # the primary window that will pop-up on screen
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

        self.varFName = StringVar() # always use self
        self.varLName = StringVar()

        self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgrey')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgrey')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgrey')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0)) 
        
        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue') 
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0)) # always follow your use of self.
        
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
        
    def cancel(self):
        self.master.destroy()


# get used to this below as well 

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() # this keep the window open, if we did not have this, the 
                    # widow would automatically close, we will call a close 
                    #  when we need it to close.