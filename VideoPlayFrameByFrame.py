# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:08:18 2020

@author: OCAC
"""

#Import Libraries

import cv2
import numpy as np

#------------------------------------------------------------------------------

#Create VideoCapture Object and read from input file

cap=cv2.VideoCapture("output video.mp4")

#------------------------------------------------------------------------------

#Check If Camera Opened Succesfully and Read Until Video is completed

if(cap.isOpened()==False):
    print("Error! opening video file")
    
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret ==True:
        
        #capture frame by frame & display the resulting frame
        
        cv2.imshow("Frame",frame)
        
        #press Q to exit
        
        if cv2.waitKey(25) & 0xFF ==ord("q"):
            break
        
    #break the loop
    
    else:
        break
    
#------------------------------------------------------------------------------
        
#When Everything is done,release,the VideoCapture object

cap.release()
cv2.destroyAllWindows()



