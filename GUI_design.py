import tkinter
from tkinter import filedialog,Tk, Label, Frame, PhotoImage, StringVar, IntVar, SUNKEN, Entry, Button, Checkbutton, Menu, mainloop
import tkinter.messagebox as tmsg
import sqlite3
from account_creation import register_user
from login import login
from Cam_Display import Camera, NUMBER
from authenticate import authenticate
from PIL import Image, ImageTk
import webbrowser
import os
from Encryption import Encrypt,Decrypt,play

from logger import Logger

root = Tk()

root.title("Baby Monitoring System")
window_width = 700
window_height = 500
root.geometry(f"{window_width}x{window_height}")
root.maxsize(window_width, window_height)
root.minsize(window_width, window_height)
desktop  = os.path.expanduser("~/Desktop")
# establishing db connection
db = sqlite3.connect ("userdata.db")
cursor = db.cursor()

log_path = os.path.expanduser(desktop + "\\Baby Camera Footage\\log.txt")
log = Logger(desktop + "/Baby Camera Footage/log.txt")

def open_file():
    """
    This function will decrypt and open the file in the GUI. Once the file is done 
    playing the window will close. The file will then be encrypted aand unable to
    be opened again until the program is ran again.
    """
    if user_access():
        key = get_key(email_input)
        filepath = filedialog.askopenfilename(initialdir=desktop+"/Baby Camera Footage",
                                          title="Camera Footage",
                                          filetypes= (("all video format", ".mp4",".avi"),
                                          ('image files', '.jpg')))
        
        try:
            Decrypt(filepath, key)
            play(filepath)
            Encrypt(filepath,key)
        except Exception:
            print("Error")

def user_access():
    """
    **Description**:
    
    Logins the user with given credentials
    """
    global email_input
    if len(email_value.get()) and len(pass_value.get()):
        email_input = email_value.get()
        password_input = pass_value.get()
        
    
        login_return = login(email_input, password_input)

        if login_return == 1:
            if authenticate(code_value.get()):
                #email_entry.delete(0, "end")
                # pass_entry.delete(0, "end")
                code_entry.delete(0, "end")
                
                log.log(f"Login successful as {email_input} for user_access")

                return True
            else: 
                log.log(f"Login failed as {email_input} for user_access")
                tmsg.showinfo(message="Incorrect verification code! Please try again!")
    else:
        tmsg.showinfo(message='Please fill in all the details!')  

def get_key(email_input):
    """
    This function will get the user key that is used in the encryption/decryption
    process and return it. 
    """
    cursor.execute("select file_key from credentials where email = ?",(email_input,))
    file_key = cursor.fetchone()
    return (file_key[0])
    

def create_connection(db_file):
    """
    **Description**:

    Creates a connection to a specified sql db file

    **Args**:

    `db_file` *(string)*: String path file to database

    **Returns**:

    Connection established to database.
    """
    conn = None
    try:
        log.log(f"Connection established to database.")
        conn = sqlite3.connect(db_file)
    except:
        log.log(f"Connection failed to database.")
        tmsg.showinfo(message = "Could not establish connection to the database!")
    return conn

def submit_new_user_details():
    """
    **Description**:
    
    Sends new user details to register them for account creation.
    """
    if len(email_signup_value.get()) and len(pass_signup_value.get()) and len(phone_number_value.get()) and confirmation_value.get():
        if pass_signup_value.get() == confirm_pass_signup_value.get():
            register_user_return = register_user(email_signup_value.get(), phone_number_value.get(), pass_signup_value.get(), confirm_pass_signup_value.get())
            log.log(f"New user registered: {email_signup_value.get()}")
            if register_user_return == 1:
                email_signup_entry.delete(0, "end")
                phone_number_entry.delete(0, "end")
                pass_signup_entry.delete(0, "end")
                confirm_pass_signup_entry.delete(0, "end")
            elif register_user_return == 0:
                return
    else:
        tmsg.showinfo(message='Please fill in all the details and check "I agree"!')

def signin_function ():
    """
    **Description**:
    
    Logins the user with given credentials
    """
    if len(email_value.get()) and len(pass_value.get()):

        email_input = email_value.get()
        password_input = pass_value.get()

        login_return = login(email_input, password_input)

        if login_return == 1:
            if authenticate(code_value.get()):
                
                log.log(f"Login successful as {email_input} for record")

                email_entry.delete(0, "end")
                pass_entry.delete(0, "end")
                code_entry.delete(0, "end")
                session = Camera()
                session.live_feed(NUMBER, email_input)
            else:
                log.log(f"Login failed as {email_input} for record") 
                tmsg.showinfo(message="Incorrect verification code! Please try again!")
    else:
        tmsg.showinfo(message='Please fill in all the details!')

def clear_signup_fields ():
    """
    **Description**:

    Clears the fields for signup
    """
    email_signup_entry.delete(0, "end")
    phone_number_entry.delete(0, "end")
    pass_signup_entry.delete(0, "end")
    confirm_pass_signup_entry.delete(0, "end")


def about_menu ():
    """
    **Description**:

    Shows info for the about menu
    """
    tmsg.showinfo(message="This is application for monitoring your kid at home directly through your webcam!")

def callback(url):
    """
    **Description**:

    Opens a tab in the web browser from a specified URL

    **Args**:

    `url` *(string)*: Specified URL path
    """
    webbrowser.open_new_tab(url)


# Design
photo = PhotoImage(file="child_monitor.png")
bg_label = Label(root, image=photo)
bg_label.place(x=0, y=0)

heading_frame = Frame(root, borderwidth=4, relief=SUNKEN)
heading_frame.place(x=320, y=40)
heading_text = Label(heading_frame, text="Welcome to Baby Monitoring System!",
                     fg="yellow", font="comicsansms 16 bold", bg="brown")
heading_text.grid()

# sign in
signin_text = Label(root, text="Enter your account email address/paassword.\nScan your QR code using Google Authenticator app:", fg="coral", justify="left")
signin_text.place(x=320, y=90)

login_frame = Frame(root, borderwidth=6, relief=SUNKEN)
login_frame.place(x=320, y=128)

email_label = Label(login_frame, text="Email:")
email_label.grid(row=0, column=0)

password_label = Label(login_frame, text="Password:")
password_label.grid(row=1, column=0)

code_label = Label(login_frame, text="Verification Code:")
code_label.grid(row=2, column=0)

email_value = StringVar()
pass_value = StringVar()
code_value = StringVar()

email_entry = Entry(login_frame, textvariable=email_value)
email_entry.grid(row=0, column=1)

pass_entry = Entry(login_frame, show='*', textvariable=pass_value)
pass_entry.grid(row=1, column=1)

code_entry = Entry(login_frame, textvariable=code_value)
code_entry.grid(row=2, column=1)

submit_button = Button(login_frame, text="Record", command=signin_function)
submit_button.grid(row=3, column=0)

access_footage_button = Button(login_frame, text="Access Footage", command=open_file)
access_footage_button.grid(row=3, column=1)

# signup
signup_text = Label(root, text="Please sign up here if you don't have an account:", fg="coral")
signup_text.place(x=320, y=270)
signup_frame = Frame(root, borderwidth=6, relief=SUNKEN)
signup_frame.place(x=320, y=290)

email_signup_label = Label(signup_frame, text="Email:")
email_signup_label.grid(row=3, column=0)

phone_number_label = Label(signup_frame, text="Phone Number:\ne.g.: (551) 432-1234")
phone_number_label.grid(row=4, column=0)

password_signup_label = Label(signup_frame, text="Password:\n(Min 8 Characters)")
password_signup_label.grid(row=5, column=0)

confirm_pass_signup_label = Label(signup_frame, text="Confirm Password:")
confirm_pass_signup_label.grid(row=6, column=0)

email_signup_value = StringVar()
phone_number_value = StringVar()
pass_signup_value = StringVar()
confirm_pass_signup_value = StringVar()
confirmation_value = IntVar()

email_signup_entry = Entry(signup_frame, textvariable=email_signup_value)
email_signup_entry.grid(row=3, column=1)

phone_number_entry = Entry (signup_frame, textvariable=phone_number_value)
phone_number_entry.grid(row=4, column=1)

pass_signup_entry = Entry(signup_frame, show='*', textvariable=pass_signup_value)
pass_signup_entry.grid(row=5, column=1)

confirm_pass_signup_entry = Entry(signup_frame, show='*', textvariable=confirm_pass_signup_value)
confirm_pass_signup_entry.grid(row=6, column=1)

confirmation = Checkbutton(signup_frame, text = "I agree", variable=confirmation_value)
confirmation.grid(row = 7, column = 0)

submit_signup_button = Button(signup_frame, text="Register", command=submit_new_user_details)
submit_signup_button.grid(row=8, column=0)

clear_signup_button = Button (signup_frame, text = "Clear Fields", command=clear_signup_fields)
clear_signup_button.grid(row=8, column=1)

# menubar
menu_bar = Menu (root)
options_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label = "Options", menu=options_menu)
options_menu.add_command(label = "About", command=about_menu)
options_menu.add_command(label = "Exit", command=root.destroy)
root.config(menu=menu_bar)

# qrcode
qrcode_image = Image.open("MyQRCode.png")
qrcode_image = qrcode_image.resize((100, 100), Image.Resampling.LANCZOS)
qr_code = ImageTk.PhotoImage(qrcode_image)
qr_label = tkinter.Label(image=qr_code)
qr_label.image = qr_code
qr_label.place(x=0, y=0)

# ios and android download links to the Google Authenticator app
link_ios = Label(root, text="Google Authenticator (iOS)",font='Helveticabold 11 underline', fg="light green", cursor="hand2")
link_android = Label(root, text="Google Authenticator (Android)",font='Helveticabold 11 underline', fg="light green", cursor="hand2")
link_ios.place(x=0, y=101)
link_android.place(x=0, y=121)
link_ios.bind("<Button-1>", lambda e: callback("https://apps.apple.com/us/app/google-authenticator/id388497605"))
link_android.bind("<Button-1>", lambda e: callback("https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&pli=1"))

mainloop()