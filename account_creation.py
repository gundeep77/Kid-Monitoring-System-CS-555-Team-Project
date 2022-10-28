import hashlib
import re
import sqlite3

# Regex for email in the form of [ (String)@(String).(any 2 or more characters) ]
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    return re.fullmatch(regex, email)


def register_user(email, phoneNumber, password,cfnpassword ):

    if isValid(email):

        if cfnpassword == password:
            enc = cfnpassword.encode()
            hash1 = hashlib.md5(enc).hexdigest()

            params = (email, hash1, phoneNumber)

            db = sqlite3.connect ("userdata.db")
            cursor = db.cursor()
            cursor.execute (''' CREATE TABLE IF NOT EXISTS credentials (email text, password text, phoneNumber Integer )''')
            cursor.execute('''INSERT INTO credentials VALUES (?,?,?)''', params)
            db.commit()

            print("Registration successful")

        else:
            print("Passwords do not match")

    else:
        print("Invalid Email")
    