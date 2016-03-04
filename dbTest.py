import pickle

f = open("test/booksDb","rb")
obj = pickle.load(f)
print (obj)
