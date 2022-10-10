# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 16:30:23 2022

@author: Akshay
"""

from tkinter import *

root = Tk()

root.title("Ascii")

root.geometry("400x400")
root.configure(background='snow')

inputWord = Entry(root)
inputWord.place(relx= 0.5, rely=0.5, anchor=CENTER)
label = Label(root,text="name in ascii", bg="red", fg="black")

def asciiConverter():
    wordGot= inputWord.get()
    
    for letter in wordGot: 
        label["text"] += str(ord(letter)) + " "
        
        btn=Button(root,text="Show name in Ascii",command=asciiConverter, bg='gold', fg = 'black')
        btn.place(relx=5, rely=5, anchor=CENTER)
        label.place(relx=5, rely=5, anchor=CENTER)
        
root.mainloop()