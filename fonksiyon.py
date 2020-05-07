def verileniYaz(gelenBilgi):
	print("Bu fonksiyona gönderilen bilgi: ",gelenBilgi)

def topla(a,b):
    print("Toplam...: ",a+b)

def ePostaYap(hesap,alan="serdarsezgin.com"):
    print("{}@{}".format(hesap,alan))

def ePostaYap1(*gelenler):
    return gelenler[0]+"@"+gelenler[1]

def denemeFon(ilkArguman,*digerleri):
    print(ilkArguman)
    print(digerleri)

def bolme(a,b):
    if (type(a)==type(1) or type(a)==type(1.2)) and (type(b)==type(1) or type(b)==type(1.2)):
            return a/b
    else:
            return (a,"ve",b, "birbirlerine bölünemezler.")

def ePostaYap2(hesap,alan="serdarsezgin.com"):
    return ("{}@{}".format(hesap,alan))
