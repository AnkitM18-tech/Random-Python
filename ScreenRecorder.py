# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:30:51 2020

@author: OCAC
"""

import cv2
import numpy as np
from PIL import ImageGrab

def ScreenRecorder():
    fourcc=cv2.VideoWriter_fourcc(*"XVID")
    out=cv2.VideoWriter("output video.mp4",fourcc,5.0,(1366,768))
    
    while True:
        img =ImageGrab.grab()
        img_np=np.array(img)
        frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recorder",frame)
        out.write(frame)
        
        if cv2.waitKey(1)==27:
            break
    out.release()
    cv2.destroyAllWindows()
    
ScreenRecorder()