""" Python import statement"""
from pymongo import MongoClient

#Create the URL variable
url = "mongodb+srv://admin:admin@cluster0.mnrwy.mongodb.net/pytech"

#Create the client variable
client = MongoClient(url)

#Create the db variable
db = client.pytech

# New person data document 
jane = {
    "student_id": "1010",
    "first_name": "Jane",
    "last_name": "Doe"
}

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
    
# print the header for the insert statements
print("\n  -- INSERT STATEMENTS --")

# Display thor student insert
jane_student_id = students.insert_one(jane).inserted_id
print("  Inserted student record Thor Odinson into the students collection with document_id " 
      + str(jane_student_id))

# find document by student_id
doc = db.students.find_one({"student_id": "1010"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM .find_one() QUERY --")
print("  Student ID: " + doc["student_id"] + "\n  First Name: " 
      + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# call the delete_one method to remove the student_test_doc
deleted_student_jane = students.delete_one({"student_id": "1010"})

# find all students in the collection using the .find{} method
docs = db.students.find({})

# print the header
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM .find() QUERY --")

# loop over the collection and output the results 
for doc in docs:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] 
          + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")