from tkinter import *
from tkinter import ttk,messagebox

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
  
  data = [(1,'aa','ram'),(2,'bb','shyam')]
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
  
  def insert_book():
    tree.insert("",END,values=(e1.get(),e2.get(),e2.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
  
  b1 = Button(r1,text="Add",command=insert_book)
  b1.pack()
  
  def delete_book():
    selected = tree.focus()
    if not selected:
      messagebox.askokcancel('a','no item selected')
    else:
      res = messagebox.askyesno('b','Are you sure you want to delete ?')
      if res:
        tree.delete(selected)
  
  b2 = Button(r1,text="Delete",command=delete_book)
  b2.pack() 
  
  r1.place(x=10,y=20)
  
  b1 = Button(root,text='Go to Authors',command=gotoAuthor)
  b1.pack(side='bottom')