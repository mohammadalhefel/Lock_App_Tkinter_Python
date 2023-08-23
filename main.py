import tkinter.font as tkf
import os
import cv2
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
# print(tkf.families())
root.geometry("290x500")
root.title("Screen Lock [Mohammad Al Hefel]")
image = ImageTk.PhotoImage(Image.open('/home/kasper/Desktop/Python/lock_app/icon.ico'))
root.wm_iconphoto(True, image)
root.resizable(False , False)
root.wait_visibility(root)
root.wm_attributes("-alpha", 0.9)

# Functions
def zero(enent=None):
    en1.insert(END , 0)

def one(enent=None):
    en1.insert(END , 1)

def two(enent=None):
    en1.insert(END , 2)

def three(enent=None):
    en1.insert(END , 3)

def four(enent=None):
    en1.insert(END , 4)

def five(enent=None):
    en1.insert(END , 5)

def six(enent=None):
    en1.insert(END , 6)

def seven(enent=None):
    en1.insert(END , 7)

def eight(enent=None):
    en1.insert(END , 8)

def nine(enent=None):
    en1.insert(END , 9)

def clear(enent=None):
    en1.delete("0" , END)
    label_err.place(x = 1700  , y = 1700)

def ok():
    global password
    password = en1.get()
    if password == "1234":
        messagebox.showinfo("Welcome" , "Welcome , Correct Password")
        win = Tk()
        win.geometry("200x60")
        win.title("Mohammad Al Hefel")
        text = Label(win , fg = "#00a388" ,text = "Welcome To Programm")
        text.pack()
        win.resizable(False , False)
        win.mainloop()
    
    if password != "123":
        global label_err
        # messagebox.showerror("Error" , "Wrong Password")
        label_err = Label(root , text = "Wrong Password !" , fg="#F00" , bg="#FFF")
        label_err.place(x = 83 , y = 157)
        capture = cv2.VideoCapture(0)
        ret , image = capture.read()
        cv2.imwrite("/home/kasper/Desktop/Python/lock_app/lock.png" , image)
        del(capture)
# Design Body
# Label
label = Label(root , text="Screen Lock" , fg="#FFF" , bg="#00a388", pady = 8 , font=("TeX Gyre Pagella" , 28))
label.pack(fill="x")

# Frame
frm1 = Frame(root , bg="#FFF")
frm1.place(x = 1 , y = 50 , width = 298 , height = 460)

# Title
title_1 = Label(frm1 , text = "Enter Password" , fg = "#000" , bg = "#FFF" ,font = ("Noto Serif Armenian" , 16))
title_1.place(x = 64 , y = 15 )

# Entry
en1 = Entry(frm1 , fg = "#00a388" , bg="#FFF" , justify = CENTER ,bd=2 , relief=RIDGE , width = 20 , font=("TeX Gyre Pagella" , 18))
en1.place(x = 20 , y = 70)

# Create Buttons

b1 = Button(frm1 , text= "1" , fg="#FFF" ,bg="#00a388" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,
            command = one)
b1.place(x = 35 , y = 140 )

b2 = Button(frm1 , text= "2" , fg="#FFF" ,bg="#00a388" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,command = two)
b2.place(x = 115 , y = 140 )

b3 = Button(frm1 , text= "3" , fg="#FFF" ,bg="#00a388" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,command = three)
b3.place(x = 195 , y = 140 )

b4 = Button(frm1 , text= "4" , fg="#FFF" ,bg="#00a388" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,command = four)
b4.place(x = 35 , y = 210 )

b5 = Button(frm1 , text= "5" , fg="#FFF" ,bg="#00a388" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,command = five)
b5.place(x = 115 , y = 210 )

b6 = Button(frm1 , text= "6" , fg="#FFF" ,bg="#00a388" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,command = six)
b6.place(x = 195 , y = 210 )

b7 = Button(frm1 , text= "7" , fg="#FFF" ,bg="#00a388" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,command = seven)
b7.place(x = 35 , y = 280 )

b8 = Button(frm1 , text= "8" , fg="#FFF" ,bg="#00a388" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,command = eight)
b8.place(x = 115 , y = 280 )

b9 = Button(frm1 , text= "9" , fg="#FFF" ,bg="#00a388" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,command = nine)
b9.place(x = 195 , y = 280 )

b_clear = Button(frm1 , text= "AC" , fg="red" ,bg="#FFF" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,
                 command=clear)
b_clear.place(x = 35 , y = 350 )

b0 = Button(frm1 , text= "0" , fg="#FFF" ,bg="#00a388" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) ,command = zero)
b0.place(x = 115 , y = 350 )

b_ok = Button(frm1 , text= "OK" , fg="#00a388" ,bg="#FFF" , bd = 0 , relief = SOLID , width = 3 , cursor="hand2" , font = ("Noto Serif Armenian" , 16) , command = ok)
b_ok.place(x = 195 , y = 350 )

root.mainloop()