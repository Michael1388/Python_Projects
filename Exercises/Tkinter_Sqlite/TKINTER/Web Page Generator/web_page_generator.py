# Python 3.10.9
#
# Michael LaRocca
# 
# Python Course
# Web Page Generator Project Assignment   
# Step 314
# 
# Scope:  
# Create a tool that can automatically create a basic HTML web page.
# The page is very simple - it will just have the text "Stay tuned for 
# our amazing summer sale!".
# Your task is to create a Tkinter GUI and Python script that will 
# automatically create the .html file needed.
# Add: 
# 1.	Creates a GUI that allows the user to input text and initiate the 
# web page generation process.
# 2.	Generates a web page that sets the user’s input as the body text 
# for the web page.
# 3.	Opens the generated web page in a new tab in the browser.


import tkinter as tk
from tkinter import * 
import webbrowser
from tkinter import ttk # import

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        # define our master frame configuration
        self.master = master
        self.master.minsize(200,200) # (Height, Width pixels)
        self.master.maxsize()
        # Set title of GUI window
        self.master.title("Web Page Generator")

        # Default HTML Page button and command to make it run when clicked on
        self.default_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.default_btn.grid(padx=(10, 10), pady=(10, 10))

         # Submit Custom Text button and command to make it run when clicked on
        self.submit_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.submit_btn.grid(padx=(10, 10), pady=(10, 10))

         # Creates entry for Submit Custom Text
        self.submit_entry = Entry(width=155 )
        # Positions entry in GUI using tkinter grid() padx and pady are the same as
        # the button to ensure they will line up
        self.submit_entry.grid(row=1, column=1, rowspan=2, columnspan=2, padx=(20, 10), pady=(30, 0))
    
         # Define Labels
        self.lbl_default = tk.Label(self.master,text='Click for Default HTML page:')  
        self.lbl_default.grid(row=0,column=1,padx=(27,0),pady=(10,0),sticky=N+W)
       
        self.lbl_submit = tk.Label(self.master,text='Enter CUSTOM TEXT below and click "Submit Custom Text" Button:') 
        self.lbl_submit.grid(row=1,column=1,padx=(27,0),pady=(10,0),sticky=N+W)

    # create html document
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent) # pass 'htmlContent' into write function
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
    
    # create Custom html document and define a function to ".get " the Entry data
    def customHTML(self):
        print(self.submit_entry.get())
        htmlText = self.submit_entry.get()
        htmlFile = open("index1.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent) # pass 'htmlContent' into write function
        htmlFile.close()
        webbrowser.open_new_tab("index1.html") 
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


    