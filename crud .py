import customtkinter as ctk
import mysql.connector
from CTkMessagebox import CTkMessagebox

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="myk")
mycursor = mydb.cursor()

def insert():
    uname = txtname.get()
    mail = txtmail.get()
    sql = "INSERT INTO user (name, email) VALUES (%s, %s)"
    values = (uname, mail)
    mycursor.execute(sql, values)
    mydb.commit()
    if mycursor.rowcount == 1:
        txtname.delete(0, ctk.END)
        txtmail.delete(0, ctk.END)
        CTkMessagebox(title="Database", message="Record Inserted")

def update():
    id = txtid.get()
    uname = txtname.get()
    mail = txtmail.get()
    sql = "UPDATE user SET name=%s, email=%s WHERE id=%s"
    values = (uname, mail, id)
    mycursor.execute(sql, values)
    mydb.commit()
    if mycursor.rowcount == 1:
        txtid.delete(0, ctk.END)
        txtname.delete(0, ctk.END)
        txtmail.delete(0, ctk.END)
        CTkMessagebox(title="Database", message="Record Updated")

def delete():
    id = txtid.get()
    sql = "DELETE FROM user WHERE id=%s"
    values = (id,)
    mycursor.execute(sql, values)
    mydb.commit()
    if mycursor.rowcount == 1:
        txtid.delete(0, ctk.END)
        txtname.delete(0, ctk.END)
        txtmail.delete(0, ctk.END)
        

def searchid():
    id = txtid.get()
    sql = "SELECT * FROM user WHERE id=%s"
    values = (id,)
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    txtname.delete(0, ctk.END)
    txtmail.delete(0, ctk.END)
    if len(myresult) == 1:
        for x in myresult:
            txtname.insert(0, x[1])
            txtmail.insert(0, x[2])
    else:
        CTkMessagebox(title="Database", message="No record found")

root = ctk.CTk()
root.geometry("400x400")
root.title("User Database Management")

frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20, fill='both', expand=True)

txtid = ctk.CTkEntry(frame, placeholder_text="Enter ID")
txtid.pack(pady=(0, 10), fill='x')

searchbtn = ctk.CTkButton(frame, text="Search", command=searchid)
searchbtn.pack(pady=(0, 10))

txtname = ctk.CTkEntry(frame, placeholder_text="Enter Name")
txtname.pack(pady=(0, 10), fill='x')

txtmail = ctk.CTkEntry(frame, placeholder_text="Enter Email")
txtmail.pack(pady=(0, 20), fill='x')

insertbtn = ctk.CTkButton(frame, text="Insert", command=insert)
insertbtn.pack(pady=(0, 10))

updatebtn = ctk.CTkButton(frame, text="Update", command=update)
updatebtn.pack(pady=(0, 10))

deletebtn = ctk.CTkButton(frame, text="Delete", command=delete)
deletebtn.pack(pady=(0, 10))

root.mainloop()
