import base64
import os
import vlc
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import cv2

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
# print("Encrypted: \n" + str(token))
# token = f.decrypt(token)
# print("Decrypted: \n"+ str(token))



def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    file = open(filename, "wb")
    file.write(data)
    file.close()

def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()


    
# Decrypt("/Users/rolandjohn/Desktop/Baby Camera Footage/2022-11-13/09-11-20.avi",2)
def play_Files():
    choice = ""
    while choice != "3":
        print("Please select your option.")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Quit")
        choice = input()
        if choice == "1" or choice == "2":
            key = int(input("Enter a key as int!\n"))
            filename = input("Enter filename with extension:\n")
        if choice == "1":
            Encrypt(filename, key)
        if choice == "2":
            Decrypt(filename, key)
            print("File ready to play.")
            
    # if choice =="3":
    #     cap.release()
    #     cv2.destroyAllWindows()
        
        
play_Files()

