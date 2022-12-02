import os
from datetime import datetime

class Logger:
    """
    **Description**:
    
    Class designed for logging events on the app.

    """

    # filepath is the path of the file
    def __init__(self, filepath):
        self.filepath = filepath
    
    # Logs an event, the variable event is a string
    def log(self, event):
        with open(self.filepath, "a") as f:
            f.write(f"[{datetime.now()}] {event} \n")
            f.close()


# File path, needs to have a log.txt in there or some file that can be opened.
# desktop  = os.path.expanduser("~/Desktop\\Baby Camera Footage") + str("\\log.txt")
