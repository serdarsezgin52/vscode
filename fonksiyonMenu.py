def carpim():
    print("Bu fonksiyon çarpma işlemi yapacak")

def toplam():
    print("Bu fonksiyon toplama işlemi yapacak")

def bolum():
    print("Bu fonksiyon bölme işlemi yapacak")

def cikis():
    print("Şimdi Çıkılacak...")
    

istenen=""

while istenen!="E":
    print("Hangi işlemin yapılmasını istiyorsunuz?")
    print("[C]arpma [T]oplama [B]olme [E)xit")

    istenen=input()

    menu={
            "C":carpim,
            "c":carpim,
            "T":toplam,
            "t":toplam,
            "B":bolum,
            "b":bolum,
            "E":cikis,
            "e":cikis
}

    menu[istenen]()
