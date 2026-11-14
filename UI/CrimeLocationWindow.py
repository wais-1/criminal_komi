# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CrimeLocationWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

from crime_map import CrimeMap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 680)
        MainWindow.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0.09 #6E0204,\n"
"    stop: 0.87 #9B5D61\n"
");")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 241, 31))
        self.label.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;")
        self.crime_map = CrimeMap(self.centralwidget)
        self.crime_map.setGeometry(QRect(40, 280, 721, 341))
        self.crime_map.setObjectName("crime_map")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 50, 521, 231))
        self.frame.setStyleSheet(u"background-color: none;")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"background-color: none;")
        self.horizontalLayout = QHBoxLayout(self.frame1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame1)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"font-size: 16px;\n"
"background-color: none;")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size: 16px;\n"
"background-color: none;")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame1)

        self.frame2 = QFrame(self.frame)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_2 = QHBoxLayout(self.frame2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(u"font-size: 16px;\n"
"background-color: none;")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size: 16px;\n"
"background-color: none;")

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout.addWidget(self.frame2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet(u"font-size: 16px;\n"
"background-color: none;")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font-size: 16px;\n"
"background-color: none;")

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setStyleSheet(u"font-size: 16px;\n"
"background-color: none;")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-size: 16px;\n"
"background-color: none;")

        self.horizontalLayout_4.addWidget(self.label_10)


        self.verticalLayout.addWidget(self.frame_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 580, 200, 41))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 15px;\n"
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0415\u0421\u0422\u041e \u041f\u0420\u0415\u0421\u0422\u0423\u041f\u041b\u0415\u041d\u0418\u042f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0434\u0440\u0435\u0441", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0439\u043e\u043d:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0439\u043e\u043d", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0442\u0438\u043f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
    # retranslateUi

