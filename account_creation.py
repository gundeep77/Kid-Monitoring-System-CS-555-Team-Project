
from tkinter import *
import sqlite3

def register_user():

    email_info = email.get()
    password_info = password.get()
    phoneNumber_info = phoneNumber.get()
    cfnpassword_info = cfn_password.get()

    params = (email_info, password_info, phoneNumber_info )

    db = sqlite3.connect ("userdata.db")
    cursor = db.cursor() 
    cursor.execute (''' CREATE TABLE IF NOT EXISTS credentials (email text, password text, phoneNumber Integer )''')
    
    if (cfnpassword_info.casefold() == password_info.casefold()):

        cursor.execute('''INSERT INTO credentials VALUES (?,?,?)''', params)
        db.commit()
        Label (screen1, text = "Registration successful", fg = "green", font = ("Calibri", 11)).pack()

        email_entry.delete (0, END)
        password_entry.delete (0, END)
        phoneNumber_entry.delete (0, END)
    else :
        Label (screen1, text = "Passwords do not match", fg = "green", font = ("Calibri", 11)).pack()
        

def register():

    global screen1
    screen1 = Toplevel(screen)
    screen1.title ("Register")
    screen1.geometry("300x250")

    global email
    global password
    global cfn_password
    global phoneNumber
    global email_entry
    global password_entry
    global phoneNumber_entry
    global cfnpassword_entry


    email = StringVar()
    password = StringVar()
    cfn_password = StringVar()
    phoneNumber = IntVar()


    Label( screen1, text = "Please enter details below").pack()
    Label( screen1, text = "").pack()
    Label( screen1, text = "Email *").pack()
    email_entry = Entry(screen1, textvariable= email)
    email_entry.pack()
    Label( screen1, text = "").pack()

    Label (screen1, text = "Password *").pack()
    password_entry = Entry(screen1, textvariable= password)
    password_entry.pack()
    Label( screen1, text = "").pack()

    Label (screen1, text = "Confirm password *").pack()
    cfnpassword_entry = Entry(screen1, textvariable= cfn_password)
    cfnpassword_entry.pack()
    Label( screen1, text = "").pack()

    Label (screen1, text = "Phone Number *").pack()
    phoneNumber_entry = Entry(screen1, textvariable= phoneNumber)
    phoneNumber_entry.pack()
    
    Label(screen1, text = "").pack()
    Button (screen1, text = "Register", width = "10", height = "1", command= register_user).pack()

def main_screen():
    global screen
    screen = Tk ()
    screen.geometry ("300x250")
    screen.title("BabyMonitor")
    Label (text = "Account creation", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button (text = "Register", width = "10", height = "2", command=register).pack()
    screen.mainloop()

main_screen()
