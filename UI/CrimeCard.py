# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CrimeCard.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(561, 200)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 541, 153))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_img = QLabel(self.widget)
        self.lbl_img.setObjectName(u"lbl_img")
        self.lbl_img.setStyleSheet(u"background-color: #000000;")

        self.horizontalLayout_3.addWidget(self.lbl_img)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_name = QLabel(self.widget)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;")

        self.verticalLayout.addWidget(self.lbl_name)

        self.lbl_mini_descr = QLabel(self.widget)
        self.lbl_mini_descr.setObjectName(u"lbl_mini_descr")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_mini_descr.sizePolicy().hasHeightForWidth())
        self.lbl_mini_descr.setSizePolicy(sizePolicy)
        self.lbl_mini_descr.setStyleSheet(u"background-color: none;\n"
"font-size: 16pt;")
        self.lbl_mini_descr.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lbl_mini_descr.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_mini_descr)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_edit = QPushButton(self.widget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_edit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #35451A;\n"
"padding: 7px;\n"
"color: #FFE5E5;")

        self.horizontalLayout.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.widget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #9C0000;\n"
"padding: 7px;\n"
"color: #FFE5E5;")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.btn_read = QPushButton(self.widget)
        self.btn_read.setObjectName(u"btn_read")
        self.btn_read.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_read.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 15px;\n"
"color: #FFE5E5;")

        self.horizontalLayout_2.addWidget(self.btn_read)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_img.setText("")
        self.lbl_name.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0430\u0442\u044c\u0438", None))
        self.lbl_mini_descr.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u041c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u041c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u041c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u041c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u041c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.btn_edit.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_delete.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_read.setText(QCoreApplication.translate("Form", u"\u0427\u0438\u0442\u0430\u0442\u044c", None))
    # retranslateUi

