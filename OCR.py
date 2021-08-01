# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 01:15:30 2020

@author: OCAC
"""

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #path to tesseract

def convert():
    img=Image.open("test.png")
    text=pytesseract.image_to_string(img)
    print(text)
    
convert()