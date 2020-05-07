from tkinter import *


def yaz():
    E.config(text="Merhaba %s" % Bgir.get())


ana=Tk()

E=Label(text="Adınız ve soyadınız:")
E.pack()

Bgir=Entry()
Bgir.pack()

D=Button(text="Tamam", command=yaz)
D.pack()
ana.mainloop()