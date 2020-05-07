import pymongo
from bson.objectid import ObjectId
myclient = pymongo.MongoClient("mongodb+srv://serdar:fKW4EDTv8VsCLjtf@cluster0-aq7x1.gcp.mongodb.net/node--app?retryWrites=true&w=majority")


mydb = myclient["node--app"]
mycollection = mydb["product"]

# update_one
# update_many

for i in mycollection.find():
    print(i)
mycollection.update_one(
    {"name":"Iphone 6"},
    {"$set":{
        "price": 4500
    }}
)

for i in mycollection.find():
    print(i)