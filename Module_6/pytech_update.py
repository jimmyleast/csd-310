
""" Python import statement"""
from pymongo import MongoClient

#Create the URL variable
url = "mongodb+srv://admin:admin@cluster0.mnrwy.mongodb.net/pytech"

#Create the client variable
client = MongoClient(url)

#Create the db variable
db = client.pytech

# Create the students variable 
students = db.students

# find all students in the collection using the .find{} method
docs = db.students.find({})

# print the header
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM .find() QUERY --")

# loop over the collection and output the results 
for doc in docs:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] 
          + "\n  Last Name: " + doc["last_name"] + "\n")
    
# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Odinson II"}})

# find document by student_id
doc = db.students.find_one({"student_id": "1007"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM .find_one() QUERY --")
print("  Student ID: " + doc["student_id"] + "\n  First Name: " 
      + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")