from tkinter import *

ana=Tk()

cerceve = Frame()
cerceve.pack()

B1 = Button(cerceve)
B1.config(text="Birinci Düğme", font=("Verdana", 20, "bold"), bg="#cadeab", fg="blue", )
B1.pack(side=LEFT)

B2 = Button(cerceve)
B2.config(text="İkinci Düğme", font=("Courier New", 20, "italic underline"), )
B2.pack(side=RIGHT)

ana.mainloop()