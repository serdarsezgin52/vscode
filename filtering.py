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

def getProductById(id):
    connection = mysql.connector.connect(host ="localhost", user ="root", password = "1234", database = "node-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)
    

    result = cursor.fetchone()
   
    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")

def getProduct():
    connection = mysql.connector.connect(host ="localhost", user ="root", password = "1234", database = "node-app")
    cursor = connection.cursor()

    sql = "Select * From Products"
    
    cursor.execute(sql)
    
    result = cursor.fetchall()
    for result in result:
        print(f"{result}")
            

getProduct()