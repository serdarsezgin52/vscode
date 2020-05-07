from tkinter import *

def pencereAc():
	Penceren = Toplevel()
	Penceren.title("Penceren")
	BP2 = Label(Penceren, text="Sonradan Açılan üst düzey pencere")
	BP2.pack()


ana=Tk()
ana.title("ANA PENCERE")
Pencere1=Toplevel()
Pencere1.title("Pencere1")

B=Button(ana, text="Yeni Pencere İçin Tıkla...", command=pencereAc)
B.pack()

B1=Button(Pencere1, text="Birinci üst düzey pencere")
B1.pack()

ana.mainloop()