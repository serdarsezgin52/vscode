import random

sayi=random.randint(1,10)
can = int(input("kaç hak kullanmak istersiniz: "))
hak = can
sayac=0

while hak > 0:
    hak -=1
    sayac +=1
    cevap=int(input("sayı: "))
    if sayi==cevap:
        print(f"Doğru tahmin {sayac}. defada bildiniz. Toplam puanınız: {100-(100/can)*(sayac-1)}")
        break
    elif sayi > cevap:
        print("yukarı")
    else:
        print("aşağı")

    if hak==0:
        print(f'hakkınız bitti. Tutlan sayı: ,{sayi}')
        
    
    

