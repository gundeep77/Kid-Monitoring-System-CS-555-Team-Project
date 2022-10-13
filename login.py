# Serverless Implementation of a login service
# Login requires an email and password which is then hashed (MD5) and saved to a file

# Original Code:
# https://medium.com/@moinahmedbgbn/a-basic-login-system-with-python-746a64dc88d6

import hashlib
import re

# Regex for email in the form of (String)@(String).(More than 2 characters)
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      return True
    else:
      return False
      
def signup(email, pwd, conf_pwd):
    # TODO: Check if email is already registered
    if isValid(email):
        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            
            with open("credentials", "w") as f:
                f.write(email + "\n")
                f.write(hash1)
                f.close()
                
            print("Login Created")
        
        else:
            print("Passwords do not match \n")
    
    else:
        print("Invalid Email")
         
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

while 1:
    print("********** Login System **********")
    print("1 : Sign Up")
    print("2 : Log in")
    print("3 : Exit")
    # Throws ValueError
    ch = int(input("Enter your choice: "))
    if ch == 1:
        email = input("Enter email address: ")
        pwd = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        
        signup(email, pwd, conf_pwd)
    elif ch == 2:
        email = input("Enter email: ")
        pwd = input("Enter password: ")
        
        login(email, pwd)
    elif ch == 3:
        break
    else:
        print("Unknown Input")