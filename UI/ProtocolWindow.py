# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProtocolWindow.ui'
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
    QMainWindow, QMenuBar, QScrollArea, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

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
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 776, 1062))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none;")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_name = QLabel(self.frame)
        self.lbl_name.setObjectName(u"lbl_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_name.sizePolicy().hasHeightForWidth())
        self.lbl_name.setSizePolicy(sizePolicy)
        self.lbl_name.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;")

        self.verticalLayout.addWidget(self.lbl_name)

        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setStyleSheet(u"background-color: none;")
        self.horizontalLayout = QHBoxLayout(self.frame1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.frame1)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_7)

        self.lbl_date = QLabel(self.frame1)
        self.lbl_date.setObjectName(u"lbl_date")
        sizePolicy.setHeightForWidth(self.lbl_date.sizePolicy().hasHeightForWidth())
        self.lbl_date.setSizePolicy(sizePolicy)
        self.lbl_date.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.lbl_date.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.lbl_date)


        self.verticalLayout.addWidget(self.frame1)

        self.lbl_descr = QLabel(self.frame)
        self.lbl_descr.setObjectName(u"lbl_descr")
        sizePolicy.setHeightForWidth(self.lbl_descr.sizePolicy().hasHeightForWidth())
        self.lbl_descr.setSizePolicy(sizePolicy)
        self.lbl_descr.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.lbl_descr.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lbl_descr.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_descr)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.lbl_audio = QLabel(self.frame_2)
        self.lbl_audio.setObjectName(u"lbl_audio")
        self.lbl_audio.setMinimumSize(QSize(500, 189))
        self.lbl_audio.setStyleSheet(u"background-color: #000000;")

        self.horizontalLayout_2.addWidget(self.lbl_audio)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: none;")
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_victim = QLabel(self.frame_3)
        self.lbl_victim.setObjectName(u"lbl_victim")
        sizePolicy.setHeightForWidth(self.lbl_victim.sizePolicy().hasHeightForWidth())
        self.lbl_victim.setSizePolicy(sizePolicy)
        self.lbl_victim.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"text-transform: uppercase;")

        self.verticalLayout_2.addWidget(self.lbl_victim)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.lbl_full_name = QLabel(self.frame_4)
        self.lbl_full_name.setObjectName(u"lbl_full_name")
        sizePolicy.setHeightForWidth(self.lbl_full_name.sizePolicy().hasHeightForWidth())
        self.lbl_full_name.setSizePolicy(sizePolicy)
        self.lbl_full_name.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_5.addWidget(self.lbl_full_name)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.lbl_status = QLabel(self.frame_5)
        self.lbl_status.setObjectName(u"lbl_status")
        sizePolicy.setHeightForWidth(self.lbl_status.sizePolicy().hasHeightForWidth())
        self.lbl_status.setSizePolicy(sizePolicy)
        self.lbl_status.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_6.addWidget(self.lbl_status)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_7.addWidget(self.label_15)

        self.lbl_date_birth = QLabel(self.frame_6)
        self.lbl_date_birth.setObjectName(u"lbl_date_birth")
        sizePolicy.setHeightForWidth(self.lbl_date_birth.sizePolicy().hasHeightForWidth())
        self.lbl_date_birth.setSizePolicy(sizePolicy)
        self.lbl_date_birth.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_7.addWidget(self.lbl_date_birth)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_8.addWidget(self.label_18)

        self.lbl_degree = QLabel(self.frame_7)
        self.lbl_degree.setObjectName(u"lbl_degree")
        sizePolicy.setHeightForWidth(self.lbl_degree.sizePolicy().hasHeightForWidth())
        self.lbl_degree.setSizePolicy(sizePolicy)
        self.lbl_degree.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_8.addWidget(self.lbl_degree)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: none;")
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_witness = QLabel(self.frame_8)
        self.lbl_witness.setObjectName(u"lbl_witness")
        sizePolicy.setHeightForWidth(self.lbl_witness.sizePolicy().hasHeightForWidth())
        self.lbl_witness.setSizePolicy(sizePolicy)
        self.lbl_witness.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"text-transform: uppercase;")

        self.verticalLayout_3.addWidget(self.lbl_witness)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_19 = QLabel(self.frame_9)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_9.addWidget(self.label_19)

        self.lbl_witness_name = QLabel(self.frame_9)
        self.lbl_witness_name.setObjectName(u"lbl_witness_name")
        sizePolicy.setHeightForWidth(self.lbl_witness_name.sizePolicy().hasHeightForWidth())
        self.lbl_witness_name.setSizePolicy(sizePolicy)
        self.lbl_witness_name.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_9.addWidget(self.lbl_witness_name)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_21 = QLabel(self.frame_10)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_10.addWidget(self.label_21)

        self.lbl_level = QLabel(self.frame_10)
        self.lbl_level.setObjectName(u"lbl_level")
        sizePolicy.setHeightForWidth(self.lbl_level.sizePolicy().hasHeightForWidth())
        self.lbl_level.setSizePolicy(sizePolicy)
        self.lbl_level.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_10.addWidget(self.lbl_level)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_23 = QLabel(self.frame_11)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_11.addWidget(self.label_23)

        self.lbl_programm = QLabel(self.frame_11)
        self.lbl_programm.setObjectName(u"lbl_programm")
        sizePolicy.setHeightForWidth(self.lbl_programm.sizePolicy().hasHeightForWidth())
        self.lbl_programm.setSizePolicy(sizePolicy)
        self.lbl_programm.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_11.addWidget(self.lbl_programm)


        self.verticalLayout_3.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_8)


        self.verticalLayout_4.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea.setStyleSheet(u"border: none;\n"
        "background-color: transparent;\n")

        self.horizontalLayout_3.addWidget(self.scrollArea)

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
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u0434\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f:", None))
        self.lbl_date.setText(QCoreApplication.translate("MainWindow", u"01.01.2025", None))
        self.lbl_descr.setText(QCoreApplication.translate("MainWindow", u"10 \u043e\u043a\u0442\u044f\u0431\u0440\u044f 2026 \u0433\u043e\u0434\u0430 \u043e\u043a\u043e\u043b\u043e 21:15 \u044f \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u043b\u0441\u044f \u0434\u043e\u043c\u043e\u0439 \u043f\u043e \u0442\u0440\u043e\u0442\u0443\u0430\u0440\u0443 \u0432\u0434\u043e\u043b\u044c \u0443\u043b\u0438\u0446\u044b \u041b\u0435\u043d\u0438\u043d\u0430 \u0432 \u0441\u0442\u043e\u0440\u043e\u043d\u0443 \u0443\u043b\u0438\u0446\u044b \u0413\u0430\u0433\u0430\u0440\u0438\u043d\u0430. \u0412 \u0440\u0443\u043a\u0430\u0445 \u044f \u043d\u0435\u0441 \u0447\u0435\u0440\u043d\u0443\u044e \u043a\u043e\u0436\u0430\u043d\u0443\u044e \u043c\u0443\u0436\u0441\u043a\u0443\u044e \u0441\u0443\u043c\u043a\u0443.\n"
"\u0412\u043e\u0437\u043b\u0435 \u0434\u043e\u043c\u0430 \u2116 24 \u044f \u0443\u0441\u043b\u044b\u0448\u0430\u043b \u0441\u0437\u0430\u0434\u0438 \u0431\u044b\u0441\u0442\u0440\u044b\u0435 \u0448\u0430\u0433\u0438. \u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u0439 \u0440\u0435"
                        "\u0437\u043a\u043e \u0438 \u0441\u0438\u043b\u044c\u043d\u043e \u0440\u0432\u0430\u043d\u0443\u043b \u0441\u0443\u043c\u043a\u0443 \u0438\u0437 \u043c\u043e\u0438\u0445 \u0440\u0443\u043a. \u041e\u0442 \u043d\u0435\u043e\u0436\u0438\u0434\u0430\u043d\u043d\u043e\u0441\u0442\u0438 \u044f \u043f\u043e\u0442\u0435\u0440\u044f\u043b \u0440\u0430\u0432\u043d\u043e\u0432\u0435\u0441\u0438\u0435 \u0438 \u0443\u043f\u0430\u043b \u043d\u0430 \u043a\u043e\u043b\u0435\u043d\u043e. \u042f \u043a\u0440\u0438\u043a\u043d\u0443\u043b: \u00ab\u0421\u0442\u043e\u0439!\u00bb, \u043d\u043e \u043d\u0430\u043f\u0430\u0434\u0430\u0432\u0448\u0438\u0439 \u0431\u0440\u043e\u0441\u0438\u043b\u0441\u044f \u0431\u0435\u0436\u0430\u0442\u044c \u0438 \u0441\u043a\u0440\u044b\u043b\u0441\u044f \u0432 \u0442\u0435\u043c\u043d\u043e\u043c \u043f\u0435\u0440\u0435\u0443\u043b\u043a\u0435 \u043c\u0435\u0436\u0434\u0443 \u0434\u043e\u043c\u0430\u043c\u0438.\n"
"\u0412 \u043f\u043e\u0445\u0438\u0449\u0435\u043d\u043d\u043e\u0439 \u0441\u0443\u043c"
                        "\u043a\u0435 \u043d\u0430\u0445\u043e\u0434\u0438\u043b\u0438\u0441\u044c:\n"
"\u2022 \u0422\u0435\u043b\u0435\u0444\u043e\u043d iPhone 14 \u0432 \u0441\u0438\u043d\u0435\u043c \u0447\u0435\u0445\u043b\u0435;\n"
"\u2022 \u041a\u043e\u0436\u0430\u043d\u044b\u0439 \u043a\u043e\u0448\u0435\u043b\u0435\u043a \u0438 15 000 \u0440\u0443\u0431\u043b\u0435\u0439 \u043d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438;\n"
"\u2022 \u041f\u0430\u0441\u043f\u043e\u0440\u0442 \u043d\u0430 \u043c\u043e\u0435 \u0438\u043c\u044f \u0438 \u043a\u043b\u044e\u0447\u0438.\n"
"\u041e\u0431\u0449\u0438\u0439 \u0443\u0449\u0435\u0440\u0431 \u0441\u043e\u0441\u0442\u0430\u0432\u0438\u043b \u043e\u043a\u043e\u043b\u043e 85 000 \u0440\u0443\u0431\u043b\u0435\u0439, \u0447\u0442\u043e \u0434\u043b\u044f \u043c\u0435\u043d\u044f \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0441\u0443\u043c\u043c\u043e\u0439.\n"
"\u041f\u0440\u0438\u043c\u0435\u0442\u044b \u043d\u0430"
                        "\u043f\u0430\u0434\u0430\u0432\u0448\u0435\u0433\u043e:\n"
"\u041c\u0443\u0436\u0447\u0438\u043d\u0430 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0440\u043e\u0441\u0442\u0430 (175\u2013180 \u0441\u043c), \u0445\u0443\u0434\u043e\u0449\u0430\u0432\u044b\u0439. \u0411\u044b\u043b \u043e\u0434\u0435\u0442 \u0432 \u0442\u0435\u043c\u043d\u0443\u044e \u043a\u0443\u0440\u0442\u043a\u0443 \u0441 \u043a\u0430\u043f\u044e\u0448\u043e\u043d\u043e\u043c \u0438 \u0442\u0435\u043c\u043d\u044b\u0435 \u0448\u0442\u0430\u043d\u044b. \u0418\u0437-\u0437\u0430 \u0442\u0435\u043c\u043d\u043e\u0442\u044b \u043b\u0438\u0446\u0430 \u044f \u043d\u0435 \u0440\u0430\u0437\u0433\u043b\u044f\u0434\u0435\u043b, \u043d\u043e \u0437\u0430\u043f\u043e\u043c\u043d\u0438\u043b \u0435\u0433\u043e \u044f\u0440\u043a\u043e-\u0431\u0435\u043b\u044b\u0435 \u043a\u0440\u043e\u0441\u0441\u043e\u0432\u043a\u0438 \u043d\u0430 \u0442\u043e\u043b\u0441\u0442\u043e\u0439 \u043f\u043e\u0434\u043e\u0448\u0432\u0435. \u0420\u0430\u043d\u0435\u0435 \u044d"
                        "\u0442\u043e\u0433\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430 \u044f \u043d\u0438\u043a\u043e\u0433\u0434\u0430 \u043d\u0435 \u0432\u0438\u0434\u0435\u043b.\n"
"\u0421 \u043c\u043e\u0438\u0445 \u0441\u043b\u043e\u0432 \u0437\u0430\u043f\u0438\u0441\u0430\u043d\u043e \u0432\u0435\u0440\u043d\u043e, \u043c\u043d\u043e\u044e \u043f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u043e/\u0432\u0438\u0434\u0435\u043e:", None))
        self.lbl_audio.setText("")
        self.lbl_victim.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0442\u0435\u0440\u043f\u0435\u0432\u0448\u0438\u0439", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e:", None))
        self.lbl_full_name.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0432\u0430\u043d\u043e\u0432 \u0418\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u0449\u0438\u0442\u044b:", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0435\u0442", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.lbl_date_birth.setText(QCoreApplication.translate("MainWindow", u"01.01.1999", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u0442\u044f\u0436\u0435\u0441\u0442\u0438:", None))
        self.lbl_degree.setText(QCoreApplication.translate("MainWindow", u"\u0442\u044f\u0436\u0435\u043b\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
        self.lbl_witness.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e:", None))
        self.lbl_witness_name.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0432\u0430\u043d\u043e\u0432 \u0418\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043d\u0430\u0434\u0435\u0436\u043d\u043e\u0441\u0442\u0438:", None))
        self.lbl_level.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0434\u0435\u0436\u0435\u043d", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0437\u0430\u0449\u0438\u0442\u044b:", None))
        self.lbl_programm.setText(QCoreApplication.translate("MainWindow", u"\u0435\u0441\u0442\u044c", None))
    # retranslateUi

