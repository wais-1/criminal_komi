# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddEditCrime.ui'
##
## Created by: Qt User Interface Compiler version 6.10.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 850)
        Dialog.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0.09 #6E0204,\n"
"    stop: 0.87 #9B5D61\n"
");")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 10, 271, 21))
        self.label_3.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"color: rgba(8, 8, 8, 0.66);\n"
"color: #FFE5E5;")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 70, 341, 51))
        self.lineEdit.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 58, 16))
        self.label.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 130, 181, 16))
        self.label_2.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 150, 341, 51))
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 230, 341, 51))
        self.lineEdit_3.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 210, 181, 16))
        self.label_4.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 290, 181, 16))
        self.label_5.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 390, 341, 41))
        self.comboBox.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 370, 181, 16))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 440, 181, 16))
        self.label_7.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(30, 460, 341, 41))
        self.comboBox_2.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 510, 181, 16))
        self.label_8.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.comboBox_3 = QComboBox(Dialog)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(30, 530, 341, 41))
        self.comboBox_3.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 600, 341, 51))
        self.lineEdit_5.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 580, 181, 16))
        self.label_9.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 760, 162, 61))
        self.buttonBox.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 15px;\n"
"color: #FFE5E5;")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 680, 100, 51))
        self.pushButton.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 15px;\n"
"color: #FFE5E5;")
        self.lineEdit_7 = QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(30, 680, 221, 51))
        self.lineEdit_7.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 660, 351, 16))
        self.label_10.setStyleSheet(u"background-color: none;\n"
"font-size: 12pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 730, 291, 16))
        self.label_11.setStyleSheet(u"background-color: none;\n"
"font-size: 12pt;\n"
"color: rgba(255, 8, 8, 0.66);")
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(30, 320, 121, 31))
        self.dateEdit.setStyleSheet(u"color: rgba(8, 8, 8, 0.66);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041c\u0438\u043d\u0438 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0438", None))
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u0441\u0442\u0430\u0442\u044c\u0438", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0438\u0448\u0435\u0441\u0442\u0432\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u043e\u0441\u0442\u0438", None))
        self.lineEdit_5.setText("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"id \u043c\u0435\u0441\u0442\u0430 \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.lineEdit_7.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0414\u043b\u044f \u041e\u0411\u041d\u041e\u0412\u041b\u0415\u041d\u0418\u042f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 id \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 id \u0434\u043b\u044f \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f", None))
    # retranslateUi

