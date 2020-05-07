from tkinter import *
from tkinter import colorchooser


def renkSec():
    a=colorchooser.askcolor()
    E.config(bg=a[1])

ana=Tk()

E=Label(text="Arkaplan rengini değiştirmek\n için düğmeye tıklayınız.")
E.pack()

D=Button(text="Renk Seç", command=renkSec)
D.pack()

ana.mainloop()