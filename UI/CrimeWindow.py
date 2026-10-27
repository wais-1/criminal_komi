# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CrimeWindow.ui'
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
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 600)
        MainWindow.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0.09 #6E0204,\n"
"    stop: 0.87 #9B5D61\n"
");")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 821, 600))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 819, 1151))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_img = QLabel(self.frame)
        self.lbl_img.setObjectName(u"lbl_img")
        self.lbl_img.setStyleSheet(u"background-color: #000000;")
        self.scrollAreaWidgetContents.setStyleSheet(u"border: none;\n"
        "background-color: transparent;\n")
        self.scrollArea.setStyleSheet(u"border: none;\n"
        "background-color: transparent;\n")

        self.horizontalLayout_4.addWidget(self.lbl_img)

        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"background-color: none;")
        self.verticalLayout = QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_fullname = QLabel(self.frame1)
        self.lbl_fullname.setObjectName(u"lbl_fullname")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_fullname.sizePolicy().hasHeightForWidth())
        self.lbl_fullname.setSizePolicy(sizePolicy1)
        self.lbl_fullname.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"text-transform: uppercase;")

        self.verticalLayout.addWidget(self.lbl_fullname)

        self.frame2 = QFrame(self.frame1)
        self.frame2.setObjectName(u"frame2")
        sizePolicy1.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy1)
        self.frame2.setStyleSheet(u"background-color: none;")
        self.horizontalLayout = QHBoxLayout(self.frame2)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.frame2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_8)

        self.lbl_date_birth = QLabel(self.frame2)
        self.lbl_date_birth.setObjectName(u"lbl_date_birth")
        sizePolicy1.setHeightForWidth(self.lbl_date_birth.sizePolicy().hasHeightForWidth())
        self.lbl_date_birth.setSizePolicy(sizePolicy1)
        self.lbl_date_birth.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.lbl_date_birth.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.lbl_date_birth)


        self.verticalLayout.addWidget(self.frame2)

        self.frame3 = QFrame(self.frame1)
        self.frame3.setObjectName(u"frame3")
        sizePolicy1.setHeightForWidth(self.frame3.sizePolicy().hasHeightForWidth())
        self.frame3.setSizePolicy(sizePolicy1)
        self.frame3.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_2 = QHBoxLayout(self.frame3)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lbl_signs = QLabel(self.frame3)
        self.lbl_signs.setObjectName(u"lbl_signs")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_signs.sizePolicy().hasHeightForWidth())
        self.lbl_signs.setSizePolicy(sizePolicy3)
        self.lbl_signs.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.lbl_signs.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lbl_signs.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.lbl_signs)


        self.verticalLayout.addWidget(self.frame3)

        self.frame4 = QFrame(self.frame1)
        self.frame4.setObjectName(u"frame4")
        sizePolicy1.setHeightForWidth(self.frame4.sizePolicy().hasHeightForWidth())
        self.frame4.setSizePolicy(sizePolicy1)
        self.frame4.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_3 = QHBoxLayout(self.frame4)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.frame4)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.lbl_status = QLabel(self.frame4)
        self.lbl_status.setObjectName(u"lbl_status")
        sizePolicy1.setHeightForWidth(self.lbl_status.sizePolicy().hasHeightForWidth())
        self.lbl_status.setSizePolicy(sizePolicy1)
        self.lbl_status.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_3.addWidget(self.lbl_status)


        self.verticalLayout.addWidget(self.frame4)


        self.horizontalLayout_4.addWidget(self.frame1)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame5 = QFrame(self.scrollAreaWidgetContents)
        self.frame5.setObjectName(u"frame5")
        self.frame5.setStyleSheet(u"background-color: none;")
        self.verticalLayout_2 = QVBoxLayout(self.frame5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_article_name = QLabel(self.frame5)
        self.lbl_article_name.setObjectName(u"lbl_article_name")
        sizePolicy1.setHeightForWidth(self.lbl_article_name.sizePolicy().hasHeightForWidth())
        self.lbl_article_name.setSizePolicy(sizePolicy1)
        self.lbl_article_name.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"text-transform: uppercase;")

        self.verticalLayout_2.addWidget(self.lbl_article_name)

        self.frame6 = QFrame(self.frame5)
        self.frame6.setObjectName(u"frame6")
        sizePolicy1.setHeightForWidth(self.frame6.sizePolicy().hasHeightForWidth())
        self.frame6.setSizePolicy(sizePolicy1)
        self.frame6.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_5 = QHBoxLayout(self.frame6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.frame6)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.lbl_article_date = QLabel(self.frame6)
        self.lbl_article_date.setObjectName(u"lbl_article_date")
        sizePolicy1.setHeightForWidth(self.lbl_article_date.sizePolicy().hasHeightForWidth())
        self.lbl_article_date.setSizePolicy(sizePolicy1)
        self.lbl_article_date.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_5.addWidget(self.lbl_article_date)


        self.verticalLayout_2.addWidget(self.frame6)

        self.frame7 = QFrame(self.frame5)
        self.frame7.setObjectName(u"frame7")
        sizePolicy1.setHeightForWidth(self.frame7.sizePolicy().hasHeightForWidth())
        self.frame7.setSizePolicy(sizePolicy1)
        self.frame7.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_6 = QHBoxLayout(self.frame7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_13 = QLabel(self.frame7)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.lbl_secret = QLabel(self.frame7)
        self.lbl_secret.setObjectName(u"lbl_secret")
        sizePolicy1.setHeightForWidth(self.lbl_secret.sizePolicy().hasHeightForWidth())
        self.lbl_secret.setSizePolicy(sizePolicy1)
        self.lbl_secret.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_6.addWidget(self.lbl_secret)


        self.verticalLayout_2.addWidget(self.frame7)

        self.frame8 = QFrame(self.frame5)
        self.frame8.setObjectName(u"frame8")
        sizePolicy1.setHeightForWidth(self.frame8.sizePolicy().hasHeightForWidth())
        self.frame8.setSizePolicy(sizePolicy1)
        self.frame8.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_7 = QHBoxLayout(self.frame8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_15 = QLabel(self.frame8)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_7.addWidget(self.label_15)

        self.lbl_article_status = QLabel(self.frame8)
        self.lbl_article_status.setObjectName(u"lbl_article_status")
        sizePolicy1.setHeightForWidth(self.lbl_article_status.sizePolicy().hasHeightForWidth())
        self.lbl_article_status.setSizePolicy(sizePolicy1)
        self.lbl_article_status.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_7.addWidget(self.lbl_article_status)


        self.verticalLayout_2.addWidget(self.frame8)

        self.frame9 = QFrame(self.frame5)
        self.frame9.setObjectName(u"frame9")
        sizePolicy1.setHeightForWidth(self.frame9.sizePolicy().hasHeightForWidth())
        self.frame9.setSizePolicy(sizePolicy1)
        self.frame9.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_8 = QHBoxLayout(self.frame9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_18 = QLabel(self.frame9)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_8.addWidget(self.label_18)

        self.lbl_type = QLabel(self.frame9)
        self.lbl_type.setObjectName(u"lbl_type")
        sizePolicy1.setHeightForWidth(self.lbl_type.sizePolicy().hasHeightForWidth())
        self.lbl_type.setSizePolicy(sizePolicy1)
        self.lbl_type.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_8.addWidget(self.lbl_type)


        self.verticalLayout_2.addWidget(self.frame9)


        self.verticalLayout_3.addWidget(self.frame5)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: none;")
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_clue_name = QLabel(self.frame_3)
        self.lbl_clue_name.setObjectName(u"lbl_clue_name")
        sizePolicy1.setHeightForWidth(self.lbl_clue_name.sizePolicy().hasHeightForWidth())
        self.lbl_clue_name.setSizePolicy(sizePolicy1)
        self.lbl_clue_name.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"text-transform: uppercase;")

        self.verticalLayout_6.addWidget(self.lbl_clue_name)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_13 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_28 = QLabel(self.frame_4)
        self.label_28.setObjectName(u"label_28")
        sizePolicy1.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy1)
        self.label_28.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_13.addWidget(self.label_28)

        self.lbl_clue_nomination = QLabel(self.frame_4)
        self.lbl_clue_nomination.setObjectName(u"lbl_clue_nomination")
        sizePolicy1.setHeightForWidth(self.lbl_clue_nomination.sizePolicy().hasHeightForWidth())
        self.lbl_clue_nomination.setSizePolicy(sizePolicy1)
        self.lbl_clue_nomination.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_13.addWidget(self.lbl_clue_nomination)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_30 = QLabel(self.frame_5)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)
        self.label_30.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_14.addWidget(self.label_30)

        self.lbl_clue_date = QLabel(self.frame_5)
        self.lbl_clue_date.setObjectName(u"lbl_clue_date")
        sizePolicy1.setHeightForWidth(self.lbl_clue_date.sizePolicy().hasHeightForWidth())
        self.lbl_clue_date.setSizePolicy(sizePolicy1)
        self.lbl_clue_date.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_14.addWidget(self.lbl_clue_date)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_15 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_32 = QLabel(self.frame_6)
        self.label_32.setObjectName(u"label_32")
        sizePolicy1.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy1)
        self.label_32.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_15.addWidget(self.label_32)

        self.lbl_clue_descr = QLabel(self.frame_6)
        self.lbl_clue_descr.setObjectName(u"lbl_clue_descr")
        sizePolicy1.setHeightForWidth(self.lbl_clue_descr.sizePolicy().hasHeightForWidth())
        self.lbl_clue_descr.setSizePolicy(sizePolicy1)
        self.lbl_clue_descr.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_15.addWidget(self.lbl_clue_descr)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_34 = QLabel(self.frame_7)
        self.label_34.setObjectName(u"label_34")
        sizePolicy1.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy1)
        self.label_34.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_16.addWidget(self.label_34)

        self.lbl_clue_type = QLabel(self.frame_7)
        self.lbl_clue_type.setObjectName(u"lbl_clue_type")
        sizePolicy1.setHeightForWidth(self.lbl_clue_type.sizePolicy().hasHeightForWidth())
        self.lbl_clue_type.setSizePolicy(sizePolicy1)
        self.lbl_clue_type.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_16.addWidget(self.lbl_clue_type)


        self.verticalLayout_6.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.btn_read_protocol = QPushButton(self.scrollAreaWidgetContents)
        self.btn_read_protocol.setObjectName(u"btn_read_protocol")
        sizePolicy1.setHeightForWidth(self.btn_read_protocol.sizePolicy().hasHeightForWidth())
        self.btn_read_protocol.setSizePolicy(sizePolicy1)
        self.btn_read_protocol.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_read_protocol.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #3D0A0A;\n"
"padding: 15px;\n"
"color: #FFE5E5;")

        self.verticalLayout_3.addWidget(self.btn_read_protocol)

        self.frame10 = QFrame(self.scrollAreaWidgetContents)
        self.frame10.setObjectName(u"frame10")
        self.frame10.setStyleSheet(u"background-color: none;")
        self.verticalLayout_5 = QVBoxLayout(self.frame10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame11 = QFrame(self.frame10)
        self.frame11.setObjectName(u"frame11")
        sizePolicy1.setHeightForWidth(self.frame11.sizePolicy().hasHeightForWidth())
        self.frame11.setSizePolicy(sizePolicy1)
        self.frame11.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_9 = QHBoxLayout(self.frame11)
        self.horizontalLayout_9.setSpacing(25)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.frame11)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"text-transform: uppercase;")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.lbl_case_number = QLabel(self.frame11)
        self.lbl_case_number.setObjectName(u"lbl_case_number")
        sizePolicy1.setHeightForWidth(self.lbl_case_number.sizePolicy().hasHeightForWidth())
        self.lbl_case_number.setSizePolicy(sizePolicy1)
        self.lbl_case_number.setStyleSheet(u"background-color: none;\n"
"font-size: 20pt;\n"
"text-transform: uppercase;")

        self.horizontalLayout_9.addWidget(self.lbl_case_number)


        self.verticalLayout_5.addWidget(self.frame11)

        self.frame12 = QFrame(self.frame10)
        self.frame12.setObjectName(u"frame12")
        sizePolicy1.setHeightForWidth(self.frame12.sizePolicy().hasHeightForWidth())
        self.frame12.setSizePolicy(sizePolicy1)
        self.frame12.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_10 = QHBoxLayout(self.frame12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_21 = QLabel(self.frame12)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_10.addWidget(self.label_21)

        self.lbl_case = QLabel(self.frame12)
        self.lbl_case.setObjectName(u"lbl_case")
        sizePolicy1.setHeightForWidth(self.lbl_case.sizePolicy().hasHeightForWidth())
        self.lbl_case.setSizePolicy(sizePolicy1)
        self.lbl_case.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_10.addWidget(self.lbl_case)


        self.verticalLayout_5.addWidget(self.frame12)

        self.frame13 = QFrame(self.frame10)
        self.frame13.setObjectName(u"frame13")
        sizePolicy1.setHeightForWidth(self.frame13.sizePolicy().hasHeightForWidth())
        self.frame13.setSizePolicy(sizePolicy1)
        self.frame13.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_11 = QHBoxLayout(self.frame13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_23 = QLabel(self.frame13)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)
        self.label_23.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_11.addWidget(self.label_23)

        self.lbl_date_open = QLabel(self.frame13)
        self.lbl_date_open.setObjectName(u"lbl_date_open")
        sizePolicy1.setHeightForWidth(self.lbl_date_open.sizePolicy().hasHeightForWidth())
        self.lbl_date_open.setSizePolicy(sizePolicy1)
        self.lbl_date_open.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_11.addWidget(self.lbl_date_open)


        self.verticalLayout_5.addWidget(self.frame13)

        self.frame_2 = QFrame(self.frame10)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_12 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)
        self.label_25.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_12.addWidget(self.label_25)

        self.lbl_date_close = QLabel(self.frame_2)
        self.lbl_date_close.setObjectName(u"lbl_date_close")
        sizePolicy1.setHeightForWidth(self.lbl_date_close.sizePolicy().hasHeightForWidth())
        self.lbl_date_close.setSizePolicy(sizePolicy1)
        self.lbl_date_close.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")

        self.horizontalLayout_12.addWidget(self.lbl_date_close)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame10)

        self.lbl_date_text = QLabel(self.scrollAreaWidgetContents)
        self.lbl_date_text.setObjectName(u"lbl_date_text")
        self.lbl_date_text.setStyleSheet(u"background-color: none;\n"
"font-size: 14pt;")
        self.lbl_date_text.setTextFormat(Qt.TextFormat.AutoText)
        self.lbl_date_text.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lbl_date_text.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lbl_date_text)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 820, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_img.setText("")
        self.lbl_fullname.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043d\u0438\u043a\u0430", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.lbl_date_birth.setText(QCoreApplication.translate("MainWindow", u"01.01.2000", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043e\u0431\u044b\u0435 \u043f\u0440\u0438\u043c\u0435\u0442\u044b:", None))
        self.lbl_signs.setText(QCoreApplication.translate("MainWindow", u"\u043c\u0443\u0436\u0447\u0438\u043d\u0430 \u043d\u0430 \u0432\u0438\u0434 30\u201335 \u043b\u0435\u0442, \u0440\u043e\u0441\u0442 \u043e\u043a\u043e\u043b\u043e 180 \u0441\u043c, \u0445\u0443\u0434\u043e\u0449\u0430\u0432\u043e\u0433\u043e \u0442\u0435\u043b\u043e\u0441\u043b\u043e\u0436\u0435\u043d\u0438\u044f, \u0438\u043c\u0435\u0435\u0442 \u0442\u043e\u043d\u043a\u0438\u0439 \u0448\u0440\u0430\u043c \u043d\u0430 \u043b\u0435\u0432\u043e\u0439 \u0431\u0440\u043e\u0432\u0438, \u0442\u0430\u0442\u0443\u0438\u0440\u043e\u0432\u043a\u0443 \u0432 \u0432\u0438\u0434\u0435 \u043f\u0430\u0443\u043a\u0430 \u043d\u0430 \u0448\u0435\u0435 \u0441\u043f\u0440\u0430\u0432\u0430, \u0437\u0430\u043c\u0435\u0442\u043d\u043e \u043f\u0440\u0438\u0445\u0440\u0430\u043c\u044b\u0432\u0430\u0435\u0442 \u043d\u0430 \u043f\u0440\u0430\u0432\u0443\u044e \u043d\u043e\u0433\u0443 \u0438 \u043f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u043e \u043a\u0440\u0443\u0442\u0438\u0442 \u0432 \u0440\u0443\u043a\u0430\u0445 \u043c\u0435\u0442\u0430"
                        "\u043b\u043b\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0437\u0430\u0436\u0438\u0433\u0430\u043b\u043a\u0443.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"\u0432 \u0440\u043e\u0437\u044b\u0441\u043a\u0435", None))
        self.lbl_article_name.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0430\u0442\u044c\u0438", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f:", None))
        self.lbl_article_date.setText(QCoreApplication.translate("MainWindow", u"01.01.2000", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u043e\u0441\u0442\u0438:", None))
        self.lbl_secret.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0435\u0441\u0435\u043a\u0440\u0435\u0442\u043d\u043e", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.lbl_article_status.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u043a\u0440\u044b\u0442\u043e", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f:", None))
        self.lbl_type.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e\u0442\u0438\u0432 \u043b\u0438\u0447\u043d\u043e\u0441\u0442\u0438", None))
        self.lbl_clue_name.setText(QCoreApplication.translate("MainWindow", u"\u0443\u043b\u0438\u043a\u0430", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.lbl_clue_nomination.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u043f\u0438\u0441\u044c \u0441 \u043a\u0430\u043c\u0435\u0440\u044b \u0434\u043e\u043c\u043e\u0444\u043e\u043d\u0430", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.lbl_clue_date.setText(QCoreApplication.translate("MainWindow", u"03.01.2025", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.lbl_clue_descr.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0443\u044d\u0442\u044b \u0434\u0432\u0443\u0445 \u043c\u0443\u0436\u0447\u0438\u043d, \u0432\u044b\u043d\u043e\u0441\u044f\u0449\u0438\u0445 \u0442\u044f\u0436\u0435\u043b\u044b\u0439 \u043f\u0440\u044f\u043c\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u0432 \u0421\u044b\u043a\u0442\u044b\u0432\u043a\u0430\u0440\u0435.", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f:", None))
        self.lbl_clue_type.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0430\u043d\u043d\u044b\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432", None))
        self.btn_read_protocol.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0442\u0430\u0442\u044c \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u0434\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0433\u043e\u043b\u043e\u0432\u043d\u043e\u0435 \u0434\u0435\u043b\u043e \u2116", None))
        self.lbl_case_number.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u044c\u044f \u0423\u041a:", None))
        self.lbl_case.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u044c\u044f 158. \u041a\u0440\u0430\u0436\u0430", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f:", None))
        self.lbl_date_open.setText(QCoreApplication.translate("MainWindow", u"01.01.2025", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0440\u044b\u0442\u0438\u044f:", None))
        self.lbl_date_close.setText(QCoreApplication.translate("MainWindow", u"01.04.2025", None))
        self.lbl_date_text.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0435 \u041a\u043e\u043c\u0438 \u0440\u0430\u0441\u0441\u043b\u0435\u0434\u0443\u0435\u0442\u0441\u044f \u0434\u0435\u0440\u0437\u043a\u043e\u0435 \u043e\u0433\u0440\u0430\u0431\u043b\u0435\u043d\u0438\u0435: \u0432 \u043d\u043e\u0447\u044c \u043d\u0430 10 \u043e\u043a\u0442\u044f\u0431\u0440\u044f \u0432 \u0433\u043e\u0440\u043e\u0434\u0435 \u0412\u043e\u0440\u043a\u0443\u0442\u0430 \u0433\u0440\u0443\u043f\u043f\u0430 \u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u0445 \u043b\u0438\u0446 \u0441\u043e\u0432\u0435\u0440\u0448\u0438\u043b\u0430 \u0442\u0449\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0441\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0435 \u043d\u0430\u043f\u0430\u0434\u0435\u043d\u0438\u0435 \u043d\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044c\u043d\u043e-\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u043a\u043b\u0430\u0434 \u043a\u0440\u0443\u043f\u043d"
                        "\u043e\u0433\u043e \u0433\u043e\u0440\u043d\u043e-\u043e\u0431\u043e\u0433\u0430\u0442\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0442\u0430, \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0439 \u043d\u0430 \u043f\u0440\u043e\u043c\u044b\u0448\u043b\u0435\u043d\u043d\u043e\u0439 \u043e\u043a\u0440\u0430\u0438\u043d\u0435 \u0433\u043e\u0440\u043e\u0434\u0430.\n"
"\u0417\u043b\u043e\u0443\u043c\u044b\u0448\u043b\u0435\u043d\u043d\u0438\u043a\u0438 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e \u043d\u0435\u0439\u0442\u0440\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043b\u0438 \u043e\u0445\u0440\u0430\u043d\u043d\u0443\u044e \u0441\u0438\u0433\u043d\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044e \u0438 \u0432\u044b\u0432\u0435\u043b\u0438 \u0438\u0437 \u0441\u0442\u0440\u043e\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0443 \u0432\u043d\u0435\u0448\u043d\u0435\u0433\u043e \u0432\u0438\u0434"
                        "\u0435\u043e\u043d\u0430\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u044f, \u043f\u043e\u0441\u043b\u0435 \u0447\u0435\u0433\u043e \u043f\u0440\u043e\u043d\u0438\u043a\u043b\u0438 \u0432 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0441\u043a\u043b\u0430\u0434\u0430, \u043e\u0442\u043a\u0443\u0434\u0430 \u043f\u043e\u0445\u0438\u0442\u0438\u043b\u0438 \u043f\u0430\u0440\u0442\u0438\u044e \u0434\u043e\u0440\u043e\u0433\u043e\u0441\u0442\u043e\u044f\u0449\u0435\u0433\u043e \u043f\u0440\u043e\u043c\u044b\u0448\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f \u043e\u0431\u0449\u0435\u0433\u043e \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0438 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0433\u0435\u043e\u0434\u0435\u0437\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0431\u043e\u0440\u043e\u0432"
                        " \u043e\u0431\u0449\u0435\u0439 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c\u044e \u0431\u043e\u043b\u0435\u0435 15 \u043c\u0438\u043b\u043b\u0438\u043e\u043d\u043e\u0432 \u0440\u0443\u0431\u043b\u0435\u0439. \u041f\u043e \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u043c \u0434\u0430\u043d\u043d\u044b\u043c \u0441\u043b\u0435\u0434\u0441\u0442\u0432\u0438\u044f, \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043d\u0438\u043a\u0438 \u0434\u0435\u0439\u0441\u0442\u0432\u043e\u0432\u0430\u043b\u0438 \u043f\u043e \u043d\u0430\u0432\u043e\u0434\u043a\u0435, \u043e\u0442\u043b\u0438\u0447\u043d\u043e \u0437\u043d\u0430\u043b\u0438 \u0433\u0440\u0430\u0444\u0438\u043a \u043e\u0431\u0445\u043e\u0434\u0430 \u0442\u0435\u0440\u0440\u0438\u0442\u043e\u0440\u0438\u0438 \u0432\u0435\u0434\u043e\u043c\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0439 \u043e\u0445\u0440\u0430\u043d\u043e\u0439 \u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043b\u0438 \u0434"
                        "\u043b\u044f \u0432\u044b\u0432\u043e\u0437\u0430 \u0442\u044f\u0436\u0435\u043b\u043e\u0433\u043e \u0433\u0440\u0443\u0437\u0430 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u043d\u043e\u043f\u0440\u0438\u0432\u043e\u0434\u043d\u044b\u0439 \u0433\u0440\u0443\u0437\u043e\u0432\u043e\u0439 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c \u0432\u044b\u0441\u043e\u043a\u043e\u0439 \u043f\u0440\u043e\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u0438.\n"
"\u0421\u043a\u0440\u044b\u0432\u0430\u044f\u0441\u044c \u0441 \u043c\u0435\u0441\u0442\u0430 \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0432 \u0443\u0441\u043b\u043e\u0432\u0438\u044f\u0445 \u0441\u0438\u043b\u044c\u043d\u043e\u0439 \u043e\u0441\u0435\u043d\u043d\u0435\u0439 \u043c\u0435\u0442\u0435\u043b\u0438, \u043d\u0430\u043f\u0430\u0434\u0430\u0432\u0448\u0438\u0435 \u043d\u0430\u043f\u0440\u0430\u0432\u0438\u043b\u0438\u0441\u044c \u0432 \u0441\u0442\u043e"
                        "\u0440\u043e\u043d\u0443 \u0440\u0430\u0437\u0432\u0430\u043b\u0438\u043d \u0437\u0430\u0431\u0440\u043e\u0448\u0435\u043d\u043d\u043e\u0433\u043e \u043f\u043e\u0441\u0451\u043b\u043a\u0430-\u043f\u0440\u0438\u0437\u0440\u0430\u043a\u0430 \u0420\u0443\u0434\u043d\u0438\u043a, \u0433\u0434\u0435 \u0441\u043b\u0435\u0434\u044b \u0442\u044f\u0436\u0435\u043b\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0438 \u0437\u0430\u0442\u0435\u0440\u044f\u043b\u0438\u0441\u044c; \u0432 \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u0432 \u0440\u0435\u0433\u0438\u043e\u043d\u0435 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d \u043f\u043b\u0430\u043d \u00ab\u041f\u0435\u0440\u0435\u0445\u0432\u0430\u0442\u00bb, \u043d\u0430 \u0432\u044a\u0435\u0437\u0434\u0430\u0445 \u0432 \u0433\u043e\u0440\u043e\u0434 \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u044b \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u043e\u0441\u0442\u044b "
                        "\u0413\u0418\u0411\u0414\u0414, \u0430 \u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0435 \u0441\u043b\u0443\u0436\u0431\u044b \u043e\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u044e\u0442 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u0435\u0439 \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u044e\u0442 \u043f\u0443\u043d\u043a\u0442\u044b \u043f\u0440\u0438\u0435\u043c\u0430 \u043b\u043e\u043c\u0430 \u0438 \u0447\u0435\u0440\u043d\u044b\u0445 \u043c\u0435\u0442\u0430\u043b\u043b\u043e\u0432.", None))
    # retranslateUi

