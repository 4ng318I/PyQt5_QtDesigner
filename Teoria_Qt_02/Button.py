from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt5.QtGui import QIcon, QFont
# para hacer mas grande el icono del boton
from PyQt5.QtCore import QSize
import sys


# se cre la clase del tipo de ventana en este caso QWidget con acceso a todos sus atributos y metodos
class Window(QWidget):
    # ahora creamos el constructor init y el super para heredar esto es independiente de PyQt
    def __init__(self):
        # super da acceso a metodos y propiedades de una clase padre
        super().__init__()


        # agregamos propiedades de la clase QWidget invocando al self del constructor
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI QPushButton")
        self.setWindowIcon(QIcon('images/library.png'))
        # para el Icon necesitamos importar otro modulo que no esta en la ventana QWidget
        #self.setWindowIcon()
        # fijar dimensiones
        #self.setFixedWidth(700)
        #self.setFixedHeight(400)

        # llamamos a la funcion donde creamos el boton
        self.create_button()



        # cambiar estilos de ventana
        self.setStyleSheet('background-color:grey')
        # la opacidad valor entre 0 y 1
        self.setWindowOpacity(0.9)


    def create_button(self):
        btn = QPushButton('Click!',self)
        btn.setGeometry(100,100,130,130)
        btn.setFont(QFont('Times', 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon('images/library.png'))
        # para hacer el icon mas grande dentro del boton
        btn.setIconSize(QSize(40,40))

        # popup menu
        menu = QMenu()
        menu.setFont(QFont('Times', 12, QFont.Weight.ExtraBold))
        menu.setStyleSheet('color:red')
        menu.addAction('Copy')
        menu.addAction('cut')
        menu.addAction('Paste')
        btn.setMenu(menu)



# Aqui creamos el objeto de nuestra aplicacion

app = QApplication(sys.argv)

# lo siguiente el objeto de nuestra ventana tipo QWidget
window = Window()
window.show()

sys.exit(app.exec_())