"""This file will display our webcam footage. We must import cv2 for the display to work."""
from datetime import datetime
import cv2
import tkinter.messagebox as tmsg

filename = str(datetime.now())+'.mp4'
global  NUMBER
NUMBER=0

class Camera:
    def check_cam(self, NUMBER):
        cam = cv2.VideoCapture(NUMBER) 
        if cam.isOpened():
            # print("Camera Recording...")
            return True
        else:
            return False
                
    def live_feed(self, NUMBER):
        if not self.check_cam(NUMBER):
            # print("Warning: Feed unavailable. \nReason: Camera " + str(NUMBER) + " is not found.")
            tmsg.showinfo(message="Cannot access camera! Please grant permission and sign in again!")
            return
        """Display function to show our webcam footage. No arguments are passed. To display our webcam 
        footage for our current selected camera simply pass display()."""
        #this will be our initialized webcam feed starting from 0 because we only have
        #one webcam currently in service. For each successive webcam we will increment
        #the cv2.VideoCapture size.
        feed = cv2.VideoCapture(NUMBER)
        disabledpngpath = r'camdisabled.png'
        disabledpng = cv2.imread(disabledpngpath)
        disabledpng = cv2.resize(disabledpng, (640,480))
        
        disableWebcam = False
        
        #this inner function will convert the video to a standard 480p resolution across
        #all webcams that we have. Because most webcams these days on the market are a 
        #minimum of 480p this is a good standard size resolution to have.
        def make_480p(feed):
            feed.set(3,640)
            feed.set(4,480)

        make_480p(feed)
        out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc('m','p','4','v'), 10, (640,480))
        while True:
            ret, display = feed.read()
            
            #will display our current webcam feed with the current date and time in the 
            #center of the window.
            cv2.rectangle(display, (195, 32), (427, 12), (0, 0, 0), -1)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(display,str(datetime.now()),(210,25), font, .4,(390,255,255),1,cv2.LINE_AA)
            out.write(display)
            if(disableWebcam):
                cv2.imshow('Webcam '+str(NUMBER+1), disabledpng)
            else:
                cv2.imshow('Webcam '+str(NUMBER+1), display)
            
            #if we want to exit our display before we reach the 100 milliseconds 
            #our waitKey function is set for we can simply press the SPACEBAR and it will
            #stop our program. Ideally, we would want this to be a GUI item to 
            #close our program.
            if cv2.waitKey(100)==32:
                tmsg.showinfo(message="Recording finished! You can find the recording where your app is located.")
                break
            
            if cv2.waitKey(20)==27:
                disableWebcam = 1 - disableWebcam            
        #this will release our resource so that another program can use our camera.

        out.release()
        feed.release()
        
        #when we exit the script we can destroy the windows
        cv2.destroyAllWindows()