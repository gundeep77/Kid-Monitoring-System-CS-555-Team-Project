"""This file will display our webcam footage. We must import cv2 for the display to work."""

import keyboard as kb
from calendar import c
import numpy as np
import cv2

"""Display function to show our webcam footage. No arguments are passed. To display our webcam 
footage for our current selected camera simply pass display()."""
def display():
    #this will be our initialized webcam feed starting from 0 because we only have
    #one webcam currently in service. For each successive webcam we will increment
    #the cv2.VideoCapture size.
    feed = cv2.VideoCapture(0)

    while True:
        ret, display = feed.read()
        
        #will dispaly our current webcam feed
        cv2.imshow('Webcam',display)
        
        #if we want to exit our display before we reach the 100 milliseconds 
        #our waitKey function is set for we can simply press 'a' and it will
        #stop our program.
        if cv2.waitKey(100)==ord('a'):
            break

        # if cv2.waitKey(100)==ord('a'):
        #     break
    #this will release our resource so that another program can use our camera.
    feed.release()
    #when we exit the script we can destroy the windows
    cv2.destroyAllWindows()   


#this will run our display
display()
