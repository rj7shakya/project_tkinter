from tkinter import *
from books import book_setup
from authors import author_setup

root = Tk()
books = Frame(root)
authors = Frame(root)

books.place(x=0,y=0,relwidth=1,relheight=1)
authors.place(x=0,y=0,relwidth=1,relheight=1)
books.lift()

book_setup(books,lambda: authors.lift())
author_setup(authors,lambda: books.lift())

root.geometry('320x300')
root.mainloop()