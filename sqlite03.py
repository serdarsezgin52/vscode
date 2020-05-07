import sqlite3

#vt.sqlite adlı bir veritabanı dosyası oluşturup
#bu veritabanına bağlanıyoruz.
db = sqlite3.connect("vt.sqlite")

#Veritabanı üzerinde istediğimiz işlemleri yapabilmek
#için bir imleç oluşturmamız gerekiyor.
im = db.cursor()

#imlecin execute() metodunu kullanarak, veritabanı içinde
#"kullanicilar" adlı bir tablo oluşturuyoruz. Bu tabloda
#kullanıcı_adi ve parola olmak üzere iki farklı sütun var.
im.execute("""CREATE TABLE IF NOT EXISTS kullanicilar
    (kullanici_adi, parola)""")

#Yukarıda oluşturduğumuz tabloya yerleştireceğimiz verileri
#hazırlıyoruz. Verilerin liste içinde birer demet olarak
#nasıl gösterildiğine özellikle dikkat ediyoruz.
veriler = [
            ("ahmet123", "12345678"),
            ("mehmet321", "87654321"),
            ("selin456", "123123123")
          ]

#veriler adlı liste içindeki bütün verileri kullanicilar adlı
#tabloya yerleştiriyoruz. Burada tek öğeli bir demet
#tanımladığımıza dikkat edin: (i,)
for i in veriler:
    im.execute("""INSERT INTO kullanicilar VALUES %s""" %(i,))

#Yaptığımız değişikliklerin tabloya işlenebilmesi için
#commit() metodunu kullanıyoruz.
db.commit()

#Kullanıcıdan kullanıcı adı ve parola bilgilerini alıyoruz...
kull = input("Kullanıcı adınız: ")
paro = input("Parolanız: ")

#Burada yine bir SQL komutu işletiyoruz. Bu komut, kullanicilar
#adlı tabloda yer alan kullanici_adi ve parola adlı sütunlardaki
#bilgileri seçiyor.
if kull.isalnum() and paro.isalnum():
    im.execute("""SELECT * FROM kullanicilar WHERE
    kullanici_adi = '%s' AND parola = '%s' """%(kull, paro))

#Hatırlarsanız daha önce fetchall() adlı bir metottan
#söz etmiştik. İşte bu fetchone() metodu da ona benzer.
#fetchall() bütün verileri alıyordu, fetchone() ise
#verileri tek tek alır.
data = im.fetchone()

#Eğer data adlı değişken False değilse, yani bu
#değişkenin içinde bir değer varsa kullanıcı adı
#ve parola doğru demektir. Kullanıcıyı içeri alıyoruz.
if data:
    print("Programa hoşgeldin {}!".format(data[0]))

#Aksi halde kullanıcıya olumsuz bir mesaj veriyoruz.
else:
    print("Parola veya kullanıcı adı yanlış!")