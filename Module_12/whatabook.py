""" 
    Title: what_a_book.py
    Author: Jimmy Easter
    Date: 12/10/2021
    Description: WhatABook program; Console program that interfaces with a MySQL database
"""

""" import statements """
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def showMenu():
    print("\n  -- Main Menu --")

    print("    1. View Books\n    2. View Store Locations\n    3. View Users\n    4. Exit Program")

    try:
        userInput = int(input('      <Example enter: 1 to see all of the book listings>: '))

        return userInput
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def viewBooks(_cursor):
    # inner join query 
    cursor.execute("SELECT book_id, book_name, author, details from book")

    # get the results from the cursor object 
    books = cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")
    
    # iterate over the player data set and display the results 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def viewLocations(cursor):
    cursor.execute("SELECT store_id, locale from store")

    locations = cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def validateUser():
    """ validate the users ID """

    try:
        userID = int(input('\n      Enter a customers User id <Example 1 for Jimmy  =  user_id 1>: '))

        if userID < 0 or userID > 3:
            print("\n  Invalid customer number, program terminated...\n")
            sys.exit(0)

        return userID
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def mainMenu():
    """ display the users account menu """

    try:
        print("\n      -- Customer Menu --")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        menu_option = int(input('        <Example enter: 1 for all the books currently in your wishlist>: '))

        return menu_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def viewWishlist(cursor, user_id):
    """ query the database for a list of books added to the users wishlist """

    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
    
    wishlist = cursor.fetchall()

    print("\n        -- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def availableBooks(cursor, user_id):
    """ query the database for a list of books not in the users wishlist """

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))

    print(query)

    cursor.execute(query)

    books_to_add = cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def addBook(cursor, user_id, book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the WhatABook database 

    cursor = db.cursor() # cursor for MySQL queries

    print("\n  Welcome to the WhatABook Application! ")

    user_selection = showMenu() # show the main menu 

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            viewBooks(cursor)

        # if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            viewLocations(cursor)

        # if the user selects option 3, call the validate_user method to validate the entered user_id 
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
                    #getting and printing user details
            cursor.execute("SELECT user_id, first_name, last_name FROM user")
            users = cursor.fetchall()
            for user in users:
                print(" \n User ID: {}\n  First Name: {}\n  Last Name: {}\n".format(user[0], user[1], user[2]))
            my_user_id = validateUser()
            account_option = mainMenu()

            # while account option does not equal 3
            while account_option != 3:

                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    viewWishlist(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    availableBooks(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    addBook(cursor, my_user_id, book_id)

                    db.commit() # commit the changes to the database 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                # show the account menu 
                account_option = mainMenu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
            
        # show the main menu
        user_selection = showMenu()

    print("\n\n  Program terminated...")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()