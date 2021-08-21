from tkinter import *
from tkinter import messagebox
from tkinter import font
import tkinter
from PIL import ImageTk, Image
from tkinter import CENTER
from playsound import playsound
import tkvideo
from time import sleep
import pygame
import mysql.connector
import pyautogui

window = Tk()


def data(event):
    quit()


def play():
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/thispc/Downloads/Space-Invader-main/background.wav")
    pygame.mixer.music.play(loops=5)


def action(value):
    if value == "PLAY!":
        import game


    elif value == "QUIT":
        exit()

    elif value == "LEADERBOARD!":
        import leaderboard


    elif value == "ADMIN":
        import admin


image = Image.open('Img_space_bg.png')
# The (450, 350) is (height, width)
image = image.resize((1500, 1000), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
img = Label(window, image=my_img)
img.place(x=0, y=0)

image_2 = Image.open("ScreenshotStarfield.png")
img_resize = image_2.resize((10, 20), Image.ANTIALIAS)
img_bg = ImageTk.PhotoImage(img_resize)

fontstyle = ("Garamond", 35, "bold")

L1 = Label(window, text="SPACE INVADERS", font=fontstyle, bg="light blue")

L1.place(x=470, y=200)

fontstyle2 = ("Garamond", 29)
Button_play = Button(window, text='PLAY!', width=6, height=2, font=fontstyle2, bg="light blue",
                     command=lambda: action(mytext2))
Button_play.place(x=1150, y=500)
mytext2 = Button_play.cget('text')

fontstyle3 = ("Garamond", 29)
Button_sql = Button(window, text='LEADERBOARD!', height=2, width=17, font=fontstyle2, bg="light blue",
                    command=lambda: action(mytext3))
Button_sql.place(x=500, y=500)
mytext3 = Button_sql.cget('text')

fontstyle4 = ("Garamond", 29)
Button_quit = Button(window, text='QUIT', font=fontstyle2, height=2, width=8, bg="light blue",
                     command=lambda: action(mytext4))
Button_quit.place(x=150, y=500)
mytext4 = Button_quit.cget('text')

fontstyle5 = ("Garamond", 29)
Button_admin = Button(window, text='ADMIN', font=fontstyle2, height=2, width=8, bg="light blue",
                      command=lambda: action(mytext5))
Button_admin.place(x=625, y=700)
mytext5 = Button_admin.cget('text')

window.geometry("1500x1000")
window.title("Space Invaders")
window.mainloop()
