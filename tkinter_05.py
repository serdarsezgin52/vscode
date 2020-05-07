from tkinter import *

def DugmeX(x):
	L.config(text="Şimdi  '%s'  düğmesine tıkladınız." % x)


ana=Tk()
L=Label(text="Aşağıdaki düğmelerden birisine tıklayınız")
L.pack()

B1=Button(text="Çıkma")
B1.config(command=(lambda : DugmeX("ÇIKMA")))
B1.pack(side="left")

B2=Button(text="Çık")
B2.config(command=(lambda : DugmeX("ÇIK")))
B2.pack(side="right")

ana.mainloop()