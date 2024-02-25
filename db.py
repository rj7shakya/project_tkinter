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