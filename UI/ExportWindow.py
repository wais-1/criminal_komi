# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ExportWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QHBoxLayout, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(331, 266)
        Dialog.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0.09 #6E0204,\n"
"    stop: 0.87 #9B5D61\n"
");")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 210, 81, 41))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 311, 201))
        self.frame.setStyleSheet(u"background-color: none;")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"background-color: none;")
        self.verticalLayout = QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.frame1)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.25);\n"
"border-radius: 20px;")

        self.verticalLayout.addWidget(self.lineEdit)

        self.checkBox_2 = QCheckBox(self.frame1)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"background-color: none;")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.comboBox = QComboBox(self.frame1)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)


        self.horizontalLayout.addWidget(self.frame1)

        self.frame2 = QFrame(self.frame)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setStyleSheet(u"background-color: none;")
        self.verticalLayout_2 = QVBoxLayout(self.frame2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_4 = QRadioButton(self.frame2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"background-color: none;")

        self.verticalLayout_2.addWidget(self.radioButton_4)

        self.radioButton = QRadioButton(self.frame2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"background-color: none;")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.frame2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"background-color: none;")

        self.verticalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.frame2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"background-color: none;")

        self.verticalLayout_2.addWidget(self.radioButton_2)


        self.horizontalLayout.addWidget(self.frame2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0438", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u043e\u043b\u044c", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"PDF", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"CSV", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"JSON", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Excel", None))
    # retranslateUi

