# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceQfXRFo.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(949, 550)
        MainWindow.setMaximumSize(QSize(999999, 557))
        MainWindow.setStyleSheet(u"background-color: rgb(39, 44, 54)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Topbar = QFrame(self.centralwidget)
        self.Topbar.setObjectName(u"Topbar")
        self.Topbar.setMaximumSize(QSize(16777215, 50))
        self.Topbar.setFrameShape(QFrame.NoFrame)
        self.Topbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Topbar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.togglemenu = QFrame(self.Topbar)
        self.togglemenu.setObjectName(u"togglemenu")
        self.togglemenu.setMaximumSize(QSize(90, 58))
        self.togglemenu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.togglemenu.setFrameShape(QFrame.NoFrame)
        self.togglemenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.togglemenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle_menu_but = QPushButton(self.togglemenu)
        self.toggle_menu_but.setObjectName(u"toggle_menu_but")
        self.toggle_menu_but.setMinimumSize(QSize(58, 58))
        self.toggle_menu_but.setStyleSheet(u"border: none ;")
        icon = QIcon()
        icon.addFile(u"icons/burger_icon.png", QSize(), QIcon.Normal, QIcon.On)
        self.toggle_menu_but.setIcon(icon)
        self.toggle_menu_but.setIconSize(QSize(50, 58))

        self.verticalLayout_2.addWidget(self.toggle_menu_but)


        self.horizontalLayout.addWidget(self.togglemenu)

        self.frame_top = QFrame(self.Topbar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Topbar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setEnabled(True)
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.Content)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(90, 16777215))
        self.left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.left_menu.setFrameShape(QFrame.NoFrame)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.top_left_menu = QFrame(self.left_menu)
        self.top_left_menu.setObjectName(u"top_left_menu")
        self.top_left_menu.setFrameShape(QFrame.StyledPanel)
        self.top_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.top_left_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.autorize_but = QPushButton(self.top_left_menu)
        self.autorize_but.setObjectName(u"autorize_but")
        self.autorize_but.setMinimumSize(QSize(90, 0))
        font = QFont()
        font.setPointSize(9)
        self.autorize_but.setFont(font)
        self.autorize_but.setStyleSheet(u"QPushButton \n"
"{\n"
"	color: white;\n"
"	border: none ;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color:rgb(12, 13, 16)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/autorize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.autorize_but.setIcon(icon1)
        self.autorize_but.setIconSize(QSize(30, 58))

        self.verticalLayout_4.addWidget(self.autorize_but)

        self.info_but = QPushButton(self.top_left_menu)
        self.info_but.setObjectName(u"info_but")
        self.info_but.setMinimumSize(QSize(90, 0))
        self.info_but.setFont(font)
        self.info_but.setStyleSheet(u"QPushButton \n"
"{\n"
"	color: white;\n"
"	border: none ;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color:rgb(12, 13, 16)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/info_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_but.setIcon(icon2)
        self.info_but.setIconSize(QSize(30, 58))

        self.verticalLayout_4.addWidget(self.info_but)


        self.verticalLayout_3.addWidget(self.top_left_menu, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.bottom_left_menus = QFrame(self.left_menu)
        self.bottom_left_menus.setObjectName(u"bottom_left_menus")
        self.bottom_left_menus.setFrameShape(QFrame.StyledPanel)
        self.bottom_left_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.bottom_left_menus)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.logout_but = QPushButton(self.bottom_left_menus)
        self.logout_but.setObjectName(u"logout_but")
        self.logout_but.setMinimumSize(QSize(90, 0))
        self.logout_but.setStyleSheet(u"QPushButton \n"
"{\n"
"	color: white;\n"
"	border: none ;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color:rgb(12, 13, 16)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/logout_but.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_but.setIcon(icon3)
        self.logout_but.setIconSize(QSize(30, 58))

        self.verticalLayout_10.addWidget(self.logout_but)


        self.verticalLayout_3.addWidget(self.bottom_left_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.left_menu)

        self.main_pages = QFrame(self.Content)
        self.main_pages.setObjectName(u"main_pages")
        self.main_pages.setFrameShape(QFrame.NoFrame)
        self.main_pages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_pages)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Info_page = QWidget()
        self.Info_page.setObjectName(u"Info_page")
        self.verticalLayout_9 = QVBoxLayout(self.Info_page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.info_page_frame = QFrame(self.Info_page)
        self.info_page_frame.setObjectName(u"info_page_frame")
        self.info_page_frame.setFrameShape(QFrame.StyledPanel)
        self.info_page_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.info_page_frame)

        self.stackedWidget.addWidget(self.Info_page)
        self.authorize_page = QWidget()
        self.authorize_page.setObjectName(u"authorize_page")
        self.verticalLayout_5 = QVBoxLayout(self.authorize_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.authorize_frame = QFrame(self.authorize_page)
        self.authorize_frame.setObjectName(u"authorize_frame")
        self.authorize_frame.setMinimumSize(QSize(0, 500))
        self.authorize_frame.setFrameShape(QFrame.StyledPanel)
        self.authorize_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.authorize_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.data_input_frame = QFrame(self.authorize_frame)
        self.data_input_frame.setObjectName(u"data_input_frame")
        self.data_input_frame.setMinimumSize(QSize(0, 300))
        self.data_input_frame.setFrameShape(QFrame.StyledPanel)
        self.data_input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.data_input_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 20, 0, 0)
        self.login_lineedit = QLineEdit(self.data_input_frame)
        self.login_lineedit.setObjectName(u"login_lineedit")
        self.login_lineedit.setMinimumSize(QSize(321, 31))
        self.login_lineedit.setMaximumSize(QSize(321, 31))
        self.login_lineedit.setLayoutDirection(Qt.RightToLeft)
        self.login_lineedit.setStyleSheet(u"background-color: white;\n"
"border-radius:10px")
        self.login_lineedit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.login_lineedit)

        self.password_lineEdit = QLineEdit(self.data_input_frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMaximumSize(QSize(321, 31))
        self.password_lineEdit.setStyleSheet(u"border-radius:10px;\n"
"background-color:white;")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.password_lineEdit)

        self.checkBox = QCheckBox(self.data_input_frame)
        self.checkBox.setObjectName(u"checkBox")
        font1 = QFont()
        font1.setPointSize(10)
        self.checkBox.setFont(font1)
        self.checkBox.setStyleSheet(u"color:white")

        self.verticalLayout_8.addWidget(self.checkBox)

        self.DB_choice_CB = QComboBox(self.data_input_frame)
        self.DB_choice_CB.setObjectName(u"DB_choice_CB")
        self.DB_choice_CB.setMaximumSize(QSize(321, 31))
        self.DB_choice_CB.setStyleSheet(u"background-color:white")
        self.DB_choice_CB.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_8.addWidget(self.DB_choice_CB)

        self.checkBox_2 = QCheckBox(self.data_input_frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font1)
        self.checkBox_2.setStyleSheet(u"color:white")

        self.verticalLayout_8.addWidget(self.checkBox_2)

        self.label = QLabel(self.data_input_frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(321, 50))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white")

        self.verticalLayout_8.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.data_input_frame, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.authorize_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Authorize_button = QPushButton(self.frame_2)
        self.Authorize_button.setObjectName(u"Authorize_button")
        self.Authorize_button.setEnabled(True)
        self.Authorize_button.setMinimumSize(QSize(162, 39))
        self.Authorize_button.setMaximumSize(QSize(162, 39))
        font2 = QFont()
        font2.setFamily(u"Montserrat")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.Authorize_button.setFont(font2)
        self.Authorize_button.setStyleSheet(u"QPushButton\n"
"{\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: rgb(64, 72, 89);\n"
"}")

        self.verticalLayout_7.addWidget(self.Authorize_button, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.authorize_frame)

        self.stackedWidget.addWidget(self.authorize_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.main_pages)

        self.logging_frame = QFrame(self.Content)
        self.logging_frame.setObjectName(u"logging_frame")
        self.logging_frame.setMinimumSize(QSize(400, 0))
        self.logging_frame.setFrameShape(QFrame.StyledPanel)
        self.logging_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.logging_frame)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_menu_but.setText("")
        self.autorize_but.setText("")
        self.info_but.setText("")
        self.logout_but.setText("")
        self.login_lineedit.setText("")
        self.login_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d.........", None))
        self.password_lineEdit.setText("")
        self.password_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c........", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.DB_choice_CB.setCurrentText("")
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0435\u0441\u0441\u0438\u044e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d \u0438 \u043f\u0430\u0440\u043e\u043b\u044c \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e!!!", None))
        self.Authorize_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e\u0419\u0422\u0418", None))
    # retranslateUi

