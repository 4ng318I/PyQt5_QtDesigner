# Forma de tener actualizados los archivos ui
# sin hacerlo desde la terminal
from PyQt5.QtWidgets import QApplication, QWidget
import sys
# importamos el modulo para convertir los archivos ui a py
from PyQt5 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("ventanaUI.ui", self)


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec_()