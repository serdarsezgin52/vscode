import sqlite3
vt=sqlite3.connect("veritabani.sqlite")
im=vt.cursor()
im.execute("CREATE TABLE ogrenci(isim, soyisim, numara)")

o1="""INSERT INTO ogrenci VALUES
('Gokhan','YAVAS','143')"""
im.execute(o1)
vt.commit()
vt.close() 