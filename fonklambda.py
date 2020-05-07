a=lambda x,y:x*y
print(a(2,5))

b=lambda x=5,y=4:x*y
print(b())

c=lambda x=5,y=2:x/y
print(c())

d=lambda x=5,y=3:x**y
print(d())

##e=lambda x,y:x+y
##x=input("ilk sayı : ")
##y=input("ikinci sayı : ")
##print(e())

a=99
def f():
    a=191
    print("f() fonksiyonunda a değişkeninin değeri:",a)

b=99
def g():
    b=b+200
    print("g() fonsiyonunda b değişkeninin değeri:",b)

c=99
def h():
    global c
    c=c+200
    print("h() fonsiyonunda b değişkeninin değeri:",c)
    
def carpim(x,y):
    'Verilen sayıların çarpımını döndüren bir fonksiyondur.'
    return x*y
