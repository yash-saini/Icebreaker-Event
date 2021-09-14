# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 00:31:47 2021

@author: yash
"""

from tkinter import *
from PIL import ImageTk, Image
import random
import json
with open(r"data.json") as f: 
    data1 = json.load(f)
l=data1['Questions']

window = Tk()

#Canvas
#canvas1 = Canvas(window, width = 500,height = 800,bg='bisque')

#widthxheight
window.geometry('1000x800')
canvas1 = Canvas(window, width = 1500,height = 800)
canvas1.pack(fill = "both", expand = True)

#bg=ImageTk.PhotoImage(Image.open(r"Water_image.jpg"))
bg1=PhotoImage(file=r"stadium5.png")

#Display image
canvas1.create_image( 0, 0, image = bg1, anchor = "nw")

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="Red", font=("Helvetica", 16),wraplength=350)
        self.label.pack()
        self.buttons()
        self.store=[]
    def remove_text(self):  
        #self.label.config(window,text="")
        window.destroy()
        
    def ques(self):
        fr=random.sample(l,3)
        for x in fr: 
            self.label = Label(canvas1,text=x,font=("Helvetica", 16,"bold"),wraplength=300,bg='#DBDBDB')
            self.label.pack()
    def buttons(self):
        bt =Button(canvas1, text="Ques", font=("Helvetica", 9,"bold"),anchor="e",bg="yellow",command=self.ques).pack(pady=10)
        bt2=Button(canvas1, text="Clear", anchor="w",font=("Helvetica", 9,"bold"),bg="yellow",command=self.remove_text).pack(pady=10)

    
app=App(window)
window.wm_title("Icebreaker Event")
window.mainloop()
