from Çalışan import Çalışan
class MaviYaka(Çalışan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk,sektör,tecrübe,maaş,yipranma_payi):#özellikler
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektör, tecrübe, maaş)

        try:
            if yipranma_payi>0.2 or yipranma_payi<0.5:
             self.yipranma_payi=yipranma_payi
        
        except:
            print("Hata!")

    
    def get_yipranma_payi(self):
        return self.yipranma_payi
    
    def set_yipranma_payi(self,yipranma_payi):
        self.yipranma_payi=yipranma_payi 


    def zam_hakki(self): #maaş hesabı
       try:
        eski_maaş=self.maaş
        if self.tecrübe<2:
           sonuc=self.yipranma_payi*10
           yeni_maaş=eski_maaş+sonuc
           return yeni_maaş
       
        elif (self.tecrübe>=2 and self.tecrübe<=4)and (self.maaş<15000):
         sonuc=(self.maaş%self.tecrübe)/2+self.yipranma_payi*10
         yeni_maaş=eski_maaş+sonuc
         return yeni_maaş
        
        elif(self.tecrübe>4)and(self.maaş<25000):
           sonuc=(self.maaş%self.tecrübe)/3+self.yipranma_payi*10
           yeni_maaş=eski_maaş+sonuc
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
          print("Hata!")
        
           
           
    
