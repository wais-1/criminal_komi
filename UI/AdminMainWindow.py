# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminMainWindow.ui'
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
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0.09 #6E0204,\n"
"    stop: 0.87 #9B5D61\n"
");")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 80, 201, 141))
        self.label.setStyleSheet(u"background-color: #000000;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 80, 351, 21))
        self.label_2.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 120, 351, 71))
        self.label_3.setStyleSheet(u"background-color: none;\n"
"font-size: 16pt;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(670, 190, 101, 41))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 15px;\n"
"color: #FFE5E5;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 100, 191, 41))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 50, 50))
        self.label_4.setStyleSheet(u"border-radius: 25px;\n"
"background-color: #000000;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 40, 151, 16))
        self.label_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_5.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 150, 191, 41))
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 200, 191, 41))
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 250, 191, 41))
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 300, 191, 41))
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(230, 10, 401, 41))
        self.lineEdit.setStyleSheet(u"background-color: rgba(8, 8, 8, 0.66);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;\n"
"border: none;")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(660, 10, 101, 41))
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.pushButton_7.setStyleSheet(u"border-radius: 10px;\n"
"background-color:  none;\n"
"color: #FFE5E5;")
        icon = QIcon()
        icon.addFile(u"../../../../Users/daria/Downloads/icon-filters.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setFlat(False)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(450, 200, 111, 31))
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #35451A;\n"
"padding: 7px;\n"
"color: #FFE5E5;")
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(570, 200, 71, 31))
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #9C0000;\n"
"padding: 7px;\n"
"color: #FFE5E5;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0430\u0442\u044c\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"admin", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0423\u0414", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u0434\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0434\u043e\u0437\u0440\u0435\u0432\u0430\u0435\u043c\u043e\u0433\u043e", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u043b\u0438\u043a\u0443", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u043d\u0430\u0439\u0442\u0438?", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b   ", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

