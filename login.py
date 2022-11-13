# Serverless Implementation of a login service
# Login requires an email and password which is then hashed (MD5) and saved to a file

import hashlib
import sqlite3
import tkinter.messagebox as tmsg

def login(email, password):
    """
    **Description**:
    
    Logs in a user given an email and password

    **Args**:

    `email` *(string)*: E-mail address\n
    `password` *(string)*: Password
    
    **Returns**:

    1 if passes, nothing otherwise.
    """

    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    db = sqlite3.connect("userdata.db")

    cursor = db.cursor()

    statement = f"SELECT email from credentials WHERE email = '{email}' and password = '{auth_hash}'"
    try:
        cursor.execute(statement)
    except:
        tmsg.showinfo(message="User doesn't exist! Please sign up first!")
        return

    if not cursor.fetchone():
        tmsg.showinfo(message="Incorrect Credentials!")
        return
    else:
        return 1