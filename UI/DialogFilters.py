# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogFilters.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 770)
        Dialog.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0.09 #6E0204,\n"
"    stop: 0.87 #9B5D61\n"
");")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 10, 91, 21))
        self.label_5.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"color: rgba(8, 8, 8, 0.66);\n"
"color: #FFE5E5;")
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(30, 110, 110, 22))
        self.dateEdit.setDate(QDate(2026, 1, 1))
        self.dateEdit_2 = QDateEdit(Dialog)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(180, 110, 110, 22))
        self.dateEdit_2.setDate(QDate(2026, 1, 1))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 110, 16, 16))
        self.label.setStyleSheet(u"background-color: none;\n"
"font-size: 16pt;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 201, 16))
        self.label_2.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 150, 201, 16))
        self.label_3.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.cb_crime_type = QComboBox(Dialog)
        self.cb_crime_type.setObjectName(u"cb_crime_type")
        self.cb_crime_type.setGeometry(QRect(30, 180, 261, 32))
        self.cb_crime_type.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 230, 201, 16))
        self.label_4.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.line_district = QLineEdit(Dialog)
        self.line_district.setObjectName(u"line_district")
        self.line_district.setGeometry(QRect(30, 260, 261, 31))
        self.line_district.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 0 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.line_district.setEchoMode(QLineEdit.EchoMode.Normal)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 40, 201, 31))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"font-size: 18pt;\n"
"text-transform: uppercase;")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 310, 201, 31))
        self.label_7.setStyleSheet(u"background-color: none;\n"
"font-size: 18pt;\n"
"text-transform: uppercase;")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 350, 201, 16))
        self.label_8.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 430, 201, 16))
        self.label_9.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.cb_status_case = QComboBox(Dialog)
        self.cb_status_case.setObjectName(u"cb_status_case")
        self.cb_status_case.setGeometry(QRect(30, 460, 261, 32))
        self.cb_status_case.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.cb_investigator = QComboBox(Dialog)
        self.cb_investigator.setObjectName(u"cb_investigator")
        self.cb_investigator.setGeometry(QRect(30, 380, 261, 32))
        self.cb_investigator.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 510, 201, 31))
        self.label_10.setStyleSheet(u"background-color: none;\n"
"font-size: 18pt;\n"
"text-transform: uppercase;")
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 550, 201, 16))
        self.label_11.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 630, 201, 16))
        self.label_12.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.cb_criminal_status = QComboBox(Dialog)
        self.cb_criminal_status.setObjectName(u"cb_criminal_status")
        self.cb_criminal_status.setGeometry(QRect(30, 660, 261, 32))
        self.cb_criminal_status.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 700, 111, 51))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 15px;\n"
"color: #FFE5E5;")
        self.cb_criminal = QComboBox(Dialog)
        self.cb_criminal.setObjectName(u"cb_criminal")
        self.cb_criminal.setGeometry(QRect(30, 580, 261, 32))
        self.cb_criminal.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 700, 111, 51))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 15px;\n"
"color: #FFE5E5;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f:", None))
        self.cb_crime_type.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0439\u043e\u043d:", None))
        self.line_district.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0439\u043e\u043d \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044e:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e \u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044e:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0421\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0434\u0435\u043b\u0430:", None))
        self.cb_status_case.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u0430\u0442\u0443\u0441 \u0434\u0435\u043b\u0430", None))
        self.cb_investigator.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043d\u0438\u043a\u0443:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u0424\u0418\u041e \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043d\u0438\u043a\u0430:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.cb_criminal_status.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u043f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.cb_criminal.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043d\u0438\u043a\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0441\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
    # retranslateUi

