from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel
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
        self.setGeometry(200,200,300,200)
        self.setWindowTitle("Python GUI Radio Button")
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

        # llamamos a la funcion
        self.create_radio_button()



    def create_radio_button(self):
        # primero creamos el objeto Layout H
        hbox = QHBoxLayout()

        radb1 = QRadioButton('Python')
        radb1.setIcon(QIcon('images/python.png'))
        radb1.setIconSize(QSize(20, 40))
        radb1.setFont(QFont('Times', 12))
        radb1.setChecked(True)
        radb1.toggled.connect(self.radio_selected)

        radb2 = QRadioButton('JavaScript')
        radb2.setIcon(QIcon('images/js.png'))
        radb2.setIconSize(QSize(20, 40))
        radb2.setFont(QFont('Times', 12))
        radb2.toggled.connect(self.radio_selected)

        radb3 = QRadioButton('Java')
        radb3.setIcon(QIcon('images/java.png'))
        radb3.setIconSize(QSize(20, 40))
        radb3.setFont(QFont('Times', 12))
        radb3.toggled.connect(self.radio_selected)


        # mostramos el Layout con lo que tenga en su interior
        hbox.addWidget(radb1)
        hbox.addWidget(radb2)
        hbox.addWidget(radb3)


        # montamos un Label
        self.label = QLabel('')
        self.label.setFont(QFont('Sanserif', 15))

        # creamos objeto vertical layout
        vbox = QVBoxLayout()
        # mostramos lo que hay dentro de este vertical layout
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)


        self.setLayout(vbox)


    # Creamos metodo para el funcionamiento del radio button
    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label.setText(f'you have selected: {radio_btn.text()}')



# Aqui creamos el objeto de nuestra aplicacion

app = QApplication(sys.argv)

# lo siguiente el objeto de nuestra ventana tipo QWidget
window = Window()
window.show()

sys.exit(app.exec_())