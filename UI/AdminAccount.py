# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminAccount.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

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
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 151, 16))
        self.label_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_5.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 470, 81, 41))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 60, 761, 391))
        self.scrollArea.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -406, 745, 797))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none;")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"font-size: 16pt;")

        self.verticalLayout.addWidget(self.label_6)

        self.tableView = QTableView(self.frame)
        self.tableView.setObjectName(u"tableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)
        self.tableView.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.25);\n"
"border-radius: 20px;")

        self.verticalLayout.addWidget(self.tableView)


        self.verticalLayout_2.addWidget(self.frame)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_7.setStyleSheet(u"background-color: none;\n"
"font-size: 16pt;")

        self.verticalLayout_2.addWidget(self.label_7)

        self.tableView_2 = QTableView(self.scrollAreaWidgetContents)
        self.tableView_2.setObjectName(u"tableView_2")
        sizePolicy1.setHeightForWidth(self.tableView_2.sizePolicy().hasHeightForWidth())
        self.tableView_2.setSizePolicy(sizePolicy1)
        self.tableView_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.25);\n"
"border-radius: 20px;")

        self.verticalLayout_2.addWidget(self.tableView_2)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_8.setStyleSheet(u"background-color: none;\n"
"font-size: 16pt;")

        self.verticalLayout_2.addWidget(self.label_8)

        self.tableView_3 = QTableView(self.scrollAreaWidgetContents)
        self.tableView_3.setObjectName(u"tableView_3")
        sizePolicy1.setHeightForWidth(self.tableView_3.sizePolicy().hasHeightForWidth())
        self.tableView_3.setSizePolicy(sizePolicy1)
        self.tableView_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.25);\n"
"border-radius: 20px;")

        self.verticalLayout_2.addWidget(self.tableView_3)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 5px;\n"
"color: #FFE5E5;")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"admin", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0437\u0430\u0434", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c 2FA", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u043f\u0430\u0440\u043e\u043b\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0440\u043e\u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0434\u0430\u043d\u043d\u044b\u0445 \u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u0445", None))
    # retranslateUi

