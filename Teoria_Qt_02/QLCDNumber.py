from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTime, QTimer
import sys


# se cre la clase del tipo de ventana en este caso QWidget con acceso a todos sus atributos y metodos
class Window(QWidget):
    # ahora creamos el constructor init y el super para heredar esto es independiente de PyQt
    def __init__(self):
        # super da acceso a metodos y propiedades de una clase padre
        super().__init__()

        # Llamada al LCD
        timer = QTimer()
        timer.timeout.connect(self.show_LCD)
        #inicializamos el tiempo en milisegundos
        timer.start(1000)

        #mostramos el lcd
        self.show_LCD()


        # agregamos propiedades de la clase QWidget invocando al self del constructor
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI QLCDNumber")
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


    def show_LCD(self):
        vbox = QVBoxLayout()

        lcd = QLCDNumber()
        lcd.setStyleSheet('background-color:red')

        vbox.addWidget(lcd)

        # obtener el tiempo actual
        time = QTime.currentTime()
        # ahora viene poner el formato
        text = time.toString('hh:mm')

        # ahora ensenamos el texto en el lcd
        lcd.display(text)



        self.setLayout(vbox)


# Aqui creamos el objeto de nuestra aplicacion

app = QApplication(sys.argv)

# lo siguiente el objeto de nuestra ventana tipo QWidget
window = Window()
window.show()

sys.exit(app.exec_())