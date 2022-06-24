
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit



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

        self.yazı_alanı.setText('Kaydedilecek Öğrencinin bilgilerini giriniz')
        self.nameLabel.setText('İsim:')#Yazı belirleme
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
        self.buton2.clicked.connect(self.fonk2)
        self.show()

    def click(self):
        self.yazı_alanı.setText("Kayıt Başarılı")
        self.yazı_alanı.move(150,200)



    def fonk(self):#Kayıt işlemi
        self.yazı_alanı.setText("Kayıt Başarılı")
        self.yazı_alanı.move(150, 200)
        self.gir.clear()
        self.gir2.clear()
        self.gir3.clear()
        self.gir4.clear()


    def fonk2(self):#Silme işlemi
        self.yazı_alanı.setText("Silme İşlemi başarılı")
        self.yazı_alanı.move(150, 200)
        self.gir.clear()
        self.gir2.clear()
        self.gir3.clear()
        self.gir4.clear()


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())

