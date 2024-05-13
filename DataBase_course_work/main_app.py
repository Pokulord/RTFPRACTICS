###################################################
##
## Программа для взаимодействия с базой данных,
## созданная в рамках курсовой работы
## v 1.0 (Early Beta)
## Interface Was Created with PyQt5 and PySide2
###################################################


#Модули для отображения интерфейса
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# Импорт интерфейса
from ui_interface import Ui_MainWindow

#Импорт Функций интерфейса
from ui_functions import *

# Импорт функций для работы с БД

from db_functions import Connect_to_DB

import os
import json

if "session.json" not in os.listdir() :
    session_content = {
    "current_session" :
    {
        "login" : "",
        "password" : "",
        "widgets":
        {
            "logs" : False,
            "db_button" : False
        },
        "cur_db" : "",
        "cur_table" : ""
    }
    }
    with open("session.json" , "w") as creating_json:
            json.dump(session_content, creating_json, indent= 4)

with open("session.json", "r") as json_session:
    json_session_content = json.load(json_session)

class MainWin(QMainWindow):

    def auth_to_db(self):
        bd_login = self.ui.login_lineedit.text().strip()
        bd_pass = self.ui.password_lineEdit.text().strip()
        need_bd = self.ui.DB_choice_CB.currentText()
        if self.db.connect_to_database("localhost",bd_login, bd_pass, need_bd):
             print("Успешеное подключение к БД")

    def update_session(self, session_flags): 
            with open("session.json" , "w") as updating_json:
                if session_flags[0] == "widgets":
                    is_true = json_session_content["current_session"]["widgets"][session_flags[-1]] == False
                    json_session_content["current_session"]["widgets"][session_flags[-1]] = is_true
                    json.dump(json_session_content, updating_json, indent= 4)
                    Ui_Functions.HideElems(self, all_ui_elements)
                    Ui_Functions.ShowInterface(self, all_ui_elements, json_session_content)

    def __init__(self):
        global all_ui_elements
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Connect_to_DB()
        all_ui_elements = {
        "service":
        {
            "logs": self.ui.logging_frame,
            "logout_but" : self.ui.logout_but
        },
        "work_with_db":
        {
            "db_button": self.ui.db_work_but,
            "wrong_pass" : self.ui.wrong_pass_label
        }
        }
        self.setWindowTitle("Программа для базы данных")
        self.setWindowIcon(QtGui.QIcon("icons/main_win_icon.png"))
        Ui_Functions.HideElems(self,all_ui_elements)
        Ui_Functions.ShowInterface(self, all_ui_elements, json_session_content)
        self.ui.autorize_but.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.authorize_page))
        self.ui.enable_logs.clicked.connect(lambda check = None ,  flag = ["widgets", "logs"] : self.update_session(flag))
        self.ui.Authorize_button.clicked.connect(self.auth_to_db)
        #Переключение Burger-menu





        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec_())
