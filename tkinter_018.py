import sys
from tkinter import *


ana=Tk()

metin=open("c:\\aile.txt").read()
M=Message(text=metin)
M.config(justify="left")
M.pack()

D=Button(text="Çık", command=sys.exit)
D.pack()

ana.mainloop()