"""This file will display our webcam footage. We must import cv2 for the display to work."""
from datetime import datetime
import cv2
import tkinter.messagebox as tmsg
import os
from Encryption import Encrypt, Decrypt
import sqlite3
import numpy as np
from PIL import ImageGrab
from logger import Logger

global  NUMBER
NUMBER=0

#Code to create footage storage folder to user desktop
desktop  = os.path.expanduser("~/Desktop")
today = datetime.today().strftime('%Y-%m-%d')
def createFolder(desktop):
    try:
        if not os.path.exists(desktop+"/Baby Camera Footage"):
            os.makedirs(desktop+"/Baby Camera Footage")
        if not os.path.exists(desktop+ "/Baby Camera Footage/"+today):
            os.makedirs(desktop+ "/Baby Camera Footage/"+today)
    except OSError:
        print('Error: Creating Directory.')
    return desktop+"/Baby Camera Footage/"+today+"/"
createFolder(desktop) 

log_path = os.path.expanduser(desktop + "/Baby Camera Footage/log.txt")
log = Logger(log_path)

class Camera:
    """
    **Description**:
    
    Camera class made to handle webcam footage.
    """

    def check_cam(self, NUMBER):
        """
        **Description**:
        
        Checks to see if the camera is opened or not.
        
        **Args**:

        `NUMBER` *(int)*: Takes in an integer value defined globally to capture video from indexed camera
        """
        cam = cv2.VideoCapture(NUMBER) 
        if cam.isOpened():
            return True
        else:
            return False
       
    def live_feed(self, NUMBER, currentuseremail):
        """
        **Description**:
        
        Display function to show our webcam footage. No arguments are passed. To display our webcam 
        footage for our current selected camera simply pass display().
        
        **Args**:

        `NUMBER` *(int)*: Takes in an integer value defined globally to capture video from indexed camera
        """
        if not self.check_cam(NUMBER):
            tmsg.showinfo(message="Cannot access camera! Please grant permission and sign in again!")
            return
        
        #this will be our initialized webcam feed starting from 0 because we only have
        #one webcam currently in service. For each successive webcam we will increment
        #the cv2.VideoCapture size.
        feed = cv2.VideoCapture(NUMBER)
        
        # image that blocks camera feed when it is disabled
        disabledpngpath = r'camdisabled.png'
        disabledpng = cv2.imread(disabledpngpath)
        disabledpng = cv2.resize(disabledpng, (640,480))

        disableWebcam = False
        
        # for motion detection
        frame_count = 0
        previous_frame = None
        
        #this inner function will convert the video to a standard 480p resolution across
        #all webcams that we have. Because most webcams these days on the market are a 
        #minimum of 480p this is a good standard size resolution to have.
        def make_480p(feed):
            feed.set(3,640)
            feed.set(4,480)

        make_480p(feed)
        current_time = datetime.now().strftime("%H-%M-%S")
        filename = str(current_time)+'.mp4'
        video = desktop+"/Baby Camera Footage/"+today+"/"+filename
        
        out = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*'mp4v'), 10, (640,480))
        while True:
            ret, display = feed.read()
            
            #will display our current webcam feed with the current date and time in the 
            #center of the window.
            cv2.rectangle(display, (195, 32), (427, 12), (0, 0, 0), -1)

            # time stamp font
            font = cv2.FONT_HERSHEY_SIMPLEX            
#

            img_rgb = display
            # img_rgb = cv2.cvtColor(src=img_brg, code=cv2.COLOR_BGR2RGB)

            if ((frame_count % 10) == 0 and (img_rgb is not None)):

                # 2. Prepare image; grayscale and blur
                prepared_frame = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                prepared_frame = cv2.GaussianBlur(src=prepared_frame, ksize=(5,5), sigmaX=0)

                # 3. Set previous frame and continue if there is None
                if (previous_frame is None):
                # First frame; there is no previous one yet
                    previous_frame = prepared_frame
                    continue

                # calculate difference and update previous frame
                diff_frame = cv2.absdiff(src1=previous_frame, src2=prepared_frame)
                previous_frame = prepared_frame

                # 4. Dilute the image a bit to make differences more seeable; more suitable for contour detection
                kernel = np.ones((5, 5))
                diff_frame = cv2.dilate(diff_frame, kernel, 1)

                # 5. Only take different areas that are different enough (>20 / 255)
                # The thresh value was default 20, but I upped it to 50 so it doesn't catch every single thing that moves.
                thresh_frame = cv2.threshold(src=diff_frame, thresh=50, maxval=255, type=cv2.THRESH_BINARY)[1]

                contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
                
                # code of highlighting the contour of the detected change
                # removed for adding too much clutter
                # cv2.drawContours(image=img_rgb, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)     

                contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
                
                # create one bounding box for all detected contours
                # xx/yy represents ending coordinates, not width/height
                (x,y,xx,yy) = (640,480,0,0)
                for contour in contours:
                    if cv2.contourArea(contour) < 50:
                        # too small: skip!
                        continue
                    # find the coordinates for the one bounding box    
                    (xP, yP, wP, hP) = cv2.boundingRect(contour)
                    if (xP+wP > xx):
                        (x,y,xx,yy) = (x,y,xP+wP,yy)
                    if (yP+hP > yy):
                        (x,y,xx,yy) = (x,y,xx,yP+hP)                        
                    if (xP < x):
                        (x,y,xx,yy) = (xP,y,xx,yy)
                    if (yP < y):
                        (x,y,xx,yy) = (x,yP,xx,yy)
                    log.log("Movement detected.")
                
                # draw one bounding box only if it changes from default
                if ((x,y,xx,yy) != (640,480,0,0)):
                    cv2.rectangle(img=img_rgb, pt1=(x, y), pt2=(xx, yy), color=(0, 255, 0), thickness=2)

#
            cv2.putText(img_rgb ,str(datetime.now()),(210,25), font, .4,(390,255,255),1,cv2.LINE_AA)
            out.write(img_rgb)
            
            
            
            if(disableWebcam):
                cv2.imshow('Webcam '+str(NUMBER+1), disabledpng)
            else:
                cv2.imshow('Webcam '+str(NUMBER+1), img_rgb)
            
            #if we want to exit our display before we reach the 100 milliseconds 
            #our waitKey function is set for we can simply press the SPACEBAR and it will
            #stop our program. Ideally, we would want this to be a GUI item to 
            #close our program.
            keypress = cv2.waitKey(1);

            # Ends the session
            if keypress == 32:

                #sconnect to database and search for current user's file key 
                db = sqlite3.connect ("userdata.db")
                cursor = db.cursor()
                cursor.execute("select file_key from credentials where email = ?", (currentuseremail,))
                file_key = cursor.fetchone()

                tmsg.showinfo(message="Footage encrypted and saved in Baby Monitor Footage on Desktop! You can access it by logging in through the app.")
                break
            
            # Disabled the live feed temporarily
            elif keypress == 27:
                disableWebcam = 1 - disableWebcam    

            # Saves screenshot
            elif keypress == 115:
                screenshot = str(datetime.now().strftime("%H-%M-%S-%MS"))+".jpg"
                if not cv2.imwrite(desktop+"/Baby Camera Footage/"+screenshot, img_rgb):
                    print("Couldn't save screenshot")
                    
        #this will release our resource so that another program can use our camera.

        out.release()
        feed.release()
        
        
        #when we exit the script we can destroy the windows
        Encrypt(video, file_key[0])
        cv2.destroyAllWindows()
        
    cv2.destroyAllWindows()