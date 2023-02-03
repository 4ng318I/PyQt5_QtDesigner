from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


# se cre la clase del tipo de ventana en este caso QWidget con acceso a todos sus atributos y metodos
class Window(QWidget):
    # ahora creamos el constructor init y el super para heredar esto es independiente de PyQt
    def __init__(self):
        # super da acceso a metodos y propiedades de una clase padre
        super().__init__()


        # agregamos propiedades de la clase QWidget invocando al self del constructor
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI QLabel")
        self.setWindowIcon(QIcon('images/library.png'))
        # para el Icon necesitamos importar otro modulo que no esta en la ventana QWidget
        #self.setWindowIcon()
        # fijar dimensiones
        #self.setFixedWidth(700)
        #self.setFixedHeight(400)

        # cambiar estilos de ventana
        self.setStyleSheet('background-color:grey')
        # la opacidad valor entre 0 y 1
        self.setWindowOpacity(0.5)

        """
        label = QLabel("GUI Development", self)
        #label.setText("New text is hier")
        label.move(100, 150)
        label.setFont(QFont("Sanserif", 15))
        label.setStyleSheet("color:red")
        #label.setText(str(12))
        label.setNum(15)
        label.clear()
        """

        """
        # para cargar imagenes en un label creamos primero el objeto label  y le pasamos como parametro el padre self
        label = QLabel(self)
        # ahora creamos el objeto de QPixmap, le importamos arriba
        pixmap = QPixmap('images/library.png')
        #ahora ponemos el pixmap en el label
        label.setPixmap(pixmap)
        """

        # ahora probamos QMovie para pequenas animaciones GIFS
        label = QLabel(self)
        movie = QMovie('images/biblioteca.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()



# Aqui creamos el objeto de nuestra aplicacion

app = QApplication(sys.argv)

# lo siguiente el objeto de nuestra ventana tipo QWidget
window = Window()
window.show()

sys.exit(app.exec_())