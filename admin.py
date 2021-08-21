import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk

import mysql.connector
import mysql.connector


def admin():
    # some kind of password system here which returns True if password is correct
    return True


if admin():

    mycur = mysql.connector.connect(
        host="localhost",
        user="root",
        password="stuti23", )

    cur = mycur.cursor()
    cur.execute("USE game_data")


    def update(rows):
        for i in rows:
            trv.insert("", 'end', values=i)


    def clear():
        cur.execute("delete from score")
        mycur.commit()
        screen.destroy()


    def delete():
        del1 = Tk()
        del1.title("Delete")
        del1.iconbitmap("icon.ico")
        del1.geometry("500x200")

        lbl = Label(del1, text="Enter the UserID for which data is to be deleted")
        lbl.grid(column=0, row=0)
        ent = Entry(del1, width=25)
        ent.grid(column=2, row=0)

        def get():
            cur.execute("Select UserId from score")
            flag = True
            for data in cur:
                if ent.get() not in data:
                    flag = False
            if flag:
                cur.execute("delete from score where UserID='%s'" % (ent.get()))
                mycur.commit()
                del1.destroy()
                screen.destroy()

            else:
                lbl.configure(text="Enter valid UserID")

        btn = Button(del1, text="Okay", command=get)
        btn.place(x=250, y=150)


    def updatescore():
        update1 = Tk()
        update1.title("Update")
        update1.iconbitmap("icon.ico")
        update1.geometry("500x200")

        ulbl = Label(update1, text="Enter the UserID for which data is to be updated")
        ulbl.grid(column=0, row=0)
        ent = Entry(update1, width=25)
        ent.grid(column=2, row=0)

        def upd1():
            cur.execute("Select UserId from score")
            flag = True
            for data in cur:
                if ent.get() not in data:
                    flag = False

            if flag:
                lbl1 = Label(update1, text="Enter the new score")
                lbl1.grid(column=0, row=2)
                ent1 = Entry(update1, width=25)
                ent1.grid(column=2, row=2)

                def upd2():
                    cur.execute("Update score set Score='%s' where UserID='%s'" % (ent1.get(), ent.get()))
                    mycur.commit()
                    update1.destroy()
                    screen.destroy()

                ubtn = Button(update1, text="Okay", command=upd2)
                ubtn.place(x=250, y=150)

            else:
                ulbl.configure(text="Enter valid UserID")

        btn2 = Button(update1, text="Okay", command=upd1)
        btn2.place(x=250, y=150)


    def add():
        add1 = Tk()
        add1.title("Add")
        add1.geometry("500x200")

        albl = Label(add1, text="Enter UserID")
        albl.grid(column=0, row=0)
        ent = Entry(add1, width=25)
        ent.grid(column=2, row=0)

        def ad1():
            cur.execute("Select UserId from score")
            flag = True
            for data in cur:
                if ent.get() in data:
                    flag = False

            if flag:
                lbl1 = Label(add1, text="Enter score")
                lbl1.grid(column=0, row=2)
                ent1 = Entry(add1, width=25)
                ent1.grid(column=2, row=2)

                def ad2():
                    date = datetime.date.today()
                    cur.execute("Insert into score values(%s,%s,%s)", (ent.get(), ent1.get(), date))
                    mycur.commit()
                    add1.destroy()
                    screen.destroy()

                abtn = Button(add1, text="Okay", command=ad2)
                abtn.place(x=250, y=150)

            else:
                albl.configure(text="UserID already exists!")

        btn2 = Button(add1, text="Okay", command=ad1)
        btn2.place(x=250, y=150)


    screen = tk.Tk()
    screen.title("Admin")
    screen.configure(background="grey")
    screen.iconbitmap("icon.ico")
    screen.geometry("1200x1000")

    wrapper1 = LabelFrame(screen, text="Scoreboard")
    wrapper2 = LabelFrame(screen, text="Clear")
    wrapper1.pack(fill='both', expand='yes', padx=20, pady=10)

    trv = ttk.Treeview(wrapper1, columns=(1, 2, 3), show='headings')
    trv.pack()

    trv.heading(1, text="UserName")
    trv.heading(2, text="Level")
    trv.heading(3, text="Date")

    cur.execute("SELECT * FROM Score ORDER BY Score DESC")
    rows = cur.fetchall()
    update(rows)

    cbtn1 = Button(screen, text="Clear", command=clear)
    cbtn1.place(x=300, y=800)

    cbtn2 = Button(screen, text="Delete", command=delete)
    cbtn2.place(x=500, y=800)

    cbtn3 = Button(screen, text="Add", command=add)
    cbtn3.place(x=700, y=800)

    cbtn4 = Button(screen, text="Update", command=updatescore)
    cbtn4.place(x=900, y=800)

    screen.mainloop()
else:
    denied = tk.Tk()
    denied.title("Access denied")
    denied.geometry("600x600")

    t1 = Label(denied, text="ACCESS\n DENIED", font=("Garamond", 25))
    t1.place(x=200, y=200)
