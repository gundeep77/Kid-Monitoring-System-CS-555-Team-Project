""""
Note: Encryption happens automatically when the video recordings ends. 
Decryption requires the user to select the file path name and then enter the key.
"""

import sys

import numpy as np
import cv2
sys.tracebacklimit=None


def Encrypt(filename, key):
    """
    Args: filename: The name of the file we are encrypting
    key: The key used to encrypt the file

    Pass the filename and the user specific database key to 
    'lock the file'
    """
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
        print("File successfully encrypted.")
    except FileNotFoundError:
        print("File does not exist!")
    except ValueError:
        print("Key is invalid.")
    except Exception:
        print("Invalid key or file name.")
    

def Decrypt(filename, key):
    """
    Args: filename: The name of the file we are decrypting
    key: The key used to decrypt the file

    Pass the filename and the user specific database key to 
    'unlock the file'
    """
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
        print("File successfully decrypted.")
    except FileNotFoundError:
        print("File does not exist!")
    except ValueError:
        print("Key is invalid.")
    except Exception:
        print("Invalid key or file name.")
    
def play(file):
    """
    Args: filename: The name of the file we are trying to
    access. Only called after decryption of the file

    Pass the filename to play the file. Press spacebar key
    to end playback.
    """
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

