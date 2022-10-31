# Serverless Implementation of a login service
# Login requires an email and password which is then hashed (MD5) and saved to a file

import hashlib
import sqlite3
import tkinter.messagebox as tmsg
from authenticate import authenticate

def login(email, password):

    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    db = sqlite3.connect("userdata.db")

    cursor = db.cursor()

    statement = f"SELECT email from credentials WHERE email = '{email}' and password = '{auth_hash}'"
    cursor.execute(statement)

    if not cursor.fetchone():
        tmsg.showinfo(message="User doesn't exist!")
        return
    else:
        # if not authenticate(password):
        #     tmsg.showinfo(message="Login failed! Please sign in again using a newly generated QR code!")
        #     return
        return 1