import numpy as np

num1 = np.array([10,15,30,45,60])

num2 = np.arange(5,15)

num3 = np.arange(50,100,5)

num4 = np.zeros(10)

num5 =np.ones(10)

num6 = np.linspace(0,100,5)

num7 = np.random.randint(1,50,6)

num8 = np.random.randn(10) # yapamadım.. OK.

num9 = np.random.randint(1,50,48).reshape(8,6) # sayısal loto 6/49 Örnek

matris = np.random.randint(-50,50,48).reshape(8,6)
print(matris)

# rowtotal = matris.sum(axis=1)
# coltotal = matris.sum(axis=0)

# print(rowtotal)
# print(coltotal)

num10 = matris.max()  # matristeki en büyük sayı
num11 = matris.min()  # matristeki en küçük sayı
num12 = matris.mean() # matrisdeki sayıların ortalaması 
num13 = matris.argmax()  # matristeki en büyük sayının indexi
num14 = matris.argmin()  # matristeki en kücük sayının indexi

arr = np.arange(10,20)
print (arr)
num15 = arr[:3]
num16 = arr[::-1]
num17 = matris[3,2]
num18 = matris[:,0]
num19 = matris**2
ciftler = matris[matris %2 == 0]
pozitif = ciftler[ciftler>0]
print(pozitif)