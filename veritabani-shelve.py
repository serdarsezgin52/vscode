import shelve
dbf=shelve.open("ornek.db")
dbf["serdarsezgin"]="serdar@gmail.com"
dbf["rahşan"]="rahsan@gmail.com"
dbf.close()

dbf=shelve.open("ornek.db")
dbf["sezer"]="sezer@gmail.com"
print(dbf["serdarsezgin"])
print(dbf["sezer"])
dbf.close()

dbf=shelve.open("ornek.db")
dbf["sezer"]="sezersezgin@gmail.com"
print(dbf["sezer"])
dbf.close()