from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

cur_page = 'login'
change_flag = False

class UpdatePage():
    def __init__(self):
        super().__init__()

    @property
    def cur_page(self):
        return cur_page

    @cur_page.setter
    def cur_page(self, new_val):
        global cur_page
        cur_page = new_val

    @property
    def change_flag(self):
        return change_flag
    
    @change_flag.setter
    def change_flag(self, new_val):
        global change_flag
        change_flag = new_val