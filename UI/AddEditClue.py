# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddEditClue.ui'
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
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 520)
        Dialog.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0.09 #6E0204,\n"
"    stop: 0.87 #9B5D61\n"
");")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 70, 341, 51))
        self.lineEdit.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 360, 181, 16))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 440, 162, 61))
        self.buttonBox.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 15px;\n"
"color: #FFE5E5;")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 91, 16))
        self.label.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 10, 271, 21))
        self.label_3.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"color: rgba(8, 8, 8, 0.66);\n"
"color: #FFE5E5;")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 380, 341, 41))
        self.comboBox.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 220, 341, 51))
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 200, 91, 16))
        self.label_4.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 300, 341, 51))
        self.lineEdit_3.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 280, 91, 16))
        self.label_5.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 130, 181, 16))
        self.label_2.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(30, 160, 121, 31))
        self.dateEdit.setStyleSheet(u"color: rgba(8, 8, 8, 0.66);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0443\u043b\u0438\u043a\u0438", None))
        self.lineEdit_2.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.lineEdit_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"id \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
    # retranslateUi

