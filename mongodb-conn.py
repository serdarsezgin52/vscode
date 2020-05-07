import pymongo
myclient = pymongo.MongoClient("mongodb+srv://serdar:fKW4EDTv8VsCLjtf@cluster0-aq7x1.gcp.mongodb.net/node--app?retryWrites=true&w=majority")


mydb = myclient["node--app"]
mycollection = mydb["product"]

# product = {"Name":"Samsung S6", "price": 2000}

# result = mycollection.insert_one(product)

# print(result)
# print(type(result))

productList = [
    {"name":"Samsung S7", "price": 3000, "description": "fena değil"},
    {"name":"Samsung S8", "price": 4000,  "categories": ['telefon','elektronik']}
]