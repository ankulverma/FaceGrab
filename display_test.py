from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        self.result_photo = QtWidgets.QLabel(Dialog)
        self.result_photo.setGeometry(QtCore.QRect(230, 250, 201, 191))
        id="0206cs181118"
        #
        img = "ImageSourceDirectory/" + id + ".jpg"
        self.result_photo.setPixmap(QtGui.QPixmap(img))
        self.result_photo.setScaledContents(True)
        #
        self.result_photo.setObjectName("result_photo")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
