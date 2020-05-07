# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:35:11 2020

@author: BADROBOT
"""


import re

metin="""Dağ başını duman almış
gümüş dere durmaz akar
güneş ufuktan şimdi doğar
"""
print(re.sub("\s","",metin))

metin1="Silikon vadisi, google.com ve apple.com arasındaki rekabeti konuşuyor."
liste=metin1.split()
for i in liste:
    sonuc=re.search(".com$",i)
    if sonuc:
        print(sonuc.string)

