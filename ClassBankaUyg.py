class BankaHesabi:
    def __init__(self,ilkMiktar=0):
        self.kalanPara=ilkMiktar
        print("Yeni hesap {} TL ile açılmıştır".format(ilkMiktar))

    def Parayatirma(self,YatanMiktar):
        self.kalanPara=self.kalanPara+YatanMiktar

    def Paracekme(self,CekilenMiktar):
        self.kalanPara=self.kalanPara-CekilenMiktar

    def kalanPara(self):
        return self.kalanPara

    def havale(self,miktar,kime):
        self.Paracekme(miktar)
        kime.Parayatirma(miktar)
    