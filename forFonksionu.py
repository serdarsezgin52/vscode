for i in range(1,3):
    print("We're on time %d"%(i))
for x in range(1, 11):
    for y in range(1, 11):
        print('%d * %d = %d' % (x, y, x*y))

for x in range(3):
    print(x)
else:
    print('Final x = %d' % (x))

for i in range(1,10):
    print(i)

a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)
b=["Serdar","Rahşan","Sezer","Aslı","Cemal","Sakine","Murat","Sibel"]
s=1
for isim in b:
    print("isim-->",s,isim)
    s+=1
nums=[1,2,3,4,5]
for num in nums:
    for letter in "abc":
        # if num==3:
        # print("Found!")
        # break
        # continue
        print(num,letter)

for i in range(1,11):
    print(i)

x=0
# while x<10:
while True:
    if x == 5:
        break
    print(x)
    x+=1
