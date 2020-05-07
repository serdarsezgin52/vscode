from tkinter import *

ana=Tk()

cerceve = Frame()
cerceve.pack()

B1 = Button(cerceve)
B1.config(text="Birinci Düğme", height=10, width=12 )
B1.pack(side=LEFT)

B2 = Button(cerceve)
B2.config(text="İkinci Düğme", width=12, height=5 )
B2.pack(side=RIGHT)

ana.mainloop()