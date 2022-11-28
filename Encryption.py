'''This program will encrypt and decrypt files with a given key. The default key we have
is 123. When we integrate with the database the keys will be specific to the user.

Note: Encryption happens automatically when the video recordings ends. 
Decryption requires the user to select the file path name and then enter the key.
'''

import sqlite3
import time
import cv2
import os
import sys

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
        print("Filed successfully encrypted.")
    except FileNotFoundError:
        print("File does not exist!")
    except ValueError:
        print("Key is invalid.")
    except Exception:
        print("Invalid key or file name.")
    

def Decrypt(filename, key):
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
        print("Filed successfully decrypted.")
    except FileNotFoundError:
        print("File does not exist!")
    except ValueError:
        print("Key is invalid.")
    except Exception:
        print("Invalid key or file name.")
    

    

# def play_Files():
#     """
#     Args: None
#     The user will follow the propmpts to decrypt/encrypt files when
#     given a pathname and key. If the key is the correct key for that
#     user then the selected encryption 
#     """
#     choice = ""
#     while choice != "3":
#         print("Please select your option.")
#         print("1. Encrypt File")
#         tmsg.showinfo("2. Decrypt File")
#         tmsg.showinfo("3. Quit")
#         choice = input()
#         if choice=="3":
#             tmsg.showinfo("Program Complete.")
#             break
#         key = input("Enter key:\n")
#         if check_key(key) == False:
#             tmsg.showinfo("Key is invalid.")
#             continue
#         if choice == "1" or choice == "2":
            
#             filename = input("Enter filename with extension:\n")
#         if choice == "1":
#             Encrypt(filename, key)
#         if choice == "2":
#             Decrypt(filename, attempt = Entry())
            
                      

def play(file):
    # cap = cv2.VideoCapture(file)
    # if not cap.isOpened():
    #     print("Can't receive frame (stream end?). Exiting ...")
    #     exit(0)

    # while(cap.isOpened()):
    #     ret, img = cap.read()
    #     if ret:
    #         imgin = img[:,:,(0,1,2)]
    #     else:
    #         break
    #     cv2.imshow("Footage", img)
    #     cv2.waitKey(30)  
    # cap.release() 
    # cv2.destroyWindow("Footage")
    # Create a video capture object, in this case we are reading the video from a file
    vid_capture = cv2.VideoCapture(file)
    
    if (vid_capture.isOpened() == False):
        print("Error opening the video file")
    # Read fps and frame count
    else:
    # Get frame rate information
    # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
        fps = vid_capture.get(5)
        print('Frames per second : ', fps,'FPS')
        
        # Get frame count
        # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
        frame_count = vid_capture.get(7)
        print('Frame count : ', frame_count)
        
    while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool 
    # and the second is frame
        ret, frame = vid_capture.read()
        if ret == True:
            cv2.imshow('Frame',frame)
            # 20 is in milliseconds, try to increase the value, say 50 and observe
            key = cv2.waitKey(20)
            
            if key == 32:
                break
        else:
            break
        
    # Release the video capture object
    vid_capture.release()
    cv2.destroyAllWindows()     

