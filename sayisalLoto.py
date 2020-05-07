#!/usr/bin/python                                                
# -*- coding:utf-8 -*-                                           
                                                                 
################################################################################
# Huseyin OZDEMIR                                                
# husonet                                                        
# 19.12.2016                                                     
# Bu betik rastgele bir den kırkdokuza kadar rastgele sayi uretir
################################################################################
                                                                 
import random                                                    
                                                                 
RANDOM_SAYI = 6                                                  
                                                                 
DIZI        = []                                                 
YENI_DIZI   = []                                                 
                                                                 
#-------------------------------------------------------------------------------
# dizimizi tek tek yazmamak adina donguyle doldur                
def diziDoldur():                                                
    i = 1                                                        
    while i <= 49:                                               
        DIZI.append(i)                                           
        i+=1                                                     
                                                                 
#-------------------------------------------------------------------------------
# rasgele sayi secme islemi yapilsin                             
def sayisalLoto():                                               
    result = []                                                  
    i = 1                                                        
    while i <= RANDOM_SAYI:                                      
        rnd = random.choice(DIZI)                                
        if rnd  in YENI_DIZI:                                    
            continue                                             
        YENI_DIZI.append(rnd)                                    
        i+=1                                                     
    YENI_DIZI.sort()                                             
    result = YENI_DIZI                                           
    return result 

if __name__ == '__main__':
    diziDoldur()
    print (sayisalLoto())