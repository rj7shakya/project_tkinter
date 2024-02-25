from tkinter import *

def book_setup(root,gotoAuthor):
  
  b1 = Button(root,text='Go to Authors',command=gotoAuthor)
  b1.pack(side='bottom')