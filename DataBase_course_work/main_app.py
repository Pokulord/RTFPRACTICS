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

import json

with open("session.json", "r") as json_session:
    json_session_content = json.load(json_session)

class MainWin(QMainWindow):

    def update_session(self, session_flags): 
        print(json_session_content)

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        all_ui_elements = {
        "service":
        {
            "logs": self.ui.logging_frame,
            "logout_but" : self.ui.logout_but
        },
        "work_with_db":
        {
            "db_button": self.ui.db_work_but,
        }
        }

        self.setWindowTitle("Программа для базы данных")
        self.setWindowIcon(QtGui.QIcon("icons/main_win_icon.png"))
        Ui_Functions.HideElems(self,all_ui_elements)
        Ui_Functions.ShowInterface(self, all_ui_elements, json_session_content)
        self.ui.autorize_but.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.authorize_page))
        self.ui.enable_logs.clicked.connect(lambda check = None ,  flag = ["widgets", "logs"] : self.update_session(flag))
        #Переключение Burger-menu





        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec_())
