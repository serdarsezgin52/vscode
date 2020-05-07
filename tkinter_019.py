import sys
from tkinter import *

ana=Tk()

def yaz():
	print(var1.get(), var2.get(), var3.get())


L=Label(text="Hagi dilleri biliyorsunuz?")
L.pack()

Td1=Checkbutton(text="Perl")
var1=IntVar()
Td1.config(variable=var1)
Td1.pack(anchor=NW)


Td2=Checkbutton(text="Python")
var2=IntVar()
Td2.config(variable=var2)
Td2.pack(anchor=NW)
var2.set(1)

Td3=Checkbutton(text="Tcl/Tk")
var3=IntVar()
Td3.config(variable=var3)
Td3.pack(anchor=NW)

D1=Button(text="Seçimler", command=yaz)
D1.pack(side="left")

D2=Button(text="Çık", command=sys.exit)
D2.pack(side="right")

ana.mainloop()