import pickle

data={
    "a":[1,3.4,4,6+5j],
    "b":("sefdara ","asdasdas","seksen"),
    "c":{"serdar":"sezgin","rahşan":"arzu"}
}

with open("dosya_1.txt","wb") as f:
    pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)

##with open("dosya.txt","rb") as f:
##    dosya2=f
##    data2=pickle.load(dosya2)
##    y=data2
##    print(y)