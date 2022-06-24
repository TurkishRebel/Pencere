import sys
from PyQt5 import QtWidgets, QtGui


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        

    def init_ui(self):
        self.gir = QtWidgets.QLineEdit()
        self.yazı_alanı = QtWidgets.QLabel("Bana henüz tıklanmadı")
        self.buton = QtWidgets.QPushButton("Bana tıkla")
        self.buton2 = QtWidgets.QPushButton("Temizle")
        self.buton3 = QtWidgets.QPushButton("Bas")
        self.say = 0

        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addWidget(self.gir)
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.buton)        
        v_box.addWidget(self.buton2)
        v_box.addWidget(self.buton3)

        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        self.setLayout(v_box)
        self.setLayout(h_box)
        self.buton.clicked.connect(self.click)
        self.buton2.clicked.connect(self.fonk)
        self.buton3.clicked.connect(self.fonk2)

        self.show()

    def click(self):
        self.say += 1
        self.yazı_alanı.setText("Bana" + str(self.say) + "defa tıklandı")

        self.show()

    def fonk(self):
        self.gir.clear()
    def fonk2(self):
        self.yazı_alanı.setText("AAAAAAA")

    
       
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
