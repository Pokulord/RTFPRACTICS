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

    def ShowInterface(self , all_ui_elements):
        global json_session
        self.ui.stackedWidget.setCurrentWidget(self.ui.start_page)
        with open("session.json", "r") as json_session:
            json_session_content = json.load(json_session)
            print("Файл JSON успешно открыт")
            for json_parameter in list(json_session_content["current_session"]["widgets"].keys()):
                # if json_session_content["current_session"]["widgets"][json_parameter] == "True" and json_parameter in list(all_ui_elements["service"].keys() or json_parameter in list(all_ui_elements["work_with_db"].keys())):
                #     all_ui_elements["service"][json_parameter].show()
                for widget_type in list(all_ui_elements.keys()):
                    for widget in list(all_ui_elements[widget_type]):
                        if json_session_content["current_session"]["widgets"][widget] == "True":
                            all_ui_elements[widget_type][widget].show()
                        # print("АКтивные элементы")
                        # print(json_session_content["current_session"]["widgets"][widget])
                


            

