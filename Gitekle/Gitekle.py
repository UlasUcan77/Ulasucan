class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satis_tutari = 0
        
    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi
        
    def get_magaza_adi(self):
        return self.__magaza_adi
    
    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi
        
    def get_satici_adi(self):
        return self.__satici_adi
    
    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi
        
    def get_satici_cinsi(self):
        return self.__satici_cinsi
    
    def set_satis_tutari(self, satis_tutari):
        self.__satis_tutari = satis_tutari
        
    def get_satis_tutari(self):
        return self.__satis_tutari
    
    def magaza_satis_tutari(self, magaza_adi):
        toplam_satis_tutari = 0
        for magaza in magazalar:
            if magaza.get_magaza_adi() == magaza_adi:
                toplam_satis_tutari += magaza.get_satis_tutari()
        return toplam_satis_tutari
    
    def __str__(self):
        return f"Mağaza Adı: {self.__magaza_adi}, Satıcı Adı: {self.__satici_adi}, Satıcı Cinsi: {self.__satici_cinsi}, Toplam Satış Tutarı: {self.__satis_tutari}"
    
magazalar = []
while True:
    magaza_adi = input("Mağaza adını girin (çıkmak için 'a' girin): ")
    if magaza_adi == "a":
        break
        
    satici_adi = input("Satıcının adını girin: ")
    satici_cinsi = input("Satıcının cinsini girin: ")
    satis_tutari = float(input("Satış tutarını girin: "))
    
    magaza = Magaza(magaza_adi, satici_adi, satici_cinsi)
    magaza.set_satis_tutari(satis_tutari)
    magazalar.append(magaza)
    
    toplam_satis_tutari = magaza.magaza_satis_tutari(magaza_adi)
    
for magaza in magazalar:
    print(magaza)
    
print(f"Toplam Satış Tutarı: {toplam_satis_tutari}")    
