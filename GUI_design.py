from sqlite3 import Row
from tkinter import *
from turtle import heading
from unittest import TextTestResult
from PIL import ImageTk, Image
from numpy import place

root = Tk()

root.title("Baby Monitoring System")
root.geometry("700x500")


def get_values():
    print(f"Username is {user_entry.get()}")
    print(f"Password is {pass_entry.get()}")


photo = PhotoImage(file="child.png")
bg_label = Label(root, image=photo)
bg_label.place(x=0, y=0)

heading_frame = Frame(root, borderwidth=4, relief=SUNKEN)
heading_frame.place(x=320, y=150)
heading_text = Label(heading_frame, text="Welcome to Baby Monitoring System!\nPlease sign in here:",
                     fg="yellow", font="comicsansms 16 bold", bg="brown")
heading_text.grid()

login_frame = Frame(root, borderwidth=6)
login_frame.place(x=320, y=250)

user_label = Label(login_frame, text="Username:")
user_label.grid(row=0, column=0)

password_label = Label(login_frame, text="Password:")
password_label.grid(row=1, column=0)

user_value = StringVar()
pass_value = StringVar()

user_entry = Entry(login_frame, textvariable=user_value)
user_entry.grid(row=0, column=1)

pass_entry = Entry(login_frame, show='*', textvariable=pass_value)
pass_entry.grid(row=1, column=1)


submit_button = Button(login_frame, text="Submit", command=get_values)
submit_button.grid(row=2, column=0)

mainloop()
