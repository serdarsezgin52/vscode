# Dosyayı açıp yoksa oluşturup içine bilgi girişi yapar.
with open("Python.txt","w") as f:
    f.write("Python Öğreniyorum Arkadaşlar")

# Varalan Dosyayı Açıp İçindeki veriyi okur.
with open("Python.txt","r") as f:
    s=f.read()
print(s)

