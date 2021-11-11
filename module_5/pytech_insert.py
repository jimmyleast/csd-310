""" Python import statement"""

from pymongo import MongoClient

# URL variable
url = "mongodb+srv://admin:admin@cluster0.mnrwy.mongodb.net/pytech"

#client variable
client = MongoClient(url)

#db variable
db = client.pytech


""" three student documents"""
# Thor Odinson data document 
thor = {
    "student_id": "1007",
    "first_name": "Thor",
    "last_name": "Odinson",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.6",
            "start_date": "October 18, 2021",
            "end_date": "December 19, 2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Tracy Shelanskey",
                    "grade": "A"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Darrell Payne",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# Loki Odinson data document 
loki = {
    "student_id": "1008",
    "first_name": "Loki",
    "last_name": "Odinson",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.25",
            "start_date": "October 18, 2021",
            "end_date": "December 19, 2021",
            "courses": [
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Darrell Payne",
                    "grade": "A"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Darrell Payne",
                    "grade": "B"
                }
            ]
        }
    ]
}

# Bruce Banner data document
bruce = {
    "student_id": "1009",
    "first_name": "Bruce",
    "last_name": "Banner",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "2.5",
            "start_date": "October 18, 2021",
            "end_date": "December 19, 2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Darrell Payne",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Darrell Payne",
                    "grade": "B"
                }
            ]
        }
    ]
}

# Create the students variable 
students = db.students

# print the header for the insert statements
print("\n  -- INSERT STATEMENTS --")

# Display thor student insert
thor_student_id = students.insert_one(thor).inserted_id
print("  Inserted student record Thor Odinson into the students collection with document_id " + str(thor_student_id))
# Display loki student insert
loki_student_id = students.insert_one(loki).inserted_id
print("  Inserted student record Loki Odinson into the students collection with document_id " + str(loki_student_id))
# Display bruce student insert
bruce_student_id = students.insert_one(bruce).inserted_id
print("  Inserted student record Bruce Banner into the students collection with document_id " + str(loki_student_id))
# print the end statement
input("\n\n  End of program, press any key to exit... ")
