# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:26:18 2020

@author: OCAC
"""

from tkinter import *
root=Tk()

def send():
    send="you:"+a.get()
    text.insert(END,"\n"+send)
    if(a.get()=="hi"):
        text.insert(END,"\n"+"Bot:hello")
    elif(a.get()=="hello"):
        text.insert(END,"\n"+"Bot:hi")
    elif(a.get()=="How are you?"):
        text.insert(END,"\n"+"Bot:I am Fine.What about you?")
    elif(a.get()=="I am fine"):
        text.insert(END,"\n"+"Bot:Nice To hear that")
    else:
        text.insert(END,"\n"+"Bot:Sorry I didn't get you")
        
text=Text(root,bg="white")
text.grid(row=0,column=0,columnspan=2)
a=Entry(root,width=80)
send=Button(root,text="Send",bg="white",width=20,command=send).grid(row=1,column=1)
a.grid(row=1,column=0)
root.title("Simple ChatBot")
root.mainloop()