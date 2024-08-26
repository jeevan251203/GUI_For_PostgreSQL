import psycopg2
from tkinter import *

conn = psycopg2.connect(
            host="localhost",
            dbname="postgres",
            user="postgres",
            password="1234",
            port=5432)

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS student 
(ID int primary key,Name varchar(30),CGPA float)''')

conn.commit()

def insert():
    window1 = Toplevel()
    Label(window1, text="ID").grid(row=0, column=0)
    Label(window1, text="NAME").grid(row=1, column=0)
    Label(window1, text="CGPA").grid(row=2, column=0)
    id = Entry(window1, width=50)
    name = Entry(window1, width=50)
    cgpa = Entry(window1, width=50)
    id.grid(row=0, column=1)
    name.grid(row=1, column=1)
    cgpa.grid(row=2, column=1)

    Button(window1, text="ADD", command=lambda: doinsert(id.get(),name.get(), cgpa.get())).grid(row=3,column=1)
    Button(window1, text="EXIT", command=lambda: window1.destroy()).grid(row=3, column=0)
    def doinsert(a,b,c):
        cur.execute(f"INSERT INTO student VALUES ({a},'{b}',{c}) ")
        conn.commit()
        print('RECORD INSERTED')
        def clear():
            id.delete(0,END)
            name.delete(0,END)
            cgpa.delete(0,END)
        clear()

def delete():
    window2 = Toplevel()
    Label(window2, text="ENTER ID").grid(row=0, column=0)
    delete_value = Entry(window2, width=50)
    delete_value.grid(row=0, column=1)
    Button(window2, text="DELETE", command=lambda: dodelete(delete_value.get())).grid(row=1, column=1)

    def dodelete(b):
        cur.execute(f"DELETE FROM student WHERE id = {b}")
        conn.commit()
        print("RECORD DELETED SUCCESSFULLY")
        window2.destroy()

def update():
    window3 = Toplevel()
    Label(window3, text="ID").grid(row=0, column=0)
    Label(window3, text="NAME").grid(row=1, column=0)
    Label(window3, text="CGPA").grid(row=2, column=0)
    id = Entry(window3, width=50)
    name = Entry(window3, width=50)
    cgpa = Entry(window3, width=50)
    id.grid(row=0, column=1)
    name.grid(row=1, column=1)
    cgpa.grid(row=2, column=1)

    def do_update(a,b,c):
        cur.execute(f"UPDATE student SET name='{b}',cgpa={c} WHERE id ={a}")
        conn.commit()
        window3.destroy()
        print('UPDATED SUCCESSFULLY')

    Button(window3, text="UPDATE", command=lambda: do_update(id.get(), name.get(), cgpa.get())).grid(row=3, column=1)


a = Tk()
a.title("STUDENT MANAGEMENT SYSTEM")
Button(a, text="INSERT", width=50,command=lambda :insert()).grid(row=0, column=0)
Button(a, text="DELETE", width=50,command=lambda :delete()).grid(row=1, column=0)
Button(a, text="EXIT", width=50, command=lambda: a.quit()).grid(row=3, column=0)
Button(a, text="UPDATE", width=50, command=lambda:update()).grid(row=2, column=0)

a.mainloop()
conn.close()