# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:08:12 2020

@author: OCAC
"""

import pyttsx3
import speech_recognition as sr

def getSpeech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something....!")
        audio=r.listen(source)
        print("Done!")
        
    try:
        text=r.recognize_google(audio)
        print("You said "+ text)
        
    except Exception as ex:
        print(ex)
        
getSpeech()