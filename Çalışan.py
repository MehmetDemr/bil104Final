from İnsan import İnsan
class Çalışan(İnsan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk,sektör,tecrübe,maaş):#özellikler
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)
        if (sektör=="teknoloji" or sektör=="muhasebe" or sektör=="inşaat" or sektör=="diğer"):#kontrol edildi.
            self.sektör=sektör
        else:
            self.sektör=None
        
        self.tecrübe=tecrübe
        self.maaş=maaş
    
    def set_sektör(self,sektör):
        self.sektör=sektör

    def get_sektör(self):
        return self.sektör
    
    def set_tecrübe(self,tecrübe):
        self.tecrübe=tecrübe

    def get_tecrübe(self):
        return self.tecrübe
    
    def set_maaş(self,maaş):
        self.maaş=maaş

    def get_maaş(self):
        return self.maaş
    
    def zam_hakki(self):
        try:
         eski_maaş=self.maaş
         if self.tecrübe<2:
            yeni_maaş=eski_maaş
            return yeni_maaş
        
         elif (self.tecrübe<=2 and self.tecrübe>=4) and (self.maaş<15000):#maaş hesabı
            zam_orani=self.maaş%self.tecrübe
            sonuc=eski_maaş*zam_orani
            yeni_maaş=sonuc+eski_maaş
            return yeni_maaş
        
         elif(self.tecrübe>4)and (self.maaş<25000):
            zam_orani=(self.maaş%self.tecrübe)/2
            sonuc=eski_maaş*zam_orani
            yeni_maaş=sonuc+eski_maaş
            return yeni_maaş
         
         else:
             yeni_maaş=eski_maaş
             return yeni_maaş
    
        
        except:
            print("Hata!")
    
    def __str__(self):
        try:
         return f"Ad: {self.get_ad()} Soyad:{self.get_soyad()} Tecrübe:{self.get_tecrübe()} Yeni Maaş:{self.zam_hakki()}"
        except:
            print("Bir hata oluştu!")