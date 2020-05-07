import sqlite3

connection = sqlite3.connect("sample.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")
result = cursor.fetchall()
for i in result:
    print(f"Öğrenci Id: {i[0]} - Öğrenci Adı: {i[1]} -- Ders Notu: {i[2]}")

connection.close()
