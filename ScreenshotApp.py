# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 04:24:01 2020

@author: OCAC
"""

import time
import pyautogui
import tkinter as tk

def screenShot():
    name=int(round(time.time()*1000))      #generating random Number
    name="C:/Users/OCAC/Desktop/Python Programs/Projects/Screenshotsdata/{}.png".format(name)             #saving each ss in png
    time.sleep(5)
    img=pyautogui.screenshot(name)
    img.show()
 
"""
creating a screen for interaction
"""
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(
        frame,
        text="Take Screenshot",
        command=screenShot)

button.pack(side=tk.LEFT)
close=tk.Button(
        frame,
        text="Quit",
        command=quit)

close.pack(side=tk.LEFT)

root.mainloop()