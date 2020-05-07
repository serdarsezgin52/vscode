import sys

print(sys.argv[1:len(sys.argv)])

sayiDeger=map(int,sys.argv[1:len(sys.argv)])
print (sayiDeger)

##def addit(n):
##    return n+n
##numbers=(1,2,3,4)
##result=map(addit,numbers)
##print(list(result))

##numbers=(1,2,3,4)
##result=map(lambda x:x+x, numbers)
##print(list(result))

##numbers1=[1,2,3]
##numbers2=[4,5,6]
##
##result=map(lambda x,y:x+y,numbers1,numbers2)
##print(list(result))
##
### List of strings 
##l = ['sat', 'bat', 'cat', 'mat'] 
##
### map() can listify the list of strings individually 
##test = list(map(list, l)) 
##print(test) 
