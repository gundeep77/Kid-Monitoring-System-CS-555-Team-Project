# Serverless Implementation of a login service
# Login requires an email and password which is then hashed and saved to a file

# Original Code:
# https://medium.com/@moinahmedbgbn/a-basic-login-system-with-python-746a64dc88d6

import hashlib

def signup():
    # TODO: Check if valid email
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        
        with open("credentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
            f.close()
            
        print("Login Created")
    
    else:
        print("Passwords do not match \n")
         
def login():
     email = input("Enter email: ")
     pwd = input("Enter password: ")
     auth = pwd.encode()
     auth_hash = hashlib.md5(auth).hexdigest()
     with open("credentials.txt", "r") as f:
         stored_email, stored_pwd = f.read().split("\n")
     f.close()
     if email == stored_email and auth_hash == stored_pwd:
         print("Logged in Successfully!")
     else:
         print("Login failed! \n")

while 1:
    print("********** Login System **********")
    print("1 : Sign Up")
    print("2 : Log in")
    print("3 : Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Unknown Input")