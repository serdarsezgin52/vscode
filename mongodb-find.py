import pymongo
from bson.objectid import ObjectId
myclient = pymongo.MongoClient("mongodb+srv://serdar:fKW4EDTv8VsCLjtf@cluster0-aq7x1.gcp.mongodb.net/node--app?retryWrites=true&w=majority")


mydb = myclient["node--app"]
mycollection = mydb["product"]

# result = mycollection.find_one()
for i in mycollection.find({},{"_id":0}):
    print(i)
# print(result)


