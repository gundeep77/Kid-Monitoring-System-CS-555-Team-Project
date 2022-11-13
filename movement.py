import numpy as np
import cv2
from PIL import ImageGrab

# Derived from a tutorial:
# https://towardsdatascience.com/image-analysis-for-beginners-creating-a-motion-detector-with-opencv-4ca6faba4b42
def motion_detector():
    """
    **Description**:

    Detects movement on a display.
    """
  
    frame_count = 0
    previous_frame = None
    
    while True:
        frame_count += 1

        # At the moment, this just grabs the image on the screen.
        # 1. Load image; convert to RGB
        img_brg = np.array(ImageGrab.grab())
        img_rgb = cv2.cvtColor(src=img_brg, code=cv2.COLOR_BGR2RGB)

        if ((frame_count % 2) == 0):

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
            cv2.drawContours(image=img_rgb, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)     

            contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) < 50:
                    # too small: skip!
                    continue
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(img=img_rgb, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)

        cv2.imshow('Motion detector', img_rgb)

        if (cv2.waitKey(30) == 27):
            break

motion_detector()
        
    
    


