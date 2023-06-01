from İnsan import İnsan
class İşsiz(İnsan):
    def __init__(self,tc_no, ad, soyad, yaş, cinsiyet, uyruk,maviyaka,beyazyaka,yönetici): #özellikler
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)
        self.maviyaka=maviyaka
        self.beyazyaka=beyazyaka
        self.yönetici=yönetici
        self.eski_tecrübe={"mavi yaka":self.maviyaka,
                           "beyaz yaka":self.beyazyaka,
                           "yönetici":self.yönetici
                           
                           } #dictionary oluşturdum.
    
    def get_maviyaka(self):
        return self.maviyaka
    
    def set_maviyaka(self,maviyaka):
        self.maviyaka=maviyaka

    def get_beyazyaka(self):
        return self.beyazyaka
    
    def set_beyazyaka(self,beyazyaka):
        self.beyazyaka=beyazyaka

    def get_maviyaka(self):
        return self.maviyaka
    
    def set_maviyaka(self,maviyaka):
        self.maviyaka=maviyaka

    
        
    
    def statu_bul(self):
        statu_puani=self.eski_tecrübe.__getitem__("mavi yaka")*0.2+self.eski_tecrübe.__getitem__("beyaz yaka")*0.35+self.eski_tecrübe.__getitem__("yönetici")*0.45 #hangi statüye uygun puanlaması
        liste=[]
        liste.append(statu_puani)
        Uygun=max(liste)
        if Uygun<=1.5:
            statü="mavi yakalı"
            return statü
        elif Uygun<4 and Uygun>1.5:
            statü="beyaz yakalı"
            return statü
        
        else:
            statü="yönetici"
            return statü
    
            
        
        
    
    def __str__(self):
        try:
         return f"Ad:{self.get_ad()} Soyad:{self.get_soyad()} Statü:{self.statu_bul()}"
        except:
            print("Hata!")
