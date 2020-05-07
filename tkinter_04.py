from tkinter import *
from sys import exit

def solTus(event):
	widget.config(text="sol tuşa tıkladınız.")
	

def sagTus(event):
	widget.config(text="sağ tuşa tıkladınız.")


ana=Tk()
widget=Button()
widget.config(text="sol ya da sağ tuşa tıklayınız")
widget.bind('<Button-1>',solTus)
widget.bind('<Button-3>',sagTus)
widget.pack()
cks=Button(text="Çıkış",command=exit)
cks.pack()
ana.mainloop()
