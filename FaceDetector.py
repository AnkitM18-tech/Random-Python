# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:24:05 2020

@author: OCAC
"""

#importing libraries

import numpy as np
import cv2

#------------------------------------------------------------------------------

#load trained classifiers .xml files for detection

face_cascade=cv2.CascadeClassifier("face.xml")
eyes_cascade=cv2.CascadeClassifier("eye.xml")

#------------------------------------------------------------------------------

#Get a videocapture object for the camera

cap=cv2.VideoCapture(0)

#------------------------------------------------------------------------------

#Set Up an infinite loop and use read() method to read frames using object

while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    
    #Showing frames

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
    
        eyes=eyes_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
    cv2.imshow("img",img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

#------------------------------------------------------------------------------
        
#After loop release cap object

cap.release()
cv2.destroyAllWindows()
                   