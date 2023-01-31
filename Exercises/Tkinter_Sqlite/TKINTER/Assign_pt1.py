# Python 3.10.9
#
# Michael LaRocca
# 
# TKINTER Assignment 
# PT 1, 2    
# 
# 


from tkinter import * 

win = Tk()

b1 = Button(win, text="One")
b2 = Button(win, text="Two")

b1.pack()
b2.pack()

b1.pack(side=LEFT)
b2.pack(side=LEFT)

b1.pack(side=LEFT, padx = 10)
b2.pack(side=LEFT, padx = 10)

b3 = Button(win, text="Submit")
b3.pack(side=BOTTOM, padx = 10)

b4 = Button(win, text="CLOSE")
b4.pack(side=RIGHT, padx = 10)