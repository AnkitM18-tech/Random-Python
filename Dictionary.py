# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 04:03:45 2020

@author: OCAC
"""
from difflib import get_close_matches
import json
data=json.load(open("original.json"))

word=input("Enter The Word You want to Search:")

if data.get(word):
    meaning=(data[word])
elif data.get(word.lower()):
    meaning=(data[word.lower()])
elif data.get(word.capitalize()):
    meaning=(data[word.capitalize()])
elif data.get(word.upper()):
    meaning=(data[word.upper()])
elif data.get(word.title()):
    meaning=(data[word.title()])
elif len(get_close_matches(word,data.keys())) >0 :
    print(f"Did You Mean {get_close_matches(word,data.keys())[0]} instead?")
    decision=input("Press\"yes\" or \"no\":")
    if decision =="yes":
        meaning=data[get_close_matches(word,data.keys())[0]]
    elif decision =="no":
        meaning="The Word Doesn't exist in the Dictionary"
    else:
        meaning="You Have Entered The Wrong Input!"
    
else:
    meaning="The Word Doesn't Exist in the Dictionary"
    
if type(meaning) == list:
    for item in meaning:
        print("\n"+item)

else:
    print("\n"+meaning)
    