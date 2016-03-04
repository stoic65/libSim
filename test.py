from tkinter import *
import tkinter.font as tkFont 
import pickle
import os.path
import time
import hashlib
from PIL import ImageTk,Image

root = Tk()
root.title("Test page")

def func(frm):
	frm.destroy()

frm = Frame(root)
frm.pack()
b1 = Button(frm,text = "Enter",bg = "blue",fg = "white",command = lambda:func(frm))

b2 = Button(frm,text = "Ok",bg = "blue",fg = "white",command = lambda:func(frm))

b1.grid(row = 0,column = 0,padx = 20,pady = 20)

b2.grid(row = 0,column = 1,padx = 20,pady = 20)







root.mainloop()