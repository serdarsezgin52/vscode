from tkinter import *
from tkinter import messagebox


def onayAl():

	if messagebox.askyesno("Onayla","Hard diskinizi biçimlemek istediğinizden eminmisiniz?"):
	   messagebox.showwarning("Evet","Hard diskinizi tertemiz yaptım")
	else:
		messagebox.showinfo("Hayır","Biçimleme iptal edildi")

def hata():
	messagebox.showerror("Hata","Bu programdan çıkmak yasaklanmıştır")


ana=Tk()

B1=Button(text="Biçimle", command=onayAl)
B1.pack(side=LEFT)

B2=Button(text="Çık", command=hata)
B2.pack(side=RIGHT)

ana.mainloop()
