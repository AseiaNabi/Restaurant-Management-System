# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cart.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3
import datetime as date
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication


class Ui_Cart(object):
    def setupUi(self, Cart):
        Cart.setObjectName("Cart")
        Cart.resize(602, 620)
        self.frame_11 = QtWidgets.QFrame(Cart)
        self.frame_11.setGeometry(QtCore.QRect(10, 10, 581, 601))
        self.frame_11.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_28 = QtWidgets.QLabel(self.frame_11)
        self.label_28.setGeometry(QtCore.QRect(200, -30, 191, 191))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("Pictures/New/Logo.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        self.label_4.setGeometry(QtCore.QRect(250, 100, 91, 31))
        self.label_4.setStyleSheet("font: 75 20pt \"Arial\";\n"
"color: rgb(198, 156, 109);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.frame_17 = QtWidgets.QFrame(self.frame_11)
        self.frame_17.setGeometry(QtCore.QRect(10, 130, 561, 461))
        self.frame_17.setStyleSheet("background-color: rgb(51, 55, 53);\n"
"border-radius: 15px;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setLineWidth(3)
        self.frame_17.setObjectName("frame_17")
        self.proceedbtn = QtWidgets.QPushButton(self.frame_17)
        self.proceedbtn.setGeometry(QtCore.QRect(290, 420, 181, 31))
        self.proceedbtn.setStyleSheet("background-color: rgb(220, 166, 88);\n"
"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.proceedbtn.setObjectName("proceedbtn")
        self.label_11 = QtWidgets.QLabel(self.frame_17)
        self.label_11.setGeometry(QtCore.QRect(220, 360, 61, 21))
        self.label_11.setStyleSheet("font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.total = QtWidgets.QLabel(self.frame_17)
        self.total.setGeometry(QtCore.QRect(300, 360, 91, 21))
        self.total.setStyleSheet("font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.total.setObjectName("total")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_17)
        self.tableWidget.setGeometry(QtCore.QRect(10, 11, 541, 291))
        self.tableWidget.setStyleSheet("font: 10pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget.setRowCount(15)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.romovebtn = QtWidgets.QPushButton(self.frame_17)
        self.romovebtn.setGeometry(QtCore.QRect(90, 420, 181, 31))
        self.romovebtn.setStyleSheet("background-color: rgb(220, 166, 88);\n"
"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.romovebtn.setObjectName("romovebtn")
        self.label_13 = QtWidgets.QLabel(self.frame_17)
        self.label_13.setGeometry(QtCore.QRect(20, 310, 141, 21))
        self.label_13.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_17)
        self.label_14.setGeometry(QtCore.QRect(240, 310, 111, 21))
        self.label_14.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_17)
        self.label_15.setGeometry(QtCore.QRect(430, 310, 111, 21))
        self.label_15.setStyleSheet("font: 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")

        self.DisplayData()
        self.romovebtn.pressed.connect(self.removeItem)
        self.proceedbtn.pressed.connect(self.proceed)
        self.retranslateUi(Cart)
        QtCore.QMetaObject.connectSlotsByName(Cart)

    def DisplayData(self):
        global conn, cursor
        conn = sqlite3.connect("restaurant.db", isolation_level=None)
        cursor = conn.cursor()
        query = "SELECT * FROM cart"

        items_list = []
        for row in cursor.execute(query):
            items_list.append(row[5])

        test_list = [float(i) for i in items_list]
        sum_taxed = str(sum(test_list))
        total = "" + sum_taxed + " Afs"
        self.total.repaint()
        QApplication.processEvents()
        self.total.setText(total)

        tableRow = 0
        for row in cursor.execute(query):
            self.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(row[5]))
            tableRow += 1
        cursor.close()
        conn.close()

    def removeItem(self):
        row = self.tableWidget.currentRow()
        conn = sqlite3.connect("restaurant.db", isolation_level=None)
        cursor = conn.cursor()
        if row > -1:
            item_name = str(self.tableWidget.item(row, 0).text())
            print(item_name)

            sql_update_query = """DELETE FROM cart where item_name = ?"""
            cursor.execute(sql_update_query, (item_name,))
            conn.commit()
            cursor.close()
            conn.close()
            self.tableWidget.removeRow(row)

    def proceed(self):
        self.DisplayData()

        conn = sqlite3.connect("restaurant.db", isolation_level=None)
        cursor = conn.cursor()
        query = "SELECT * FROM cart"

        # today = date.date.today()
        today = '2021-05-27'

        items_list2 = []
        for row in cursor.execute(query):
            items_list2.append(row[1])
            items = ", ".join(items_list2)

        items_list1 = []
        for row in cursor.execute(query):
            items_list1.append(row[4])

        test_list1 = [float(i) for i in items_list1]
        sum_total = sum(test_list1)

        items_list = []
        for row in cursor.execute(query):
            items_list.append(row[5])

        test_list = [float(i) for i in items_list]
        sum_taxed = sum(test_list)

        net_profit = sum_taxed - sum_total

        cursor.execute(
            "INSERT INTO `orders` (items, total, net_profit, date) VALUES (?, ?, ?, ?)",
            (str(items), str(sum_total), str(net_profit), str(today)))

        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText("Order is placed. Cart will now be emptied!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

        cursor.execute('DELETE FROM cart;', )

        cursor.close()
        conn.close()

    def retranslateUi(self, Cart):
        _translate = QtCore.QCoreApplication.translate
        Cart.setWindowTitle(_translate("Cart", "Form"))
        self.label_4.setText(_translate("Cart", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cart Items</span></p></body></html>"))
        self.proceedbtn.setText(_translate("Cart", "Proceed"))
        self.label_11.setText(_translate("Cart", "Total :"))
        self.total.setText(_translate("Cart", ""))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Cart", "Item"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Cart", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Cart", "Price Per Unit"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Cart", "Total"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Cart", "Taxed Total"))
        self.romovebtn.setText(_translate("Cart", "Remove"))
        self.label_13.setText(_translate("Cart", "Tex on Food Items: 6%"))
        self.label_14.setText(_translate("Cart", "Tex on Drinks: 12%"))
        self.label_15.setText(_translate("Cart", "Tex on Extra: 21%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cart = QtWidgets.QWidget()
    ui = Ui_Cart()
    ui.setupUi(Cart)
    Cart.show()
    sys.exit(app.exec_())