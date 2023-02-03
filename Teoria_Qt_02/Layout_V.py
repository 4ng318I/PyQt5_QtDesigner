from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
import sys


# se cre la clase del tipo de ventana en este caso QWidget con acceso a todos sus atributos y metodos
class Window(QWidget):
    # ahora creamos el constructor init y el super para heredar esto es independiente de PyQt
    def __init__(self):
        # super da acceso a metodos y propiedades de una clase padre
        super().__init__()


        # agregamos propiedades de la clase QWidget invocando al self del constructor
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI QVBoxLayout")
        self.setWindowIcon(QIcon('images/library.png'))
        # para el Icon necesitamos importar otro modulo que no esta en la ventana QWidget
        #self.setWindowIcon()
        # fijar dimensiones
        #self.setFixedWidth(700)
        #self.setFixedHeight(400)

        # cambiar estilos de ventana
        self.setStyleSheet('background-color:grey')
        # la opacidad valor entre 0 y 1
        self.setWindowOpacity(0.9)

        # creamos el objeto layout vertical
        layout_V = QVBoxLayout()

        # creamos los botones para el Layout
        btn1 = QPushButton('Click one')
        btn2 = QPushButton('Click two')
        btn3 = QPushButton('Click Three')
        btn4 = QPushButton('Click four')


        # colocamos los botones en el layout vertical
        layout_V.addWidget(btn1)
        layout_V.addWidget(btn2)
        layout_V.addWidget(btn3)
        layout_V.addWidget(btn4)
        layout_V.addSpacing(100)
        # con addStrech te los junta todos arriba
        layout_V.addStretch(5)

        # mostramos los botones dentro del layout vertical
        self.setLayout(layout_V)



# Aqui creamos el objeto de nuestra aplicacion

app = QApplication(sys.argv)

# lo siguiente el objeto de nuestra ventana tipo QWidget
window = Window()
window.show()

sys.exit(app.exec_())