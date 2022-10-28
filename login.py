# Serverless Implementation of a login service
# Login requires an email and password which is then hashed (MD5) and saved to a file

# Login Code:
# https://medium.com/@moinahmedbgbn/a-basic-login-system-with-python-746a64dc88d6
# Email Regex Code
# https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/

import hashlib
import re

# Regex for email in the form of [ (String)@(String).(any 2 or more characters) ]
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    return re.fullmatch(regex, email)
               
def login(email, pwd):
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    # TODO: Catch FileNotFoundError
    with open("credentials", "r") as f:
       stored_email, stored_pwd = f.read().split("\n")
       f.close()
    if email == stored_email and auth_hash == stored_pwd:
       print("Logged in Successfully!")
    else:
       print("Incorrect Email or Password \n")