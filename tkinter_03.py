import tkinter as tk
#pen = tk.Tk()
#mes = tk.Label(text='Merhaba Dünya',
#               fg="white", bg="black",
#               width=15,
#               height=10
#               )
#mes.pack()


#but = tk.Button(
#    text="Bas",
#    width=25,
#    height=5,
#    bg="red",
#    fg="yellow"
#)
#but.pack()

#giris = tk.Entry(
#    fg="yellow",
#    bg="blue",
#    width=50
#)
#giris.pack()
#pen.mainloop()

#windows = tk.Tk()
#label = tk.Label(text="Name")
#entry = tk.Entry()

#label.pack()
#entry.pack()

# window = tk.Tk()
# text_box = tk.Text()
# text_box.pack()
# window.mainloop()


import random
from tkinter import *

sarkilar = ['Seni Seviyorum', 'gülüm benim', ' bal dudaklım', 'Hatasız Kul Olmaz']

def degistir():
	widget.config(text=random.choice(sarkilar))

ana=Tk()
widget=Button()
widget.config(text='Şarkılar')
widget.config(command=degistir)
widget.pack(expand=YES, fill=BOTH)
ana.mainloop()