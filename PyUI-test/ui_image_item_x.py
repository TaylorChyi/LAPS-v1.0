# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/ui_image_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Wid_Image_Item(object):
    def setupUi(self, Wid_Image_Item):
        Wid_Image_Item.setObjectName("Wid_Image_Item")
        Wid_Image_Item.resize(207, 228)
        self.verticalLayout = QtWidgets.QVBoxLayout(Wid_Image_Item)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Wid_Image_Item)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(Wid_Image_Item)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Wid_Image_Item)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Wid_Image_Item)
        QtCore.QMetaObject.connectSlotsByName(Wid_Image_Item)

    def retranslateUi(self, Wid_Image_Item):
        _translate = QtCore.QCoreApplication.translate
        Wid_Image_Item.setWindowTitle(_translate("Wid_Image_Item", "Form"))
        self.pushButton.setText(_translate("Wid_Image_Item", "删除"))
        self.label_2.setText(_translate("Wid_Image_Item", "图片名.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wid_Image_Item = QtWidgets.QWidget()
    ui = Ui_Wid_Image_Item()
    ui.setupUi(Wid_Image_Item)
    Wid_Image_Item.show()
    sys.exit(app.exec_())