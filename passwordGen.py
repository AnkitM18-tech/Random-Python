# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:59:14 2020

@author: OCAC
"""

import string
import random
def gen():
    str1=string.ascii_uppercase
    
    str2=string.ascii_lowercase
   
    str3=string.digits
  
    str4=string.punctuation
    
    passlength=int(input("Enter the password length:"))
    
    s=[]
    s.extend(list(str1))
    s.extend(list(str2))
    s.extend(list(str3))
    s.extend(list(str4))
    random.shuffle(s)
    passwd=("".join(s[0:passlength]))
    print(passwd)
    
gen()