import tkinter
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *



mycur = mysql.connector.connect(
    host="localhost",
    user="root",
    password="stuti23", )

cur = mycur.cursor()
cur.execute("USE game_data")


def update(rows):
    for i in rows:
        trv.insert("", 'end', values=i)


screen = tk.Tk()
screen.title("High Scores")
screen.configure(background="grey")
screen.iconbitmap("icon.ico")
screen.geometry("600x600")

wrapper1 = LabelFrame(screen, text="Leaderboard")
wrapper1.pack(fill='both', expand='yes', padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1, 2, 3), show='headings', height='10')
trv.pack()

trv.heading(1, text="UserName")
trv.heading(2, text="Level")
trv.heading(3, text="Date")

cur.execute("SELECT * FROM Score ORDER BY Score DESC")
rows = cur.fetchall()
update(rows)


screen.mainloop()