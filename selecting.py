import mysql.connector

def insertproduct(name,price,imageUrl,description):
        connection = mysql.connector.connect(host ="localhost", user ="root", password = "1234", database = "node-app")
        cursor = connection.cursor()

        sql = "INSERT INTO products (name, price,imageUrl,description) VALUES (%s,%s,%s,%s)"
        values = (name,price,imageUrl,description)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print(f"{cursor.rowcount} Adet Kayıt Eklendi")
            print(f"Son Eklenen Kaydın Id :{cursor.lastrowid}")
        except mysql.connector.Error as err:
            print("hata: ", err)
        finally:
            connection.close()
            print("Database Bağlantısı Kapandı..!")

def insertproducts(list):
        connection = mysql.connector.connect(host ="localhost", user ="root", password = "1234", database = "node-app")
        cursor = connection.cursor()

        sql = "INSERT INTO products (name, price,imageUrl,description) VALUES (%s,%s,%s,%s)"
        values = list
        cursor.executemany(sql,values)

        try:
            connection.commit()
            print(f"{cursor.rowcount} Adet Kayıt Eklendi")
            print(f"Son Eklenen Kaydın Id :{cursor.lastrowid}")
        except mysql.connector.Error as err:
            print("hata: ", err)
        finally:
            connection.close()
            print("Database Bağlantısı Kapandı..!")

def getProducts():
    connection = mysql.connector.connect(host ="localhost", user ="root", password = "1234", database = "node-app")
    cursor = connection.cursor()

    # cursor.execute("Select * From Products")
    cursor.execute("Select name, price From Products")

    # result = cursor.fetchall()
    result = cursor.fetchone()

    print(f"name: {result[0]} price: {result[1]}")

    # for product in result:
    #     # print(f"name: {product[1]} price: {product[2]}")
    #     print(f"name: {product[0]} price: {product[1]}")

getProducts()