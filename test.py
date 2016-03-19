
from tkinter import *
import tkinter.font as tkFont 
import pickle
import os.path
import time
import hashlib
from PIL import ImageTk,Image
from datetime import date

root = Tk()

img= ImageTk.PhotoImage(Image.open("icons/more.gif"))
	
b = Button(root,image = img,height = 24,width = 24)
b.grid(row = 2,column = 1,sticky = E,padx = 5)



root.mainloop()