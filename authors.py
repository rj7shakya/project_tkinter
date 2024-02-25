from tkinter import *

def author_setup(root,gotoBooks):
  
  b1 = Button(root,text='Go to Books',command=gotoBooks)
  b1.pack(side='bottom')
  