# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 20:28:13 2020

@author: OCAC
"""

import pyshorteners
url=input("Enter The URL:\n")

print("URL after Shortening:- ",pyshorteners.Shortener().tinyurl.short(url))