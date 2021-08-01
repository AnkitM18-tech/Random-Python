# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:05:03 2020

@author: OCAC
"""

import pyttsx3

data=input("Enter The Text Which You want to Convert To Speech:")

engine=pyttsx3.init()
engine.say(data)
engine.runAndWait()