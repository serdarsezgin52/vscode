import pymongo
from bson.objectid import ObjectId
myclient = pymongo.MongoClient("mongodb+srv://serdar:fKW4EDTv8VsCLjtf@cluster0-aq7x1.gcp.mongodb.net/node--app?retryWrites=true&w=majority")


mydb = myclient["node--app"]
mycollection = mydb["product"]

filter = {"name":"Samsung S8"}

# result = mycollection.find({
#     "name": {
#         "$in" : ["Samsung S9", "Samsung S7"]
#     }
# })
# result = mycollection.find({
#     "price":{
#         "$gt": 2000 # den büyük olan kayıtlar $gte eşit ve büyük olan
#     }
# })


result = mycollection.find({
    "name": {"$regex": "^S" }  # Başlangıç harfini ver 
})
for i in result:
    print(i)
# print(result) 