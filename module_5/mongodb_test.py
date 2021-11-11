
from pymongo import MongoClient

# URL variable
url = "mongodb+srv://admin:admin@cluster0.mnrwy.mongodb.net/pytech"

#client variable
client = MongoClient(url)

#db variable
db = client.pytech

# print the header
print("\n -- Pytech COllection List --")
# print the collection
print(db.list_collection_names())

# print the end statement
input("\n\n  End of program, press any key to exit... ")


