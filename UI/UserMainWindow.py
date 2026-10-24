# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserMainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0.09 #6E0204,\n"
"    stop: 0.87 #9B5D61\n"
");")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_search = QLineEdit(self.centralwidget)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setGeometry(QRect(170, 20, 401, 41))
        self.line_search.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.btn_filters = QPushButton(self.centralwidget)
        self.btn_filters.setObjectName(u"btn_filters")
        self.btn_filters.setGeometry(QRect(600, 20, 101, 41))
        self.btn_filters.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_filters.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_filters.setStyleSheet(u"border-radius: 10px;\n"
"background-color:  none;\n"
"color: #FFE5E5;")
        icon = QIcon()
        icon.addFile(u"../../../../Users/daria/Downloads/icon-filters.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_filters.setIcon(icon)
        self.btn_filters.setFlat(False)
        self.lbl_avatar = QLabel(self.centralwidget)
        self.lbl_avatar.setObjectName(u"lbl_avatar")
        self.lbl_avatar.setGeometry(QRect(10, 20, 50, 50))
        self.lbl_avatar.setStyleSheet(u"border-radius: 25px;\n"
"background-color: #000000;")
        self.lbl_username = QLabel(self.centralwidget)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setGeometry(QRect(70, 40, 151, 16))
        self.lbl_username.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lbl_username.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(170, 70, 700, 461))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 698, 459))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.scrollAreaWidgetContents.setStyleSheet(u"border: none;\n"
        "background-color: transparent;\n")
        self.scrollArea.setStyleSheet(u"border: none;\n"
        "background-color: transparent;\n")
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.line_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u043d\u0430\u0439\u0442\u0438?", None))
        self.btn_filters.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b   ", None))
        self.lbl_avatar.setText("")
        self.lbl_username.setText(QCoreApplication.translate("MainWindow", u"user", None))
    # retranslateUi

