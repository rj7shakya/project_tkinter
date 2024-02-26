import psycopg2
from tkinter import messagebox

connection = psycopg2.connect(
	host='localhost',
	database='project',
	user='postgres',
	password='inspiron'
)

cursor = connection.cursor()


def get_authors():
  cursor.execute("select * from authors")
  rows = cursor.fetchall()
  return rows

def insert_author(id,name):
  try:
    cursor.execute(f"insert into authors values ({id},'{name}')")
    connection.commit()
    return True
  
  except psycopg2.Error as error:
    messagebox.showerror('a',error)
    return False
    

def delete_author(id):
  try:
    cursor.execute(f"delete from authors where id ={id}")
    connection.commit()
    return True
  
  except psycopg2.Error as error:
    messagebox.showerror('a',error)
    return False
  
  
def get_books():
  cursor.execute(""" select books.id, books.name, authors.name
                      from books inner join authors
                      on books.author_id = authors.id;   """)
  rows = cursor.fetchall()
  return rows


def insert_book(id,name,author_id):
  try:
    cursor.execute(f"insert into books values ({id},'{name}',{author_id})")
    connection.commit()
    return True
  
  except psycopg2.Error as error:
    messagebox.showerror('a',error)
    return False
  
  
def delete_book(id):
  try:
    cursor.execute(f"delete from books where id ={id}")
    connection.commit()
    return True
  
  except psycopg2.Error as error:
    messagebox.showerror('a',error)
    return False