# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InvestigatorMainWindow.ui'
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
        MainWindow.resize(1000, 650)
        MainWindow.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0.09 #6E0204,\n"
"    stop: 0.87 #9B5D61\n"
");")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_add_crime = QPushButton(self.centralwidget)
        self.btn_add_crime.setObjectName(u"btn_add_crime")
        self.btn_add_crime.setGeometry(QRect(10, 100, 191, 41))
        self.btn_add_crime.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_add_crime.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.search = QLineEdit(self.centralwidget)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(220, 10, 401, 41))
        self.search.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.btn_filters = QPushButton(self.centralwidget)
        self.btn_filters.setObjectName(u"btn_filters")
        self.btn_filters.setGeometry(QRect(650, 10, 101, 41))
        self.btn_filters.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_filters.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_filters.setStyleSheet(u"border-radius: 10px;\n"
"background-color:  none;\n"
"color: #FFE5E5;")
        icon = QIcon()
        icon.addFile(u"../../../../Users/daria/Downloads/icon-filters.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_filters.setIcon(icon)
        self.btn_filters.setFlat(False)
        self.btn_add_protocol = QPushButton(self.centralwidget)
        self.btn_add_protocol.setObjectName(u"btn_add_protocol")
        self.btn_add_protocol.setGeometry(QRect(10, 200, 191, 41))
        self.btn_add_protocol.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_add_protocol.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.btn_add_murder = QPushButton(self.centralwidget)
        self.btn_add_murder.setObjectName(u"btn_add_murder")
        self.btn_add_murder.setGeometry(QRect(10, 250, 191, 41))
        self.btn_add_murder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_add_murder.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.btn_add_clue = QPushButton(self.centralwidget)
        self.btn_add_clue.setObjectName(u"btn_add_clue")
        self.btn_add_clue.setGeometry(QRect(10, 300, 191, 41))
        self.btn_add_clue.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_add_clue.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.btn_add_criminal_case = QPushButton(self.centralwidget)
        self.btn_add_criminal_case.setObjectName(u"btn_add_criminal_case")
        self.btn_add_criminal_case.setGeometry(QRect(10, 150, 191, 41))
        self.btn_add_criminal_case.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_add_criminal_case.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
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
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(10, 350, 191, 41))
        self.pushButton_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(230, 80, 700, 451))
        self.scrollArea.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 700, 451))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(10, 400, 191, 41))
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(10, 450, 191, 41))
        self.pushButton_12.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(10, 500, 191, 41))
        self.pushButton_13.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(760, 10, 101, 41))
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_exit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: none;\n"
"padding: 5px;\n"
"color: red;\n"
"border: 1px solid red;")
        self.btn_exit.setIcon(icon)
        self.btn_exit.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_add_crime.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u043d\u0430\u0439\u0442\u0438?", None))
        self.btn_filters.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b   ", None))
        self.btn_add_protocol.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u0434\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.btn_add_murder.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0434\u043e\u0437\u0440\u0435\u0432\u0430\u0435\u043c\u043e\u0433\u043e", None))
        self.btn_add_clue.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u043b\u0438\u043a\u0443", None))
        self.btn_add_criminal_case.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0423\u0414", None))
        self.lbl_avatar.setText("")
        self.lbl_username.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043c\u0435\u0441\u0442\u043e", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0442\u0435\u0440\u043f\u0435\u0432\u0448\u0435\u0433\u043e", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044f", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u0438\u0432\u044f\u0437\u0430\u0442\u044c \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

