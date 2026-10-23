# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddEditRecord.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateTimeEdit, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 610)
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
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 10, 291, 21))
        self.label_3.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"color: rgba(8, 8, 8, 0.66);\n"
"color: #FFE5E5;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 130, 181, 16))
        self.label_2.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 300, 341, 51))
        self.lineEdit_4.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 280, 181, 16))
        self.label_5.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 101, 16))
        self.label.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.dateTimeEdit = QDateTimeEdit(Dialog)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(30, 160, 194, 22))
        self.dateTimeEdit.setStyleSheet(u"color: rgba(8, 8, 8, 0.66);")
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 220, 341, 51))
        self.lineEdit_5.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 200, 181, 16))
        self.label_8.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 360, 181, 16))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.lineEdit_6 = QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(30, 380, 341, 51))
        self.lineEdit_6.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.lineEdit_7 = QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(30, 460, 341, 51))
        self.lineEdit_7.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 440, 181, 16))
        self.label_7.setStyleSheet(u"background-color: none;\n"
"font-size: 10pt;\n"
"color: rgba(8, 8, 8, 0.66);")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(110, 530, 162, 51))
        self.buttonBox.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 15px;\n"
"color: #FFE5E5;")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b\u0430 \u0434\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f", None))
        self.lineEdit_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041f\u0443\u0442\u044c \u043a \u0432\u0438\u0434\u0435\u043e \u0444\u0430\u0439\u043b\u0443", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u043a\u0430\u0437\u0430\u043d\u0438\u0439", None))
        self.lineEdit_5.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u041f\u0443\u0442\u044c \u043a \u0430\u0443\u0434\u0438\u043e \u0444\u0430\u0439\u043b\u0443", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"id \u043f\u043e\u0441\u0442\u0440\u0430\u0434\u0430\u0432\u0448\u0435\u0433\u043e", None))
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"id \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044f", None))
    # retranslateUi

