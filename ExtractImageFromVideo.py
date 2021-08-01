# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:24:59 2020

@author: OCAC
"""
#Import libraries

import cv2
import os

#------------------------------------------------------------------------------

#Reading The video

cam=cv2.VideoCapture("C:/Users/OCAC/Desktop/Python Programs/Projects/output video.mp4")

#------------------------------------------------------------------------------

#Create A Folder

try:
    if not os.path.exists("videoData"):
        os.makedirs("videoData")
        
except OSError:
    print("Error:Creating directory of data!")
    
#------------------------------------------------------------------------------
    
currentFrame=0

#Reading From Frame

while True:
    ret,frame=cam.read()
    
    #if video is still left continue creating images
    
    if ret:
        name="./videoData/frame" +str(currentFrame) + ".jpg"
        print("Creating...." + name)
        
        #writing extracted image
        
        cv2.imwrite(name,frame)
        
        #increase the counter so that it will show how many frames you have created
        
        currentFrame+=1
    else:
        break
        
#-------------------------------------------------------------------------------
cam.release()
cv2.destroyAllWindows()        
        
        
        
        