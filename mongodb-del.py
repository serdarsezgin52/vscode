import pymongo
from bson.objectid import ObjectId
myclient = pymongo.MongoClient("mongodb+srv://serdar:fKW4EDTv8VsCLjtf@cluster0-aq7x1.gcp.mongodb.net/node--app?retryWrites=true&w=majority")


mydb = myclient["node--app"]
mycollection = mydb["product"]

# delete_one()
# delete_many()
for i in mycollection.find():
    print(i)
print('*'*50)

# mycollection.delete_one({"name": "Samsung S11"}) # Seçilen tek kayıtı siler
# mycollection.delete_many({"name": {"$regex":"^S"}})  #Seçilen harf ile başlayan tüm kayıtları siler
mycollection.delete_many({})  # Tüm kayıtları siler





for i in mycollection.find():
    print(i)

