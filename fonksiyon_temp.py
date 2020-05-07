Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def verileniYaz(gelenBilgi):
	print("Bu fonksiyona gönderilen bilgi: "),gelenBilgi

	
>>> verileniYaz("Bir cümle gönderiyorum")
Bu fonksiyona gönderilen bilgi: 
>>> def verileniYaz(gelenBilgi):
	print("Bu fonksiyona gönderilen bilgi: ",gelenBilgi)

	
>>> verileniYaz("Bir cümle gönderiyorum")
Bu fonksiyona gönderilen bilgi:  Bir cümle gönderiyorum
>>> def topla(a,b):
	print("Toplam...: ", a+b)

	
>>> topla(5,6)
Toplam...:  11
>>> def ePostaYap(hesap,alan="gmail.com"):
	print("{}@{}".format(hesap,alan))

	
>>> ePostaYap("SerdarSezgin")
SerdarSezgin@gmail.com
>>> ePostaYap("RahsanSezgin")
RahsanSezgin@gmail.com
>>> topla(15,30)
Toplam...:  45
>>> ePostaYap("serdar","outlook.com")
serdar@outlook.com
>>> ePostaYap(alan="serdarsezgin.com",hesap="info")
info@serdarsezgin.com
>>> 