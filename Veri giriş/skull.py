import sqlite3
class Veritabanı:
    def vtbaglanti(self):
        try:
            self.baglanti=sqlite3.connect("dilhan.db")
            self.imlec=self.baglanti.cursor()
            self.baglanti.commit()
            self.tablo="Create table if not Exists hali ('Numara' integer not null primary key, 'Ad' text not null, 'Soyad' text not null)"
            self.imlec.execute(self.tablo)
            self.baglanti.commit()
        except Exception as a:
            print(str(a),":Hata Kodu")

    def vtveriekle(self,ad,soyad,numara):
        self.sorgu="insert into hali (Numara,Ad,Soyad) values (?,?,?)"
        try:
            self.vtbaglanti()
            self.imlec.execute(self.sorgu,(numara,ad,soyad))
            self.baglanti.commit()
            self.baglanti.close()
        except Exception as a:
            print(str(a),":Hata Kodu")

    def vtverilistele(self):
        self.sorgu="Select * from hali"
        try:
            self.imlec.execute(self.sorgu)
            self.veriler=self.imlec.fetchall()
            for i in self.veriler:
                print(i)
        except Exception as a:
            print(str(a),":Hata kodu")

    def vtveriguncelle(self,alanadi,numara,revize):
       self.sorgu="update hali set"+alanadi+"=? where Numara=?"
       try:
           self.baglanti()
           self.imlec.execute(self.sorgu,(revize,numara))
           self.baglanti.commit()
           self.baglanti.close()
       except Exception as a:
           print(str(a),":Hata kodu")

    def vtverisilme(self, numara):
        self.sorgu = "Delete from hali where Numara={?}"
        try:
            self.vtbaglanti()
            self.imlec.execute(self.sorgu)
            self.vtbaglanti.commit()
            self.vtbaglanti.close()
        except Exception as a:
            print(str(a), ":Hata Kodu")
















