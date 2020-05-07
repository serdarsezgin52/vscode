class Hesmak():
    def __init__(self, a, b):
        self.a=a
        self.b=b
    
    def toplam(self):
        return self.a + self.b

    def fark(self):
        return self.a - self.b

    def carpim(self):
        return self.a * self.b
    
    def bolum(self):
        return self.a / self.b

a = int(input("İlk Sayıyı Giriniz :"))
b = int(input("İlk Sayıyı Giriniz :"))
obj=Hesmak(a,b)
secim=1
while secim !=0:
    print("0. Çıkış")
    print("1. Toplama")
    print("2. Çıkartma")
    print("3. Çarpma")
    print("4. Bölme")
    
    secim = input("Yapmak İstediğiniz İşlemi Seçiniz :")

    if secim==1:
        print("Sonuç :", obj.toplam())
    elif secim==2:
        print("Sonuç :", obj.fark())
    elif secim==3:
        print("Sonuç :", obj.carpim())
    elif secim==4:
        print("Sonuç :", obj.bolum())
    elif secim==0:
        print("Çıkış Yaptınız!")
    else:
        print("Hatalı Seçim Yaptınız!")

print()

