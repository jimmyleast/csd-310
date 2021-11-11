
from pymongo import MongoClient

# URL variable
url = "mongodb+srv://admin:admin@cluster0.mnrwy.mongodb.net/pytech"

#client variable
client = MongoClient(url)

#db variable
db = client.pytech

# print the collection
print(db.list_collection_names())


