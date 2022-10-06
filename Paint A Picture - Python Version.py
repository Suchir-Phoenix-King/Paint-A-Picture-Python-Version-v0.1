# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:11:45 2022

@author: PC_RC
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Paint A Picture - Python Version")
root.geometry("600x600")


color_label = Label(root, text = "Enter a Color: ")
color_label.place(relx = 0.6, rely = 0.9, anchor = CENTER)

input_box = Entry(root)
input_box.insert(0, "black")
input_box.place(relx = 0.8, rely = 0.9)

canvas = Canvas(root, width = 590, height = 510, bg = "white", highlightbackground="lightgrey")
canvas.pack()

img = ImageTk.PhotoImage(Image.open("start_point1.png"))
my_image = canvas.create_image(50,50,image = img)

direction = ""
oldx = 50
oldy = 50
newx = 50
newy = 50

def draw(direction, oldx, oldy, newx, newy):
    fill_color = input_box.get()

root.bind("<Right>")
root.bind("<Left>")
root.bind("<Up>")
root.bind("<Down>")

root.mainloop()