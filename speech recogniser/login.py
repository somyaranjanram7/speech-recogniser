import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call


def Okay():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",port=3306,database="projectable")
    mycursor=mysqldb.cursor()
    username=e1.get()
    password=e2.get()

    sql="select * from login where username = %s and password = %s"
    mycursor.execute(sql,[(username),(password)])
    results=mycursor.fetchall()
    if results:
        messagebox.showinfo("Login Successfully")
        root.destroy()
        call(["python", "main.py"])
        return True
    else:
        messagebox.showinfo("","Incorrect Username and Password")
        return False

def New():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", port=3307,database="projectable")
    mycursor = mysqldb.cursor()
    username = e1.get()
    password = e2.get()

    sql = "insert into login values(%s,%s)"
    mycursor.execute(sql, [(username), (password)])
    mysql.commit()
    messagebox.showinfo("User added successfully")

root =Tk()
root.title("Login")
root.config(bg="blue4")
root.geometry("350x230")
global e1
global e2

Label(root, text="USERNAME",font=('italic', 13), fg='hotpink',bg='blue4').place(x=40,y=30)
Label(root, text="PASSWORD",font=('italic', 13), fg='hotpink',bg='blue4').place(x=40,y=60)

e1=Entry(root)
e1.place(x=180,y=30)
e1.config(bg='blue4',fg='white')

e2=Entry(root)
e2.place(x=180,y=60)
e2.config(show='*',bg='blue4',fg='white')

Button(root,text="Login",font=('bold', 13), bg='red', fg='white',relief=RAISED,borderwidth=10,
       command=Okay,height=2,width=10).place(x=40,y=130)
Button(root,text="Create",font=('bold', 13), bg='red', fg='white',relief=RAISED,borderwidth=10,
       command=New,height=2,width=10).place(x=180,y=130)
root.mainloop()
