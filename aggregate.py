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

def getproducts():
        connection = mysql.connector.connect(host ="localhost", user ="root", password = "1234", database = "node-app")
        cursor = connection.cursor()
        
        cursor.execute("Select * From Products Order By name, price")
        
        result = cursor.fetchall()

        for product in result:
            print(f"id: {product[0]} name: {product[1]} price: {product[2]} ")
        
        

     

""" try:
            connection.commit()
            print(f"{cursor.rowcount} Adet Kayıt Eklendi")
            print(f"Son Eklenen Kaydın Id :{cursor.lastrowid}")
        except mysql.connector.Error as err:
            print("hata: ", err)
        finally:
            connection.close()
            print("Database Bağlantısı Kapandı..!")

         sql = "INSERT INTO products (name, price,imageUrl,description) VALUES (%s,%s,%s,%s)"
        values = list """

def getProductById(id):
    connection = mysql.connector.connect(host ="localhost", user ="root", password = "1234", database = "node-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)
    

    result = cursor.fetchone()
   
    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")

def getProductInfo():
    connection = mysql.connector.connect(host ="localhost", user ="root", password = "1234", database = "node-app")
    cursor = connection.cursor()

    # sql = "Select COUNT(*) From Products "  
    # sql = "Select AVG(price) From Products " 
    # sql = "Select SUM(price) From Products "  
    # sql = "Select MIN(price) From Products " 
    # sql = "Select MAX(price) From Products " 
    sql = "Select name, price From Products Where price =(Select MAX(price) From Products)" 

    cursor.execute(sql)
    

    result = cursor.fetchone()
   
    print(f"result: {result[0]} price: {result[1]}")

getProductInfo()
