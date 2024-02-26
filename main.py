from tkinter import *
from books import book_setup
from authors import author_setup,author_update_setup

root = Tk()
books = Frame(root)
authors = Frame(root)
author_update = Frame(root)

books.place(x=0,y=0,relwidth=1,relheight=1)
authors.place(x=0,y=0,relwidth=1,relheight=1)
author_update.place(x=0,y=0,relwidth=1,relheight=1)
books.lift()

book_setup(books,lambda: authors.lift())
author_setup(authors,lambda: books.lift(),lambda: author_update.lift())
author_update_setup(author_update,[],lambda: authors.lift())

root.geometry('320x300')
root.mainloop()