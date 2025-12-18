import sqlite3

conn=sqlite3.connect("Emergency_contect.db")
cursor=conn.cursor()

#create table
cursor.execute("""CREATE TABLE IF NOT EXISTS contects (
               id INTEGER PRIMARY KEY ,
               name VARCHAR(25) NOT NULL,
               phone NUMBER(10),
               email VARCHAR(25),
               relation VARCHAR(25))""")
conn.commit()

#add contect

def add_contect(name,phone,email,relation):
    cursor.execute("INSERT INTO contects (name,phone,email,relation) VALUES (?,?,?,?)",(name,phone,email,relation))
    conn.commit()
    print(f"Contect {name} added successfully!....")

#view contect

def view_contect():
    cursor.execute("SELECT * FROM contects")
    for items in cursor.fetchall():
        print(items)

#delete contect

def delete_contect(contact_id):
    cursor.execute("DELETE FROM contects WHERE id=?",(contact_id,))
    conn.commit()
    print(f"Contact {contact_id} was deleted successfully!...")
def delete_all():
    cursor.execute("DELETE FROM contects")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='contects'")
    conn.commit()

#add_contect("Mei",8825,"meiyanban70@gmail.com",'friend')

 