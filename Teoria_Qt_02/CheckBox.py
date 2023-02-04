from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QCheckBox, QLabel
from PyQt5.QtGui import QIcon, QFont
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
        self.setWindowTitle("Python GUI CheckBox")
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


        # creamos Layout para el label
        hbox = QHBoxLayout()




        #creamos layout vertical para el resto
        vbox = QVBoxLayout()

        # a continuacion los objetos checkbox
        self.checkbox_1 = QCheckBox('Python')
        self.checkbox_1.setFont(QFont('Times', 14))
        self.checkbox_1.setIcon(QIcon('images/python.png'))
        self.checkbox_1.setIconSize(QSize(20, 20))

        self.checkbox_1.stateChanged.connect(self.Item_selected)

        self.checkbox_2 = QCheckBox('Java')
        self.checkbox_2.setFont(QFont('Times', 14))
        self.checkbox_2.setIcon(QIcon('images/java.png'))
        self.checkbox_2.setIconSize(QSize(20, 20))

        self.checkbox_2.stateChanged.connect(self.Item_selected)

        self.checkbox_3 = QCheckBox('JavaScript')
        self.checkbox_3.setFont(QFont('Times', 14))
        self.checkbox_3.setIcon(QIcon('images/js.png'))
        self.checkbox_3.setIconSize(QSize(20, 20))

        self.checkbox_3.stateChanged.connect(self.Item_selected)

        # creamos un objeto en layout horizintal y lo mostramos
        self.label = QLabel('')
        self.label.setFont(QFont('Times', 14))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)



        # agregamos los objetos al layout
        hbox.addWidget(self.checkbox_1)
        hbox.addWidget(self.checkbox_2)
        hbox.addWidget(self.checkbox_3)


        vbox.addLayout(hbox)

        # mostramos el layout
        self.setLayout(vbox)

    # vamos a por el metodo
    def Item_selected(self):
        value = ''

        if self.checkbox_1.isChecked():
            value = self.checkbox_1.text()

        if self.checkbox_2.isChecked():
            value = self.checkbox_2.text()

        if self.checkbox_3.isChecked():
            value = self.checkbox_3.text()

        self.label.setText("You habe selected: " + value)



# Aqui creamos el objeto de nuestra aplicacion

app = QApplication(sys.argv)

# lo siguiente el objeto de nuestra ventana tipo QWidget
window = Window()
window.show()

sys.exit(app.exec_())