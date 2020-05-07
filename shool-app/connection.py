import mysql.connector
    

connection = mysql.connector.connect(
    host ="localhost",
    database = "schooldb",
    user = "root",
    password ="1234"
)