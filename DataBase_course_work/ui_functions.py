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


# Конвертируем дату в строку

def conver_date_to_string(date_object):
    if date_object is None:
        return
    return date_object.strftime("%d-%m-%Y")

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
        if not is_auth:
            self.ui.autorize_but.show()
        if json_session_content["current_session"]["widgets"]["logs"] :
            self.ui.enable_logs.setChecked(True)
        if cur_widget != None:
            self.ui.stackedWidget.setCurrentWidget(all_ui_elements[cur_widget[0]][cur_widget[1]])

    def InsertTables(self, list_of_tables):
        for table_cell in list_of_tables:
            for table in table_cell:
                print(f"Добавляю таблицу {table}")
                self.ui.table_choice_comboBox.addItem(table)

    def Update_table(self, list_of_columns = None, t_rows = None):
        if list_of_columns is not  None and t_rows is not None:
            self.ui.bd_table.setColumnCount(len(list_of_columns))
            self.ui.bd_table.setHorizontalHeaderLabels(list_of_columns)
            self.ui.bd_table.setRowCount(0)
            self.ui.bd_table.setRowCount(len(t_rows) + 1)
            t_rows = [list(row) for row in t_rows]
            for row in range(len(t_rows)):
                for row_element in range(len(t_rows[row])):
                    try:
                        if isinstance(t_rows[row][row_element], datetime.date):
                            t_rows[row][row_element] = conver_date_to_string(t_rows[row][row_element])
                    except:
                        pass
            print(t_rows)
            for row in range(len(t_rows)):
                for row_str in range(len(t_rows[row])):
                    self.ui.bd_table.setItem(row, row_str, QtWidgets.QTableWidgetItem(str(t_rows[row][row_str])))

                


            


