"""
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir("Merhaba\n",10)
"""

def listeyeCevir(*params):
    liste = []

    for param in params:
        liste.append(param)

    return liste

result = listeyeCevir(10,12,324,12,"serdar")

print (result)
