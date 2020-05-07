
ilkdosya=open("/benim.txt","w")
ilkdosya.write("Bu ilk Satır.")
ilkdosya.write("Bu ikinci Satır.")
ilkdosya.close()
ilkdosya=open("/benim.txt","w")
ilkdosya.write("Bu ilk satır.\n")
ilkdosya.write("Bu ikinci satır.\n")
ilkdosya.close()
ilkdosya=open("/benim.txt","r")
f=ilkdosya
f.readline()
f.readlines()
f.close()

import os #işletim isitemi ile alakalı komutlar modulü
dir(os)   # os modülünün metodlarını listeler
os.name   #işletim tipinin tipini verir.
os.environ # sistemin çevre değişkenlerini listeler.
for e in os.environ.keys():
    print(e,"---->",os.environ[e])
os.system(":\\windows\\system32\\notpad.exe")
os.system("dir c:\\")
dosya=open("c:\\aile.txt","r")
print(open("c:\\aile.txt","r").read())
print(dosya.read())
dosya.close()
dosya=open("c:\\aile.txt","w")
dosya.write("\nAilemizde başka kimse yok")
dosya.close()
dosya=open("/aile.txt","r")
dosya.read()
dosya=open("/aile.txt","a")
dosya.write("Serdar SEZGİN\n")
dosya.write("Arzu Rahşan SEZGİN\n")
dosya.close()
dosya=open("/aile.txt","w")
dosya.write("Serdar SEZGİN\n")
dosya.write("Arzu Rahşan SEZGİN\n")
dosya.write("Aslan Sezer SEZGİN\n")
dosya.write("Aslı Sezen SEZGİN\n")
dosya.write("Cemal Levent SEZGİN\n")
dosya.close()
dosya=open("/aile.txt","r")
for d in dosya:
    print("isim--->",d)

os.name
os.listdir("c:\\")
dosya=open("/aile.txt","r")
for d in dosya:
    for s in d:
        print(d,s)

with open("/aile.txt","r") as f:
    f.readlines()
    f.close()
with open("/aile.txt","a") as f:
    f.write("Arzu Rahşan SEZGİN\n"
            "Aslan Sezer SEZGİN\n"
            "Aslı Sezen SEZGİN\n"
            "Cemal Levet SEZGİN\n"
    )
f.close()
with open("/denemetxt.txt","w") as f:
    f.write("Bu birinci satır\n"
            "Bu ikinci satır\n"
            "Bu üçüncü satır\n"
            "Bu dördüncü satır\n")
f.close()
import os
os.listdir()
os.chdir("c:\\")
os.listdir()
with open("/denemetxt.txt","r") as f:
    f.readlines()
