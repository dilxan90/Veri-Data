from skull import Veritabanı
Vt=Veritabanı()
print("""
        VT'ye Hoşgeldiniz
        1-Veri Ekle 
        2-Veri Listele
        3-Veri Güncelleme
        4-Veri Silme
        """)
secim=int(input("Seç"))
if secim==1:
    ad=str(input("Ad:"))
    soyad=str(input("Soyad:"))
    num=int(input("num"))
    Vt.vtveriekle(ad,soyad,num)
elif secim==2:
       Vt.vtverilistele()
elif secim==3:
   num=int(input("numara"))
   alanadi=str(input("hangi alanda"))
   revize=str(input("yeni değer gir"))
   Vt.vtveriguncelle(alanadi,num,revize)
elif secim==4:
     silinecekveri=int(input("silinecek numara"))
     Vt.vtverisilme(silinecekveri)

else:
   print("hatalı seçim")


