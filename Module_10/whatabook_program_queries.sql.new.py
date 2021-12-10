""" import statements """
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

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the whatabook database 
     #create the cursor
    cursor = db.cursor()
    
    print("\n  -- Main Menu --")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. View your whishlist\n    5. Add a book\n    6. Exit the program")
    
    #taking the initial user input
    mainMenu = int(input(" Please chose an Option 1 - 6: "))
    #matching the user input to the action
    if mainMenu == 1:
        #getting and printing book details
        cursor.execute("SELECT book_id, book_name, author, details FROM book")
        books = cursor.fetchall()
        for book in books:
            print("  Book ID: {}\n  Book Name: {}\n  Authors Name: {}\n  Book Details: {}\n".format(book[0], book[1], book[2], book[3]))
    elif mainMenu ==2:
        #getting and printing location details
        cursor.execute("SELECT store_id, locale from store")
        stores = cursor.fetchall()
        for store in stores:
            print("  Store ID: {}\n  Store Location: {}\n ".format(store[0], store[1]))
    elif mainMenu ==3:
        #getting and printing user details
        cursor.execute("SELECT user_id, first_name, last_name FROM user")
        users = cursor.fetchall()
        for user in users:
            print("  User ID: {}\n  First Name: {}\n  Last Name: {}\n".format(user[0], user[1], user[2]))
            #asking user if they would like to see their current whishlist
        makeUpdates = int(input("Would you like to view your current wishlist? Enter 10 for yes or 11 for no \n"))
        if makeUpdates == 10:
            #taking the user id whishlist they would like to see
            userID = int(input("Please enter a user ID 1, 2 or 3 :"))
            #getting and printing requested whishlist details
            cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = {}".format (userID))
            whishlists = cursor.fetchall()
            for whishlist in whishlists:
                print("  User ID: {}\n  First Name: {}\n  Last Name: {}\n Book ID: {}\n  Book Name: {}\n  Author Name: {}\n".format(whishlist[0], whishlist[1], whishlist[2], whishlist[3], whishlist[4], whishlist[5]))
        else:
            mainMenu
    elif mainMenu == 4:
        #getting and printing all user whishlist details
        cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = 1,2 ,3 ")
        whishlists = cursor.fetchall()
        for whishlist in whishlists:
            print("  User ID: {}\n  First Name: {}\n  Last Name: {}\n Book ID: {}\n  Book Name: {}\n  Author Name: {}\n".format(whishlist[0], whishlist[1], whishlist[2], whishlist[3], whishlist[4], whishlist[5]))
    elif mainMenu == 5:
        #getting and printing all user details
        cursor.execute("SELECT user_id, first_name, last_name FROM user")
        users = cursor.fetchall()
        for user in users:
            print("  User ID: {}\n  First Name: {}\n  Last Name: {}\n".format(user[0], user[1], user[2]))
            #getting and printing all book details
        cursor.execute("SELECT book_id, book_name, author, details from book")
        books = cursor.fetchall()
        for book in books:
            print("  Book ID: {}\n  Book Name: {}\n  Authors Name: {}\n  Book Details: {}\n".format(book[0], book[1], book[2], book[3]))
            #taking user and book id numbers to add new book to user whishlist
        userID = int(input("Please enter a user id 1-3"))
        bookID= int(input("Please enter a book id 1-20"))
        cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(userID,bookID))
        # commit the insert to the database 
        db.commit()
    else:
        #exiting the program
        input("\n\n  Press any key to continue... ")
        
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