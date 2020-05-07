import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', password='1234',database='siniflar')
cursor = cnx.cursor()

query = ("Select no, adisoyadi, fen, matematik, sosyal FROM  2a")

cursor.execute(query)

for(no, adisoyadi,fen,matematik,sosyal) in cursor:
    print(no,adisoyadi,fen,matematik,sosyal)

cursor.close()
cnx.close()