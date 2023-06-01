from Çalışan import Çalışan
class BeyazYaka(Çalışan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk,sektör,tecrübe,maaş,teşvik_primi):#özellikler
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektör, tecrübe, maaş)
        try:
            if teşvik_primi>500 or teşvik_primi<2500:#teşavik primi kontrolü.
             self.teşvik_primi=teşvik_primi
        
        except:
            print("Hata!")
    
    def get_teşvik_primi(self):
        return self.teşvik_primi
    
    def set_teşvik_primi(self,teşvik_primi):
        self.teşvik_primi=teşvik_primi 

    def zam_hakki(self):#maaş hesabı.
        eski_maaş=self.maaş
        try:
            if self.tecrübe<2:
                sonuc=self.teşvik_primi
                yeni_maaş=eski_maaş+sonuc
                return yeni_maaş
            
            elif (self.tecrübe>=2 and self.tecrübe<=4) and (self.maaş<15000):
                sonuc=(self.maaş%self.tecrübe)*5+self.teşvik_primi
                yeni_maaş=eski_maaş+sonuc
                return yeni_maaş
            
            elif(self.tecrübe>4) and (self.maaş<25000):
                sonuc=(self.maaş%self.tecrübe)*4+self.teşvik_primi
                yeni_maaş=sonuc+eski_maaş
                return yeni_maaş
            
            else:
                yeni_maaş=eski_maaş
                return eski_maaş
        
        except:
            print("Hata!")
    
    def __str__(self):
        try:
         return f"Ad:{self.get_ad()} Soyad:{self.get_soyad()} Tecrübe:{self.get_tecrübe()}yıl Yeni Maaşı:{self.zam_hakki()} "
        except:
            print("Hata!")
    


        
    