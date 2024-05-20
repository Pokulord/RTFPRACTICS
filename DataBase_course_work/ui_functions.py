##################################################
## Программа для взаимодействия с базой данных,
## созданная в рамках курсовой работы
## v 1.0 (Early Beta)
## Interface Was Created with PyQt5 and PySide2
###################################################

# Импорт интрфейса
from main_app import *
# Импорт модулей для работы с сессией через JSON-файл
import json
from datetime import datetime


# Класс для функций

class Ui_Functions(MainWin):

    #Функця для переключения Burger-menu
    def ToggleBurgerMenu(self, max_width, enable):
        pass

    #Скрыть изначально ненужные элементы
    def HideElems(sefl,ui_elements):
        for key in list(ui_elements.keys()):
            for widget in ui_elements[key]:
                ui_elements[key][widget].hide()

    def ShowInterface(self , all_ui_elements, json_session_content, cur_widget = None, is_auth = False):
        print(cur_widget)
        global json_session
        self.ui.stackedWidget.setCurrentWidget(self.ui.start_page)
        print("Файл JSON успешно открыт")
        for json_parameter in list(json_session_content["current_session"]["widgets"].keys()):
            for widget_type in list(all_ui_elements.keys()):
                for widget in list(all_ui_elements[widget_type]):
                    try:
                        if json_session_content["current_session"]["widgets"][widget] :
                            all_ui_elements[widget_type][widget].show()
                    except:
                        pass
        if is_auth:
            self.ui.db_work_but.show()
            self.ui.logout_but.show()
            self.ui.autorize_but.hide()
        if json_session_content["current_session"]["widgets"]["logs"] :
            self.ui.enable_logs.setChecked(True)
        if cur_widget != None: 
            self.ui.stackedWidget.setCurrentWidget(all_ui_elements[cur_widget[0]][cur_widget[1]])

        # if is_auth:

                


            


