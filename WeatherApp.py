# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:40:49 2020

@author: OCAC
"""

import requests
from bs4 import BeautifulSoup

search="weather in mumbai"
url=f"https://www.google.com/search?&q=(search)"

r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")

update=s.find("div",class_="BNeawe").text
print(update)