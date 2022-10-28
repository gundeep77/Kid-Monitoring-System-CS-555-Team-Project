# Serverless Implementation of a login service
# Login requires an email and password which is then hashed (MD5) and saved to a file

# Login Code:
# https://medium.com/@moinahmedbgbn/a-basic-login-system-with-python-746a64dc88d6
# Email Regex Code
# https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/

import hashlib
import sqlite3
import re

# Regex for email in the form of [ (String)@(String).(any 2 or more characters) ]
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    return re.fullmatch(regex, email)
               
def login(email,password):

    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    db = sqlite3.connect("userdata.db")

    cursor = db.cursor()

    statement = f"SELECT email from credentials WHERE email = '{email}' and password = '{auth_hash}'"
    cursor.execute(statement)

    if not cursor.fetchone():
            print("Login failed")
    else:
        # 2FA must be added here. If it passes print msg below else print login failed
            print("Welcome")