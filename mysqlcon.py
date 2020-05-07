import mysql.connector

mdb =mysql.connector.connect(
        host ="localhost",
        user = "root",
        password = "1234",
        database = "mydatabase"
)

mycursor = mdb.cursor()

mycursor.execute("CREATE TABLE   customers (Name VARCHAR(255), address VARCHAR(255))")


#print(mdb)