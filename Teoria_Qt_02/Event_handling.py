from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont
import sys


# se cre la clase del tipo de ventana en este caso QWidget con acceso a todos sus atributos y metodos
class Window(QWidget):
    # ahora creamos el constructor init y el super para heredar esto es independiente de PyQt
    def __init__(self):
        # super da acceso a metodos y propiedades de una clase padre
        super().__init__()


        # agregamos propiedades de la clase QWidget invocando al self del constructor
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI Event handling")
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

        # llamada a la funcion que crea los widgets
        self.create_widget()


    def create_widget(self):
        # creamos esa fucion para el layout_H, boton y el label
        Layout_H = QHBoxLayout()
        btn1 = QPushButton('Click me!')
        # slot del boton
        btn1.clicked.connect(self.clicked_button)
        # puedes pasar el label como objeto de clase con self o con veriable
        self.label = QLabel('Test Standard')
        label2 = QLabel('Text 3')

        # adjuntamos los elementos al grid
        Layout_H.addWidget(btn1)
        Layout_H.addWidget(self.label)
        Layout_H.addWidget(label2)

        # mostramos el layout_H con sus elementos dentro
        self.setLayout(Layout_H)


    def clicked_button(self):
        self.label.setText('Another Text!!')
        self.label.setFont(QFont('Times', 15))
        self.label.setStyleSheet('color:red')





# Aqui creamos el objeto de nuestra aplicacion

app = QApplication(sys.argv)

# lo siguiente el objeto de nuestra ventana tipo QWidget
window = Window()
window.show()

sys.exit(app.exec_())