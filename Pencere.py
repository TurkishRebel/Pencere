import sys
import PyQt5.QtWidgets as QtWidgets


def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 2")#Pencere adı

    pencere.setGeometry(100,100,500,500) #Pencere Büyüklüğü
    pencere.show()

    sys.exit(app.exec())
Pencere()