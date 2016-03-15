
from tkinter import *
import tkinter.font as tkFont 
import pickle
import os.path
import time
import hashlib
from PIL import ImageTk,Image
from datetime import date


backgroundColour = "#204060"
buttonColour = "#990000"
staffFile = "staffDb"
studentFile = "studentDb"
booksFile = "booksDb"
staffMasterObject = {}
studentMasterObject = {}
booksMasterObject = {}
studentMaxBookCount = 5
textLight = "white"
currentPerson = {}
textMainView = "#ffe6cc"
innerFrameColour = "#1a0d00"

monthList  = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

if os.path.exists(staffFile):
	f = open(staffFile,"rb")
	staffMasterObject = pickle.load(f)
	f.close()


if os.path.exists(studentFile):
	f = open(studentFile,"rb")
	studentMasterObject = pickle.load(f)
	f.close()


if os.path.exists(booksFile):
	f = open(booksFile,"rb")
	booksMasterObject = pickle.load(f)
	f.close()



def isEmptyChecker(*args):
	for item in args:
		if item is "":
			return True
	return False

def passwordMatch(userId,password,masterObject):
	p = hashlib.md5()
	p.update(password.encode())
	if p.digest() == masterObject[userId]["password"]:
		return True
	else:
		return False


def loadShelfView(personObject):

	def callback(event):
		personObject.bookClick(event.widget.item)
		
	#Classical books 
	classic_counter = 0
	classic_array = {}
	for item in booksMasterObject:
		if booksMasterObject[item]["genre"] == "Classic":
			img= ImageTk.PhotoImage(Image.open(booksMasterObject[item]["coverImagePath"]))
			a = classic_counter
			classic_array[classic_counter] = Button(personObject.currentView.classicFrame,image = img,height = 70,width = 60)
			classic_array[classic_counter].grid(row = 1,column = classic_counter,sticky = W,padx = 5)
			classic_array[classic_counter].image = img
			classic_array[classic_counter].item = item
			classic_array[classic_counter].bind("<Button-1>",callback)
			if booksMasterObject[item]["isIssued"] == True:
				classic_array[classic_counter].configure(state = "disable")
			classic_counter+=1
			if classic_counter==8:
				break


	mystery_counter = 0
	mystery_array = {}
	for item in booksMasterObject:
		if booksMasterObject[item]["genre"] == "Mystery":
			img= ImageTk.PhotoImage(Image.open(booksMasterObject[item]["coverImagePath"]))
			mystery_array[mystery_counter] = Button(personObject.currentView.mysteryFrame,image = img,height = 70,width = 60)
			mystery_array[mystery_counter].grid(row = 1,column = mystery_counter,sticky = W,padx = 10)
			mystery_array[mystery_counter].image = img
			mystery_array[mystery_counter].item = item
			mystery_array[mystery_counter].bind("<Button-1>",callback)
			if booksMasterObject[item]["isIssued"] == True:
				mystery_array[mystery_counter].configure(state = "disable")			
			mystery_counter+=1
			if mystery_counter==8:
				break

	scifi_counter = 0
	scifi_array = {}
	for item in booksMasterObject:
		if booksMasterObject[item]["genre"] == "Scifi":
			img= ImageTk.PhotoImage(Image.open(booksMasterObject[item]["coverImagePath"]))
			scifi_array[scifi_counter] = Button(personObject.currentView.scifiFrame,image = img,height = 70,width = 60)
			scifi_array[scifi_counter].grid(row = 1,column = scifi_counter,sticky = W,padx = 10)
			scifi_array[scifi_counter].image = img
			scifi_array[scifi_counter].item = item
			scifi_array[scifi_counter].bind("<Button-1>",callback)
			if booksMasterObject[item]["isIssued"] == True:
				scifi_array[scifi_counter].configure(state = "disable")
			
			scifi_counter+=1
			if scifi_counter==8:
				break

	comedy_counter = 0
	comedy_array = {}
	for item in booksMasterObject:
		if booksMasterObject[item]["genre"] == "Comedy":
			img= ImageTk.PhotoImage(Image.open(booksMasterObject[item]["coverImagePath"]))
			comedy_array[comedy_counter] = Button(personObject.currentView.comedyFrame,image = img,height = 70,width = 60)
			comedy_array[comedy_counter].grid(row = 1,column = comedy_counter,sticky = W,padx = 10)
			comedy_array[comedy_counter].image = img
			comedy_array[comedy_counter].item = item
			comedy_array[comedy_counter].bind("<Button-1>",callback)
			if booksMasterObject[item]["isIssued"] == True:
				comedy_array[comedy_counter].configure(state = "disable")
			comedy_counter+=1
			if comedy_counter==8:
				break

	horror_counter = 0
	horror_array = {}
	for item in booksMasterObject:
		if booksMasterObject[item]["genre"] == "Horror":
			img= ImageTk.PhotoImage(Image.open(booksMasterObject[item]["coverImagePath"]))
			horror_array[horror_counter] = Button(personObject.currentView.horrorFrame,image = img,height = 70,width = 60)
			horror_array[horror_counter].grid(row = 1,column = horror_counter,sticky = W,padx = 10)
			horror_array[horror_counter].image = img
			horror_array[horror_counter].item = item
			horror_array[horror_counter].bind("<Button-1>",callback)
			if booksMasterObject[item]["isIssued"] == True:
				horror_array[horror_counter].configure(state = "disable")
			horror_counter+=1
			if horror_counter==8:
				break

	nonFiction_counter = 0
	nonFiction_array = {}
	for item in booksMasterObject:
		if booksMasterObject[item]["genre"] == "Non Fiction":
			img= ImageTk.PhotoImage(Image.open(booksMasterObject[item]["coverImagePath"]))
			#personObject.currentView.nonFictionFrame.grid_propagate(False)
			#personObject.currentView.nonFictionFrame.grid_columnconfigure(nonFiction_counter,weight = 1)
			nonFiction_array[nonFiction_counter] = Button(personObject.currentView.nonFictionFrame,image = img,height = 70,width = 60)
			nonFiction_array[nonFiction_counter].grid(row = 1,column = nonFiction_counter,sticky = W,padx = 10)
			nonFiction_array[nonFiction_counter].image = img
			nonFiction_array[nonFiction_counter].item = img
			nonFiction_array[nonFiction_counter].bind("<Button-1>",callback)
			if booksMasterObject[item]["isIssued"] == True:
				nonFiction_array[nonFiction_counter].configure(state = "disable")
			nonFiction_counter+=1
			if nonFiction_counter==8:
				break


	textBook_counter = 0
	textBook_array = {}
	for item in booksMasterObject:
		if booksMasterObject[item]["genre"] == "Textbook":
			img= ImageTk.PhotoImage(Image.open(booksMasterObject[item]["coverImagePath"]))
			#personObject.currentView.textBookFrame.grid_propagate(False)
			#personObject.currentView.textBookFrame.grid_columnconfigure(textBook_counter,weight = 1)
			textBook_array[textBook_counter] = Button(personObject.currentView.textBookFrame,image = img,height = 70,width = 60)
			textBook_array[textBook_counter].grid(row = 1,column = textBook_counter,sticky = W,padx = 10)
			textBook_array[textBook_counter].image = img
			textBook_array[textBook_counter].item = item
			textBook_array[textBook_counter].bind("<Button-1>",callback)
			if booksMasterObject[item]["isIssued"] == True:
				textBook_array[textBook_counter].configure(state = "disable")
			
			textBook_counter+=1
			if textBook_counter==8:
				break

	magazines_counter = 0
	magazines_array = {}
	for item in booksMasterObject:
		if booksMasterObject[item]["genre"] == "magazines":
			img= ImageTk.PhotoImage(Image.open(booksMasterObject[item]["coverImagePath"]))
			#personObject.currentView.magazinesFrame.grid_propagate(False)
			#personObject.currentView.magazinesFrame.grid_columnconfigure(magazines_counter,weight = 1)
			magazines_array[magazines_counter] = Button(personObject.currentView.magazinesFrame,image = img,height = 70,width = 60)
			magazines_array[magazines_counter].grid(row = 1,column = magazines_counter,sticky = W,padx = 10)
			magazines_array[magazines_counter].image = img
			magazines_array[magazines_counter].item = item
			magazines_array[magazines_counter].bind("<Button-1>",callback)
			if booksMasterObject[item]["isIssued"] == True:
				magazines_array[magazines_counter].configure(state = "disable")
			magazines_counter+=1
			if magazines_counter==8:
				break





def loadIssuedBooks(personObject):
	
	def callback(event):
		personObject.issuedBookClick(event.widget.item)
	
	personObject.myIssuedBooksInnerView = Label(personObject.currentView.myIssuedBooksView,bg = backgroundColour)
	personObject.myIssuedBooksInnerView.pack(fill = BOTH,expand = YES)
	counter_row1 = 0
	counter_row2 = 0
	books_counter = 0
	issued_books_array = {}
	for item in personObject.personDetailsObject["issuedBooks"]:
		img= ImageTk.PhotoImage(Image.open(booksMasterObject[item]["coverImagePath"]))
		issued_books_array[books_counter] = Button(personObject.myIssuedBooksInnerView,image = img,height = 70,width = 60)
		issued_books_array[books_counter].image = img
		issued_books_array[books_counter].item = item
		issued_books_array[books_counter].bind("<Button-1>",callback)
		
		#pack
		if(counter_row1>=2):
			issued_books_array[books_counter].grid(sticky = W,row = 1,column = counter_row2,padx = 10)
			counter_row2+=1
		else:
			issued_books_array[books_counter].grid(sticky = W,row = 0,column = counter_row1,padx = 10)
			counter_row1+=1
		books_counter+=1


def dateNotRight(date,month,year):
	print(date,month,year)
	print (range(1,32))
	print (range(1950,2000))
	if int(date) not in range(1,32):
		return True;
	elif month not in monthList:
		return True;
	elif int(year) not in range(1950,2000):
		return True;
	return False;





