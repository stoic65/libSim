from globalVar import *

root = Tk()
root.attributes("-alpha",0.5)
myFont = tkFont.Font(family = "Times",size = 12,weight = "bold")
bigFont = tkFont.Font(family = "Times",size = 30,weight = "bold")
reducedFont = tkFont.Font(family = "Times",size = 10)

fontPacking = (myFont,bigFont,reducedFont)

root.title("Library management System - Person Selection")
root.config(bg = backgroundColour)


#Common resources


def staffInit(master,currentFrame):

	print ("Staff selected")
	newEx = existingOrNot(master,currentFrame,"Staff")


def studentInit(master,currentFrame):

	print ("Student selected")
	newEx = existingOrNot(master,currentFrame,"Student")

			
def fineDetails(personObject,personDetailsObject):
	if(personDetailsObject["personType"]=="Staff"):
		return

	primaryKey = personDetailsObject["studentPrimaryKey"]
	if studentMasterObject[primaryKey]["issuedBookCounter"]==0:
		return
	top = Toplevel()
	top.title("Fine details")
	mainLabel = Label(top,bg = backgroundColour)
	mainLabel.pack(fill = BOTH,ipadx = 20,ipady = 20)
	Label(mainLabel,text = "Previous Fines Total = "+str(studentMasterObject[primaryKey]["currentFine"]),bg = backgroundColour,fg = textLight,font = myFont).pack(fill = BOTH)

	for item in studentMasterObject[primaryKey]["issuedBooks"]:
		curFine = 0
		d0 = date(int(booksMasterObject[item]["issuedOn"][2]),int(booksMasterObject[item]["issuedOn"][1]),int(booksMasterObject[item]["issuedOn"][0]))
		d1 = date(int(time.strftime("%y")),int(time.strftime("%m")),int(time.strftime("%d")))
		delta = d1 - d0
		if(delta.days>=2):
			curFine+=delta.days-1
		Label(mainLabel,text = booksMasterObject[item]["title"]+"  :  "+str(curFine),bg = backgroundColour,fg = textLight,font = myFont).pack(fill = BOTH)


def readBook(bookId):
	top = Toplevel()
	f = open(booksMasterObject[bookId]["bookPath"],"r")

	#scroll = Scrollbar(top)
	#scroll.pack(side = RIGHT,fill = Y)

	textFrame = Text(top,font = myFont,height = 700)
	textFrame.insert(INSERT,f.read())
	textFrame.pack()

	pass




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
		#root.minsize(1300,750)
		root.maxsize(1300,750)

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

		#More Button creation 
		for idx,item in enumerate(genreList):
			createMoreButton(item,self.innerFrame,parentObject,idx);

		#Creating more Frame
		self.moreFrame = None


		self.innerFrame.grid_propagate(False)
		self.innerFrame.grid_columnconfigure(0,weight = 1)
		for i in range(8):
			self.innerFrame.grid_rowconfigure(i,weight = 1)




		self.addRemoveUsersView = LabelFrame(self.mainViewFrame,text = "Search Results",height = 230,width = 300,bg = backgroundColour,fg = textLight)
		self.addRemoveUsersView.grid(row = 0,column  =2,sticky = N+S+E+W,padx = 5,pady = 5)

		self.addRemoveBooksView = LabelFrame(self.mainViewFrame,text = "Add/Remove Books",height = 230,width = 300,bg = backgroundColour,fg = textLight)
		self.addRemoveBooksView.grid(row = 1,column  =2,sticky = N+S+E+W,padx = 5,pady = 5)

		
		self.myDetailsView = LabelFrame(self.mainViewFrame,text = "My Details ",height = 240,width = 300,bg = backgroundColour,fg = textLight )
		self.myDetailsView.grid(row = 2,column  =2,padx = 5,pady = 5,sticky = N+S+E+W)
		self.bookDetailsView = LabelFrame(self.mainViewFrame)


		#Filter Books
		self.filterBooksView.rowconfigure(0,weight = 1)
		#self.filterBooksView.rowconfigure(1,weight = 1)
		self.innerFilterBooksView = Frame(self.filterBooksView)
		self.searchFrame = LabelFrame(self.filterBooksView,text = "Search Books",height = 120,width = 300,bg = backgroundColour,fg = textLight)
		self.searchFrame.pack(fill = BOTH)
		self.authorFilterFrame = LabelFrame(self.filterBooksView,text = "Filter by Author",height = 120,width = 300,bg = backgroundColour,fg = textLight)
		self.authorFilterFrame.pack(fill = BOTH)

		#Inside search Frame
		self.searchField = Entry(self.searchFrame)
		self.searchField.grid(row = 0,pady = 25,padx = 8,column = 0)
		self.searchSubmit = Button(self.searchFrame,text = "Submit",relief = RAISED,fg = textLight,bg = buttonColour,font = myFont,width = 7,command = lambda:searchBooks(self.searchField.get(),parentObject)) 
		self.searchSubmit.grid(row = 0,column = 1,pady = 25,padx = 8)

		#Author Searcch Entry
		#self.authorSearchField = Spinbox(self.authorFilterFrame,values = authorList)
		#self.authorSearchField.grid(row = 0,pady = 25,padx = 8,column = 0)
		#self.authorSearchSubmit = Button(self.authorFilterFrame,text = "Submit",relief = RAISED,fg = textLight,bg = buttonColour,font = myFont,width = 7) 
		#self.authorSearchSubmit.grid(row = 0,column = 1,pady = 25,padx = 8)
		





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
		self.fineLabel.grid(row = 0,padx = 70,pady = 40,sticky = E+W+N)
		
		#Loading books in mainshelf
		
		loadShelfView(self)


		#Load My Issued Books
		loadIssuedBooks(self)


		#
		self.currentView.totalFineView.details = Button(self.currentView.totalFineView,text = "Details",relief = RAISED,fg = textLight,bg = buttonColour,font = myFont,width = 15,command = lambda: fineDetails(self,personDetailsObject))
		self.currentView.totalFineView.details.grid(row = 1,sticky = W+E+S,padx = 70)
		



	def bookClick(self,bookId,bookWidget):
		print(bookId,"selected")
		if hasattr(self,"removeBookMode"):
			if(self.removeBookMode == True):
				if(booksMasterObject[bookId]["isIssued"] == False):
					bookWidget.grid_forget()
					del booksMasterObject[bookId]
					f = open(booksFile,"wb")
					pickle.dump(booksMasterObject,f)
					f.close()
					return

		self.currentView.myDetailsView.grid_forget()
		if(self.currentView.bookDetailsView.winfo_exists()):
			self.currentView.bookDetailsView.destroy()
		self.currentView.bookDetailsView = LabelFrame(self.currentView.mainViewFrame,text = "Book Details ",height = 240,width = 300,bg = backgroundColour,fg = textLight )
		self.currentView.bookDetailsView.grid(row = 2,column  =2,padx = 5,pady = 5,sticky = N+S+E+W)
		
		#self.bookIssueTop = Toplevel(bg = backgroundColour)
		#self.bookIssueTop.title("Issue Books")
		#self.bookIssueFrame = LabelFrame(self.bookIssueTop,text = "Issue Books",bg = backgroundColour,fg = textLight)
		#self.bookIssueFrame.pack(fill = BOTH,expand = YES)
		Label(self.currentView.bookDetailsView,text = "Title",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 0,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = "Author",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 1,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = "Publisher",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 2,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = "Genre",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = "Added By",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 4,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = "Added On",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 5,column = 0,padx = 5,pady = 2,sticky = W)

		for index in range(6):
			Label(self.currentView.bookDetailsView,text = ":",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = index,column = 1,padx = 2,pady = 2,sticky = W)
		
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["title"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 0,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["author"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 1,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["publisher"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 2,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["genre"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["addedBy"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 4,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["addedOn"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 5,column = 2,padx = 5,pady = 2,sticky = W)
		
		self.issueEmptySpace = Label(self.currentView.bookDetailsView,bg = backgroundColour)
		self.issueEmptySpace.grid(row = 6,columnspan = 3)
		if booksMasterObject[bookId]["isIssued"] is False:
			self.issueButton = Button(self.currentView.bookDetailsView,text = "Issue",relief = RAISED,bg = buttonColour,fg = textLight,font = myFont,command = lambda :self.issueBook(bookId))
			self.issueButton.grid(columnspan = 2, row = 8,padx = 10,column = 1)	
		else:
			Label(self.currentView.bookDetailsView,text = "Issued By",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 6,column = 0,padx = 5,pady = 2,sticky = W)
			Label(self.currentView.bookDetailsView,text = ":",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 6,column = 1,padx = 2,pady = 2,sticky = W)
			Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["issuedBy"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 6,column = 2,padx = 5,pady = 2,sticky = W)
			
			Label(self.currentView.bookDetailsView,text = "Issued On",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 7,column = 0,padx = 5,pady = 2,sticky = W)
			Label(self.currentView.bookDetailsView,text = ":",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 7,column = 1,padx = 2,pady = 2,sticky = W)
			Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["issuedOn"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 7,column = 2,padx = 5,pady = 2,sticky = W)
				
		


	def issueBook(self,bookId):
		#if student check limit
		if(self.personDetailsObject["personType"] == "Staff"):
			if staffMasterObject[self.personDetailsObject["employeeId"]]["issuedBookCounter"]>=6:
				return

		if(self.personDetailsObject["personType"] == "Student"):
			if studentMasterObject[self.personDetailsObject["studentPrimaryKey"]]["issuedBookCounter"]>=3:
				return

		booksMasterObject[bookId]["isIssued"] = True
		booksMasterObject[bookId]["issuedBy"] = self.personDetailsObject["name"]
		booksMasterObject[bookId]["issuedOn"] = (time.strftime("%d"),time.strftime("%m"),time.strftime("%y"))
		booksMasterObject[bookId]["expectedReturn"] = (str(int(time.strftime("%d"))+1),time.strftime("%m"),time.strftime("%y"))

		if(self.personDetailsObject["personType"] == "Staff"):
			staffMasterObject[self.personDetailsObject["employeeId"]]["issuedBooks"].append(bookId)
			staffMasterObject[self.personDetailsObject["employeeId"]]["issuedBookCounter"]+=1
			
			booksMasterObject[bookId]["issueHistory"].append(((int(time.strftime("%d")),int(time.strftime("%m")),int(time.strftime("%y"))),self.personDetailsObject["employeeId"]))
			f = open(staffFile,"wb")
			pickle.dump(staffMasterObject,f)
			f.close()
		else:
			studentMasterObject[self.personDetailsObject["studentPrimaryKey"]]["issuedBooks"].append(bookId)
			studentMasterObject[self.personDetailsObject["studentPrimaryKey"]]["issuedBookCounter"]+=1;
			
			booksMasterObject[bookId]["issueHistory"].append(((int(time.strftime("%d")),int(time.strftime("%m")),int(time.strftime("%y"))),self.personDetailsObject["studentPrimaryKey"]))
			f = open(studentFile,"wb")
			pickle.dump(studentMasterObject,f)
			f.close()

		f = open(booksFile,"wb")
		pickle.dump(booksMasterObject,f)
		f.close()
		#self.bookIssueTop.destroy()

		self.currentView.bookDetailsView.grid_forget()
		self.currentView.myDetailsView.grid(row = 2,column  =2,padx = 5,pady = 5,sticky = N+S+E+W)
		if self.myIssuedBooksInnerView is not None:
			self.myIssuedBooksInnerView.destroy()
		if self.currentView.moreFrame !=None:
			if self.currentView.moreFrame.winfo_exists():
				self.currentView.moreFrame.destroy()
				showMore(currentGenre,self)
			else:
				loadShelfView(self)
		else:
			loadShelfView(self)

		loadIssuedBooks(self)

		print(staffMasterObject)



	def issuedBookClick(self,bookId):
		print("Isssued",bookId)
		if(self.currentView.bookDetailsView.winfo_exists()):
			self.currentView.bookDetailsView.destroy()
		self.currentView.myDetailsView.grid_forget()
		self.currentView.bookDetailsView = LabelFrame(self.currentView.mainViewFrame,text = "Book Details ",height = 240,width = 300,bg = backgroundColour,fg = textLight )
		self.currentView.bookDetailsView.grid(row = 2,column  =2,padx = 5,pady = 5,sticky = N+S+E+W)
		

		Label(self.currentView.bookDetailsView,text = "Title",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 0,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = "Author",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 1,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = "Publisher",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 2,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = "Genre",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = "Added By",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 4,column = 0,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = "Added On",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 5,column = 0,padx = 5,pady = 2,sticky = W)

		for index in range(6):
			Label(self.currentView.bookDetailsView,text = ":",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = index,column = 1,padx = 2,pady = 2,sticky = W)
		
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["title"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 0,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["author"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 1,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["publisher"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 2,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["genre"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 3,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["addedBy"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 4,column = 2,padx = 5,pady = 2,sticky = W)
		Label(self.currentView.bookDetailsView,text = booksMasterObject[bookId]["addedOn"],padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textMainView).grid(row = 5,column = 2,padx = 5,pady = 2,sticky = W)
		
		self.issueEmptySpace = Label(self.currentView.bookDetailsView,bg = backgroundColour)
		self.issueEmptySpace.grid(row = 6,columnspan = 3,padx = 10)

		self.readButton = Button(self.currentView.bookDetailsView,text = "Read",relief = RAISED,bg = buttonColour,fg = textLight,font = myFont,command = lambda:readBook(bookId))
		self.readButton.grid(column = 0, row = 7,padx = 40)


		self.returnButton = Button(self.currentView.bookDetailsView,text = "Return",relief = RAISED,bg = buttonColour,fg = textLight,font = myFont,command = lambda :self.returnBook(bookId))
		self.returnButton.grid(column = 2, row = 7,padx = 5)

	def returnBook(self,bookId):
		print("return",bookId)


		if(self.personDetailsObject["personType"] == "Staff"):
			staffMasterObject[self.personDetailsObject["employeeId"]]["issuedBooks"].remove(bookId)
			staffMasterObject[self.personDetailsObject["employeeId"]]["issuedBookCounter"]-=1
			f = open(staffFile,"wb")
			pickle.dump(staffMasterObject,f)
			f.close()
		else:
			studentMasterObject[self.personDetailsObject["studentPrimaryKey"]]["issuedBooks"].remove(bookId)
			studentMasterObject[self.personDetailsObject["studentPrimaryKey"]]["issuedBookCounter"]-=1
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
		#self.myBooksTop.destroy()
		self.currentView.bookDetailsView.grid_forget()
		self.currentView.myDetailsView.grid(row = 2,column  =2,padx = 5,pady = 5,sticky = N+S+E+W)
		self.myIssuedBooksInnerView.destroy()
		if self.currentView.moreFrame !=None:
			if self.currentView.moreFrame.winfo_exists():
				showMore(currentGenre,self)
			else:
				loadShelfView(self)
		else:
			loadShelfView(self)
			
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

		Button(self.currentView.addRemoveBooksView,text = "Add Book",fg = textLight,bg = buttonColour,width = 10,command = self.addBook).grid(column = 0,row = 0,padx = 30,pady = 50)
		Button(self.currentView.addRemoveBooksView,text = "Remove Book",fg = textLight,bg = buttonColour,width = 10,command = self.removeBooks).grid(column = 1,row = 0,padx = 0,pady = 50)

		self.currentView.addRemoveBooksView.modeLabel  = Label(self.currentView.addRemoveBooksView,bg = backgroundColour,text = "Normal mode",fg = "red")
		self.currentView.addRemoveBooksView.modeLabel.grid(row = 1,columnspan = 2,pady = 10)  

		self.removeBookMode = False
	def addBook(self):
		self.addBookTop = Toplevel(bg = backgroundColour)
		self.addBookFrame = LabelFrame(self.addBookTop,text = "Add a book",bg = backgroundColour,fg = textLight,height = 700,width = 500)
		self.addBookFrame.pack(fill = BOTH,expand = YES,ipady = 20,ipadx = 15,padx = 20,pady = 20)
		self.titleLabel = Label(self.addBookFrame,text = "Name Of Book",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.titleLabel.grid(row = 0,column = 0,pady = 3,padx = 5,sticky = W) 
		self.titleEntry  = Entry(self.addBookFrame);
		self.titleEntry.grid (row = 0,column = 2,pady = 3,padx = 5 )
		

		self.authorLabel1 = Label(self.addBookFrame,text = "Author Name :1",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.authorLabel1.grid(row = 1,column = 0,pady = 3,padx = 5,sticky = W) 
		self.authorEntry1  = Entry(self.addBookFrame);
		self.authorEntry1.grid(row = 1,column = 2,pady = 3,padx = 5 )
		
		self.authorLabel2 = Label(self.addBookFrame,text = "Author Name:2",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.authorLabel2.grid(row = 2,column = 0,pady = 3,padx = 5,sticky = W) 
		self.authorEntry2  = Entry(self.addBookFrame);
		self.authorEntry2.grid(row = 2,column = 2,pady = 3,padx = 5 )
		
		self.authorLabel3 = Label(self.addBookFrame,text = "Author Name:3",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.authorLabel3.grid(row = 3,column = 0,pady = 3,padx = 5,sticky = W) 
		self.authorEntry3  = Entry(self.addBookFrame);
		self.authorEntry3.grid(row = 3,column = 2,pady = 3,padx = 5 )
		
		self.publisherLabel = Label(self.addBookFrame,text = "Publisher",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.publisherLabel.grid(row = 4,column = 0,pady = 3,padx = 5,sticky = W) 
		self.publisherEntry  = Entry(self.addBookFrame);
		self.publisherEntry.grid(row = 4,column = 2,pady = 3,padx = 5 )
		
		self.genreLabel = Label(self.addBookFrame,text = "Genre",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.genreLabel.grid(row = 5,column = 0,pady = 3,padx = 5,sticky = W) 
		self.genreEntry  = Spinbox(self.addBookFrame,values = ("Classic","Mystery","Scifi","Comedy","Horror","Non Fiction","Textbook"),width = 15,justify = RIGHT);
		self.genreEntry.grid(row = 5,column = 2,pady = 3,padx = 5,sticky = W )
		
		self.isbnLabel = Label(self.addBookFrame,text = "ISBN",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.isbnLabel.grid(row = 6,column = 0,pady = 3,padx = 5,sticky = W) 
		self.isbnEntry  = Entry(self.addBookFrame);
		self.isbnEntry.grid(row = 6,column = 2,pady = 3,padx = 5 )

		self.bookPathLabel = Label(self.addBookFrame,text = "Book Path",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.bookPathLabel.grid(row = 7,column = 0,pady = 3,padx = 5,sticky = W) 
		self.bookPathEntry  = Entry(self.addBookFrame);
		self.bookPathEntry.grid(row = 7,column = 2,pady = 3,padx = 5 )


		for index in range(8): 
			Label(self.addBookFrame,text = ":",bg = backgroundColour).grid(row = index,column = 1)

		self.emptySpace = Label(self.addBookFrame,bg = backgroundColour)
		self.emptySpace.grid(row = 8,columnspan = 3)
		self.submitForm = Button(self.addBookFrame,text = "Submit",relief = RAISED,bg = buttonColour,fg = textLight,font = myFont,command = lambda :self.submitBookForm(self.titleEntry.get(),self.authorEntry1.get(),self.authorEntry2.get(),self.authorEntry3.get(),self.publisherEntry.get(),self.genreEntry.get(),self.isbnEntry.get(),self.bookPathEntry.get()))
		self.submitForm.grid(columnspan = 3, row = 9)
		

	def submitBookForm(self,title,author,author2,author3,publisher,genre,isbn,bookPath):
		#Also include added on, added by
		#cover image can be empty
		if(isEmptyChecker(title,author,publisher,genre,isbn,bookPath)):
			self.emptySpace.config(text = "Some fields empty",fg = "red")
		elif (not isbn.isdigit()) or (len(isbn) != 10):
			self.emptySpace.config(text = "ISBN should be a 10 digit integer",fg = "red")
		elif genre not in genreList:
			self.emptySpace.config(text = "Please choose from given Genre",fg = "red")
		elif not os.path.exists(bookPath+".gif"):
			self.emptySpace.config(text = "Given Book path does't exist",fg = "red")
		else:
			#check if similar isbn already exists
			counter = 0
			while(isbn+":"+str(counter) in booksMasterObject):
				counter+=1
			bookId = isbn+":"+str(counter)
			booksMasterObject[bookId] = {}
			if author not in authorList:
				authorList.append(author)


			if author2 is not None:
				author = author+':'+author2
				if author2 not in authorList:
					authorList.append(author2)
			if author3 is not None:
				author = author+':'+author3
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

			if self.currentView.moreFrame !=None:
				if self.currentView.moreFrame.winfo_exists():
					showMore(currentGenre,self)
				else:
					loadShelfView(self)
			else:
				loadShelfView(self)
		
			#currentPerson = Staff(self.master,staffMasterObject[employeeId])


	def removeBooks(self):
		if(self.removeBookMode == False):
			self.currentView.addRemoveBooksView.modeLabel.configure(text = "Warning : Now in remove book Mode")
			self.removeBookMode = True
		else :
			self.currentView.addRemoveBooksView.modeLabel.configure(text = "Normal Mode")
			self.removeBookMode = False

		

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
		self.dobMonthEntry = Spinbox(self.newFrame,width = 10,justify = RIGHT,values = monthList)
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
		elif dateNotRight(dobDay,dobMonth,dobYear):
			self.emptySpace.config(text = "D.O.B date incorrect",fg = "red")
		elif not (gender=="Male" or gender == "Female"):
			self.emptySpace.config(text = "Gender data invalid",fg = "red")
		elif not phone.isdigit():
			self.emptySpace.config(text = "Enter valid phone No",fg = "red")
		elif not employeeId.isdigit():
			self.emptySpace.config(text = "Enter valid Employee Id",fg = "red")
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
			staffMasterObject[employeeId]["issuedBookCounter"] = 0
			


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
		self.branchEntry  = Spinbox(self.newFrame,width = 6,justify = RIGHT,values = ("COE","ECE","ICE","IT","MPAE","BT"))
		self.branchEntry.grid(row = 6,column = 2,pady = 3,padx = 5,sticky = W )
		
		self.yearLabel = Label(self.newFrame,text = "Year",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight)
		self.yearLabel.grid(row = 7,column = 0,pady = 3,padx = 5,sticky = W)
		self.yearEntry  = Spinbox(self.newFrame,width = 6,justify = RIGHT,from_ = 12,to = 16)
		self.yearEntry.grid(row = 7,column = 2,pady = 3,padx = 5,sticky = W )
		
		Label(self.newFrame,text = "Date Of Birth",padx = 5,pady = 2,bg = backgroundColour,font = myFont,fg = textLight).grid(pady = 3,padx = 5,row = 8,column = 0,sticky = W)
		self.dobDayEntry = Entry(self.newFrame,width = 10,justify = RIGHT)
		self.dobDayEntry.insert(END,"Enter day")
		self.dobDayEntry.grid(row = 9,column = 0,pady = 3,padx = 5)
		self.dobMonthEntry = Spinbox(self.newFrame,width = 10,justify = RIGHT,values = monthList)
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
		elif dateNotRight(dobDay,dobMonth,dobYear):
			self.emptySpace.config(text = "D.O.B date incorrect",fg = "red")
		elif not (gender=="Male" or gender == "Female"):
			self.emptySpace.config(text = "Gender data invalid",fg = "red")
		elif branch not in branchList:
			self.emptySpace.config(text = "Choose from given Branches",fg = "red")
		elif int(rollNo) not in range(1,1000):
			self.emptySpace.config(text = "Roll No not in range",fg = "red")
		elif int(year) not in range(12,17):
			self.emptySpace.config(text = "Enrollment year not in range",fg = "red")
		elif not phone.isdigit():
			self.emptySpace.config(text = "Enter valid phone No",fg = "red")
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
			studentMasterObject[studentPrimaryKey]["issuedBookCounter"] = 0


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




#Gives option to choose between existing or new user
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




#Starting Frame for login
initFrame = Frame(root,bg = backgroundColour)
initFrame.pack(fill = BOTH,expand = YES)

#Putting appropriate buttons to choose between student and staff
staffInitButton = Button(initFrame,text = "Staff Login",relief = RAISED,height = 5,width = 50,bg= buttonColour,fg = textLight,font = myFont,command = lambda: staffInit(root,initFrame))
staffInitButton.pack(side = TOP,padx = 100,pady = 50)

studentInitButton = Button(initFrame,text = "Student Login",relief = RAISED,height = 5,width = 50,bg = buttonColour,fg = textLight,font = myFont,command = lambda :studentInit(root,initFrame))
studentInitButton.pack(side = TOP,padx = 100,pady = 50)

root.mainloop()
