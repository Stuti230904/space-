import datetime
from tkinter import *

import mysql.connector

from game import level, score

mycur = mysql.connector.connect(
    host="localhost",
    user="root",
    password="stuti23", )
cur = mycur.cursor()

date = datetime.date.today()

username = Tk()
username.title("Scores")
username.configure(bg="black")
username.iconbitmap("icon.ico")
username.geometry("1500x1000")
lbl = Label(username, text="GAME OVER", font=("Garamond", 50), bg="white")
lbl.place(x=550, y=250)
lbl1 = Label(username, text="You scored " + str(level * 20 + score) + " points", font=("Garamond", 20), bg="light blue")
lbl1.place(x=650, y=400)
lbl2 = Label(username, text="Please enter the UserID", font=("Garamond", 20), bg="light blue")
lbl2.place(x=500, y=500)

txt = Entry(username, width=25)
txt.place(x=900, y=512)

cur.execute('SHOW DATABASES')
flag = True
for data in cur:
    if "game_data" in data:
        flag = False
if flag:
    cur.execute('CREATE DATABASE game_data')

cur.execute('USE game_data')

cur.execute('SHOW TABLES')

flag = True
for data in cur:
    if "score" in data:
        flag = False
if flag:
    cur.execute("CREATE TABLE score (UserID VARCHAR(50), Score INT(5), Date date)")


def submit():
    if txt.get() == "":
        x= 'DEFAULT'
    else:
        x = txt.get()
    cur.execute("Select UserID from score")
    data = ()
    for i in cur:
        data += i
    if x in data:
        cur.execute("Select Score from score where UserID= '%s'" % x)
        for lvl in cur:
            for l in lvl:
                if level > l:
                    cur.execute("Update score set Score='%s' where UserID='%s'" % (level, x))
                    mycur.commit()

        lbl3 = Label(username, text="UserID exists. High score updated!")
        lbl3.place(x=700, y=700)

    else:
        insert = ("INSERT INTO score (UserId, Score, Date) VALUE (%s, %s, %s)")
        b = (x, level, date)
        cur.execute(insert, b)
        mycur.commit()
        lbl4 = Label(username, text="New UserID created")
        lbl4.place(x=725, y=700)
    btn = Button(username, text="EXIT", height=2, width=8, bg="light blue", command=username.destroy)
    btn.place(x=750, y=750)


Btn = Button(username, text='SUBMIT', height=2, width=8, bg="light blue",
             command=submit)
Btn.place(x=750, y=600)

username.mainloop()
