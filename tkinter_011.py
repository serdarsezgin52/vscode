from tkinter import *

ana=Tk()

E1 = Label(text="Bu yazının etrafı çerçevelidir.")
E1.config(bd=3, relief=SOLID)
E1.pack(pady=5)

E2 = Label(text="Bu yazının etrafı içe göçük çerçevelidir.")
E2.config(relief=GROOVE)
E2.pack(pady=5)


E3 = Label(text="Bu yazının etrafıyukarı kalkık çerçevelidir.")
E3.config(bd=3, relief=RIDGE)
E3.pack(pady=5)


E4 = Label(text="Bu yazı içe çöküktür.")
E4.config(bd=4, relief=SUNKEN)
E4.pack(pady=5)

E5 = Label(text="Bu yazı yukarı kalkıktır.")
E5.config(bd=3, relief=RAISED)
E5.pack(pady=5)

B1 = Button()
B1.config(text="Bu Düğme Etkisizdir", state=DISABLED)
B1.pack(pady=5)

B2 = Button()
B2.config(text="Fare Bu Düğmenin Üstünde Değişir ", cursor="hand2")
B2.pack(pady=5)

ana.mainloop()