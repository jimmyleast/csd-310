""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    # insert player query 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    # player data fields 
    player_data = ("Smeagol", "Shire Folk", 1)

    # insert a new player record
    cursor.execute(add_player, player_data)
   
    # commit the insert to the database 
    db.commit()
    
    # create inner join query 
    cursor.execute("SELECT player_id, first_name,Last_name,team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    
    # get the results from the cursor object 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYERS AFTER INSERT --\n ")

    # iterate over the players data set and display the results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
        
    # create player update 
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    
    # commit the insert to the database 
    db.commit()
    
    # create inner join query 
    cursor.execute("SELECT player_id, first_name,Last_name,team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    
    # get the results from the cursor object
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYERS AFTER UPDATE --\n ")

    # iterate over the players data set and display the results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    # create player update 
    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")
    
    # commit the insert to the database 
    db.commit()
    
    # create inner join query 
    cursor.execute("SELECT player_id, first_name,Last_name,team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    
    # get the results from the cursor object
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYERS AFTER DELETE --\n ")

    # iterate over the players data set and display the results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

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