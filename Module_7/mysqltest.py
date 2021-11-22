import mysqltest



try:
    db=mysql.conn = mysql.connector.connect(
        host = "localhost", user = "root",passwd = "Tomorrow!9")
    input("\n\n press any key to continue ")
    
except mysql.connector.Error as err:
    if err.erring ==errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The user name and password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified DB does not exist")
    else:
        print(err)
finally:
    db.close()
        