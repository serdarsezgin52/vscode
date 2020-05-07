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


list = []
while True:
    name = input("Ürün Adı :")
    price = float(input("Ürün Fiyatı :"))
    imageUrl = input("ürün Resmi Adı :")
    description = input("Ürün Açıklaması :")

    list.append((name,price,imageUrl,description))

    result = input("Yeni Kayıt Eklemek İstermisiniz? (e/h)")
    if result == "h":
        print("Bilgiler Veritabanına Kaydediliyor..!")
        print(list)
        insertproducts(list)
        break
    

# insertproduct(name,price,imageUrl,description)