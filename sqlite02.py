import sqlite3

with sqlite3.connect("okul.sqlite") as vt:
    im = vt.cursor()

ogrenci = [("Gokhan","YAVAS","143"),
                ("Aysel","Utku","144"),
                ("Veli","Kon","145"),
                ("Burcu","Özel","145")]

im.execute("""CREATE TABLE IF NOT EXISTS ogrenci
        (isim, soyisim, numara)""")

for veri in ogrenci:
        im.execute("""INSERT INTO ogrenci VALUES
            (?, ?, ?)""",veri)

vt.commit()