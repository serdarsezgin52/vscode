from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os
import urllib.request
import requests
import getpass
from termcolor import colored
from colorama import init
import threading

class Instagram():
    def __init__(self):
        init(convert=True)
        self.script()
        self.threadOlustur()
        self.girisYapildimi=False
        self.tarayiciAcildimi=False
        self.aktifKullanici=""
        self.girisYap()

    def script(self):
        print("")
        print(self.uyariRenk("  _____           _                                    ____        _   ", 1))
        print(self.uyariRenk(" |_   _|         | |                                  |  _ \      | |  ", 1))
        print(self.uyariRenk("   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_) | ___ | |_ ", 1))
        print(self.uyariRenk("   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  _ < / _ \| __|", 1))
        print(self.uyariRenk("  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | | | |_) | (_) | |_ ", 1))
        print(self.uyariRenk(" |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |____/ \___/ \__|", 1))
        print(self.uyariRenk("                            __/ |                                      ", 1))
        print(self.uyariRenk("                           |___/                                       ", 1))
        print(self.uyariRenk("# ==============================================================================", 1))
        print(self.uyariRenk("# author      	:", 1) + "Mustafa Dalga")
        print(self.uyariRenk("# website    	:", 1) + "https://apierson.com")
        print(self.uyariRenk("# linkedin    	:", 1) + "https://www.linkedin.com/in/mustafadalga")
        print(self.uyariRenk("# github      	:", 1) + "https://github.com/mustafadalga")
        print(self.uyariRenk("# email      	:", 1) + "mustafadalgaa < at > gmail[.]com")
        print(self.uyariRenk("# date        	:", 1) + "15.07.2019")
        print(self.uyariRenk("# version     	:", 1) + "1.0")
        print(self.uyariRenk("# python_version:", 1) + "3.7.2")
        print(self.uyariRenk("# ==============================================================================", 1))
        print("")

    def menu(self):
        print("")
        print(self.uyariRenk("       <<< SEÇENEKLER >>>      ",1))
        print("")
        print(self.uyariRenk(" 1 -) Tüm paylaşımları indir",3))
        print(self.uyariRenk(" 2 -) Tüm paylaşımları beğen",3))
        print(self.uyariRenk(" 3 -) Tüm paylaşımları beğenmekten vazgeç",3))
        print(self.uyariRenk(" 4 -) Fotoğraf indir(tek fotoğraf)",3))
        print(self.uyariRenk(" 5 -) Video indir(tek video)",3))
        print(self.uyariRenk(" 6 -) Paylaşım beğen (tek paylaşım)",3))
        print(self.uyariRenk(" 7 -) Paylaşım beğenmekten vazgeç(tek paylaşım)",3))
        print(self.uyariRenk(" 8 -) Kullanıcı takip et",3))
        print(self.uyariRenk(" 9 -) Kullanıcı takip etmekten vazgeç",3))
        print(self.uyariRenk(" 10-) Kullanıcı engelle",3))
        print(self.uyariRenk(" 11-) Kullanıcı engel kaldır",3))
        print(self.uyariRenk(" 12-) İnstagram çıkış yap",3))
        print(self.uyariRenk(" 13-) Uygulama'dan çıkış yap",3))
        print("")
        self.islemSec()

    def islemSec(self):
        secim=input(" İşlem yapmak için bir seçim yapınız >> ").strip()
        if secim:
            try:
                secim=int(secim)
                if 0<secim<14:
                    self.secilenIslem(secim)
                    if secim==1 or secim==2 or secim==3  or secim==8 or secim==9 or secim==10 or secim==11:
                        self.profilSec(secim)
                    elif secim==4:
                        self.fotografIndir()
                    elif secim==5:
                        self.videoIndir()
                    elif secim==6:
                        self.paylasimBegen()
                    elif secim==7:
                        self.paylasimBegen(False)
                    elif secim==12:
                        self.cikisYap()
                    elif secim==13:
                        self.quit()
                else:
                    print(self.uyariRenk("[-] Lütfen geçerli bir seçim yapınız!",2))
                    self.islemSec()
            except Exception as e:
                print(e)
                print(self.uyariRenk("[-] Yapılacak işlem,  başındaki sayıya göre seçilmeli.", 2))
                self.islemSec()
        else:
            self.islemSec()

    def secilenIslem(self,secim):
        print("")
        if secim==1:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir kulllanıcının tüm paylaşımlarını indirme", 1))
        elif secim==2:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir kulllanıcının tüm paylaşımlarını beğenme", 1))
        elif secim==3:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir kulllanıcının tüm paylaşımlarını beğenmekten vazgeçme", 1))
        elif secim==4:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir fotoğrafı indirme", 1))
        elif secim==5:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir videoyu indirme", 1))
        elif secim==6:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir paylaşımı beğenme", 1))
        elif secim==7:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir paylaşımı beğenmekten vazgeçme", 1))
        elif secim==8:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir kullanıcıyı takip etme", 1))
        elif secim==9:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir kullanıcıyı takip etmekten vazgeçme", 1))
        elif secim==10:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir kullanıcıyı engelleme", 1))
        elif secim==11:
            print(self.uyariRenk(" Seçilen İşlem >>> Bir kullanıcının engelini kaldırma", 1))
        elif secim==12:
            print(self.uyariRenk(" Seçilen İşlem >>> İnstagram oturumunu kapatma", 1))
        elif secim==13:
            print(self.uyariRenk(" Seçilen İşlem >>> Python uygulamasından çıkış yapma", 1))

        if secim<12:
            print(self.uyariRenk(" [*] Ana menüye dönmek için  'menu' komutunu giriniz", 3))
        print("")

    def threadOlustur(self):
        t1 = threading.Thread(target=self.tarayiciBaslat)
        t1.daemon = True
        t1.start()

    def tarayiciBaslat(self):
        print(self.uyariRenk("[*] Tarayıcı Başlatılıyor...",1))
        self.driver = webdriver.Firefox(firefox_profile=self.dilDegistir(),executable_path="C:\\Users\\Liduma\\Desktop\\geckodriver.exe")
        self.driver.get('https://www.instagram.com/accounts/login/')

    def dilDegistir(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'en-US, en')
        return profile

    def girisYap(self,username=False,password=False):
        try:
            if not username and not password:
                print(" ")
                print(" ")
                print(self.uyariRenk("<<< Instagram Giriş Yap >>>>", 1))
                username = input('Kullanıcı adınız >> ')
                password = getpass.getpass(prompt='Parolanız >> ')
            elif not username:
                username = input('Kullanıcı adınız >> ')
            elif not password:
                password = getpass.getpass(prompt='Parolanız >> ')

            if not username and not password:
                print(self.uyariRenk("[-] Lütfen kullanıcı adınızı ve parolanızı giriniz!", 2))
                self.girisYap()
            elif not username:
                print(self.uyariRenk("[-] Lütfen kullanıcı adınızı giriniz!", 2))
                self.girisYap(False,password)
            elif not password:
                print(self.uyariRenk("[-] Lütfen parolanızı giriniz!", 2))
                self.girisYap(username,False)

            print(self.uyariRenk("[*] Kullanıcı girişi yapılıyor...",1))
            time.sleep(15)
            usernameInput = self.driver.find_elements_by_css_selector('form input')[0]
            passwordInput = self.driver.find_elements_by_css_selector('form input')[1]
            usernameInput.send_keys(username.strip())
            passwordInput.send_keys(password.strip())
            passwordInput.send_keys(Keys.ENTER)
            time.sleep(5)
            print(self.girisKontrol())
            if self.girisYapildimi:
                self.aktifKullanici=username
                self.menu()
            else:
                self.inputTemizle(usernameInput)
                self.inputTemizle(passwordInput)
                self.girisYap()
        except Exception as e:
            print(self.uyariRenk("[-] Kullanıcı girişi sırasında hata:"+str(e),2))

    def girisKontrol(self):
        if "The username you entered doesn't belong to an account. Please check your username and try again." in self.driver.page_source:
            uyari=self.uyariRenk("[-] Girdiğiniz kullanıcı adı bir hesaba ait değil. Lütfen kullanıcı adınızı kontrol edin ve tekrar deneyin.",2)
        elif "Sorry, your password was incorrect. Please double-check your password." in self.driver.page_source:
            uyari=self.uyariRenk("[-] Üzgünüz, şifreniz hatalıydı. Lütfen şifrenizi tekrar kontrol edin.",2)
        elif "https://www.instagram.com/accounts/login/two_factor" in self.driver.current_url:
            uyari=self.girisDogrulama()
        elif self.driver.current_url!="https://www.instagram.com/accounts/login/":
            uyari=self.uyariRenk("[+] Giriş işlemi başarılı",1)
            self.girisYapildimi=True
        else:
            uyari=self.uyariRenk("[-] Giriş işlemi başarısız",2)
        return uyari

    def girisDogrulama(self,durum=True):
        kod=input("Telefonunuza gönderilen kodu giriniz >> ").strip()
        if not kod:
            self.girisYap(durum)

        if durum:
            time.sleep(5)
        kodInput = self.driver.find_elements_by_css_selector('form input')[0]
        kodInput.send_keys(kod)
        kodInput.send_keys(Keys.ENTER)
        time.sleep(5)
        if "A security code is required." in self.driver.page_source:
            print(self.uyariRenk("[-] Lütfen güvenlik kodunu giriniz!",2))
            self.inputTemizle(kodInput)
            self.girisDogrulama(False)
        elif "Please check the security code and try again." in self.driver.page_source:
            print(self.uyariRenk("[-] Lütfen güvenlik kodunu kontrol edin ve tekrar deneyin.",2))
            self.inputTemizle(kodInput)
            self.girisDogrulama(False)
        elif "https://www.instagram.com/accounts/login/two_factor" not in self.driver.current_url:
            self.girisYapildimi=True
            return self.uyariRenk("[+] Giriş işlemi başarılı",1)
        else:
            return self.uyariRenk("[-] Giriş Yapılamıyor...",2)

    def inputTemizle(self,inpt):
        inpt.clear()

    def profilSec(self,secim):
        kullanici = input(" İşlem yapmak istediğiniz profilin kullanıcı adı >> ")

        if kullanici=="menu":
            self.menu()

        if not kullanici:
            self.profilSec(secim)

        if self.kullaniciKontrol(kullanici):
            print("[*] Tarayıcı '" + kullanici + "' profiline yönlendiriliyor...")
            if secim==1:
                self.paylasimlariIndir(kullanici,secim)
            elif secim==2:
                self.paylasimlariBegen(kullanici,secim)
            elif secim==3:
                self.paylasimlariBegen(kullanici,secim,False)
            elif secim==8:
                self.kullaniciTakipEt(kullanici,secim)
            elif secim==9:
                self.kullaniciTakipVazgec(kullanici,secim)
            elif secim==10:
                self.kullaniciEngelle(kullanici,secim)
            elif secim==11:
                self.kullaniciEngelKaldir(kullanici,secim)
        else:
            print(self.uyariRenk("[-] '" + kullanici + "' adında bir kullanıcı bulunamadı ",2))
            self.profilSec(secim)

    def kullaniciKontrol(self,kullaniciadi):
        response=requests.get("https://www.instagram.com/" + kullaniciadi)
        if response.status_code==404:
            return False
        else:
            return True

    def kullaniciTakipEt(self,kullaniciAdi,secim):
        print("[*] '" + kullaniciAdi + "' kullanıcısını takip etme işlemine başladı...")
        try:
            self.driver.get('https://www.instagram.com/' + kullaniciAdi)
            time.sleep(5)

            if "Sorry, this page isn't available." in self.driver.page_source:
                print(self.uyariRenk("[-] " + kullaniciAdi + " kullanıcısına ulaşılamadı", 2))
                self.profilSec(secim)

            if "This Account is Private" in self.driver.page_source:
                btn_takip = self.driver.find_element_by_css_selector("button.BY3EC")
            else:
                btn_takip = self.driver.find_element_by_css_selector('button._5f5mN')
            if (btn_takip.text == 'Follow'):
                btn_takip.click()
                if "This Account is Private" in self.driver.page_source:
                    print(self.uyariRenk("[+] " + kullaniciAdi + " kullanıcısına takip isteği gönderildi", 1))
                else:
                    print(self.uyariRenk("[+] " + kullaniciAdi + " kullanıcısı takip edilmeye başlandı", 1))
                self.profilSec(secim)
            elif btn_takip.text == "Requested":
                print(self.uyariRenk("[-] " + kullaniciAdi + " kullanıcısına takip isteği zaten gönderildi", 2))
                self.profilSec(secim)
            else:
                print(self.uyariRenk("[-] " + kullaniciAdi + " kullanıcısını zaten takip ediyorsun", 2))
                self.profilSec(secim)
        except Exception as e:
            print(self.uyariRenk("[-] " + kullaniciAdi + " kullanıcısını takip etme işlemi sırasında hata:" + str(e), 2))
            self.profilSec(secim)

    def kullaniciTakipVazgec(self,kullaniciAdi,secim):
        print("[*] '" + kullaniciAdi + "' kullanıcısı takip etmekten vazgeçiliyor...")
        try:
            self.driver.get('https://www.instagram.com/' + kullaniciAdi)
            time.sleep(5)

            if "Sorry, this page isn't available." in self.driver.page_source:
                print(self.uyariRenk("[-] " + kullaniciAdi + " kullanıcısına ulaşılamadı", 2))
                self.profilSec(secim)

            if "This Account is Private" in self.driver.page_source:
                btn_takip = self.driver.find_element_by_css_selector("button.BY3EC")
            else:
                btn_takip = self.driver.find_element_by_css_selector('button._5f5mN')

            if btn_takip.text == "Following":
                btn_takip.click()
                time.sleep(5)
                btn_popup = self.driver.find_element_by_css_selector('button.aOOlW')
                btn_popup.click()
                print(self.uyariRenk("[+] " + kullaniciAdi + " kullanıcısı takip edilmekten vazgeçildi", 1))
                self.profilSec(secim)
            else:
                print(self.uyariRenk("[-] " + kullaniciAdi + " kullanıcısını zaten takip etmiyorsun", 2))
                self.profilSec(secim)
        except Exception as e:
            print(self.uyariRenk("[-] "+kullaniciAdi+" kullanıcısını takip etmekten vazgeçme işlemi sırasında hata:"+str(e),2))
            self.profilSec(secim)

    def kullaniciEngelle(self,kullaniciAdi,secim):
        print("[*] '" + kullaniciAdi + "' kullanıcısı engelleniyor...")
        try:
            self.driver.get('https://www.instagram.com/' + kullaniciAdi)
            time.sleep(3)

            if "Sorry, this page isn't available." in self.driver.page_source:
                print(self.uyariRenk("[-] " + kullaniciAdi + " kullanıcısına ulaşılamadı", 2))
                self.profilSec(secim)

            if "This Account is Private" in self.driver.page_source:
                btn = self.driver.find_element_by_css_selector('button.BY3EC')
            else:
                btn = self.driver.find_element_by_css_selector('button._5f5mN')

            if btn.text != "Unblock":
                self.driver.find_element_by_css_selector(
                    "span.glyphsSpriteMore_horizontal__outline__24__grey_9").click()
                time.sleep(2)
                self.driver.find_elements_by_css_selector("div.mt3GC > button")[1].click()
                time.sleep(2)
                self.driver.find_elements_by_css_selector("div.mt3GC > button")[0].click()
                print(self.uyariRenk("[+] '" + kullaniciAdi + "' kullanıcısı engellendi", 1))
                self.profilSec(secim)
            else:
                print(self.uyariRenk("[-] " + kullaniciAdi + " kullanıcısı zaten engellenmiş durumda", 2))
                self.profilSec(secim)

        except Exception as e:
            print(self.uyariRenk("[-] "+kullaniciAdi+" kullanıcısını engelleme işlemi sırasında hata:"+str(e),2))
            self.profilSec(secim)

    def kullaniciEngelKaldir(self,kullaniciAdi,secim):
        print("[*] '" + kullaniciAdi + "' kullanıcısının engeli kaldırılıyor...")
        try:
            self.driver.get('https://www.instagram.com/' + kullaniciAdi)
            time.sleep(3)

            if "Sorry, this page isn't available." in self.driver.page_source:
                print(self.uyariRenk("[-] " + kullaniciAdi + " kullanıcısına ulaşılamadı", 2))
                self.profilSec(secim)

            if "This Account is Private" in self.driver.page_source:
                btn = self.driver.find_element_by_css_selector('button.BY3EC')
            else:
                btn = self.driver.find_element_by_css_selector('button._5f5mN')

            if btn.text == "Unblock":
                self.driver.find_element_by_css_selector(
                    "span.glyphsSpriteMore_horizontal__outline__24__grey_9").click()
                time.sleep(2)
                self.driver.find_elements_by_css_selector("div.mt3GC > button")[1].click()
                time.sleep(2)
                self.driver.find_elements_by_css_selector("div.mt3GC > button")[0].click()
                print(self.uyariRenk("[+] '" + kullaniciAdi + "' kullanıcısının engeli kaldırıldı.", 1))
                self.profilSec(secim)
            else:
                print(self.uyariRenk("[-] " + kullaniciAdi + " kullanıcısı zaten engellenmemiş durumda", 2))
                self.profilSec(secim)
        except Exception as e:
            print(self.uyariRenk("[-] "+kullaniciAdi+" kullanıcısının engelini kaldırma işlemi sırasında hata:"+str(e),2))
            self.profilSec(secim)

    def paylasimlariIndir(self,kullaniciadi,secim):
        self.driver.get("https://www.instagram.com/" + kullaniciadi)
        time.sleep(10)
        try:
            if "This Account is Private" not in self.driver.page_source:
                print("[*] Paylaşım tarama işlemi başladı....")
                video_urls,carousel_url=self.paylasimTara(kullaniciadi)
                print("[*] Video indirme işlemine geçiliyor...")
                print("[*] İndirilecek Tekli Video Sayısı:" + str(len(video_urls)))
                self.veriIndir(video_urls,"video")
                if len(video_urls)>0:
                    print(self.uyariRenk("[+] Video indirme işlemi tamamlandı", 1))

                print("[*] Carousel Video ve Resim paylaşımlarının tarama işlemi geçiliyor...")
                print("[*] Carouse Paylaşımlarının tarama işlemi başladı...")
                print("[*] İndirilecek Toplam Carousel Paylaşım Sayısı:" + str(len(carousel_url)))
                self.veriIndir(carousel_url,"carousel")
                if len(carousel_url)>0:
                    print(self.uyariRenk("[+] Carousel Video ve Resim paylaşımlarının indirme işlemi tamamlandı...", 1))

                print(self.uyariRenk("[+] "+kullaniciadi+" adlı kullanıcının tüm paylaşımları indirildi",1))
                self.klasorDegistir("../")
                self.profilSec(secim)
            else:
                print(self.uyariRenk("[-] "+kullaniciadi + " adlı kişinin hesabı gizli hesap olduğundan Paylaşımları indirme işlemi yapılamıyor!",2))
                self.profilSec(secim)
        except Exception as e:
            print(self.uyariRenk("[-] '"+kullaniciadi+"' kullanısının paylaşımlarını indirme işlemi sırasında bir hata oluştu:"+str(e),2))
            self.profilSec(secim)

    def paylasimTara(self,kullaniciadi):
        img_src = set()
        carousel_url = set()
        video_urls = set()
        try:
            gonderiSayisi = self.driver.find_element_by_css_selector("span.g47SY").text
            if int(gonderiSayisi) < 10:
                gonderiSayisi = 10
            for i in range(round(int(gonderiSayisi) / 10)):
                try:
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    article = self.driver.find_element_by_css_selector('article.FyNDV')
                    hrefs = article.find_elements_by_tag_name("a")
                    for href in hrefs:
                        durum = True
                        divs = href.find_elements_by_tag_name("div")
                        for div in divs:
                            if "u7YqG" in div.get_attribute("class"):
                                span = div.find_element_by_tag_name("span")
                                href = href.get_attribute("href")
                                if "mediatypesSpriteVideo__filled__32" in span.get_attribute("class"):
                                    if href not in video_urls:
                                        print(self.uyariRenk("[*] Video url:" + href, 1))
                                    video_urls.add(href)

                                    durum = False
                                elif "mediatypesSpriteCarousel__filled__32" in span.get_attribute("class"):
                                    if href not in carousel_url:
                                        print(self.uyariRenk("[*] Carousel paylaşim url:" + href, 1))
                                    carousel_url.add(href)

                                    durum = False
                        if durum:
                            src = href.find_element_by_tag_name("img").get_attribute("src")
                            if src not in img_src:
                                print(self.uyariRenk("[*] Resim url:" + src, 1))
                            img_src.add(src)
                    time.sleep(10)
                except Exception as e:
                    print(self.uyariRenk("[-] '"+kullaniciadi+"' kullanıcısının paylaşımlarını tarama işlemi sırasında hata oluştu:"+str(e),2))
                    continue
        except Exception as e:
            print(self.uyariRenk("[-] '"+kullaniciadi+"' kullanıcısının paylaşımlarını tarama işlemi sırasında hata oluştu:"+str(e),2))
            pass

        print("[*] İndirilecek Tekli Fotoğraf Sayısı:" + str(len(img_src)))
        self.klasorOlustur(kullaniciadi)
        print("[*] Fotoğraf indirme işlemi başladı")
        self.veriIndir(img_src, "resim")
        print("[*] Fotoğraf indirme işlemi tamamlandı")
        return video_urls,carousel_url

    def carouselTara(self,url):
        self.driver.get(url)
        time.sleep(10)
        try:
            ul = self.driver.find_element_by_css_selector("ul.YlNGR")
            li = ul.find_elements_by_css_selector("li._-1_m6")
            carousel_len = len(ul.find_elements_by_css_selector("li._-1_m6"))
            carousel=[]
            print("[*] " + url + " Adresi url'leri taranıyor.")
            for i in range(carousel_len):
                satir = {}
                if self.resimMi(li[i]):
                    src = li[i].find_element_by_css_selector("img.FFVAD").get_attribute("src")
                    satir['src'] = src
                    satir['tip'] = 'fotograf'
                    print(self.uyariRenk("[*] Img src:" + src, 1))
                    time.sleep(3)
                    if i < carousel_len - 1:
                        self.driver.find_element_by_css_selector("button._6CZji").click()
                else:
                    src = li[i].find_element_by_css_selector("video.tWeCl").get_attribute("src")
                    satir['src'] = src
                    satir['tip'] = 'video'
                    print(self.uyariRenk("[*] Video url:" + src, 1))
                    print("Tip:" + satir['tip'])
                    time.sleep(3)
                    if i < carousel_len - 1:
                        self.driver.find_element_by_css_selector("button._6CZji").click()
                carousel.append(satir)
            print("[*] Carousel tarama işlemi tamamlandı")
            return carousel
        except Exception as e:
            print(self.uyariRenk("[-] Carousel tarama işlemi sırasında hata oluştu:"+str(e),2))
            pass

    def resimMi(self,li):
        try:
            li.find_element_by_css_selector("img.FFVAD")
            return True
        except:
            return False

    def veriIndir(self,veri,durum):
        try:
            count = 1
            if durum=="resim":
                for img in veri:
                    try:
                        isim = str(count) + "_" + str(datetime.datetime.now()).replace(":", "_").replace(" ", "") + ".jpg"
                        count += 1
                        urllib.request.urlretrieve(img, isim)
                        print(self.uyariRenk("[+] "+img + " indirildi",1))
                    except Exception as e:
                        print(str(e))
                        continue
            elif durum=="video":
                for url in veri:
                    self.driver.get(url)
                    print("[*] Indirilecek video url:"+url)
                    time.sleep(5)
                    video = self.driver.find_element_by_css_selector("video.tWeCl").get_attribute("src")
                    isim = str(count) + str(datetime.datetime.now()).replace(":", "_").replace(" ", "") + ".mp4"
                    count += 1
                    urllib.request.urlretrieve(video, isim)
                    print(self.uyariRenk("[+] "+video + " indirildi",1))
            elif durum=="carousel":
                klasor_count = 1
                for url in veri:
                    urls = self.carouselTara(url)
                    klasor_adi = str(klasor_count) + "_carousel"
                    self.klasorOlustur(klasor_adi)
                    for link in urls:
                        if link['tip']=="fotograf":
                            isim = str(count) + str(datetime.datetime.now()).replace(":", "_").replace(" ","") + ".jpg"
                        elif link['tip']=="video":
                            isim = str(count) + str(datetime.datetime.now()).replace(":", "_").replace(" ","") + ".mp4"
                        count += 1
                        urllib.request.urlretrieve(link['src'], isim)
                        print(self.uyariRenk("[+] " + link['src'] + " indirildi", 1))
                    self.klasorDegistir("../")
                    klasor_count += 1
        except Exception as e:
            print(self.uyariRenk("[-] Veri indirme işlemi sırasında hata oluştu:" + str(e), 2))

    def paylasimlariBegen(self,kullaniciadi,secim,durum=True):
        self.driver.get("https://www.instagram.com/" + kullaniciadi)
        time.sleep(10)
        if "This Account is Private" not in self.driver.page_source:
            print("[*] '" + kullaniciadi + "' kullanıcısının paylaşımlarının tarama işlemi başladı...")
            gonderiSayisi=self.driver.find_element_by_css_selector("ul.k9GMp > li.Y8-fY > span.-nal3 > span.g47SY").text
            if int(gonderiSayisi) < 10:
                gonderiSayisi = 10
            pics_href = set()
            for i in range(round(int(gonderiSayisi) / 10)):
                try:
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    hrefs = self.driver.find_element_by_css_selector('article.FyNDV').find_elements_by_tag_name("a")
                    for href in hrefs:
                        href=href.get_attribute("href")
                        if href not in pics_href:
                            print(self.uyariRenk("[+] Url:" + href, 1))
                        pics_href.add(href)

                    time.sleep(5)
                except Exception as e:
                    print(self.uyariRenk("[-] '"+kullaniciadi+"' kullanıcısının paylaşımlarını tarama işlemi sırasında bir hata oluştu:"+str(e),2))
                    continue

            print(self.uyariRenk("[+] '" + kullaniciadi + "' kullanıcısının paylaşımlarının tarama işlemi bitti...",1))
            print("[*] Toplam paylaşım sayısı:"+str(len(pics_href)))
            if durum:
                print("[*] Paylaşım beğenme işlemi başladı...")
            else:
                print("[*] Paylaşım beğenmekten vazgeçme işlemi başladı...")
            for pic in pics_href:
                if durum:
                    print("[*] "+pic + " paylaşımı beğeniliyor...")
                else:
                    print("[*] "+pic + " paylaşımı beğenmekten vazgeçiliyor...")
                try:
                    self.driver.get(pic)
                    time.sleep(5)
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    btn_begen_class = self.driver.find_element_by_css_selector("span.fr66n > button > span").get_attribute("class")
                    if durum:
                        if "glyphsSpriteHeart__outline__24__grey_9" in btn_begen_class:
                            begen = self.driver.find_element_by_css_selector("span.glyphsSpriteHeart__outline__24__grey_9")
                            begen.click()
                            print(self.uyariRenk("[+] "+pic+" paylaşımı beğenildi",1))
                            time.sleep(10)
                        else:
                            print(self.uyariRenk("[-] Bu gönderi daha önce beğenildi.",1))
                    else:
                        if "glyphsSpriteHeart__filled__24__red_5" in btn_begen_class:
                            btn_begen = self.driver.find_element_by_css_selector("span.glyphsSpriteHeart__filled__24__red_5")
                            btn_begen.click()
                            print(self.uyariRenk("[+] "+pic + " paylaşımı beğenilmekten vazgeçildi.",1))
                            time.sleep(10)
                        else:
                            print(self.uyariRenk("[-] Bu gönderi zaten beğenilmedi.",1))
                except Exception as e:
                    print(self.uyariRenk("[-] '"+kullaniciadi+"' kullanıcısının paylaşımlarını beğenme işlemi sırasında bir hata oluştu:"+str(e),2))
                    continue


            print(self.uyariRenk("[+] '"+kullaniciadi+"' kullanıcısının paylaşımlarını beğenme işlemi tamamlandı",1))
            self.profilSec(secim)
        else:
            print(self.uyariRenk("[-] "+kullaniciadi+" adlı kişinin hesabı gizli hesap olduğundan beğeni işlemi yapılamıyor!",2))
            self.profilSec(secim)

    def paylasimBegen(self,durum=True):
        if durum:
            url = input("Beğenmek istediğiniz paylaşım url >> ").strip()
        else:
            url = input("Beğenmekten vazgeçmek istediğiniz paylaşım url >> ").strip()

        if not url:
            self.paylasimBegen(durum)
        elif url=="menu":
            self.menu()

        if self.urlKontrol(url):
            self.driver.get(url)
            if durum:
                print("[*] '" + url + "' adresindeki paylaşımın beğenme işlemi başladı...")
            else:
                print("[*] '" + url + "' adresindeki paylaşımın beğenmekten vazgeçme işlemi başladı...")
            time.sleep(10)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            if "This Account is Private" not in self.driver.page_source:
                try:
                    btn_begen_class = self.driver.find_element_by_css_selector("span.fr66n > button > span").get_attribute("class")
                    if durum:
                        if "glyphsSpriteHeart__outline__24__grey_9" in btn_begen_class:
                            begen = self.driver.find_element_by_css_selector("span.glyphsSpriteHeart__outline__24__grey_9")
                            begen.click()
                            print(self.uyariRenk("[+] "+url + " paylaşımı beğenildi",1))
                            self.paylasimBegen(durum)
                        else:
                            print(self.uyariRenk("[-] Bu gönderi daha önce beğenildi.",2))
                            self.paylasimBegen(durum)
                    else:
                        if "glyphsSpriteHeart__filled__24__red_5" in btn_begen_class:
                            btn_begen = self.driver.find_element_by_css_selector("span.glyphsSpriteHeart__filled__24__red_5")
                            btn_begen.click()
                            print(self.uyariRenk("[+] "+ url + " paylaşımı beğenilmekten vazgeçildi.",1))
                            self.paylasimBegen(durum)
                        else:
                            print(self.uyariRenk("[-] Bu gönderi zaten beğenilmedi.",2))
                            self.paylasimBegen(durum)
                except Exception as e:
                    if durum:
                        print(self.uyariRenk("[-] Paylaşım beğenme işlemi sırasında hata:"+str(e),2))
                        self.paylasimBegen(durum)
                    else:
                        print(self.uyariRenk("[-] Paylaşım beğenmekten vazgeçme işlemi sırasında hata:"+str(e),2))
                        self.paylasimBegen(durum)
            else:
                print(self.uyariRenk("[-] "+url + " paylaşımının sahibinin profili gizli hesap olduğundan beğeni işlemi yapılamıyor!",2))
                self.paylasimBegen(durum)
        else:
            self.paylasimBegen(durum)

    def fotografIndir(self):
        url=input("İndirmek istediğiniz fotoğraf url >> ").strip()

        if not url:
            self.fotografIndir()
        elif url=="menu":
            self.menu()

        if self.urlKontrol(url):
            try:
                self.driver.get(url)
                print("[*] '" + url + "' adresindeki fotoğrafın indirme işlemi başladı...")
                time.sleep(10)
                if "This Account is Private" not in self.driver.page_source:
                    klasoradi=self.driver.find_element_by_css_selector("h2.BrX75").find_element_by_css_selector("a.FPmhX").text
                    self.klasorOlustur(klasoradi)
                    img=self.driver.find_element_by_css_selector("div.KL4Bh").find_element_by_tag_name("img").get_attribute("src")
                    isim = str(datetime.datetime.now()).replace(":", "_").replace(" ", "") + ".jpg"
                    urllib.request.urlretrieve(img,isim)
                    print(self.uyariRenk("[+] "+img+" indirildi", 1))
                    self.klasorDegistir("../")
                    self.fotografIndir()
                else:
                    print(self.uyariRenk("[-] "+url + " paylaşımının sahibinin profili gizli hesap olduğundan fotoğraf indirme işlemi yapılamıyor!",2))
                    self.fotografIndir()
            except Exception as e:
                print(self.uyariRenk("[-] " + url + " paylaşımını indirme işlemi sırasında hata:" + str(e), 2))
                self.fotografIndir()
        else:
            print(self.uyariRenk("[-] indirmek istediğiniz fotoğrafın url'sine ulaşılamadı!", 2))
            self.fotografIndir()

    def videoIndir(self):
        url = input("İndirmek istediğiniz video url >> ").strip()

        if not url:
            self.videoIndir()
        elif url=="menu":
            self.menu()

        if self.urlKontrol(url):
            try:
                self.driver.get(url)
                print("[*] '" + url + "' adresindeki video'nun indirme işlemi başladı...")
                time.sleep(10)
                if "This Account is Private" not in self.driver.page_source:
                    klasoradi = self.driver.find_element_by_css_selector("h2.BrX75").find_element_by_css_selector("a.FPmhX").text
                    self.klasorOlustur(klasoradi)
                    video=self.driver.find_element_by_css_selector("video.tWeCl").get_attribute("src")
                    isim = str(datetime.datetime.now()).replace(":", "_").replace(" ", "") + ".mp4"
                    urllib.request.urlretrieve(video,isim)
                    print(self.uyariRenk("[+] "+video+" indirildi",1))
                    self.klasorDegistir("../")
                    self.videoIndir()
                else:
                    print(self.uyariRenk("[-] "+url + " paylaşımının sahibinin profili gizli hesap olduğundan video indirme işlemi yapılamıyor!",2))
                    self.videoIndir()
            except Exception as e:
                print(self.uyariRenk("[-] " + url + " paylaşımını indirme işlemi sırasında hata:"+str(e), 2))
                self.videoIndir()
        else:
            print(self.uyariRenk("[-] indirmek istediğiniz video'nun url'sine ulaşılamadı!",2))
            self.videoIndir()

    def urlKontrol(self,url):
        response=requests.get(url)
        if response.status_code==404:
            return False
        else:
            return True

    def uyariRenk(self,mesaj,durum):
        if durum==1:
            return colored(mesaj,"green")
        elif durum==2:
            return colored(mesaj,"red")
        elif durum==3:
            return colored(mesaj,"blue")

    def klasorOlustur(self,klasor):
        if not os.path.exists(klasor):
            os.mkdir(klasor)
            print(self.uyariRenk("[+] '"+klasor+"' adında klasör oluşturuldu",1))
            self.klasorDegistir(klasor)
            print("[*] '"+klasor + "' klasörüne geçiş yapıldı")
        else:
            print("[*] "+klasor+" adında klasör zaten mevcut")
            self.klasorDegistir(klasor)
            print("[*] '"+klasor + "' klasörüne geçiş yapıldı")

    def klasorDegistir(self,klasor):
        os.chdir(klasor)

    def cikisYap(self):
        print("[*] İnstagramdan çıkış yapılıyor...")
        try:
            self.driver.get("https://www.instagram.com/"+self.aktifKullanici)
            time.sleep(3)
            self.driver.find_element_by_css_selector("span.glyphsSpriteUser__outline__24__grey_9").click()
            time.sleep(5)
            ayarlar=self.driver.find_element_by_css_selector("span.glyphsSpriteSettings__outline__24__grey_9")
            ayarlar.click()
            time.sleep(3)
            cikis=self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/button[6]")
            cikis.click()
            print(self.uyariRenk("[*] İnstagramdan çıkış yapıldı...", 1))
            self.driver.get('https://www.instagram.com/accounts/login/')
            self.girisYapildimi=False
            self.girisYap()
        except Exception as e:
            print(self.uyariRenk("[-] İnstagramdan çıkış işlemi sırasında hata:" + str(e), 2))
            self.menu()

    def quit(self):
        try:
            print("[*] Uygulamadan çıkış yapılıyor...")
            self.driver.quit()
            print(self.uyariRenk("[*] Uygulamadan çıkış yapıldı...", 1))
            exit()
        except Exception as e:
            print(self.uyariRenk("[-] Uygulamadan çıkış sırasında hata oluştu:"+str(e), 2))
            self.menu()

try:
    instagram = Instagram()
except KeyboardInterrupt:
    print("\n [*] Python uygulamasından çıkış yapılıyor...")
    exit()


