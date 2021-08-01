# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:18:40 2020

@author: OCAC
"""

import cv2

imgcapture=cv2.VideoCapture(0)
result=True

while(result):
    ret,frame =imgcapture.read()
    cv2.imwrite("test2.jpg",frame)
    result=False
    print("Done! Image Captured")
    
imgcapture.release()