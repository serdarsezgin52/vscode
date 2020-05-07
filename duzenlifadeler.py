Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.match("F","Fatih")
<re.Match object; span=(0, 1), match='F'>
>>> re.match("h","Fatih")
>>> re.search("h","Fatih")
<re.Match object; span=(4, 5), match='h'>
>>> re.match("h","Fatih")
>>> "fatih"[0]=="f"
True
>>> re.match("[FM]"."Fatih")
SyntaxError: invalid syntax
>>> re.match("[FM]","Fatih")
<re.Match object; span=(0, 1), match='F'>
>>> re.match("[FM]","Melike")
<re.Match object; span=(0, 1), match='M'>
>>> re.match("[FM]","Serdar")
>>> re.match("[0-9]","Serdar")
>>> re.match("[0-9]","9.uncu Cumhurbaşkanı Serdar")
<re.Match object; span=(0, 1), match='9'>
>>> re.match("[a-z]","Serdar")
>>> re.match("[a-z]","serdar")
<re.Match object; span=(0, 1), match='s'>
>>> re.search("[^0-9a-zA-Z]","Serdar Sezgin")
<re.Match object; span=(6, 7), match=' '>
>>> re.search("[^0-9a-zA-Z]","SerdarSezgin")
>>> re.search("[^0-9a-zA-Z]","SERDARSEZGİN")
<re.Match object; span=(10, 11), match='İ'>
>>> re.search("\d","989898")
<re.Match object; span=(0, 1), match='9'>
>>> re.search("\d","dgdfg")
>>> re.search("\D","dgdfg")
<re.Match object; span=(0, 1), match='d'>
>>> re.search("\s","dg dfg")
<re.Match object; span=(2, 3), match=' '>
>>> re.search("\D","dg dfg")
<re.Match object; span=(0, 1), match='d'>
>>> re.search("\d","dgd fg")
>>> re.search("\W","dgdfg")
>>> re.search("\W","dgdf9")
>>> re.search("\W","dgdfğü9")
>>> re.search("\W","dgdfğü 9")
<re.Match object; span=(6, 7), match=' '>
>>> re.search("\W","dgdfdg9ğü")
>>> re.search("\W","dgdfdg9ğü.")
<re.Match object; span=(9, 10), match='.'>
>>> re.search("\w","dgdfdg9ğü")
<re.Match object; span=(0, 1), match='d'>
>>> re.search("\w","asdasd")
<re.Match object; span=(0, 1), match='a'>
>>> re.search("\w","2342342")
<re.Match object; span=(0, 1), match='2'>
>>> re.search("\w",".ç,;:_")
<re.Match object; span=(1, 2), match='ç'>
>>> re.search("\w",".,;:_")
<re.Match object; span=(4, 5), match='_'>
>>> re.search("\w",".,;:")
>>> re.search("\w",".,;:+")
>>> re.search("\w",".,;:+-")
>>> re.search("\w",".,;:+-%")
>>> re.match("serdar$","asdajsdr")
>>> re.match("serdar$","serdar")
<re.Match object; span=(0, 6), match='serdar'>
>>> re.search("serdar|cemal","serdarcemal")
<re.Match object; span=(0, 6), match='serdar'>
>>> re.search("serdar|cemal","serdar cemal")
<re.Match object; span=(0, 6), match='serdar'>
>>> re.search("serdar|cemal","RAHŞAN cemal")
<re.Match object; span=(7, 12), match='cemal'>
>>> HTML="""
<html>
<head><title>Bu bir deneme sayfasıdır</title></head>
<body>
Sayfa burada başlıyor
</body>
</html>
"""
>>> re.search("<title>.*</title>",HTML)
<re.Match object; span=(14, 53), match='<title>Bu bir deneme sayfasıdır</title>'>
>>> re.search("<title>.*</title>",HTML).
SyntaxError: invalid syntax
>>> re.search("<title>.*</title>",HTML).group()
'<title>Bu bir deneme sayfasıdır</title>'
>>> title=re.search("<title>.*</title>",HTML).group()
>>> print(title)
<title>Bu bir deneme sayfasıdır</title>
>>> re.search("<title>.*</title>",HTML).start()
14
>>> re.search("<title>.*</title>",HTML).start()
14
>>> 
>>> re.search("<title>.*</title>",HTML).stop()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    re.search("<title>.*</title>",HTML).stop()
AttributeError: 're.Match' object has no attribute 'stop'
>>> re.search("<title>.*</title>",HTML).end()
53
>>> re.search("<title>.*</title>",HTML).span()
(14, 53)
>>> re.search("<title>.*</title>",HTML)
<re.Match object; span=(14, 53), match='<title>Bu bir deneme sayfasıdır</title>'>
>>> re.search("<TITLE>.*</TITLE>",HTML)
>>> re.search("<TITLE>.*</TITLE>",HTML,re.IGNORECASE)
<re.Match object; span=(14, 53), match='<title>Bu bir deneme sayfasıdır</title>'>
>>> tarih="Perşembe 02/04/2020"
>>> re.search("(\d{2})/(\d{2})/(\d{2,4})",tarih)
<re.Match object; span=(9, 19), match='02/04/2020'>
>>> re.search("<title>.*</title>",HTML).endpos()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    re.search("<title>.*</title>",HTML).endpos()
TypeError: 'int' object is not callable
>>> re.search("<title>.*</title>",HTML).endpos
106
>>> metin="silikon vadisi, google.com ve apple.com arasındaki rekabeti tartışıyor."
>>> liste=metin.split()
>>> for i in liste:
	sonuc=i
	print(sonuc)

	
silikon
vadisi,
google.com
ve
apple.com
arasındaki
rekabeti
tartışıyor.
>>> sonuc
'tartışıyor.'
>>> for i in liste:
	sonuc+=i
	print(sonuc)

	
tartışıyor.silikon
tartışıyor.silikonvadisi,
tartışıyor.silikonvadisi,google.com
tartışıyor.silikonvadisi,google.comve
tartışıyor.silikonvadisi,google.comveapple.com
tartışıyor.silikonvadisi,google.comveapple.comarasındaki
tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabeti
tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.
>>> metin="silikon vadisi, google.com ve apple.com arasındaki rekabeti tartışıyor."
>>> liste=metin.split()
>>> for i in liste:
	sonuc+=i
	print(sonuc)

	
tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.silikon
tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.silikonvadisi,
tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.silikonvadisi,google.com
tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.silikonvadisi,google.comve
tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.silikonvadisi,google.comveapple.com
tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.silikonvadisi,google.comveapple.comarasındaki
tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.silikonvadisi,google.comveapple.comarasındakirekabeti
tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.
>>> sonuc
'tartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.silikonvadisi,google.comveapple.comarasındakirekabetitartışıyor.'
>>> metin
'silikon vadisi, google.com ve apple.com arasındaki rekabeti tartışıyor.'
>>> metin="silikon vadisi, google.com ve apple.com arasındaki rekabeti tartışıyor."
>>> liste=metin.split()
>>> sonuc()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    sonuc()
TypeError: 'str' object is not callable
>>> sonuc()= []
SyntaxError: cannot assign to function call
>>> sonuc= []
>>> for i in liste:
	sonuc+=i
	print(sonuc)

	
['s', 'i', 'l', 'i', 'k', 'o', 'n']
['s', 'i', 'l', 'i', 'k', 'o', 'n', 'v', 'a', 'd', 'i', 's', 'i', ',']
['s', 'i', 'l', 'i', 'k', 'o', 'n', 'v', 'a', 'd', 'i', 's', 'i', ',', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm']
['s', 'i', 'l', 'i', 'k', 'o', 'n', 'v', 'a', 'd', 'i', 's', 'i', ',', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm', 'v', 'e']
['s', 'i', 'l', 'i', 'k', 'o', 'n', 'v', 'a', 'd', 'i', 's', 'i', ',', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm', 'v', 'e', 'a', 'p', 'p', 'l', 'e', '.', 'c', 'o', 'm']
['s', 'i', 'l', 'i', 'k', 'o', 'n', 'v', 'a', 'd', 'i', 's', 'i', ',', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm', 'v', 'e', 'a', 'p', 'p', 'l', 'e', '.', 'c', 'o', 'm', 'a', 'r', 'a', 's', 'ı', 'n', 'd', 'a', 'k', 'i']
['s', 'i', 'l', 'i', 'k', 'o', 'n', 'v', 'a', 'd', 'i', 's', 'i', ',', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm', 'v', 'e', 'a', 'p', 'p', 'l', 'e', '.', 'c', 'o', 'm', 'a', 'r', 'a', 's', 'ı', 'n', 'd', 'a', 'k', 'i', 'r', 'e', 'k', 'a', 'b', 'e', 't', 'i']
['s', 'i', 'l', 'i', 'k', 'o', 'n', 'v', 'a', 'd', 'i', 's', 'i', ',', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm', 'v', 'e', 'a', 'p', 'p', 'l', 'e', '.', 'c', 'o', 'm', 'a', 'r', 'a', 's', 'ı', 'n', 'd', 'a', 'k', 'i', 'r', 'e', 'k', 'a', 'b', 'e', 't', 'i', 't', 'a', 'r', 't', 'ı', 'ş', 'ı', 'y', 'o', 'r', '.']
>>> sonuc
['s', 'i', 'l', 'i', 'k', 'o', 'n', 'v', 'a', 'd', 'i', 's', 'i', ',', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm', 'v', 'e', 'a', 'p', 'p', 'l', 'e', '.', 'c', 'o', 'm', 'a', 'r', 'a', 's', 'ı', 'n', 'd', 'a', 'k', 'i', 'r', 'e', 'k', 'a', 'b', 'e', 't', 'i', 't', 'a', 'r', 't', 'ı', 'ş', 'ı', 'y', 'o', 'r', '.']
>>> sonuc=[]
>>> sonuc
[]
>>> for i in liste:
	sonuc=+i
	print(sonuc)

	
Traceback (most recent call last):
  File "<pyshell#95>", line 2, in <module>
    sonuc=+i
TypeError: bad operand type for unary +: 'str'
>>> for i in liste:
	sonuc=i
	print(sonuc)

	
silikon
vadisi,
google.com
ve
apple.com
arasındaki
rekabeti
tartışıyor.
>>> sonuc
'tartışıyor.'
>>> sonuc()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    sonuc()
TypeError: 'str' object is not callable
>>> sonuc[]
SyntaxError: invalid syntax
>>> for i in range(1,50)
SyntaxError: invalid syntax
>>> for i in range(1,50):
	print (i)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
>>> 