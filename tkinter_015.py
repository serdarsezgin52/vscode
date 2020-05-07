from  tkinter import filedialog
from tkinter import *



def dosyaAc():
    a=filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    if a: E.config(text=a)
    else: E.config(text="Dosya açma işlemi iptal edildi.")

ana=Tk()

E=Label(text="Dosya açmak için aşağıdaki düğmeye tıklayın") 
E.pack()

D=Button(text="Dosya aç", command=dosyaAc)
D.pack()

ana.mainloop()