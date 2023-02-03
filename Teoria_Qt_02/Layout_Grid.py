from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
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
        self.setWindowTitle("Python GUI QGridLayout")
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


        # crear el objeto GridLayout
        grid = QGridLayout()

        # ahora los botones para el grid
        btn1 = QPushButton('one')
        btn2 = QPushButton('two')
        btn3 = QPushButton('three')
        btn4 = QPushButton('four')
        btn5 = QPushButton('five')
        btn6 = QPushButton('six')
        btn7 = QPushButton('seven')
        btn8 = QPushButton('eight')


        # ahora agregamos los botones al grid
        grid.addWidget(btn1,0,0)
        grid.addWidget(btn2,0,1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)


        # y mostramos el grid en el layout
        self.setLayout(grid)



# Aqui creamos el objeto de nuestra aplicacion

app = QApplication(sys.argv)

# lo siguiente el objeto de nuestra ventana tipo QWidget
window = Window()
window.show()

sys.exit(app.exec_())