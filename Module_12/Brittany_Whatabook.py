""" 
    Brittany Normandin for assignment module WhatABook
    Class: CSD 310
    Date: December 10, 2021
"""
#import statements
import sys
import mysql.connector
from mysql.connector import errorcode

#database config
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
#Display homepage
def displayHome():
    print("\n --What A BooK Menu--\n")
    print("\n 1. Store locations\n   2. Book List\n   3. My Account\n   4. Exit\n")

#Menu selection, checks if user makes a valid or invalid option
menuOptions = ["1", "2", "3", "4"]
choice = input(" Please make a selection based on the number. ")

while choice not in menuOptions:
    print("\n Invalid Selection: Please try picking one of the menu options below.")
    print("\n 1. Store locations\n   2. Book List\n   3. My Account\n   4. Exit\n")
    choice = int(input(" Please make a selection based on the number. "))

if choice in menuOptions:
    validChoice = int(choice)
    validChoice
            

#Display store locations
def show_locations(_cursor):
    _cursor.execute("Select store_id, locale from store")
    stores = _cursor.fetchall
    print("\n --Current Store Locations-- \n")
    for i in stores:
        print(f" Location: {i[1]}\n")

#Display book list
def displayBooks(_cursor):
    _cursor.execute("Select book_id, book_name, author, details from book")
    books = _cursor.fetchall()
    print("\n --Book List-- \n")
    for i in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

#Validate user account
def validateUser():
    print("\n --Account Login-- \n")
    validUserIds = ["1", "2", "3"]
    userID = input("Please enter your user ID: ")
    
    while userID not in validUserIds:
        print("\n** User ID is no valid, please try again. **\n")
        userID = input("Please enter your user ID: ")
    
    if userID in validUserIds:
        validUserID = int(userID)
        return userID

#Display user accounts
def show_account_menu():
    print("\n --Account Menu-- \n")
    print("\n 1. Wishlist\n 2. Add to Wishlist\n 3. Main Menu\n 4. Exit program")
    validAccountOptions = ["1", "2", "3", "4"]
    accountOptions = input("\n Please enter a valid menu option. ")
    
    while accountOptions not in validAccountOptions:
        print("\n** Selection is not valid: Please pick a menu option.")
        accountOptions = input("\n Please enter a valid menu option. ")
    
    if accountOptions in validAccountOptions:
        validAccountOption = int(accountOptions)
        return validAccountOption

#Display books that can be added to wishlist
def show_wishlist(_cursor, _user_id):
    _cursor.execute("Select user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " +
    "From wishlist " +
    "INNER JOIN user ON wishlist.user_id = user.user_id " +
    "INNER JOIN book ON wishlist.book_id = book.book_id " +
    "WHERE user.user_id = {}".format(_user_id))
wishlist = _cursor.fetchall()

#Print user wishlist
print("\n --Display Wishlist-- ")
for book in wishlist:
        print("     Book Name: {}\n     Author: {}\n".format(book[2], book[5]))

#List of books not in the users wishlist
def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details "
    "FROM book "
    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    print(query)
    _cursor.execute(query)
    books_to_add = _cursor.fetchall()
    print("\n --Available Books-- ")
    for book in books_to_add:
        print("\n Book ID: {}\n Book Name: {}\n".format(book[0], book[1]))
def add_book_to_wishlist(_cursor, user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#Try and catch handling potential MySQL database errors
try:
#Connect to database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

#Show the homepage
    print("\n Welcome to WhatABook Application! ")
    user_selection = displayHome()
except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)
    
#If the selection isn't 4
while user_selection != 4:
        
        #Show store locations
            if user_selection == 1:
                show_locations(cursor)
        
        #Show books
            if user_selection == 2:
                showBooks(cursor)
            
        #Asks to validate if they are a valid user
            if user_selection == 3:
            myID = validateUser()
            accountOptions = show_account_menu()
    
    #If it doesn't equal 3
while accountOptions != 3:
try:

    pass
        #Shows wishlist
            if accountOptions == 1:
                show_wishlist(cursor, myID)
            
        #Adds to wishlist
            if accountOptions == 2:
                show_books_to_add(cursor, myID)
                book_id = int(input("\n Enter the ID of the book to add: "))
                add_book_to_wishlist(cursor, myID, book_id)
            
            #Accept changes
                db.commit()
                print("\n Book id: {} was added to the wishlist!"format(book_id))
            
        #Display invalid option
            if accountOptions < 0 or accountOptions > 3:
                print("\n is not an option, please try again...")
            
        #Show account
            accountOptions = show_account_menu()

    #Display error
            if user_selection < 0 or user_selection > 4:
                print("\n is not an option, please try again...")
                user_selection = displayHome()
                print("\n\n Program ending, closing...")

#Handles errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password is incorrect.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database you are looking for does not exist.")

    else:
        print(err)

finally:
   
    #close connection to MYSQL
    db.close()