class A:
    def __init__(self):
        self.liste=[]
    def ekle(self,gelen):
        self.liste.append(gelen)

class B(A):
    def yaz(self):
        print(self.liste)

s=B()
s.ekle("SEZGİN")
s.ekle("Serdar")
s.yaz()