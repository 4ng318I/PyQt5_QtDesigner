from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QHBoxLayout, QLabel, QLineEdit
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
        self.setWindowTitle("Python GUI SpinBox")
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


        # creamos el Layout
        hbox = QHBoxLayout()

        # seguimos los widgets
        label = QLabel('Laptop price: ')
        label.setFont(QFont('Times', 14))

        self.line_edit = QLineEdit()
        self.line_edit.setFont(QFont('Times', 14))

        self.spin_box = QSpinBox()

        self.label_result = QLineEdit()
        self.label_result.setFont(QFont('Times', 14))


        # agregar los widgets al layout
        hbox.addWidget(label)
        hbox.addWidget(self.line_edit)
        hbox.addWidget(self.spin_box)
        hbox.addWidget(self.label_result)


        # y ahora a mostrarlos en el layout
        self.setLayout(hbox)


    # here we go!! llamando al metodo SpinBox_selected
        self.spin_box.valueChanged.connect(self.SpinBox_selected)

    def SpinBox_selected(self):

        if self.line_edit.text() != 0:

            price = int(self.line_edit.text())
            total_price = self.spin_box.value() * price
            self.label_result.setText(str(total_price))

        else:
            print('Wrong value')







# Aqui creamos el objeto de nuestra aplicacion

app = QApplication(sys.argv)

# lo siguiente el objeto de nuestra ventana tipo QWidget
window = Window()
window.show()

sys.exit(app.exec_())