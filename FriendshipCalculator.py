# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:35:00 2020

@author: OCAC
"""
#import libraries
import random
import tkinter as tk

#------------------------------------------------------------------------------
#rootWindow
root=tk.Tk()
root.geometry("800x200")
root.title("Friendship Calculator")

#------------------------------------------------------------------------------
#Function
def CheckLove():
    result=40+random.randint(1,60)
    text_area=tk.Text(master=root,height=2,width=60,bg="#FFFF99")
    text_area.grid(column=0,row=5)
    result=("Your Friendship Score is:",result)
    text_area.insert(tk.END,result)
#------------------------------------------------------------------------------
#Labels and Button Configuration
name1=tk.StringVar()
name2=tk.StringVar()
entryname1=tk.Entry(root,width=20,textvariable=name1)
entryname1.grid(column=1,row=1)
entryname2=tk.Entry(root,width=20,textvariable=name2)
entryname2.grid(column=1,row=2)

button2=tk.Button(root,text="\tCHECK LOVE\t",bg="blue",command=CheckLove)
button2.grid(column=1,row=3)
label1=tk.Label(root,text="Your Name: ",bg="red",font=(" ",15,"bold"))
label1.grid(row=1,column=0,pady=5,padx=5)
label2=tk.Label(root,text="Friend\'s Name: ",bg="red",font=(" ",15,"bold"))
label2.grid(row=2,column=0,pady=5,padx=5)
    
root.mainloop()