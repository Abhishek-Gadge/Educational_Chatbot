# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatbotUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("EDUCATIONAL CHATBOT")
        MainWindow.resize(1379, 717)
        self.ChatbotGUI = QtWidgets.QWidget(MainWindow)
        self.ChatbotGUI.setObjectName("ChatbotGUI")

        self.label = QtWidgets.QLabel(self.ChatbotGUI)
        self.label.setGeometry(QtCore.QRect(0, 0, 1380, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("final_project\\background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.ChatbotGUI)
        self.label_2.setGeometry(QtCore.QRect(6, -8, 201, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("final_project\\initial.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.ChatbotGUI)
        self.label_3.setGeometry(QtCore.QRect(6, 570, 161, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("final_project\\Aqua.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.ChatbotGUI)
        self.label_4.setGeometry(QtCore.QRect(1176, 12, 181, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("final_project\\date.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.ChatbotGUI)
        self.label_5.setGeometry(QtCore.QRect(1220, 550, 121, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("final_project\\date.png"))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.ChatbotGUI)
        self.label_6.setGeometry(QtCore.QRect(1220, 620, 121, 71))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("final_project\\date.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.ChatbotGUI)
        self.label_7.setGeometry(QtCore.QRect(1100, 620, 121, 71))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("final_project\\date.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_6")

        self.label_8 = QtWidgets.QLabel(self.ChatbotGUI)
        self.label_8.setGeometry(QtCore.QRect(1100, 550, 121, 71))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("final_project\\date.png"))
        self.label_8.setObjectName("label_8")

        self.pushButton = QtWidgets.QPushButton(self.ChatbotGUI)
        self.pushButton.setGeometry(QtCore.QRect(1240, 560, 91, 41))
        self.pushButton.setStyleSheet("color: rgb(5, 251, 255);\n"
"background-color:transparent;\n"
"border-radius:none;")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.ChatbotGUI)
        self.pushButton_2.setGeometry(QtCore.QRect(1234, 632, 91, 41))
        self.pushButton_2.setStyleSheet("color: rgb(5, 251, 255);\n"
"background-color:transparent;\n"
"border-radius:none;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.ChatbotGUI)
        self.pushButton_3.setGeometry(QtCore.QRect(1114, 560, 91, 41))
        self.pushButton_3.setStyleSheet("color: rgb(5, 251, 255);\n"
"background-color:transparent;\n"
"border-radius:none;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.ChatbotGUI)
        self.pushButton_4.setGeometry(QtCore.QRect(1114, 632, 91, 41))
        self.pushButton_4.setStyleSheet("color: rgb(5, 251, 255);\n"
"background-color:transparent;\n"
"border-radius:none;")
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.date = QtWidgets.QTextBrowser(self.ChatbotGUI)
        self.date.setGeometry(QtCore.QRect(1200, 30, 131, 41))
        self.date.setStyleSheet("color: rgb(5, 251, 255);\n"
"border-color: rgb(39, 255, 255);\n"
"background-color:transparent;\n"
"border-radius:none;")
        self.date.setObjectName("date")

        self.input_text = QtWidgets.QTextBrowser(self.ChatbotGUI)
        self.input_text.setGeometry(QtCore.QRect(735, 140, 441, 111))
        self.input_text.setStyleSheet("color: rgb(5, 251, 255);\n"
"border-color: rgb(39, 255, 255);\n"
"background-color:transparent;\n"
"border-color: rgb(11, 251, 255);")
        self.input_text.setObjectName("input_text")


        self.output_text = QtWidgets.QTextBrowser(self.ChatbotGUI)
        self.output_text.setGeometry(QtCore.QRect(190, 330, 651, 181))
        self.output_text.setStyleSheet("color: rgb(5, 251, 255);\n"
"background-color:transparent;\n"
"border-color: rgb(24, 255, 248);")
        self.output_text.setObjectName("output_text")

        
        
        MainWindow.setCentralWidget(self.ChatbotGUI)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_3.setText(_translate("MainWindow", "Take Note"))
        self.pushButton_4.setText(_translate("MainWindow", "Text Bot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
