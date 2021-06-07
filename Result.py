from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResultPage(object):

    def openWindow(self):
        from Search import Ui_SearchPage
        self.window = QtWidgets.QDialog()
        self.ui = Ui_SearchPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        from Search import Ui_SearchPage
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 700)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.label_bg = QtWidgets.QLabel(Dialog)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.label_bg.setStyleSheet("background-image: url(:/newPrefix/BG-FB1.jpg);")
        self.label_bg.setText("")
        self.label_bg.setObjectName("label_bg")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 470, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(47, 67, 195);\n"
"color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(130, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(9, 13, 84);")
        self.label_1.setObjectName("label_1")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(400, 480, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(47, 67, 195);\n"
"color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.result_name = QtWidgets.QLabel(Dialog)
        self.result_name.setGeometry(QtCore.QRect(230, 200, 201, 16))
        self.result_name.setText("")
        self.result_name.setObjectName("result_name")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(400, 520, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(47, 67, 195);\n"
"color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 90, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(35)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(9, 13, 84);")
        self.label_2.setObjectName("label_2")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(440, 600, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.exit.setFont(font)
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.exit.setStyleSheet("border-radius : 10;\n"
"background-color: rgb(0,0,0);\n"
"color:rgb(255,255,255);")

        self.exit.setObjectName("exit")
        self.exit.clicked.connect(Dialog.close)

        self.result_cam_id = QtWidgets.QLabel(Dialog)
        self.result_cam_id.setGeometry(QtCore.QRect(190, 480, 161, 16))
        self.result_cam_id.setText("")
        self.result_cam_id.setObjectName("result_cam_id")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(390, 100, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 13, 84);")
        self.label_3.setObjectName("label_3")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(150, 600, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.back.setStyleSheet("QPushButton{\n"
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
        self.back.setObjectName("back")
        self.back.clicked.connect(Dialog.close)
        self.back.clicked.connect(self.openWindow)

        self.result_date = QtWidgets.QLabel(Dialog)
        self.result_date.setGeometry(QtCore.QRect(480, 520, 161, 16))
        self.result_date.setText("")
        self.result_date.setObjectName("result_date")
        self.result_time = QtWidgets.QLabel(Dialog)
        self.result_time.setGeometry(QtCore.QRect(480, 480, 161, 16))
        self.result_time.setText("")
        self.result_time.setObjectName("result_time")
        self.result_photo = QtWidgets.QGraphicsView(Dialog)
        self.result_photo.setGeometry(QtCore.QRect(230, 250, 201, 191))
        self.result_photo.setObjectName("result_photo")
        self.result_loc = QtWidgets.QLabel(Dialog)
        self.result_loc.setGeometry(QtCore.QRect(190, 520, 161, 16))
        self.result_loc.setText("")
        self.result_loc.setObjectName("result_loc")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 200, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(47, 67, 195);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 520, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(47, 67, 195);\n"
"color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Camera Id:"))
        self.label_1.setText(_translate("Dialog", "FACE"))
        self.label_6.setText(_translate("Dialog", "Time:"))
        self.label_8.setText(_translate("Dialog", "Date:"))
        self.label_2.setText(_translate("Dialog", "GRAB"))
        self.exit.setText(_translate("Dialog", "EXIT"))
        self.label_3.setText(_translate("Dialog", "RESULTS"))
        self.back.setText(_translate("Dialog", "BACK"))
        self.label_4.setText(_translate("Dialog", "Name:"))
        self.label_7.setText(_translate("Dialog", "Location:"))
import img_result_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ResultPage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())