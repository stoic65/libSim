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

root = Tk()
root.attributes("-alpha",0.5)
myFont = tkFont.Font(family = "Times",size = 12,weight = "bold")
bigFont = tkFont.Font(family = "Times",size = 30,weight = "bold")
reducedFont = tkFont.Font(family = "Times",size = 10)

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



root.title("Library management System - Person Selection")
root.config(bg = backgroundColour)

#Common resources

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
			classic_array[classic_counter].grid(row = 1,column = classic_counter,sticky = W,padx = 10)
			classic_array[classic_counter].image = img
			classic_array[classic_counter].item = item
			classic_array[classic_counter].bind("<Button-1>",callback)
			
			classic_counter+=1


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
			
			mystery_counter+=1

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
			scifi_counter+=1

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
			comedy_counter+=1

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
			horror_counter+=1

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
			nonFiction_counter+=1


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
			textBook_counter+=1

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
			magazines_counter+=1





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


















class alertMessage:
	def __init__(master,messageString):
		opSuccessTopLevel = Toplevel(height = 200,width = 300,bg = backgroundColour)
		opSuccessTopLevel.title("Operation successful")
				
		successMessage = Label(opSuccessTopLevel,text = messageString,fg = textLight,bg = backgroundColour)
		successMessage.pack(padx = 50,pady = 50)

		dismissButton = Button(opSuccessTopLevel,text = "Dismiss",relief = RAISED,bg = buttonColour,font = myFont,fg = textLight,command = opSuccessTopLevel.destroy)
		dismissButton.pack(padx = 50,pady = 10)
		


class mainView:

	def __init__(self,master,parentObject,personDetailsObject):
		#Create all the views including all the frames
		print (personDetailsObject)
		self.master  = master 
		self.master.title("Main View")

		self.mainViewFrame = Frame(master,height = 800,width = 1000,bg = "black")
		self.mainViewFrame.pack(expand = YES,fill = BOTH)

		for x in range(10):
			Grid.rowconfigure(self.mainViewFrame,x,weight = 1)


		for x in range(10):
			Grid.columnconfigure(self.mainViewFrame,x,weight = 1)


		self.filterBooksView = LabelFrame(self.mainViewFrame,text = "Filter Books",height = 230,width = 300,bg = backgroundColour,fg = textLight)
		self.filterBooksView.grid(row = 0,column  =0,sticky = N+S+E+W,padx = 5,pady = 5)

		self.myIssuedBooksView = LabelFrame(self.mainViewFrame,text = "My books",height = 230,width = 300,bg = backgroundColour,fg = textLight)
		self.myIssuedBooksView.grid(row = 1,column  =0,sticky = N+S+E+W,padx = 5,pady = 5)

		self.totalFineView = LabelFrame(self.mainViewFrame,text = "Total Fine",height = 240,width = 300,bg = backgroundColour,fg = textLight)
		self.totalFineView.grid(row = 2,column  =0,sticky = N+S+E+W,padx = 5,pady = 5)
		

		self.mainShelfView = LabelFrame(self.mainViewFrame,text = "Main Shelf",height = 200,width = 700,bg = "#663300",fg = textLight)
		self.mainShelfView.grid(row = 0,column  =1,rowspan = 3,sticky = N+S+E+W,padx = 5,pady = 5)
		self.mainShelfView.grid_propagate(False)
		self.mainShelfView.grid_rowconfigure(0,weight = 1)
		self.mainShelfView.grid_columnconfigure(0,weight = 1)
		self.innerFrame = Frame(self.mainShelfView,bg = innerFrameColour,height = 500,width = 600)
		self.innerFrame.grid(padx = 20,pady =20,sticky = N+S+E+W)
		self.classicFrame = LabelFrame(self.innerFrame,text = "Classical",height = 80,width = 700,bg = innerFrameColour,fg = textLight)
		self.classicFrame.grid(row=0,sticky = E+W)
		self.mysteryFrame = LabelFrame(self.innerFrame,text = "Mystery",height = 80,width = 700,bg = innerFrameColour,fg = textLight)
		self.mysteryFrame.grid(row=1,sticky = E+W)
		self.scifiFrame = LabelFrame(self.innerFrame,text = "Sci-fi",height = 80,width = 700,bg = innerFrameColour,fg = textLight)
		self.scifiFrame.grid(row=2,sticky = E+W)
		self.comedyFrame = LabelFrame(self.innerFrame,text = "Comedy",height = 80,width = 700,bg = innerFrameColour,fg = textLight)
		self.comedyFrame.grid(row=3,sticky = E+W)
		self.horrorFrame = LabelFrame(self.innerFrame,text = "Horror",height = 80,width = 700,bg = innerFrameColour,fg = textLight)
		self.horrorFrame.grid(row=4,sticky = E+W)
		self.nonFictionFrame = LabelFrame(self.innerFrame,text = "Non Fiction",height = 80,width = 700,bg = innerFrameColour,fg = textLight)
		self.nonFictionFrame.grid(row=5,sticky = E+W)
		self.textBookFrame = LabelFrame(self.innerFrame,text = "Text Books",height = 80,width = 700,bg = innerFrameColour,fg = textLight)
		self.textBookFrame.grid(row=6,sticky = E+W)
		self.magazinesFrame = LabelFrame(self.innerFrame,text = "Magazines",height = 80,width = 700,bg = innerFrameColour,fg = textLight)
		self.magazinesFrame.grid(row=7,sticky = E+W)
		self.innerFrame.grid_propagate(False)
		self.innerFrame.grid_columnconfigure(0,weight = 1)
		for i in range(8):
			self.innerFrame.grid_rowconfigure(i,weight = 1)








		self.addRemoveUsersView = LabelFrame(self.mainViewFrame,text = "Edit Users",height = 230,width = 300,bg = backgroundColour,fg = textLight)
		self.addRemoveUsersView.grid(row = 0,column  =2,sticky = N+S+E+W,padx = 5,pady = 5)

		self.addRemoveBooksView = LabelFrame(self.mainViewFrame,text = "Add/Remove Books",height = 230,width = 300,bg = backgroundColour,fg = textLight)
		self.addRemoveBooksView.grid(row = 1,column  =2,sticky = N+S+E+W,padx = 5,pady = 5)

		
		self.myDetailsView = LabelFrame(self.mainViewFrame,text = "My Details ",height = 240,width = 300,bg = backgroundColour,fg = textLight )
		self.myDetailsView.grid(row = 2,column  =2,padx = 5,pady = 5,sticky = N+S+E+W)
		








class Person:


	def __init__(self,master,personDetailsObject):
		self.currentView = mainView(master,self,personDetailsObject)
		self.personDetailsObject = personDetailsObject
		#Placing details in current view
		#My details view
		Label(self.currentView.myDetailsView,text = "Name",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 0,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = "Gender",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 1,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = "DOB",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 2,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = "ID",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = "Phone",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 4,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = "Email",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 5,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = "Account type",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 6,column = 0,padx = 5,pady = 2,sticky = W)
		
		for index in range(7):
			Label(self.currentView.myDetailsView,text = ":",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = index,column = 1,padx = 2,pady = 2,sticky = W)
		
		Label(self.currentView.myDetailsView,text = personDetailsObject["name"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 0,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = personDetailsObject["gender"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 1,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = personDetailsObject["dateOfBirth"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 2,column = 2,padx = 5,pady = 2,sticky = W)
		if(personDetailsObject["personType"] is "Staff"):
			Label(self.currentView.myDetailsView,text = personDetailsObject["employeeId"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 2,padx = 5,pady = 2,sticky = W)
		else:
			Label(self.currentView.myDetailsView,text = personDetailsObject["studentPrimaryKey"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = personDetailsObject["phone"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 4,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = personDetailsObject["email"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 5,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.myDetailsView,text = personDetailsObject["personType"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 6,column = 2,padx = 5,pady = 2,sticky = W)
		



		# Fine View
		Label(self.currentView.totalFineView,text = "Your outstanding fine is:",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView,justify = CENTER,anchor = CENTER).grid(row = 0,padx = 5,pady = 5,sticky = N+E+W)
		self.fineLabel = Label(self.currentView.totalFineView,text = "Rs. 0" ,padx = 5,pady = 2,bg = backgroundColour,font = bigFont,fg = "red",justify = CENTER,anchor = CENTER)
		self.fineLabel.grid(row = 1,padx = 70,pady = 40,sticky = E+W+S)
		
		#Loading books in mainshelf
		
		loadShelfView(self)


		#Load My Issued Books
		loadIssuedBooks(self)




	def bookClick(self,bookId):
		print(bookId,"selected")
		self.bookIssueTop = Toplevel(bg = backgroundColour)
		self.bookIssueTop.title("Issue Books")
		self.bookIssueFrame = LabelFrame(self.bookIssueTop,text = "Issue Books",bg = backgroundColour,fg = textLight)
		self.bookIssueFrame.pack(fill = BOTH,expand = YES)
		Label(self.bookIssueFrame,text = "Title",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 0,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.bookIssueFrame,text = "Author",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 1,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.bookIssueFrame,text = "Publisher",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 2,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.bookIssueFrame,text = "Genre",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.bookIssueFrame,text = "Added By",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 4,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.bookIssueFrame,text = "Added On",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 5,column = 0,padx = 5,pady = 2,sticky = W)

		for index in range(6):
			Label(self.bookIssueFrame,text = ":",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = index,column = 1,padx = 2,pady = 2,sticky = W)
		
		Label(self.bookIssueFrame,text = booksMasterObject[bookId]["title"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 0,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.bookIssueFrame,text = booksMasterObject[bookId]["author"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 1,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.bookIssueFrame,text = booksMasterObject[bookId]["publisher"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 2,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.bookIssueFrame,text = booksMasterObject[bookId]["genre"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.bookIssueFrame,text = booksMasterObject[bookId]["addedBy"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 4,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.bookIssueFrame,text = booksMasterObject[bookId]["addedOn"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 5,column = 2,padx = 5,pady = 2,sticky = W)
		
		self.issueEmptySpace = Label(self.bookIssueFrame,bg = backgroundColour)
		self.issueEmptySpace.grid(row = 6,columnspan = 3)
		if booksMasterObject[bookId]["isIssued"] is False:
			self.issueButton = Button(self.bookIssueFrame,text = "Issue",relief = RAISED,bg = buttonColour,fg = textLight,font = myFont,command = lambda :self.issueBook(bookId))
			self.issueButton.grid(columnspan = 3, row = 8,padx = 10,pady = 10)	
		else:
			Label(self.bookIssueFrame,text = "Issued By",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 6,column = 0,padx = 5,pady = 2,sticky = W)
			Label(self.bookIssueFrame,text = ":",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 6,column = 1,padx = 2,pady = 2,sticky = W)
			Label(self.bookIssueFrame,text = booksMasterObject[bookId]["issuedBy"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 6,column = 2,padx = 5,pady = 2,sticky = W)
			
			Label(self.bookIssueFrame,text = "Issued On",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 7,column = 0,padx = 5,pady = 2,sticky = W)
			Label(self.bookIssueFrame,text = ":",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 7,column = 1,padx = 2,pady = 2,sticky = W)
			Label(self.bookIssueFrame,text = booksMasterObject[bookId]["issuedOn"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 7,column = 2,padx = 5,pady = 2,sticky = W)
				
		


	def issueBook(self,bookId):
		#if student check limit
		booksMasterObject[bookId]["isIssued"] = True
		booksMasterObject[bookId]["issuedBy"] = self.personDetailsObject["name"]
		booksMasterObject[bookId]["issuedOn"] = (time.strftime("%d"),time.strftime("%m"),time.strftime("%y"))
		booksMasterObject[bookId]["expectedReturn"] = (str(int(time.strftime("%d"))+1),time.strftime("%m"),time.strftime("%y"))

		if(self.personDetailsObject["personType"] == "Staff"):
			staffMasterObject[self.personDetailsObject["employeeId"]]["issuedBooks"].append(bookId)
			booksMasterObject[bookId]["issueHistory"].append(((int(time.strftime("%d")),int(time.strftime("%m")),int(time.strftime("%y"))),self.personDetailsObject["employeeId"]))
			f = open(staffFile,"wb")
			pickle.dump(staffMasterObject,f)
			f.close()
		else:
			studentMasterObject[self.personDetailsObject["studentPrimaryKey"]]["issuedBooks"].append(bookId)
			booksMasterObject[bookId]["issueHistory"].append(((int(time.strftime("%d")),int(time.strftime("%m")),int(time.strftime("%y"))),self.personDetailsObject["studentPrimaryKey"]))
			f = open(studentFile,"wb")
			pickle.dump(studentMasterObject,f)
			f.close()

		f = open(booksFile,"wb")
		pickle.dump(booksMasterObject,f)
		f.close()
		self.bookIssueTop.destroy()
		if self.myIssuedBooksInnerView is not None:
			self.myIssuedBooksInnerView.destroy()
		loadIssuedBooks(self)

		print(staffMasterObject)



	def issuedBookClick(self,bookId):
		print("Isssued",bookId)
		self.myBooksTop = Toplevel(bg = backgroundColour)
		self.myBooksTop.title("My Books")
		self.myBooksFrame = LabelFrame(self.myBooksTop,text = "Issued Books",bg = backgroundColour,fg = textLight)
		self.myBooksFrame.pack(fill = BOTH,expand = YES)
		Label(self.myBooksFrame,text = "Title",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 0,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.myBooksFrame,text = "Author",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 1,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.myBooksFrame,text = "Publisher",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 2,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.myBooksFrame,text = "Genre",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.myBooksFrame,text = "Added By",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 4,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.myBooksFrame,text = "Added On",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 5,column = 0,padx = 5,pady = 2,sticky = W)

		for index in range(6):
			Label(self.myBooksFrame,text = ":",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = index,column = 1,padx = 2,pady = 2,sticky = W)
		
		Label(self.myBooksFrame,text = booksMasterObject[bookId]["title"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 0,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.myBooksFrame,text = booksMasterObject[bookId]["author"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 1,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.myBooksFrame,text = booksMasterObject[bookId]["publisher"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 2,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.myBooksFrame,text = booksMasterObject[bookId]["genre"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.myBooksFrame,text = booksMasterObject[bookId]["addedBy"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 4,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.myBooksFrame,text = booksMasterObject[bookId]["addedOn"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 5,column = 2,padx = 5,pady = 2,sticky = W)
		
		self.issueEmptySpace = Label(self.myBooksFrame,bg = backgroundColour)
		self.issueEmptySpace.grid(row = 6,columnspan = 3,pady = 10,padx = 10)

		self.readButton = Button(self.myBooksFrame,text = "Read",relief = RAISED,bg = buttonColour,fg = textLight,font = myFont)
		self.readButton.grid(column = 0, row = 7)


		self.returnButton = Button(self.myBooksFrame,text = "Return",relief = RAISED,bg = buttonColour,fg = textLight,font = myFont,command = lambda :self.returnBook(bookId))
		self.returnButton.grid(column = 2, row = 7,pady = 10,padx = 10)

	def returnBook(self,bookId):
		print("return",bookId)


		if(self.personDetailsObject["personType"] == "Staff"):
			staffMasterObject[self.personDetailsObject["employeeId"]]["issuedBooks"].remove(bookId)
			f = open(staffFile,"wb")
			pickle.dump(staffMasterObject,f)
			f.close()
		else:
			studentMasterObject[self.personDetailsObject["studentPrimaryKey"]]["issuedBooks"].remove(bookId)
			d0 = date(int(booksMasterObject[bookId]["issuedOn"][2]),int(booksMasterObject[bookId]["issuedOn"][1]),int(booksMasterObject[bookId]["issuedOn"][0]))
			d1 = date(int(time.strftime("%y")),int(time.strftime("%m")),int(time.strftime("%d")))
			delta = d1 - d0
			if(delta.days>=2):
				studentMasterObject[self.personDetailsObject["studentPrimaryKey"]]["currentFine"] = delta.days-1

			f = open(studentFile,"wb")
			pickle.dump(studentMasterObject,f)
			f.close()



		booksMasterObject[bookId]["isIssued"] = False
		booksMasterObject[bookId]["issuedBy"] = None
		booksMasterObject[bookId]["issuedOn"] = None
		booksMasterObject[bookId]["expectedReturn"] = None

		
		f = open(booksFile,"wb")
		pickle.dump(booksMasterObject,f)
		f.close()
		self.myBooksTop.destroy()
		self.myIssuedBooksInnerView.destroy()
		loadIssuedBooks(self)

		print(staffMasterObject)
		pass
		


#Books

class Book:
	def __init__(self,bookDetails):
		pass






#
#
#	STAFF CLASS		
class Staff(Person):

	def __init__(self,master,personDetailsObject):
		personDetailsObject["personType"] = "Staff"
		Person.__init__(self,master,personDetailsObject)
		#Adding books

		Button(self.currentView.addRemoveBooksView,text = "Add Book",fg = textLight,bg = buttonColour,width = 10,command = self.addBook).grid(column = 0,row = 0,padx = 30,pady = 70)
		Button(self.currentView.addRemoveBooksView,text = "Remove Book",fg = textLight,bg = buttonColour,width = 10,command = self.removeBooks).grid(column = 1,row = 0,padx = 0,pady = 70)

	def addBook(self):
		self.addBookTop = Toplevel(bg = backgroundColour)
		self.addBookFrame = LabelFrame(self.addBookTop,text = "Add a book",bg = backgroundColour,fg = textLight,height = 700,width = 500)
		self.addBookFrame.pack(fill = BOTH,expand = YES,ipady = 20,ipadx = 15,padx = 20,pady = 20)
		self.titleLabel = Label(self.addBookFrame,text = "Name Of Book",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.titleLabel.grid(row = 0,column = 0,pady = 3,padx = 5,sticky = W) 
		self.titleEntry  = Entry(self.addBookFrame);
		self.titleEntry.grid (row = 0,column = 2,pady = 3,padx = 5 )
		

		self.authorLabel = Label(self.addBookFrame,text = "Author Name",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.authorLabel.grid(row = 1,column = 0,pady = 3,padx = 5,sticky = W) 
		self.authorEntry  = Entry(self.addBookFrame);
		self.authorEntry.grid(row = 1,column = 2,pady = 3,padx = 5 )
		
		self.publisherLabel = Label(self.addBookFrame,text = "Publisher",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.publisherLabel.grid(row = 2,column = 0,pady = 3,padx = 5,sticky = W) 
		self.publisherEntry  = Entry(self.addBookFrame);
		self.publisherEntry.grid(row = 2,column = 2,pady = 3,padx = 5 )
		
		self.genreLabel = Label(self.addBookFrame,text = "Genre",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.genreLabel.grid(row = 3,column = 0,pady = 3,padx = 5,sticky = W) 
		self.genreEntry  = Spinbox(self.addBookFrame,values = ("Classic","Mystery","Scifi","Comedy","Horror","Non Fiction","Textbook"),width = 15,justify = RIGHT);
		self.genreEntry.grid(row = 3,column = 2,pady = 3,padx = 5,sticky = W )
		
		self.isbnLabel = Label(self.addBookFrame,text = "ISBN",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.isbnLabel.grid(row = 4,column = 0,pady = 3,padx = 5,sticky = W) 
		self.isbnEntry  = Entry(self.addBookFrame);
		self.isbnEntry.grid(row = 4,column = 2,pady = 3,padx = 5 )

		self.bookPathLabel = Label(self.addBookFrame,text = "Book Path",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.bookPathLabel.grid(row = 5,column = 0,pady = 3,padx = 5,sticky = W) 
		self.bookPathEntry  = Entry(self.addBookFrame);
		self.bookPathEntry.grid(row = 5,column = 2,pady = 3,padx = 5 )


		for index in range(6): 
			Label(self.addBookFrame,text = ":",bg = backgroundColour).grid(row = index,column = 1)

		self.emptySpace = Label(self.addBookFrame,bg = backgroundColour)
		self.emptySpace.grid(row = 6,columnspan = 3)
		self.submitForm = Button(self.addBookFrame,text = "Submit",relief = RAISED,bg = buttonColour,fg = textLight,font = myFont,command = lambda :self.submitBookForm(self.titleEntry.get(),self.authorEntry.get(),self.publisherEntry.get(),self.genreEntry.get(),self.isbnEntry.get(),self.bookPathEntry.get()))
		self.submitForm.grid(columnspan = 3, row = 7)
		

	def submitBookForm(self,title,author,publisher,genre,isbn,bookPath):
		#Also include added on, added by
		#cover image can be empty
		if(isEmptyChecker(title,author,publisher,genre,isbn,bookPath)):
			self.emptySpace.config(text = "Employee already exists",fg = "red")
		else:
			#check if similar isbn already exists
			counter = 0
			while(isbn+":"+str(counter) in booksMasterObject):
				counter+=1
			bookId = isbn+":"+str(counter)
			booksMasterObject[bookId] = {}
			
			booksMasterObject[bookId]["title"] = title
			booksMasterObject[bookId]["author"] = author
			booksMasterObject[bookId]["publisher"] = publisher
			booksMasterObject[bookId]["genre"] = genre
			booksMasterObject[bookId]["isbn"] = isbn
			booksMasterObject[bookId]["bookPath"] = bookPath+".txt"
			booksMasterObject[bookId]["coverImagePath"] = bookPath+".gif"
			booksMasterObject[bookId]["addedBy"] = self.personDetailsObject["name"]
			booksMasterObject[bookId]["addedOn"] = (time.strftime("%d"),time.strftime("%m"),time.strftime("%y"))
			booksMasterObject[bookId]["isIssued"] = False
			booksMasterObject[bookId]["issueHistory"] = []
			booksMasterObject[bookId]["bookId"] = bookId
			
			
			
			f = open(booksFile,"wb")
			pickle.dump(booksMasterObject,f)
			f.close()
			self.addBookTop.destroy()
			alertMessage("Book Successfuly added")

			#refresh the mainViewHere
			loadShelfView(self)
			#currentPerson = Staff(self.master,staffMasterObject[employeeId])




	

	def removeBooks(self):
		pass









class staffCreationForm:
	def __init__(self,master):
		self.newFrame = Frame(master,bg = backgroundColour)
		self.newFrame.pack(fill = BOTH,expand = YES,ipady = 10,pady= 10,padx = 40 )
		
		master.title("Library management System - Staff creation")
		self.master = master
		#Creating various fields for data entry
		#Name Field
		self.nameLabel = Label(self.newFrame,text = "Name",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.nameLabel.grid(row = 0,column = 0,pady = 3,padx = 5,sticky = W) 
		self.nameEntry  = Entry(self.newFrame);
		self.nameEntry.grid (row = 0,column = 2,pady = 3,padx = 5 )
		

		self.phoneLabel = Label(self.newFrame,text = "Phone",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.phoneLabel.grid(row = 1,column = 0,pady = 3,padx = 5,sticky = W) 
		self.phoneEntry  = Entry(self.newFrame);
		self.phoneEntry.grid(row = 1,column = 2,pady = 3,padx = 5 )
		
		self.emailLabel = Label(self.newFrame,text = "Email",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.emailLabel.grid(row = 2,column = 0,pady = 3,padx = 5,sticky = W) 
		self.emailEntry  = Entry(self.newFrame);
		self.emailEntry.grid(row = 2,column = 2,pady = 3,padx = 5 )
		
		self.genderLabel = Label(self.newFrame,text = "Gender",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.genderLabel.grid(row = 3,column = 0,pady = 3,padx = 5,sticky = W) 
		self.genderEntry  = Spinbox(self.newFrame,values = ("Male","Female"),width = 6);
		self.genderEntry.grid(row = 3,column = 2,pady = 3,padx = 5,sticky = W )
		
		self.employeeIdLabel = Label(self.newFrame,text = "EmployeeId",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.employeeIdLabel.grid(row = 4,column = 0,pady = 3,padx = 5,sticky = W) 
		self.employeeEntry  = Entry(self.newFrame);
		self.employeeEntry.grid(row = 4,column = 2,pady = 3,padx = 5 )
		
		Label(self.newFrame,text = "Date Of Birth",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight).grid(pady = 3,padx = 5,row = 5,column = 0,sticky = W)
		self.dobDayEntry = Entry(self.newFrame,width = 10,justify = RIGHT)
		self.dobDayEntry.insert(END,"Enter day")
		self.dobDayEntry.grid(row = 6,column = 0,pady = 3,padx = 5)
		self.dobMonthEntry = Spinbox(self.newFrame,width = 10,justify = RIGHT,values = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
		self.dobMonthEntry.grid(row = 6,column = 1,pady = 3,padx = 5)
		self.dobYearEntry = Spinbox(self.newFrame,width = 10,justify = RIGHT,from_ = 1950,to = 2000)
		self.dobYearEntry.grid(row = 6,column = 2,pady = 3,padx = 5)
		


		self.passwordLabel = Label(self.newFrame,text = "Create Password",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.passwordLabel.grid(row = 7,column = 0,pady = 3,padx = 5,sticky = W)
		self.passwordEntry = Entry(self.newFrame,show = "*")
		self.passwordEntry.grid(row = 7,column = 2,pady = 3,padx = 5)
		
		self.retypePasswordLabel = Label(self.newFrame,text = "Retype Password",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.retypePasswordLabel.grid(row = 8,column = 0,pady = 3,padx = 5,sticky = W)
		self.retypePasswordEntry = Entry(self.newFrame,show = "*")
		self.retypePasswordEntry.grid(row = 8,column = 2,pady = 3,padx = 5)
		for index in range(9):
			if index is 6:continue 
			Label(self.newFrame,text = ":",bg = backgroundColour).grid(row = index,column = 1)


		self.emptySpace = Label(self.newFrame,bg = backgroundColour)
		self.emptySpace.grid(row = 9,columnspan = 3)
		self.submitForm = Button(self.newFrame,text = "Submit",relief = RAISED,bg = buttonColour,fg = textLight,font = myFont,command = lambda :self.submitStaffForm(self.nameEntry.get(),self.phoneEntry.get(),self.emailEntry.get(),self.genderEntry.get(),self.employeeEntry.get(),self.dobDayEntry.get(),self.dobMonthEntry.get(),self.dobYearEntry.get(),self.passwordEntry.get(),self.retypePasswordEntry.get()))
		self.submitForm.grid(columnspan = 3, row = 10)
		



	def submitStaffForm(self,name,phone,email,gender,employeeId,dobDay,dobMonth,dobYear,createPassword,retypePassword):
			
		if employeeId in staffMasterObject:
			self.emptySpace.config(text = "Employee already exists",fg = "red")
		
		elif isEmptyChecker(name,phone,email,gender,employeeId,dobDay,dobMonth,dobYear,createPassword,retypePassword):
			self.emptySpace.config(text = "One or more entries empty",fg = "red")
		elif not createPassword==retypePassword:
			self.emptySpace.config(text = "Passwords not matching",fg = "red")
		#elif dateNotRight(dobDay,dobMonth,dobYear):
		#	self.emptySpace.config(text = "D.O.B date incorrect",fg = "red")

		else:
			dateOfBirth = (dobDay,dobMonth,dobYear)
			staffMasterObject[employeeId] = {}
			staffMasterObject[employeeId]["name"] = name
			staffMasterObject[employeeId]["phone"] = phone
			staffMasterObject[employeeId]["email"] = email
			staffMasterObject[employeeId]["gender"] = gender
			staffMasterObject[employeeId]["dateOfBirth"] = dateOfBirth
			p = hashlib.md5()
			p.update(createPassword.encode())
			staffMasterObject[employeeId]["password"] = p.digest()
			staffMasterObject[employeeId]["issuedBooks"] = []
			staffMasterObject[employeeId]["employeeId"] = employeeId
			staffMasterObject[employeeId]["currentFine"]= 0
			


			print (staffMasterObject)
			f = open(staffFile,"wb")
			pickle.dump(staffMasterObject,f)
			f.close()
			self.newFrame.pack_forget()
			alertMessage("Login Successful")
			
			currentPerson = Staff(self.master,staffMasterObject[employeeId])


class staffLogin:

	def __init__(self,master):
		self.master = master
		self.newFrame = Frame(self.master,bg = backgroundColour)
		self.newFrame.pack(ipady = 10,padx = 40,pady = 10)

		#Various fields
		self.userId = Label(self.newFrame,text = "Employee Id :",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.userId.grid(row = 0,column = 0,pady = 3,padx = 5,sticky = W)
		self.userIdEntry = Entry(self.newFrame)
		self.userIdEntry.grid(row = 0,column = 1,pady = 3,padx = 5,sticky = W) 
		
		self.password = Label(self.newFrame,text = "Password :",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.password.grid(row = 1,column = 0,pady = 3,padx = 5,sticky = W)
		self.passwordEntry = Entry(self.newFrame,show = "*")
		self.passwordEntry.grid(row = 1,column = 1,pady = 3,padx = 5,sticky = W) 
		
		self.emptySpace = Label(self.newFrame,bg = backgroundColour)
		self.emptySpace.grid(row = 2,columnspan = 2)
		self.submitButton = Button(self.newFrame,text = "Submit",relief = RAISED,fg = textLight,bg = buttonColour,font = myFont,command = lambda:self.submitForm(self.userIdEntry.get(),self.passwordEntry.get()))
		self.submitButton.grid(row = 3,columnspan = 2)


	def submitForm(self,userId,password):
		if isEmptyChecker(userId,password):
			self.emptySpace.config(text = "One or more fields Empty",fg = "red")
		elif userId not in staffMasterObject:
			self.emptySpace.config(text = "Invalid User/Password",fg = "red")
		elif not passwordMatch(userId,password,staffMasterObject):
			self.emptySpace.config(text = "Invalid User/Password",fg = "red")
		else:
			self.newFrame.pack_forget()
			alertMessage("Login Successful")
			currentPerson = Staff(self.master,staffMasterObject[userId])











#EO STAFF CLASS


#STUDENT CLASS


class Student(Person):

	def __init__(self,master,personDetailsObject):
		personDetailsObject["personType"] = "Student"
		Person.__init__(self,master,personDetailsObject)
		#Calculate total fine
		totalFine = studentMasterObject[personDetailsObject["studentPrimaryKey"]]["currentFine"]
		for item in studentMasterObject[personDetailsObject["studentPrimaryKey"]]["issuedBooks"]:
			d0 = date(int(booksMasterObject[item]["issuedOn"][2]),int(booksMasterObject[item]["issuedOn"][1]),int(booksMasterObject[item]["issuedOn"][0]))
			d1 = date(int(time.strftime("%y")),int(time.strftime("%m")),int(time.strftime("%d")))
			delta = d1 - d0
			if(delta.days>=2):
				totalFine+=delta.days-1
		self.fineLabel.config(text = "Rs. "+str(totalFine))
		





class  studentCreationForm:

	def __init__(self,master):
		self.newFrame = Frame(master,bg = backgroundColour)
		self.newFrame.pack(fill = BOTH,expand = YES,ipady = 10,pady= 10,padx = 40 )
		
		master.title("Library management System - Student creation")
		self.master = master
		#Creating various fields for data entry
		self.nameLabel = Label(self.newFrame,text = "Name",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.nameLabel.grid(row = 0,column = 0,pady = 3,padx = 5,sticky = W) 
		self.nameEntry  = Entry(self.newFrame);
		self.nameEntry.grid (row = 0,column = 2,pady = 3,padx = 5 )
		
		self.phoneLabel = Label(self.newFrame,text = "Phone",padx = 5,pady = 2,bg = backgroundColour,fg = textLight,font = myFont)
		self.phoneLabel.grid(row = 1,column = 0,pady = 3,padx = 5,sticky = W) 
		self.phoneEntry  = Entry(self.newFrame);
		self.phoneEntry.grid(row = 1,column = 2,pady = 3,padx = 5 )
		
		self.emailLabel = Label(self.newFrame,text = "Email",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.emailLabel.grid(row = 2,column = 0,pady = 3,padx = 5,sticky = W) 
		self.emailEntry  = Entry(self.newFrame);
		self.emailEntry.grid(row = 2,column = 2,pady = 3,padx = 5 )
		
		self.genderLabel = Label(self.newFrame,text = "Gender",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.genderLabel.grid(row = 3,column = 0,pady = 3,padx = 5,sticky = W) 
		self.genderEntry  = Spinbox(self.newFrame,width = 6,justify = RIGHT,values = ("Male","Female"))
		self.genderEntry.grid(row = 3,column = 2,pady = 3,padx = 5,sticky = W )
		
		self.rollNoLabel = Label(self.newFrame,text = "Roll No.",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.rollNoLabel.grid(row = 4,column = 0,pady = 3,padx = 5,sticky = W)
		Label(self.newFrame,text = "(Only the number ex. 331)",padx = 5,pady = 2,bg = backgroundColour,fg = textLight,font = reducedFont).grid(row = 5,column = 0,pady = 3,padx = 5,sticky = W)
		self.rollNoEntry  = Entry(self.newFrame);
		self.rollNoEntry.grid(row = 4,column = 2,pady = 3,padx = 5 )
		
		self.branchLabel = Label(self.newFrame,text = "Branch",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.branchLabel.grid(row = 6,column = 0,pady = 3,padx = 5,sticky = W)
		self.branchEntry  = Spinbox(self.newFrame,width = 6,justify = RIGHT,values = ("COE","ECE","ICE","IT","MPAE"))
		self.branchEntry.grid(row = 6,column = 2,pady = 3,padx = 5,sticky = W )
		
		self.yearLabel = Label(self.newFrame,text = "Year",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.yearLabel.grid(row = 7,column = 0,pady = 3,padx = 5,sticky = W)
		self.yearEntry  = Spinbox(self.newFrame,width = 6,justify = RIGHT,from_ = 12,to = 16)
		self.yearEntry.grid(row = 7,column = 2,pady = 3,padx = 5,sticky = W )
		
		Label(self.newFrame,text = "Date Of Birth",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight).grid(pady = 3,padx = 5,row = 8,column = 0,sticky = W)
		self.dobDayEntry = Entry(self.newFrame,width = 10,justify = RIGHT)
		self.dobDayEntry.insert(END,"Enter day")
		self.dobDayEntry.grid(row = 9,column = 0,pady = 3,padx = 5)
		self.dobMonthEntry = Spinbox(self.newFrame,width = 10,justify = RIGHT,values = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
		self.dobMonthEntry.grid(row = 9,column = 1,pady = 3,padx = 5)
		self.dobYearEntry = Spinbox(self.newFrame,width = 10,justify = RIGHT,from_ = 1950,to = 2000)
		self.dobYearEntry.grid(row = 9,column = 2,pady = 3,padx = 5)
		

		self.passwordLabel = Label(self.newFrame,text = "Create Password",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.passwordLabel.grid(row = 10,column = 0,pady = 3,padx = 5,sticky = W)
		self.passwordEntry = Entry(self.newFrame,show = "*")
		self.passwordEntry.grid(row = 10,column = 2,pady = 3,padx = 5)
		
		self.retypePasswordLabel = Label(self.newFrame,text = "Retype Password",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.retypePasswordLabel.grid(row = 11,column = 0,pady = 3,padx = 5,sticky = W)
		self.retypePasswordEntry = Entry(self.newFrame,show = "*")
		self.retypePasswordEntry.grid(row = 11,column = 2,pady = 3,padx = 5)
		




		for index in range(10):
			if index is 5 or index is 9: continue
			Label(self.newFrame,text = ":",bg = backgroundColour).grid(row = index,column = 1)

		self.emptySpace = Label(self.newFrame,bg = backgroundColour)
		self.emptySpace.grid(row = 12,columnspan = 3)
		self.submitForm = Button(self.newFrame,text = "Submit",relief = RAISED,bg = buttonColour,fg = textLight,font = myFont,command = lambda :self.submitStudentForm(self.nameEntry.get(),self.phoneEntry.get(),self.emailEntry.get(),self.genderEntry.get(),self.rollNoEntry.get(),self.branchEntry.get(),self.yearEntry.get(),self.dobDayEntry.get(),self.dobMonthEntry.get(),self.dobYearEntry.get(),self.passwordEntry.get(),self.retypePasswordEntry.get()))
		self.submitForm.grid(columnspan = 3, row = 13)


	def submitStudentForm(self,name,phone,email,gender,rollNo,branch,year,dobDay,dobMonth,dobYear,createPassword,retypePassword):
		studentPrimaryKey = rollNo+branch+year
		if studentPrimaryKey in studentMasterObject:
			self.emptySpace.config(text = "Roll No already exists",fg = "red")
		elif isEmptyChecker(name,phone,email,gender,rollNo,branch,year,dobDay,dobMonth,dobYear,createPassword,retypePassword):
			self.emptySpace.config(text = "One or more fields empty",fg = "red")
		elif not createPassword==retypePassword:
			self.emptySpace.config(text = "Passwords not matching",fg = "red")
		#elif dateNotRight(dobDay,dobMonth,dobYear):
		#	self.emptySpace.config(text = "D.O.B date incorrect",fg = "red")
		else:
			dateOfBirth = (dobDay,dobMonth,dobYear)

			studentMasterObject[studentPrimaryKey] = {}
			studentMasterObject[studentPrimaryKey]["name"] = name
			studentMasterObject[studentPrimaryKey]["phone"] = phone
			studentMasterObject[studentPrimaryKey]["email"] = email
			studentMasterObject[studentPrimaryKey]["gender"] = gender
			studentMasterObject[studentPrimaryKey]["rollNo"] = rollNo
			studentMasterObject[studentPrimaryKey]["branch"] = branch
			studentMasterObject[studentPrimaryKey]["year"] = year
			studentMasterObject[studentPrimaryKey]["dateOfBirth"] = dateOfBirth
			p = hashlib.md5()
			p.update(createPassword.encode())
			studentMasterObject[studentPrimaryKey]["password"] = p.digest()
			studentMasterObject[studentPrimaryKey]["issuedBooks"] = [] 
			studentMasterObject[studentPrimaryKey]["studentPrimaryKey"] = studentPrimaryKey
			studentMasterObject[studentPrimaryKey]["currentFine"] = 0


			print (studentMasterObject)
			f = open(studentFile,"wb")
			pickle.dump(studentMasterObject,f)
			f.close()
			self.newFrame.pack_forget()
			opSuccessTopLevel = Toplevel(height = 200,width = 300)
			opSuccessTopLevel.title("Operation successful")
			
			successMessage = Label(opSuccessTopLevel,text = """Operation Successful""")
			successMessage.pack(padx = 50,pady = 50)

			dismissButton = Button(opSuccessTopLevel,text = "Dismiss",relief = RAISED,bg = buttonColour,font = myFont,fg = textLight,command = opSuccessTopLevel.destroy)
			dismissButton.pack(padx = 50,pady = 10)
			
			currentPerson = Student(self.master,studentMasterObject[studentPrimaryKey])


class studentLogin:

	def __init__(self,master):
		self.master = master
		self.newFrame = Frame(self.master,bg = backgroundColour)
		self.newFrame.pack(ipady = 10,padx = 40,pady = 10)

		#Various fields
		self.userId = Label(self.newFrame,text = "RollNo :",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.userId.grid(row = 0,column = 0,pady = 3,padx = 5,sticky = W)
		self.userIdEntry = Entry(self.newFrame)
		self.userIdEntry.grid(row = 0,column = 1,pady = 3,padx = 5,sticky = W) 
		Label(self.newFrame,text = "(Ex. 331COE13)",font = reducedFont,bg = backgroundColour,padx  = 5,pady = 0).grid(row = 1,column = 0,pady = 0,padx = 5)

		self.password = Label(self.newFrame,text = "Password :",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.password.grid(row = 2,column = 0,pady = 3,padx = 5,sticky = W)
		self.passwordEntry = Entry(self.newFrame,show = "*")
		self.passwordEntry.grid(row = 2,column = 1,pady = 3,padx = 5,sticky = W) 
		
		self.emptySpace = Label(self.newFrame,bg = backgroundColour)
		self.emptySpace.grid(row = 3,columnspan = 2)
		self.submitButton = Button(self.newFrame,text = "Submit",relief = RAISED,fg = textLight,bg = buttonColour,font = myFont,command = lambda:self.submitForm(self.userIdEntry.get(),self.passwordEntry.get()))
		self.submitButton.grid(row = 4,columnspan = 2)

	def submitForm(self,userId,password):
		if isEmptyChecker(userId,password):
			self.emptySpace.config(text = "One or more fields Empty",fg = "red")
		elif userId not in studentMasterObject:
			self.emptySpace.config(text = "Invalid User/Password",fg = "red")
		elif not passwordMatch(userId,password,studentMasterObject):
			self.emptySpace.config(text = "Invalid User/Password",fg = "red")
		else:
			self.newFrame.pack_forget()
			alertMessage("Login Successful")
			currentPerson = Student(self.master,studentMasterObject[userId])









class existingOrNot:
	def __init__(self,master,currentFrame,personString):
		
		currentFrame.pack_forget()
		master.title("Library management System - Existing/New")
		self.master = master
		self.person = personString
		self.newFrame  = Frame(master,bg = backgroundColour)
		self.newFrame.pack(fill = BOTH,expand = YES)
		self.existingButton = Button(self.newFrame,text = personString+" : Existing User",relief = RAISED,height = 5,width = 50,bg = buttonColour,fg = textLight,font = myFont,command = lambda :self.existingUser(personString))
		self.existingButton.pack(side = TOP,padx = 100,pady = 50)
		self.newButton = Button(self.newFrame,text = personString+" : New User",relief = RAISED,height = 5,width = 50,bg = buttonColour,fg = textLight,font = myFont,command = lambda :self.newUser(personString))
		self.newButton.pack(side = TOP,padx = 100,pady = 50)


	def existingUser(self,personString):
		print ("Existing User")
		self.newFrame.pack_forget()
		if personString is "Staff":
			staffEntry = staffLogin(self.master)
		elif personString is "Student":
			studentEntry = studentLogin(self.master)


	def newUser(self,personString):
		print ("New User")
		self.newFrame.pack_forget()
		if personString is "Staff":
			staffEntry = staffCreationForm(self.master)

		elif personString is "Student":
			staffEntry = studentCreationForm(self.master)






def staffInit(master,currentFrame):
	print ("Staff selected")
	newEx = existingOrNot(master,currentFrame,"Staff")




def studentInit(master,currentFrame):
	print ("Student selected")
	newEx = existingOrNot(master,currentFrame,"Student")
	

#root.minsize(1000,500)
#root.maxsize(1000,500)
initFrame = Frame(root,bg = backgroundColour)
initFrame.pack(fill = BOTH,expand = YES)
staffInitButton = Button(initFrame,text = "Staff Login",relief = RAISED,height = 5,width = 50,bg= buttonColour,fg = textLight,font = myFont,command = lambda: staffInit(root,initFrame))
staffInitButton.pack(side = TOP,padx = 100,pady = 50)

studentInitButton = Button(initFrame,text = "Student Login",relief = RAISED,height = 5,width = 50,bg = buttonColour,fg = textLight,font = myFont,command = lambda :studentInit(root,initFrame))
studentInitButton.pack(side = TOP,padx = 100,pady = 50)

root.mainloop()