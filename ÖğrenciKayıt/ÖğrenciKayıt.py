import sqlite3
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
sys.setrecursionlimit(3000)

con = sqlite3.connect("ogrenci_kayit.db")

cursor = con.cursor()

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setFixedSize(400, 250)#pencere boyutu kitleme
        self.setWindowTitle("Öğrenci Kayıt")
    def init_ui(self):
        self.gir = QLineEdit(self)#Kullanıcı girdisi için çubuk
        self.gir2 = QLineEdit(self)
        self.gir3 = QLineEdit(self)
        self.gir4 = QLineEdit(self)

        self.nameLabel = QLabel(self)#Yazı yeri oluşturma
        self.nameLabel2 = QLabel(self)
        self.nameLabel3 = QLabel(self)
        self.nameLabel4 = QLabel(self)
        self.yazı_alanı = QtWidgets.QLabel(self)

        self.yazı_alanı.setText("Kaydedilecek Öğrencinin bilgilerini giriniz " + "\n" + "veya silinecek öğrencinin numarasını giriniz")
        self.nameLabel.setText('İsim:')#Yazı belirleme0
        self.nameLabel2.setText('Soyisim:')
        self.nameLabel3.setText('Numara:')
        self.nameLabel4.setText('Bölüm:')

        self.buton = QtWidgets.QPushButton(self)#Buton belirleme
        self.buton2 = QtWidgets.QPushButton(self)

        self.buton.setText('Kaydet:')
        self.buton2.setText('Sil')





        self.gir.move(80, 20)#move yer değiştirme
        self.gir2.move(80, 60)
        self.gir3.move(80, 100)
        self.gir4.move(80, 140)

        self.gir.resize(200, 32)#resize konum değiştirme
        self.gir2.resize(200, 32)
        self.gir3.resize(200, 32)
        self.gir4.resize(200, 32)

        self.nameLabel.move(40,20)
        self.nameLabel2.move(20,60)
        self.nameLabel3.move(19,100)
        self.nameLabel4.move(30,140)
        self.yazı_alanı.move(60,200)
        self.buton.move(290,20)
        self.buton2.move(290,50)


        self.buton.clicked.connect(self.fonk)#butonlara fonksiyon atama
        self.buton2.clicked.connect(self.fonk3)
        self.show()

    def fonk(self):#Kayıt işlemi
      if self.gir.text() != "" or self.gir2.text() != ""or self.gir3.text() != "" or self.gir4.text() != "":
        cursor.execute("Insert into ogr Values(?,?,?,?)",(self.gir.text(), self.gir2.text(), self.gir3.text(), self.gir4.text()))
        con.commit()
        self.yazı_alanı.setText("Kayıt Başarılı!...")
        self.yazı_alanı.move(150, 200)
        self.gir.clear()#Yazıları silme
        self.gir2.clear()
        self.gir3.clear()
        self.gir4.clear()
      else:
        self.yazı_alanı.setText("Kayıtlanma yapılamadı!")
        self.yazı_alanı.move(130, 200)


    def fonk3(self):
      a = (self.gir3.text())
      def fonk2(a):
       if a != "":
        cursor.execute("Delete From ogr where numara = ?",(a,))
        con.commit()
        self.yazı_alanı.setText("Silme İşlemi başarılı")
        self.yazı_alanı.move(150, 200)

        self.gir.clear()
        self.gir2.clear()
        self.gir3.clear()
        self.gir4.clear()
       else:
           self.yazı_alanı.setText("Silme işlemi başarısız!")
           self.yazı_alanı.move(130, 200)
      fonk2(a)
def tablo_olustur():
      cursor.execute("CREATE TABLE IF NOT EXISTS ogr (ad TEXT,soyisim TEXT,numara INT,bölüm TEXT)")
      con.commit()
tablo_olustur()

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
con.close
sys.exit(app.exec_())
