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
        "role": "",
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


allowed_tables = {
     "Администратор":
     []
}

class MainWin(QMainWindow):



    def update_session(self, session_flags):
            Ui_Functions.HideElems(self, all_ui_elements)
            with open("session.json" , "w") as updating_json:
                if session_flags[0] == "widgets":
                    is_true = json_session_content["current_session"]["widgets"][session_flags[-1]] == False
                    json_session_content["current_session"]["widgets"][session_flags[-1]] = is_true
                    json.dump(json_session_content, updating_json, indent= 4) 
                    Ui_Functions.ShowInterface(self, all_ui_elements, json_session_content, cur_widget= ["pages", page_flag], is_auth= is_auth_flag) 
                    return 
                if session_flags[0] == "auth":
                     json_session_content["current_session"]["login"] = session_flags[1]
                     json_session_content["current_session"]["password"] = session_flags[2]
                     json_session_content["current_session"]["cur_db"] = session_flags[3]
                     json_session_content["current_session"]["role"] = session_flags[4]
                     json.dump(json_session_content, updating_json, indent= 4)
                     Ui_Functions.ShowInterface(self, all_ui_elements, json_session_content, ["pages", "work_with_db"], is_auth= True)
                     self.ui.current_role_label.setText(f"Ваша текущая роль : {session_flags[4]}")
                     return
                if session_flags[0] == "logout":
                     json_session_content["current_session"]["login"] = ""
                     json_session_content["current_session"]["password"] = ""
                     json_session_content["current_session"]["cur_db"] = ""
                     json.dump(json_session_content, updating_json, indent= 4)
                     Ui_Functions.ShowInterface(self, all_ui_elements, json_session_content, cur_widget=["pages","start"] ,is_auth= False)
                     return
                self.ui.stackedWidget.setCurrentWidget(all_ui_elements["pages"][page_flag])


    def Send_Query(self, query_type , data_to_insert = None):
        result = self.db.Queries(query_type= query_type, table_to_select=self.ui.table_choice_comboBox.currentText())

        if len(result) == 3:
             Ui_Functions.Update_table(self, result[0], result[1])

    def auth_to_db(self):
        global page_flag
        page_flag = "work_with_db"
        bd_login = self.ui.login_lineedit.text().strip()
        bd_pass = self.ui.password_lineEdit.text().strip()
        need_bd = self.ui.DB_choice_CB.currentText()
        role = self.ui.choice_role.currentText()
        # role = 
        if self.db.connect_to_database("localhost",bd_login, bd_pass, need_bd):
            print("Успешеное подключение к БД")
            self.ui.wrong_pass_label.hide()
            if self.ui.save_session_checkbox.isChecked():
                self.update_session(["auth", bd_login, bd_pass, need_bd, role])
            Ui_Functions.ShowInterface(self, all_ui_elements, json_session_content, ["pages", "work_with_db"], is_auth= True)
            tables_list = self.db.Select_all_db_tables()
        else:
            self.ui.wrong_pass_label.show()


    def __init__(self):
        global all_ui_elements, page_flag, is_auth_flag
        is_auth_flag = False
        page_flag = "start"
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
            "wrong_pass" : self.ui.wrong_pass_label,
        },
        "pages":
        {
             "work_with_db" : self.ui.work_with_db_page,
             "start": self.ui.start_page,
        }
        }
        self.setWindowTitle("Программа для базы данных")
        self.setWindowIcon(QtGui.QIcon("icons/main_win_icon.png"))
        Ui_Functions.HideElems(self,all_ui_elements)
        Ui_Functions.ShowInterface(self, all_ui_elements, json_session_content, is_auth= is_auth_flag)
        # В случае, если в файле сессии содержатся данные о входе
        if json_session_content['current_session']["login"] != "" :
             db_login = json_session_content['current_session']["login"]
             db_pass = json_session_content['current_session']["password"]
             need_db = json_session_content['current_session']["cur_db"]
             role = json_session_content['current_session']["role"]
             if self.db.connect_to_database("localhost", db_login, db_pass, need_db):
                  Ui_Functions.HideElems(self, all_ui_elements)
                  is_auth_flag = True
                  self.ui.current_role_label.setText(f"Ваша текущая роль: {role}")
                  page_flag = "work_with_db"
                  Ui_Functions.HideElems(self, all_ui_elements)
                  Ui_Functions.ShowInterface(self, all_ui_elements, json_session_content, is_auth=True, cur_widget=["pages",page_flag])
                  tables_list = self.db.Select_all_db_tables()
                  Ui_Functions.InsertTables(self, tables_list)
        # Привязка действий к кнопкам
        #######
        self.ui.db_work_but.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.work_with_db_page))          
        self.ui.autorize_but.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.authorize_page))
        self.ui.enable_logs.clicked.connect(lambda check = None ,  flag = ["widgets", "logs"] : self.update_session(flag))
        self.ui.Authorize_button.clicked.connect(self.auth_to_db)
        self.ui.db_work_but.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.work_with_db_page))
        self.ui.logout_but.clicked.connect(lambda : self.update_session(["logout"]))
        self.ui.choice_table_but.clicked.connect(lambda : self.Send_Query("select"))
        #######
        self.ui.bd_table.setSortingEnabled(True)
        #Переключение Burger-menu





        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec_())
