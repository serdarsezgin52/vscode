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

def updatingProduct(id, name, price):
        connection = mysql.connector.connect(host ="localhost", user ="root", password = "1234", database = "node-app")
        cursor = connection.cursor()
        values = (name, price, id)
        sql = "Update  products Set name=%s, price=%s where id=%s"

        cursor.execute(sql,values)
        try:
            connection.commit()
            print(f"{cursor.rowcount} Adet Kayıt Gğncellendi")
        except mysql.connector.Error as err:
            print("hata: ", err)
        finally:
            connection.close()
            print("Database Bağlantısı Kapandı..!")

def deleteProduct(id):
        connection = mysql.connector.connect(host ="localhost", user ="root", password = "1234", database = "node-app")
        cursor = connection.cursor()
        
        sql = "Delete from  products where id=%s"
        values = (id,)

        cursor.execute(sql,values)
        try:
            connection.commit()
            print(f"{cursor.rowcount} Adet Kayıt Silindi")
        except mysql.connector.Error as err:
            print("hata: ", err)
        finally:
            connection.close()
            print("Database Bağlantısı Kapandı..!")        

deleteProduct(7)
# updatingProduct(1,'Iphone 8', 6000)
