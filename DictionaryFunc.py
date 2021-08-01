# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:40:38 2020

@author: OCAC
"""
from difflib import get_close_matches
import json
data=json.load(open("original.json"))

word=input("Enter The Word You Want To Search:")

def translate(word):
    if word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif len(get_close_matches(word,data.keys()))>0:
        print(f"Did You Mean {get_close_matches(word,data.keys())[0]} instead?")
        decide=input("press\"yes\" or \"no\":")
        if decide == "yes":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide =="no":
            return("The Word Doesn't Exist in the Dictionary")
        else:
            return("You Have Entered Wrong Input")
    else:
        print("The Word You are looking For Is not In The Dictionary:")
    
output=translate(word)

if type(output) == list:
    for item in output:
        print("\n"+item)
        
else:
    print("\n"+output)
    
    