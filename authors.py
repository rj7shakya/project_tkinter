from tkinter import *
from tkinter import ttk,messagebox
from db import get_authors,insert_author,delete_author

def author_setup(root,gotoBooks,gotoUpdate):
  tree = ttk.Treeview(root,columns=('a','b'))
  tree['show'] = 'headings'
  tree.heading('a',text='id')
  tree.heading('b',text='name')
  tree.column('a',width=40,anchor=CENTER)
  tree.column('b',width=100,anchor=CENTER)
  tree.place(x=140,y=20)
  data = get_authors()
  
  for id,name in data:
    tree.insert("",END,values=(id,name))
  
  r1 = Frame(root)
  l1 = Label(r1,text='Author Id')
  l1.pack()
  e1 = Entry(r1,width=12)
  e1.pack()
  l2 = Label(r1,text='Author Name')
  l2.pack()
  e2 = Entry(r1,width=12)
  e2.pack()
  
  def add_item():
    completed = insert_author(e1.get(),e2.get())
    if completed:
      tree.insert("",END,values=(e1.get(),e2.get()))
      e1.delete(0,END)
      e2.delete(0,END)
  
  b1 = Button(r1,text='Add',command=add_item)
  b1.pack()
  
  def delete_item():
    selected = tree.focus()
    if not selected:
      messagebox.askokcancel('a','no item selected')
    else:
      res = messagebox.askyesno('b','Are you sure you want to delete ?')
      if res:
        values = tree.item(selected,'values')
        resp = delete_author(values[0])
        if resp:
          tree.delete(selected)
  
  b2 = Button(r1,text='Delete',command=delete_item)
  b2.pack()
  
  b2 = Button(r1,text='Update',command=lambda:gotoUpdate())
  b2.pack()
  
  r1.place(x=10,y=20)
  
  b1 = Button(root,text='Go to Books',command=gotoBooks)
  b1.pack(side='bottom')
  
  
def author_update_setup(root,data,gotoAuthors):
  b1 = Button(root,text='Cancel',command=gotoAuthors)
  b1.pack(side='bottom')
  