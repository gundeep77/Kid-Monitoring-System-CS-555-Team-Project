import hashlib
import re
import sqlite3
import tkinter.messagebox as tmsg
import random


# Regex for email in the form of [ (String)@(String).(any 2 or more characters) ] and phone number in the form of (123) 456-7890
regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
phone_regex = re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')

def isValidPhoneNumber (phoneNumber):
    """
    **Description**:
    
    Checks if a phone number is valid

    **Args**:

    `phoneNumber` *(string)*: Phone number
    
    **Returns**:

    True if valid, False otherwise
    """
    if (re.search(phone_regex, phoneNumber)):
        return True
    else:
        return False

def isValidEmail(email):
    """
    **Description**:

    Checks if an email is valid

    **Args**:

    `email` *(string)*: E-mail address

    **Returns**:
    
    True if valid, False otherwise
    """
    if re.search(regex_email, email):
        return True
    else: return False


def register_user(email, phoneNumber, password, cfm_password ):
    """
    **Description**:

    Registers a user into a database given the credentials

    **Args**:
    
    `email` *(string)*: E-mail address
    `phoneNumber` *(string)*: Phone number
    `password` *(string)*: Password
    `cfm_password` *(string)*: Confirmed password
    **Returns**:
    """

    if isValidEmail(email):
        if isValidPhoneNumber(phoneNumber):

            if cfm_password == password:
                if len(password) >= 8:
                    enc = password.encode()
                    hash1 = hashlib.md5(enc).hexdigest()

                    random_key = generateFile_key()

                    params = (email, hash1, phoneNumber, random_key)


                    db = sqlite3.connect ("userdata.db")
                    cursor = db.cursor()
                    cursor.execute (''' CREATE TABLE IF NOT EXISTS credentials (email text, password text, phoneNumber Integer, file_key Integer )''')
                    cursor.execute("select email from credentials where email = ?", (email,))
                    data = cursor.fetchall()
                    if len(data):
                        tmsg.showinfo(message="User already exists!")
                        return 0
                    cursor.execute('''INSERT INTO credentials VALUES (?,?,?,?)''', params)
                    db.commit()

                    tmsg.showinfo(message=f"Account successfully created!")
                    
                    return 1
                else: tmsg.showinfo(message="Password should be at least 8 characters long!")

            else:
                tmsg.showinfo(message="Passwords do not match!")
        else:
            tmsg.showinfo(message="Invalid phone number format!")

    else:
        tmsg.showinfo(message="Invalid email format!")
    
    
# functions for debugging purpose
def drop_table(table_name):
    """
    **Description**:
    
    Function for debugging purposes with database table

    **Args**:
    
    `table_name` *(string)*: Name of the table in database
    """
    db = sqlite3.connect ("userdata.db")
    cursor = db.cursor()
    cursor.execute(f"drop table {table_name}")

def show_all_records(table_name):
    """
    **Description**:
    
    Show all the records from given database table
    
    **Args**:

    `table_name` *(string)*: Name of the table in database.
    
    """
    db = sqlite3.connect ("userdata.db")
    cursor = db.cursor()
    cursor.execute(f"select * from {table_name}")
    data = cursor.fetchall()
    print(data)

def generateFile_key():
    """randomly generate integer key between 1 and 255 to encrypt/decrypt video files """
    file_key = random.randint(1, 255)
    return file_key


