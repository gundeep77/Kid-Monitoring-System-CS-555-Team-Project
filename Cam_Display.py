"""This file will display our webcam footage. We must import cv2 for the display to work."""
from datetime import datetime
from calendar import c
import cv2


"""Display function to show our webcam footage. No arguments are passed. To display our webcam 
footage for our current selected camera simply pass display()."""

global  NUMBER
NUMBER=0
class Camera():
    def camera_amount():
        '''Returns int value of available camera devices connected to the host device'''
        while True:
            if (cv2.VideoCapture(NUMBER).grab()) is True:
                NUMBER+=1
            elif NUMBER ==0:
                print("No cameras connected.")
            else:
                cv2.destroyAllWindows()
                return int(NUMBER)
    def display(NUMBER):
        #this will be our initialized webcam feed starting from 0 because we only have
        #one webcam currently in service. For each successive webcam we will increment
        #the cv2.VideoCapture size.
        feed = cv2.VideoCapture(NUMBER)
        #this inner function will convert the video to a standard 480p resolution across
        #all webcams that we have. Because most webcams these days on the market are a 
        #minimum of 480p this is a good standard size resolution to have.
        def make_480p(feed):
            feed.set(3,640)
            feed.set(4,480)

        make_480p(feed)

        while True:
            ret, display = feed.read()
            
            #will display our current webcam feed with the current date and time in the 
            #center of the window.
            #will display our current webcam feed with the current date and time in the 
            #center of the window.
            cv2.rectangle(display, (200, 60), (470, 25), (0, 0, 0), -1)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(display,str(datetime.now()),(210,50), font, .5,(390,255,255),1,cv2.LINE_AA)
            cv2.imshow('Webcam '+str(NUMBER+1),display)
            
            #if we want to exit our display before we reach the 100 milliseconds 
            #our waitKey function is set for we can simply press the SPACEBAR and it will
            #stop our program. Ideally, we would want this to be a GUI item to 
            #close our program.
            if cv2.waitKey(100)==32:
                break
        #this will release our resource so that another program can use our camera.
        feed.release()
        #when we exit the script we can destroy the windows
        cv2.destroyAllWindows()   


#this will run our display
for n in range(0,NUMBER+1):
    Camera.display(NUMBER)


    



