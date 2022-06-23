import sys
from PyQt5 import QtWidgets, QtGui


def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    # pencere açmakla ilgili olan kısım
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Pencere adı")  # Pencere adı

    # horizontal ve vertical box
    # stretch in yerini değiştirerek yerler değiştirilir
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")
    h_box = QtWidgets.QHBoxLayout()
    h_box.addWidget(okay)
    h_box.addStretch()
    h_box.addWidget(cancel)
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    pencere.setLayout(v_box)

    # resim basmakla ilgili olan kısım
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("A.png"))  # ekrana resim basmak
    etiket2.move(200, 70)  # resim konumu

    # buton oluşturmakla ilgili kısım
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("burası buton")
    buton.move(170, 90)

    # ekrana yazı yazmakla ilgili olan kısım
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Yazı")  # ekrana yazı yazdırmak
    etiket1.move(200, 30)  # yazı konumu
    pencere.setGeometry(100, 100, 500, 500)  # pencere boyutu
    pencere.show()
    sys.exit(app.exec())


Pencere()
