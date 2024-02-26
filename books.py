from tkinter import *
from tkinter import ttk,messagebox
from db import get_books,insert_book,delete_book

def book_setup(root,gotoAuthor):
  tree = ttk.Treeview(root,columns=('a','b','c'))
  tree['show'] = 'headings'
  tree.heading('a',text='id')  
  tree.heading('b',text='name')  
  tree.heading('c',text='author')
  tree.column('a',width=40,anchor=CENTER)  
  tree.column('b',width=60,anchor=CENTER)  
  tree.column('c',width=60,anchor=CENTER)  
  tree.place(x=140,y=20)
  
  data = get_books()
  for id,name,author in data:
    tree.insert("",END,values=(id,name,author))
    
  r1 = Frame(root)
  l1 = Label(r1,text="Book Id")
  l1.pack()
  e1 = Entry(r1,width=12)
  e1.pack()
  
  l2 = Label(r1,text="Book Name")
  l2.pack()
  e2 = Entry(r1,width=12)
  e2.pack()
  
  l3 = Label(r1,text="Author Id")
  l3.pack()
  e3 = Entry(r1,width=12)
  e3.pack()
  
  def insert_item():
    res = insert_book(e1.get(),e2.get(),e3.get())
    if res:
      data = get_books()[-1]
      tree.insert("",END,values=data)
      e1.delete(0,END)
      e2.delete(0,END)
      e3.delete(0,END)
  
  b1 = Button(r1,text="Add",command=insert_item)
  b1.pack()
  
  def delete_item():
    selected = tree.focus()
    if not selected:
      messagebox.askokcancel('a','no item selected')
    else:
      res = messagebox.askyesno('b','Are you sure you want to delete ?')
      if res:
        values = tree.item(selected,'values')
        resp = delete_book(values[0])
        if resp:
          tree.delete(selected)
  
  b2 = Button(r1,text="Delete",command=delete_item)
  b2.pack() 
  
  r1.place(x=10,y=20)
  
  b1 = Button(root,text='Go to Authors',command=gotoAuthor)
  b1.pack(side='bottom')