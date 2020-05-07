from sys import exit
from tkinter import *


def tikla():
	E.config(text="Tıklama demiştim sana")


ana=Tk()

cerceve=Frame()
cerceve.pack()

E=Label(cerceve)
E.config(text="Sakın sol düğmeye Tıklama")
E.pack(side=TOP)
D1=Button(cerceve)
D1.config(text="Tıklama")
D1.config(command=tikla)
D1.pack(side=LEFT)
D2=Button(cerceve)
D2.config(text="Çık")
D2.config(command=exit)
D2.pack(side=RIGHT)

ana.mainloop()
