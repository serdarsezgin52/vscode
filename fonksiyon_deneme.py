class Sinif:
    def __init__(self,noGelen,isimGelen):
        self.no=noGelen
        self.isim=isimGelen
    
    def yaz(self):
        print(s.no,s.isim)
    
    def deneme(self):
        print("Şimdi sınıf içerisindeki yaz() fonksiyonu çağrılacak.")
        s.yaz()
s=Sinif(42,"Serdar SEZGİN")
s.deneme()
    