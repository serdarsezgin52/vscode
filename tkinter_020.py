import sys
from tkinter import *

ana=Tk()

prDil=("perl", "Python", "tcl/Tk")


def yaz():
	for p in prDil:
		print(sonuc[p].get()),
		print()
def temizle():
	for p in prDil:
		sonuc[p].set(0)


L=Label(text="Hagi dilleri biliyorsunuz?")
L.pack()

sonuc={}

for p in prDil:
	sonuc[p]=IntVar()
	Checkbutton(text=p, variable=sonuc[p]).pack(anchor=NW)


# Td1=Checkbutton(text="Perl")
# var1=IntVar()
# Td1.config(variable=var1)
# Td1.pack(anchor=NW)


# Td2=Checkbutton(text="Python")
# var2=IntVar()
# Td2.config(variable=var2)
# Td2.pack(anchor=NW)
# var2.set(1)

# Td3=Checkbutton(text="Tcl/Tk")
# var3=IntVar()
# Td3.config(variable=var3)
# Td3.pack(anchor=NW)

D1=Button(text="Seçimler", command=yaz)
D1.pack(side="left")

D2=Button(text="Temizle", command=temizle)
D2.pack(side="right")

ana.mainloop()