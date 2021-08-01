# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 01:51:04 2020

@author: OCAC
"""

import webbrowser as wb

def webauto():
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"  # path chrome
    URLS=(
            "stackoverflow.com",
            "github.com",
            "gmail.com",
            "google.com",
            "youtube.com",
            "1337x.tw"
            )
    for url in URLS:
        print("opening :"+ url)
        wb.get(chrome_path).open(url)
        
webauto()