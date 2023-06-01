from Çalışan import Çalışan
from MaviYaka import MaviYaka
from İşsiz import İşsiz
from İnsan import İnsan
from BeyazYaka import BeyazYaka
import pandas as pd
sayac=0
i1=İnsan(123,"Dilay","Yücel",25,"Kadın","Türk")
i2=İnsan(234,"Mehmet","Demir",25,"Erkek","Türk")
j1=İşsiz(876,"Ahmet","Tan",37,"Erkek","Türk",3,4,5)
j2=İşsiz(111,"Kerem","Yak",35,"Erkek","Türk",3,2,0)
ç1=Çalışan(567,"Leyla","Yay",34,"Kadın","Türk","teknoloji",4,23000)
ç2=Çalışan(444,"Sevil","Koç",36,"Kadın","Türk","muhasebe",9,30000)
ç3=Çalışan(999,"Ata","Uzun",44,"Erkek","Türk","muhasebe",5,13000)
m1=MaviYaka(34,"Emrecan","Bozkurt",29,"Erkek","Türk","inşaat",3,10000,0.2)
m2=MaviYaka(577,"Ekrem","Zar",35,"Erkek","Türk","muhasebe",5,17000,0.3)
m3=MaviYaka(888,"Kemal","Kılıç",39,"Erkek","Türk","teknoloji",10,19000,0.4)
b1=BeyazYaka(900,"Merve","Uç",31,"Kadın","Türk","inşaat",3,17800,1000)
b2=BeyazYaka(987,"Beyza","Ran",37,"Erkek","Türk","muhasebe",2,15800,700)
b3=BeyazYaka(344,"Cristiano","Ronaldo",38,"Erkek","Portekiz","teknoloji",8,30000,2400)
print(i1)#hepsini yazdırdım.
print(i2)
print(j1)
print(j2)
print(ç1)
print(ç2)
print(ç3)
print(m1)
print(m2)
print(m3)
print(b1)
print(b2)
print(b3)



veri = {
    "TC No": [i1.get_tc_no(), i2.get_tc_no(), j1.get_tc_no(), j2.get_tc_no(), ç1.get_tc_no(), ç2.get_tc_no(), ç3.get_tc_no(), m1.get_tc_no(), m2.get_tc_no(), m3.get_tc_no(), b1.get_tc_no(), b2.get_tc_no(), b3.get_tc_no()],
    "Ad": [i1.get_ad(), i2.get_ad(), j1.get_ad(), j2.get_ad(), ç1.get_ad(), ç2.get_ad(), ç3.get_ad(), m1.get_ad(), m2.get_ad(), m3.get_ad(), b1.get_ad(), b2.get_ad(), b3.get_ad()],
    "Soyad": [i1.get_soyad(), i2.get_soyad(), j1.get_soyad(), j2.get_soyad(), ç1.get_soyad(), ç2.get_soyad(), ç3.get_soyad(), m1.get_soyad(), m2.get_soyad(), m3.get_soyad(), b1.get_soyad(), b2.get_soyad(), b3.get_soyad()],
    "Yaş": [i1.get_yaş(), i2.get_yaş(), j1.get_yaş(), j2.get_yaş(), ç1.get_yaş(), ç2.get_yaş(), ç3.get_yaş(), m1.get_yaş(), m2.get_yaş(), m3.get_yaş(), b1.get_yaş(), b2.get_yaş(), b3.get_yaş()],
    "Cinsiyet": [i1.get_cinsiyet(), i2.get_cinsiyet(), j1.get_cinsiyet(), j2.get_cinsiyet(), ç1.get_cinsiyet(), ç2.get_cinsiyet(), ç3.get_cinsiyet(), m1.get_cinsiyet(), m2.get_cinsiyet(), m3.get_cinsiyet(), b1.get_cinsiyet(), b2.get_cinsiyet(), b3.get_cinsiyet()],
    "Uyruk": [i1.get_uyruk(), i2.get_uyruk(), j1.get_uyruk(), j2.get_uyruk(), ç1.get_uyruk(), ç2.get_uyruk(), ç3.get_uyruk(), m1.get_uyruk(), m2.get_uyruk(), m3.get_uyruk(), b1.get_uyruk(), b2.get_uyruk(), b3.get_uyruk()],
    "Sektör":[0,0,0,0,ç1.get_sektör(),ç2.get_sektör(),ç3.get_sektör(),m1.get_sektör(),m2.get_sektör(),m3.get_sektör(),b1.get_sektör(),b2.get_sektör(),b3.get_sektör()],
    "Tecrübe":[0,0,0,0,ç1.get_tecrübe(),ç2.get_tecrübe(),ç3.get_tecrübe(),m1.get_tecrübe(),m2.get_tecrübe(),m3.get_tecrübe(),b1.get_tecrübe(),b2.get_tecrübe(),b3.get_tecrübe()],
    "Maaş":[0,0,0,0,ç1.get_maaş(),ç2.get_maaş(),ç3.get_maaş(),m1.get_maaş(),m2.get_maaş(),m3.get_maaş(),b1.get_maaş(),b2.get_maaş(),b3.get_maaş()],
    "Yıpranma Payı:":[0,0,0,0,0,0,0,m1.get_yipranma_payi(),m2.get_yipranma_payi(),m3.get_yipranma_payi(),0,0,0],
    "Teşvik Primi":[0,0,0,0,0,0,0,0,0,0,b1.get_teşvik_primi(),b2.get_teşvik_primi(),b3.get_teşvik_primi()],
    "Yeni Maaş":[0,0,0,0,ç1.zam_hakki(),ç2.zam_hakki(),ç3.zam_hakki(),m1.zam_hakki(),m2.zam_hakki(),m3.zam_hakki(),b1.zam_hakki(),b2.zam_hakki(),b3.zam_hakki()]
}
#burda dataframe oluşturuldu.
x=pd.DataFrame(veri)
print(x)
print()
çalışanlar=[ç1,ç2,ç3]
maviyakalılar=[m1,m2,m3]
beyazyakalılar=[b1,b2,b3]
print("Çalışanların maaş ortalaması:",(ç1.zam_hakki()+ç2.zam_hakki()+ç3.zam_hakki())/3)#maaş ortalamalarını ekrana yazdırdım.
print("Çalışanların çalışma tecrübesi ortalaması:",(ç1.get_tecrübe()+ç2.get_tecrübe()+ç3.get_tecrübe())/3)
print("Mavi yakalıların maaş ortalaması:",(m1.zam_hakki()+m2.zam_hakki()+m3.zam_hakki())/3)
print("Mavi yakalıların çalışma tecrübesi ortalaması:",(m1.get_tecrübe()+m2.get_tecrübe()+m3.get_tecrübe())/3)
print("Beyaz yakalıların maaş ortalaması:",((b1.zam_hakki()+b2.zam_hakki()+b3.zam_hakki())/3))
print("Beyaz yakalıların çalışma tecrübesi ortalaması:",(b1.get_tecrübe()+b2.get_tecrübe()+b3.get_tecrübe())/3)
print()
for y in çalışanlar and maviyakalılar and beyazyakalılar: #maaşı 15000den yüksek çalışan mavi yakalı veya beyaz yakalı kaç tane
    if y.get_maaş()>15000:
        sayac=sayac+1
print(sayac)
print()
sıralı = x.sort_values(by='Maaş')#maaşı küçükten büyüğe yazdırma.
print(sıralı)
print()
for z in beyazyakalılar: #tecrübesi 3 ten yüksek beyaz yakalı sayısı ve ismi.
    if z.get_tecrübe()>3:
        pass
print("Tecrübesi 3 seneden daha fazla olan beyaz yakalı personelimiz:")      
print("Ad:",z.get_ad(),"Soyad:",z.get_soyad())
print()
d=x.query("Maaş > 10000 and 2 <= index <= 5")#2 ile 5 arasındaki indexlerde bulunan kişilerin maaşı 10k dan yüksekse ekrana yazdır.
print(d)
print()
yeni_frame=x.loc[:,["Ad","Soyad","Sektör","Yeni Maaş"]] #Birkaç bilgi içeren daha küçük dataframe.
print(yeni_frame)



