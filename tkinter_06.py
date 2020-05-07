import sys
from tkinter import *


def gel(event):
	widget.config(text="Heey çek üzerimden şu fareyi")


def git(event):
	widget.config(text="Oh be fare üzerimden gitti...")

def sag(event):
	widget.config(text="Sağ tuşa tıkladın...")

def sol(event):
	widget.config(text="Sol tuşa tıkladın...")

def hareket(event):
	widget.config(text="Fare hareket ediyor")


ana=Tk()

widget=Button()
widget.config(text="Fareyi üzerime getir")
widget.bind('<Enter>', gel)
widget.bind('<Leave>', git)
widget.bind('<Button-3>', sag)
widget.bind('<Button-1>', sol)
widget.bind('<Motion>', hareket)
widget.pack()

ana.mainloop()