# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DrinksWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Drinkswindow(object):

    def __init__(self, window, email):
        self.window = QtWidgets.QMainWindow()
        self.emailtxt1 = email

    def openCart(self):
        from cart import Ui_Cart
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Cart()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHome(self):
        # Drinkswindow.destroy()
        from foodsWindow import Ui_FoodMenuwindow
        self.window = QtWidgets.QMainWindow()
        self.emailtxt1 = self.user.text()
        self.ui = Ui_FoodMenuwindow(window="", email=self.emailtxt1)
        self.ui.setupUi(self.window)
        self.window.show()

    def openExtras(self):
        # FoodMenuwindow.close()
        from extrasWindow import Ui_Extraswindow

        self.emailtxt1 = self.user.text()

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Extraswindow(window="", email=self.emailtxt1)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Drinkswindow):
        Drinkswindow.setObjectName("Drinkswindow")
        Drinkswindow.resize(900, 650)
        self.centralwidget = QtWidgets.QWidget(Drinkswindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 170, 700))
        self.frame.setStyleSheet("background-color: rgb(51, 55, 53);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.drinksbtn_2 = QtWidgets.QPushButton(self.frame)
        self.drinksbtn_2.setGeometry(QtCore.QRect(10, 220, 151, 31))
        self.drinksbtn_2.setStyleSheet("background-color: rgb(154, 154, 154);\n"
"font: 75 14pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/New/icons8_takeaway_hot_drink_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drinksbtn_2.setIcon(icon)
        self.drinksbtn_2.setIconSize(QtCore.QSize(20, 20))
        self.drinksbtn_2.setObjectName("drinksbtn_2")
        self.Extrasbtn_2 = QtWidgets.QPushButton(self.frame)
        self.Extrasbtn_2.setGeometry(QtCore.QRect(10, 260, 151, 31))
        self.Extrasbtn_2.setStyleSheet("background-color: rgb(154, 154, 154);\n"
"font: 75 14pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/New/icons8_plus_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Extrasbtn_2.setIcon(icon1)
        self.Extrasbtn_2.setIconSize(QtCore.QSize(20, 20))
        self.Extrasbtn_2.setObjectName("Extrasbtn_2")
        self.cartbtn = QtWidgets.QPushButton(self.frame)
        self.cartbtn.setGeometry(QtCore.QRect(10, 300, 151, 31))
        self.cartbtn.setStyleSheet("background-color: rgb(154, 154, 154);\n"
"font: 75 14pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/New/icons8_Shopping_Cart_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cartbtn.setIcon(icon2)
        self.cartbtn.setIconSize(QtCore.QSize(20, 20))
        self.cartbtn.setObjectName("cartbtn")
        self.homebtn_2 = QtWidgets.QPushButton(self.frame)
        self.homebtn_2.setGeometry(QtCore.QRect(10, 180, 151, 31))
        self.homebtn_2.setStyleSheet("background-color: rgb(154, 154, 154);\n"
"font: 75 14pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 15px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/New/icons8_home_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn_2.setIcon(icon3)
        self.homebtn_2.setIconSize(QtCore.QSize(20, 20))
        self.homebtn_2.setObjectName("homebtn_2")
        self.profile2 = QtWidgets.QPushButton(self.frame)
        self.profile2.setGeometry(QtCore.QRect(10, 540, 151, 31))
        self.profile2.setStyleSheet("background-color: rgb(154, 154, 154);\n"
"font: 75 14pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Pictures/New/icons8_user_male_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile2.setIcon(icon4)
        self.profile2.setIconSize(QtCore.QSize(20, 20))
        self.profile2.setObjectName("profile2")
        self.logoutbtn = QtWidgets.QPushButton(self.frame)
        self.logoutbtn.setGeometry(QtCore.QRect(10, 580, 151, 31))
        self.logoutbtn.setStyleSheet("background-color: rgb(154, 154, 154);\n"
"font: 75 14pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Pictures/New/icons8_logout_rounded_left_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutbtn.setIcon(icon5)
        self.logoutbtn.setIconSize(QtCore.QSize(20, 20))
        self.logoutbtn.setObjectName("logoutbtn")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(30, 30, 111, 101))
        self.label_29.setStyleSheet("border-radius: 50px;\n"
"\n"
"")
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("Pictures/New/circle-cropped.png"))
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(180, 10, 711, 641))
        self.frame_10.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_27 = QtWidgets.QLabel(self.frame_10)
        self.label_27.setGeometry(QtCore.QRect(260, -30, 191, 191))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("Pictures/New/Logo.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label_3 = QtWidgets.QLabel(self.frame_10)
        self.label_3.setGeometry(QtCore.QRect(300, 100, 111, 31))
        self.label_3.setStyleSheet("font: 75 20pt \"Arial\";\n"
"color: rgb(198, 156, 109);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.user = QtWidgets.QLabel(self.frame_10)
        self.user.setGeometry(QtCore.QRect(530, 80, 151, 31))
        self.user.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(198, 156, 109);")
        self.user.setText("")
        self.user.setAlignment(QtCore.Qt.AlignCenter)
        self.user.setObjectName("user")
        self.profile = QtWidgets.QPushButton(self.frame_10)
        self.profile.setGeometry(QtCore.QRect(610, 20, 51, 51))
        self.profile.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"\n"
"\n"
"")
        self.profile.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Pictures/New/icons8_male_user_60px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile.setIcon(icon6)
        self.profile.setIconSize(QtCore.QSize(120, 120))
        self.profile.setObjectName("profile")
        self.frame_2 = QtWidgets.QFrame(self.frame_10)
        self.frame_2.setGeometry(QtCore.QRect(90, 140, 141, 231))
        self.frame_2.setStyleSheet("background-color: rgb(51, 55, 53);\n"
"broder-radius: 25px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.label_30 = QtWidgets.QLabel(self.frame_2)
        self.label_30.setGeometry(QtCore.QRect(0, 10, 140, 121))
        self.label_30.setStyleSheet("image: url(:/newPrefix/social-share.jpg);")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_2)
        self.label_31.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_31.setStyleSheet("font: 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame_2)
        self.label_32.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label_32.setStyleSheet("font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.cartbtn_2 = QtWidgets.QPushButton(self.frame_2)
        self.cartbtn_2.setGeometry(QtCore.QRect(70, 190, 61, 31))
        self.cartbtn_2.setStyleSheet("background-color: rgb(220, 166, 88);\n"
"font: 75 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.cartbtn_2.setObjectName("cartbtn_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 190, 51, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Calibri\";\n"
"border-radius: 15px;")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.frame_3 = QtWidgets.QFrame(self.frame_10)
        self.frame_3.setGeometry(QtCore.QRect(290, 140, 141, 231))
        self.frame_3.setStyleSheet("background-color: rgb(51, 55, 53);\n"
"broder-radius: 25px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.label_39 = QtWidgets.QLabel(self.frame_3)
        self.label_39.setGeometry(QtCore.QRect(0, 10, 141, 121))
        self.label_39.setStyleSheet("border-image: url(:/newPrefix/za1hymxhctgxs4sra4mi.jpg);\n"
"")
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_3)
        self.label_40.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_40.setStyleSheet("font: 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.frame_3)
        self.label_41.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label_41.setStyleSheet("font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.cartbtn_5 = QtWidgets.QPushButton(self.frame_3)
        self.cartbtn_5.setGeometry(QtCore.QRect(70, 190, 61, 31))
        self.cartbtn_5.setStyleSheet("background-color: rgb(220, 166, 88);\n"
"font: 75 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.cartbtn_5.setObjectName("cartbtn_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 190, 51, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Calibri\";\n"
"border-radius: 15px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_10)
        self.frame_4.setGeometry(QtCore.QRect(490, 140, 141, 231))
        self.frame_4.setStyleSheet("background-color: rgb(51, 55, 53);\n"
"broder-radius: 25px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(3)
        self.frame_4.setObjectName("frame_4")
        self.label_42 = QtWidgets.QLabel(self.frame_4)
        self.label_42.setGeometry(QtCore.QRect(0, 10, 141, 121))
        self.label_42.setStyleSheet("image: url(:/newPrefix/jazz-x-nestle.png);")
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_4)
        self.label_43.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_43.setStyleSheet("font: 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.frame_4)
        self.label_44.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label_44.setStyleSheet("font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.cartbtn_6 = QtWidgets.QPushButton(self.frame_4)
        self.cartbtn_6.setGeometry(QtCore.QRect(70, 190, 61, 31))
        self.cartbtn_6.setStyleSheet("background-color: rgb(220, 166, 88);\n"
"font: 75 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.cartbtn_6.setObjectName("cartbtn_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 190, 51, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Calibri\";\n"
"border-radius: 15px;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.frame_5 = QtWidgets.QFrame(self.frame_10)
        self.frame_5.setGeometry(QtCore.QRect(90, 380, 141, 231))
        self.frame_5.setStyleSheet("background-color: rgb(51, 55, 53);\n"
"broder-radius: 25px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(3)
        self.frame_5.setObjectName("frame_5")
        self.label_33 = QtWidgets.QLabel(self.frame_5)
        self.label_33.setGeometry(QtCore.QRect(0, 10, 140, 121))
        self.label_33.setStyleSheet("image: url(:/newPrefix/images.jpg);")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_5)
        self.label_34.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_34.setStyleSheet("font: 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_5)
        self.label_35.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label_35.setStyleSheet("font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.cartbtn_3 = QtWidgets.QPushButton(self.frame_5)
        self.cartbtn_3.setGeometry(QtCore.QRect(70, 190, 61, 31))
        self.cartbtn_3.setStyleSheet("background-color: rgb(220, 166, 88);\n"
"font: 75 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.cartbtn_3.setObjectName("cartbtn_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 190, 51, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Calibri\";\n"
"border-radius: 15px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_10)
        self.frame_6.setGeometry(QtCore.QRect(290, 380, 141, 231))
        self.frame_6.setStyleSheet("background-color: rgb(51, 55, 53);\n"
"broder-radius: 25px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setLineWidth(3)
        self.frame_6.setObjectName("frame_6")
        self.label_36 = QtWidgets.QLabel(self.frame_6)
        self.label_36.setGeometry(QtCore.QRect(0, 10, 140, 121))
        self.label_36.setStyleSheet("image: url(:/newPrefix/image_1583158709874_water.jpg);")
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame_6)
        self.label_37.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_37.setStyleSheet("font: 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame_6)
        self.label_38.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label_38.setStyleSheet("font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.cartbtn_4 = QtWidgets.QPushButton(self.frame_6)
        self.cartbtn_4.setGeometry(QtCore.QRect(70, 190, 61, 31))
        self.cartbtn_4.setStyleSheet("background-color: rgb(220, 166, 88);\n"
"font: 75 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.cartbtn_4.setObjectName("cartbtn_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 190, 51, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Calibri\";\n"
"border-radius: 15px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_10)
        self.frame_7.setGeometry(QtCore.QRect(490, 380, 141, 231))
        self.frame_7.setStyleSheet("background-color: rgb(51, 55, 53);\n"
"broder-radius: 25px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setLineWidth(3)
        self.frame_7.setObjectName("frame_7")
        self.label_45 = QtWidgets.QLabel(self.frame_7)
        self.label_45.setGeometry(QtCore.QRect(0, 10, 140, 121))
        self.label_45.setStyleSheet("image: url(:/newPrefix/89f2147916973d7fa6a4df3ecbfcff99.png);")
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.frame_7)
        self.label_46.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_46.setStyleSheet("font: 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.frame_7)
        self.label_47.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label_47.setStyleSheet("font: 10pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.cartbtn_7 = QtWidgets.QPushButton(self.frame_7)
        self.cartbtn_7.setGeometry(QtCore.QRect(70, 190, 61, 31))
        self.cartbtn_7.setStyleSheet("background-color: rgb(220, 166, 88);\n"
"font: 75 12pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.cartbtn_7.setObjectName("cartbtn_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 190, 51, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Calibri\";\n"
"border-radius: 15px;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        Drinkswindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Drinkswindow)
        self.statusbar.setObjectName("statusbar")
        Drinkswindow.setStatusBar(self.statusbar)

        self.cartbtn_2.pressed.connect(self.addPepsiToCart)
        self.cartbtn_5.pressed.connect(self.addFantaToCart)
        self.cartbtn_6.pressed.connect(self.addNestleToCart)
        self.cartbtn_3.pressed.connect(self.addRedBullToCart)
        self.cartbtn_4.pressed.connect(self.addWaterToCart)
        self.cartbtn_7.pressed.connect(self.addBarbicanToCart)

        self.Extrasbtn_2.pressed.connect(self.openExtras)
        self.homebtn_2.pressed.connect(self.openHome)
        self.cartbtn.pressed.connect(self.openCart)

        self.retranslateUi(Drinkswindow)
        QtCore.QMetaObject.connectSlotsByName(Drinkswindow)

    def addPepsiToCart(self):
        name = self.label_31.text()
        price = 20
        amount = int(self.lineEdit.text())
        conn = sqlite3.connect("restaurant.db", isolation_level=None)
        cursor = conn.cursor()
        total = amount * price
        taxed_total = total + (total * 0.12)

        cursor.execute(
            "INSERT INTO `cart` (item_name, quantity, price, total, taxed_total) VALUES (?, ?, ?, ?, ?)",
            (name, str(amount), str(price), str(total), str(taxed_total)))
        conn.commit()

    def addFantaToCart(self):
        name = self.label_40.text()
        price = 20
        amount = int(self.lineEdit_4.text())
        conn = sqlite3.connect("restaurant.db", isolation_level=None)
        cursor = conn.cursor()
        total = amount * price
        taxed_total = total + (total * 0.12)

        cursor.execute(
            "INSERT INTO `cart` (item_name, quantity, price, total, taxed_total) VALUES (?, ?, ?, ?, ?)",
            (name, str(amount), str(price), str(total), str(taxed_total)))
        conn.commit()

    def addNestleToCart(self):
        name = self.label_43.text()
        price = 15
        amount = int(self.lineEdit_5.text())
        conn = sqlite3.connect("restaurant.db", isolation_level=None)
        cursor = conn.cursor()
        total = amount * price
        taxed_total = total + (total * 0.12)

        cursor.execute(
            "INSERT INTO `cart` (item_name, quantity, price, total, taxed_total) VALUES (?, ?, ?, ?, ?)",
            (name, str(amount), str(price), str(total), str(taxed_total)))
        conn.commit()

    def addRedBullToCart(self):
        name = self.label_34.text()
        price = 120
        amount = int(self.lineEdit_2.text())
        conn = sqlite3.connect("restaurant.db", isolation_level=None)
        cursor = conn.cursor()
        total = amount * price
        taxed_total = total + (total * 0.12)

        cursor.execute(
            "INSERT INTO `cart` (item_name, quantity, price, total, taxed_total) VALUES (?, ?, ?, ?, ?)",
            (name, str(amount), str(price), str(total), str(taxed_total)))
        conn.commit()

    def addWaterToCart(self):
        name = self.label_37.text()
        price = 20
        amount = int(self.lineEdit_3.text())
        conn = sqlite3.connect("restaurant.db", isolation_level=None)
        cursor = conn.cursor()
        total = amount * price
        taxed_total = total + (total * 0.12)

        cursor.execute(
            "INSERT INTO `cart` (item_name, quantity, price, total, taxed_total) VALUES (?, ?, ?, ?, ?)",
            (name, str(amount), str(price), str(total), str(taxed_total)))
        conn.commit()

    def addBarbicanToCart(self):
        name = self.label_46.text()
        price = 70
        amount = int(self.lineEdit_6.text())
        conn = sqlite3.connect("restaurant.db", isolation_level=None)
        cursor = conn.cursor()
        total = amount * price
        taxed_total = total + (total * 0.12)

        cursor.execute(
            "INSERT INTO `cart` (item_name, quantity, price, total, taxed_total) VALUES (?, ?, ?, ?, ?)",
            (name, str(amount), str(price), str(total), str(taxed_total)))
        conn.commit()


    def retranslateUi(self, Drinkswindow):
        _translate = QtCore.QCoreApplication.translate
        Drinkswindow.setWindowTitle(_translate("Drinkswindow", "Drinks"))
        self.drinksbtn_2.setText(_translate("Drinkswindow", "Drinks"))
        self.Extrasbtn_2.setText(_translate("Drinkswindow", "Extras"))
        self.cartbtn.setText(_translate("Drinkswindow", "Cart"))
        self.homebtn_2.setText(_translate("Drinkswindow", "Home"))
        self.profile2.setText(_translate("Drinkswindow", "Profile"))
        self.logoutbtn.setText(_translate("Drinkswindow", "Log out"))
        self.label_3.setText(_translate("Drinkswindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Drinks Menu</span></p></body></html>"))
        self.label_31.setText(_translate("Drinkswindow", "Pepsi"))
        self.label_32.setText(_translate("Drinkswindow", "20 AFS"))
        self.cartbtn_2.setText(_translate("Drinkswindow", "Add"))
        self.lineEdit.setPlaceholderText(_translate("Drinkswindow", "Amount"))
        self.label_40.setText(_translate("Drinkswindow", "Fanta"))
        self.label_41.setText(_translate("Drinkswindow", "20 AFS"))
        self.cartbtn_5.setText(_translate("Drinkswindow", "Add"))
        self.lineEdit_4.setPlaceholderText(_translate("Drinkswindow", "Amount"))
        self.label_43.setText(_translate("Drinkswindow", "Nestle Juice"))
        self.label_44.setText(_translate("Drinkswindow", "15 AFS"))
        self.cartbtn_6.setText(_translate("Drinkswindow", "Add"))
        self.lineEdit_5.setPlaceholderText(_translate("Drinkswindow", "Amount"))
        self.label_34.setText(_translate("Drinkswindow", "Redbull"))
        self.label_35.setText(_translate("Drinkswindow", "120 AFS"))
        self.cartbtn_3.setText(_translate("Drinkswindow", "Add"))
        self.lineEdit_2.setPlaceholderText(_translate("Drinkswindow", "Amount"))
        self.label_37.setText(_translate("Drinkswindow", "Water"))
        self.label_38.setText(_translate("Drinkswindow", "20 AFS"))
        self.cartbtn_4.setText(_translate("Drinkswindow", "Add"))
        self.lineEdit_3.setPlaceholderText(_translate("Drinkswindow", "Amount"))
        self.label_46.setText(_translate("Drinkswindow", "Barbican"))
        self.label_47.setText(_translate("Drinkswindow", "70 AFS"))
        self.cartbtn_7.setText(_translate("Drinkswindow", "Add"))
        self.lineEdit_6.setPlaceholderText(_translate("Drinkswindow", "Amount"))
        self.user.setText(_translate("Drinkswindow", self.emailtxt1))
import images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Drinkswindow = QtWidgets.QMainWindow()
    ui = Ui_Drinkswindow(window="", email="")
    ui.setupUi(Drinkswindow)
    Drinkswindow.show()
    sys.exit(app.exec_())
