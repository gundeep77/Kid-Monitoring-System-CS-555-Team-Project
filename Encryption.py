'''This program will encrypt and decrypt files with a given key. The default key we have
is 123. When we integrate with the database the keys will be specific to the user.

Note: Encryption happens automatically when the video recordings ends. 
Decryption requires the user to select the file path name and then enter the key.
'''
from tkinter import *
import cv2
import os
import sys
import tkinter.messagebox as tmsg
import numpy as np
import cv2
sys.tracebacklimit=None
# import base64
# import os
# from cryptography.fernet import Fernet
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.hkdf import HKDF
# import cv2

# password = b"password"
# hkdf = HKDF(
#      algorithm=hashes.SHA256(),  # You can swap this out for hashes.MD5()
#      length=32,
#      salt=None,    # You may be able to remove this line but I'm unable to test
#      info=None,    # You may also be able to remove this line
#      backend=default_backend()
# )
# key = base64.urlsafe_b64encode(hkdf.derive(password))
# f = Fernet(key)
# token = f.encrypt(b"Secret message!")
# tmsg.showinfo("Encrypted: \n" + str(token))
# token = f.decrypt(token)
# tmsg.showinfo("Decrypted: \n"+ str(token))


def check_key(key):
    try: 
        key = int(key)
        if 1<=key<=255:
            return key
    except Exception:
        tmsg.showinfo("Key is invalid")
    return False

def Encrypt(filename, key):
    try:
        file = open(filename, "rb")
        data = file.read()
        file.close()

        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ key
            
        file = open(filename, "wb")
        file.write(data)
        file.close()
        tmsg.showinfo("Filed successfully encrypted.")
    except FileNotFoundError:
        tmsg.showinfo("File does not exist!")
    except ValueError:
        tmsg.showinfo("Key is invalid.")
    except Exception:
        tmsg.showinfo("Invalid key or file name.")
    

def Decrypt(filename, key):
    try:
        file = open(filename, "rb")
        data = file.read()
        file.close()
        attempt = Entry()
        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ key
            
        
        file = open(filename, "wb")
        file.write(data)
        file.close()
        tmsg.showinfo("Filed successfully decrypted.")
    except FileNotFoundError:
        tmsg.showinfo("File does not exist!")
    except ValueError:
        tmsg.showinfo("Key is invalid.")
    except Exception:
        tmsg.showinfo("Invalid key or file name.")
    

    

def play_Files():
    """
    Args: None
    The user will follow the propmpts to decrypt/encrypt files when
    given a pathname and key. If the key is the correct key for that
    user then the selected encryption 
    """
    choice = ""
    while choice != "3":
        tmsg.showinfo("Please select your option.")
        tmsg.showinfo("1. Encrypt File")
        tmsg.showinfo("2. Decrypt File")
        tmsg.showinfo("3. Quit")
        choice = input()
        if choice=="3":
            tmsg.showinfo("Program Complete.")
            break
        key = input("Enter key:\n")
        if check_key(key) == False:
            tmsg.showinfo("Key is invalid.")
            continue
        if choice == "1" or choice == "2":
            
            filename = input("Enter filename with extension:\n")
        if choice == "1":
            Encrypt(filename, key)
        if choice == "2":
            Decrypt(filename, attempt = Entry())
            
                      

def play(file):
    
    cap = cv2.VideoCapture(file)
    if not cap.isOpened():
        print("Can't receive frame (stream end?). Exiting ...")
        exit(0)

    while(cap.isOpened()):
        ret, img = cap.read()
        if ret:
            imgin = img[:,:,(0,1,2)]
        else:
            break
        cv2.imshow("Footage", img)
        cv2.waitKey(30)   
    cv2.destroyAllWindows()     
        


