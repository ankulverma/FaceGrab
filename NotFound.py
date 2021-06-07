from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NotFound(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(9, 13, 84);")
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(60, 80, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(9, 13, 84);")
        self.label_1.setObjectName("label_1")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(250, 210, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.okButton.setFont(font)
        self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.okButton.setStyleSheet("QPushButton{\n"
"border-radius : 10;\n"
"background-color: rgb(20,135,193);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(16,108,154);\n"
"color:rgb(249,253,254);\n"
"}\n"
"QpushButton:pressed{\n"
"background-color: rgb(rgb(17,116,175));\n"
"}\n"
"")
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(Dialog.close)

        self.label_bg = QtWidgets.QLabel(Dialog)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.label_bg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_bg.setText("")
        self.label_bg.setObjectName("label_bg")
        self.label_bg.raise_()
        self.label_2.raise_()
        self.label_1.raise_()
        self.okButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Person Not Found."))
        self.label_1.setText(_translate("Dialog", "SORRY !!"))
        self.okButton.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_NotFound()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
