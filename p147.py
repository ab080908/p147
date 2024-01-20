#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:27:41 2024

@author: GB
"""

from tkinter import*
import random

root=Tk()
root.geometory= ("400x400")
root.title=("p147")
root.configure(background = "snow")
enter_word= Entry(root)
enter_word.place(relx= 0.5,rely=0.5, anchor= CENTER)
label_ascii= Label(root, bg='orange', fg='black',text="Name in Ascii code: ")
def AsciiConverter():
    input_word= str(enter_word.get())
    for letter in input_word:
        label_ascii["text"]+=str(ord(letter))+ " "
        ascii= int(ord(letter))
        encrypted= ascii-1
        label_ascii["text"]+= str(chr(encrypted) )
btn=Button(root, text="Show name in ascii", command= AsciiConverter, bg='gold', fg='black')
btn.place(relx=0.5,rely=0.4, anchor=CENTER)
label_ascii.place(relx=0.5, rely=0.6, anchor= CENTER)
root.mainloop()
