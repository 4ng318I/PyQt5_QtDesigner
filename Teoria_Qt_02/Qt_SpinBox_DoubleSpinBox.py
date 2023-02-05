# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_SpinBox_DoubleSpinBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(704, 271)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_price_pen = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_price_pen.setFont(font)
        self.lineEdit_price_pen.setObjectName("lineEdit_price_pen")
        self.horizontalLayout.addWidget(self.lineEdit_price_pen)
        self.spinBox = QtWidgets.QSpinBox(Form)

        # conexion con el doble spinbox
        self.spinBox.editingFinished.connect(self.first_result)


        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.lineEdit_price_pen_result = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_price_pen_result.setFont(font)
        self.lineEdit_price_pen_result.setObjectName("lineEdit_price_pen_result")
        self.horizontalLayout.addWidget(self.lineEdit_price_pen_result)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_price_sugar = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_price_sugar.setFont(font)
        self.lineEdit_price_sugar.setObjectName("lineEdit_price_sugar")
        self.horizontalLayout_2.addWidget(self.lineEdit_price_sugar)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)

        # conexion con el doble spinbox
        self.doubleSpinBox.editingFinished.connect(self.second_result)

        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        self.lineEdit_price_sugar_result = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_price_sugar_result.setFont(font)
        self.lineEdit_price_sugar_result.setObjectName("lineEdit_price_sugar_result")
        self.horizontalLayout_2.addWidget(self.lineEdit_price_sugar_result)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_total = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_total.setFont(font)
        self.label_total.setStyleSheet("")
        self.label_total.setText("")
        self.label_total.setObjectName("label_total")
        self.verticalLayout.addWidget(self.label_total)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)





    def first_result(self):
        if self.lineEdit_price_pen.text() != 0:
            first_price = int(self.lineEdit_price_pen.text())
            total_first_price = first_price * self.spinBox.value()

            self.lineEdit_price_pen_result.setText(str(total_first_price))


    def second_result(self):
        if self.lineEdit_price_sugar.text() != 0:
            second_price = int(self.lineEdit_price_sugar.text())
            total_second_price = second_price * self.doubleSpinBox.value()

            self.lineEdit_price_sugar_result.setText(str(total_second_price))

            total_pen_price = int(self.lineEdit_price_pen_result.text())
            monto_total = total_pen_price + total_second_price

            self.label_total.setText(f'El Monto total es de: {monto_total}')



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Pen price:"))
        self.label_2.setText(_translate("Form", "Sugar price:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
