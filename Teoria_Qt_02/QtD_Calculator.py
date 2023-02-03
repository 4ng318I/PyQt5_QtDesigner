# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtD_Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(352, 181)
        self.widget = QtWidgets.QWidget(Calculator)
        self.widget.setGeometry(QtCore.QRect(10, 20, 322, 122))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_1.setFont(font)
        self.lbl_1.setObjectName("lbl_1")
        self.horizontalLayout.addWidget(self.lbl_1)
        self.Entry_num_1 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Entry_num_1.setFont(font)
        self.Entry_num_1.setObjectName("Entry_num_1")
        self.horizontalLayout.addWidget(self.Entry_num_1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_2.setFont(font)
        self.lbl_2.setObjectName("lbl_2")
        self.horizontalLayout_2.addWidget(self.lbl_2)
        self.Entry_num_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Entry_num_2.setFont(font)
        self.Entry_num_2.setObjectName("Entry_num_2")
        self.horizontalLayout_2.addWidget(self.Entry_num_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_suma = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_suma.setFont(font)
        self.btn_suma.setObjectName("btn_suma")

        self.btn_suma.clicked.connect(self.Suma)

        self.horizontalLayout_3.addWidget(self.btn_suma)
        self.btn_resta = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_resta.setFont(font)
        self.btn_resta.setObjectName("btn_resta")

        self.btn_resta.clicked.connect(self.Resta)

        self.horizontalLayout_3.addWidget(self.btn_resta)
        self.btn_multi = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_multi.setFont(font)
        self.btn_multi.setObjectName("btn_multi")

        self.btn_multi.clicked.connect(self.Multi)

        self.horizontalLayout_3.addWidget(self.btn_multi)
        self.btn_divi = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_divi.setFont(font)
        self.btn_divi.setObjectName("btn_divi")

        self.btn_divi.clicked.connect(self.Divi)

        self.horizontalLayout_3.addWidget(self.btn_divi)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_resultado = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_resultado.setFont(font)
        self.label_resultado.setText("")
        self.label_resultado.setObjectName("label_resultado")
        self.verticalLayout.addWidget(self.label_resultado)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    # Agregamos las funciones con las operaciones de la calculadora

    def Suma(self):
        num1 = int(self.Entry_num_1.text())
        num2 = int(self.Entry_num_2.text())
        resultado = num1 + num2
        self.label_resultado.setText(f"El resultado es: {resultado}")


    def Resta(self):
        num1 = int(self.Entry_num_1.text())
        num2 = int(self.Entry_num_2.text())
        resultado = num1 - num2
        self.label_resultado.setText(f"El resultado es: {resultado}")


    def Multi(self):
        num1 = int(self.Entry_num_1.text())
        num2 = int(self.Entry_num_2.text())
        resultado = num1 * num2
        self.label_resultado.setText(f"El resultado es: {resultado}")


    def Divi(self):
        num1 = int(self.Entry_num_1.text())
        num2 = int(self.Entry_num_2.text())
        resultado = num1 / num2
        self.label_resultado.setText(f"El resultado es: {round(resultado, 2)}")




    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Form"))
        self.lbl_1.setText(_translate("Calculator", "Number 1:"))
        self.Entry_num_1.setPlaceholderText(_translate("Calculator", "Introduce un numero"))
        self.lbl_2.setText(_translate("Calculator", "Number 2:"))
        self.Entry_num_2.setPlaceholderText(_translate("Calculator", "Introduce otro numero"))
        self.btn_suma.setText(_translate("Calculator", "+"))
        self.btn_resta.setText(_translate("Calculator", "-"))
        self.btn_multi.setText(_translate("Calculator", "*"))
        self.btn_divi.setText(_translate("Calculator", "/"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QWidget()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
