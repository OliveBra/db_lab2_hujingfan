from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect
import pymysql
from PyQt6.QtWidgets import QTableWidget
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QAbstractItemView
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap
# Connect to the database
ssms = pymysql.connect(host="127.0.0.1", user="root",
                       password="314159", database="ssms")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Set window size
        self.setGeometry(400, 200, 700, 600)
        self.setWindowTitle('Main Application')

        # 1. Login in page part
        # Login form
        self.signin = QLabel('Please sign in', self)
        self.user = QLabel('Username:', self)
        self.username_input = QLineEdit(self)
        self.password = QLabel('Password:', self)
        self.password_input = QLineEdit(self)
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login)
        # place
        self.signin.setGeometry(QRect(310, 70, 111, 41))
        self.user.setGeometry(QRect(210, 130, 131, 31))
        self.username_input.setGeometry(QRect(210, 170, 300, 20))
        self.password.setGeometry(QRect(210, 220, 71, 16))
        self.password_input.setGeometry(QRect(210, 250, 300, 20))
        self.login_button.setGeometry(QRect(320, 320, 75, 25))

        # 2. Main page part
        self.student_button = QPushButton('学生基本信息', self)
        self.student_button.clicked.connect(self.display_student_page)
        self.student_button.setGeometry(QRect(250, 90, 200, 25))

        self.class_button = QPushButton('班级信息', self)
        self.class_button.setGeometry(QRect(250, 130, 200, 25))
        self.class_button.clicked.connect(self.display_class_page)

        self.course_button = QPushButton('课程信息', self)
        self.course_button.setGeometry(QRect(250, 210, 200, 25))
        self.course_button.clicked.connect(self.display_course_page)

        self.stu_cou_button = QPushButton('学生选课信息', self)
        self.stu_cou_button.setGeometry(QRect(250, 240, 200, 25))
        self.stu_cou_button.clicked.connect(self.display_stu_cou_page)

        self.score_button = QPushButton('成绩信息', self)
        self.score_button.setGeometry(QRect(250, 270, 200, 25))
        self.score_button.clicked.connect(self.display_score_page)

        # 3. student part
        self.student_button1 = QPushButton('学生基本信息查询', self)
        self.student_button1.clicked.connect(self.display_student_search_page)
        self.student_button1.setGeometry(QRect(250, 90, 200, 25))
        self.student_back_button = QPushButton('<---Back', self)
        self.student_back_button.clicked.connect(self.display_main_page)
        self.student_back_button.setGeometry(QRect(0, 0, 200, 25))

        self.student_button2 = QPushButton('学生基本信息更新', self)
        self.student_button2.setGeometry(QRect(250, 130, 200, 25))
        self.student_button2.clicked.connect(self.display_student_update_page)

        # 4. student search part
        self.student_search_back_button = QPushButton('<---Back', self)
        self.student_search_back_button.clicked.connect(
            self.display_student_page)
        self.student_search_back_button.setGeometry(QRect(0, 0, 200, 25))

        self.stu_search_label_1 = QLabel('一、学生基本信息查询', self)
        self.stu_search_label_1.setGeometry(QRect(80, 70, 141, 20))
        self.stu_search_label_2 = QLabel('按学生学号查询', self)
        self.stu_search_label_2.setGeometry(QRect(80, 110, 121, 20))
        self.stu_search_lineEdit1 = QLineEdit(self)
        self.stu_search_lineEdit1.setGeometry(QRect(80, 140, 161, 20))
        self.stu_search_button1 = QPushButton('查询', self)
        self.stu_search_button1.setGeometry(QRect(250, 140, 75, 24))
        self.stu_search_button1.clicked.connect(self.stu_search_by_id)
        self.stu_search_label_3 = QLabel('按学生姓名查询', self)
        self.stu_search_label_3.setGeometry(QRect(80, 170, 121, 20))
        self.stu_search_lineEdit2 = QLineEdit(self)
        self.stu_search_lineEdit2.setGeometry(QRect(80, 200, 161, 20))
        self.stu_search_button2 = QPushButton('查询', self)
        self.stu_search_button2.setGeometry(QRect(250, 200, 75, 24))
        self.stu_search_button2.clicked.connect(self.stu_search_by_name)

        # 5.student update part
        self.student_update_back_button = QPushButton('<---Back', self)
        self.student_update_back_button.clicked.connect(
            self.display_student_page)
        self.student_update_back_button.setGeometry(QRect(0, 0, 200, 25))

        # 5.1 student revise part
        self.student_revise_label_1 = QLabel('一、学生基本信息修改', self)
        self.student_revise_label_1.setGeometry(QRect(80, 70, 141, 20))
        self.student_revise_label_2 = QLabel('输入学生学号修改', self)
        self.student_revise_label_2.setGeometry(QRect(80, 110, 121, 20))
        self.student_revise_lineEdit1 = QLineEdit(self)
        self.student_revise_lineEdit1.setGeometry(QRect(80, 140, 161, 20))
        self.student_revise_button1 = QPushButton('打开', self)
        self.student_revise_button1.setGeometry(QRect(250, 140, 75, 24))
        self.student_revise_button1.clicked.connect(self.stu_revise_open)

        # 5.2 student add part
        self.student_add_label_1 = QLabel('二、学生信息添加', self)
        self.student_add_label_1.setGeometry(QRect(80, 170, 141, 20))
        self.student_add_button = QPushButton('添加学生信息', self)
        self.student_add_button.setGeometry(QRect(80, 200, 161, 24))
        self.student_add_button.clicked.connect(self.stu_add_open)

        # 5.3 student delete part
        self.student_delete_label_1 = QLabel('三、学生信息删除', self)
        self.student_delete_label_1.setGeometry(QRect(80, 230, 141, 20))
        self.student_delete_label_2 = QLabel('输入学生学号删除', self)
        self.student_delete_label_2.setGeometry(QRect(80, 260, 121, 20))
        self.student_delete_lineEdit1 = QLineEdit(self)
        self.student_delete_lineEdit1.setGeometry(QRect(80, 290, 161, 20))
        self.student_delete_button1 = QPushButton('删除', self)
        self.student_delete_button1.setGeometry(QRect(250, 290, 75, 24))
        self.student_delete_button1.clicked.connect(self.stu_delete)

        # 6 class part
        self.class_back_button = QPushButton('<---Back', self)
        self.class_back_button.setGeometry(QRect(0, 0, 200, 25))
        self.class_back_button.clicked.connect(self.display_main_page)

        self.class_label_1 = QLabel('一、班级信息查询', self)
        self.class_label_1.setGeometry(QRect(80, 70, 141, 20))
        self.class_search_button = QPushButton('查询所有班级信息', self)
        self.class_search_button.setGeometry(QRect(80, 110, 161, 24))
        self.class_search_button.clicked.connect(self.class_search)

        self.class_label_2 = QLabel('二、班级信息更新', self)
        self.class_label_2.setGeometry(QRect(80, 170, 141, 20))
        self.class_label_5 = QLabel('选择一个班级进行修改,输入班级id', self)
        self.class_label_5.setGeometry(QRect(80, 200, 200, 20))
        self.class_lieEdit1 = QLineEdit(self)
        self.class_lieEdit1.setGeometry(QRect(80, 230, 161, 20))
        self.class_revise_button = QPushButton('打开', self)
        self.class_revise_button.setGeometry(QRect(250, 230, 75, 24))
        self.class_revise_button.clicked.connect(self.class_revise_open)

        self.class_label_3 = QLabel('三、班级信息添加', self)
        self.class_label_3.setGeometry(QRect(80, 260, 141, 20))
        self.class_add_button = QPushButton('添加班级信息', self)
        self.class_add_button.setGeometry(QRect(80, 300, 161, 24))
        self.class_add_button.clicked.connect(self.class_add_open)

        self.class_label_4 = QLabel('四、班级信息删除', self)
        self.class_label_4.setGeometry(QRect(80, 350, 141, 20))
        self.class_label_6 = QLabel('输入班级id删除', self)
        self.class_label_6.setGeometry(QRect(80, 380, 121, 20))
        self.class_delete_lineEdit1 = QLineEdit(self)
        self.class_delete_lineEdit1.setGeometry(QRect(80, 410, 161, 20))
        self.class_delete_button = QPushButton('删除', self)
        self.class_delete_button.setGeometry(QRect(250, 410, 75, 24))
        self.class_delete_button.clicked.connect(self.class_delete_open)

        # 7 course part
        self.course_back_button = QPushButton('<---Back', self)
        self.course_back_button.setGeometry(QRect(0, 0, 200, 25))
        self.course_back_button.clicked.connect(self.display_main_page)

        self.course_label_1 = QLabel('一、课程信息查询', self)
        self.course_label_1.setGeometry(QRect(80, 70, 141, 20))
        self.course_label_2 = QLabel('查询所有课程信息', self)
        self.course_label_2.setGeometry(QRect(80, 110, 121, 20))
        self.course_search_button = QPushButton('查询', self)
        self.course_search_button.setGeometry(QRect(250, 110, 75, 24))
        self.course_search_button.clicked.connect(self.course_search)

        self.course_label_3 = QLabel('二、课程信息更新', self)
        self.course_label_3.setGeometry(QRect(80, 140, 141, 20))
        self.course_label_4 = QLabel('选择一个课程进行修改,输入课程id', self)
        self.course_label_4.setGeometry(QRect(80, 170, 200, 20))
        self.course_lineEdit1 = QLineEdit(self)
        self.course_lineEdit1.setGeometry(QRect(80, 200, 161, 20))
        self.course_revise_button = QPushButton('打开', self)
        self.course_revise_button.setGeometry(QRect(250, 200, 75, 24))
        self.course_revise_button.clicked.connect(self.course_revise_open)

        self.course_label_5 = QLabel('三、课程信息添加', self)
        self.course_label_5.setGeometry(QRect(80, 230, 141, 20))
        self.course_add_button = QPushButton('添加课程信息', self)
        self.course_add_button.setGeometry(QRect(80, 260, 161, 24))
        self.course_add_button.clicked.connect(self.course_add_open)

        self.course_label_6 = QLabel('四、课程信息删除', self)
        self.course_label_6.setGeometry(QRect(80, 290, 141, 20))
        self.course_label_7 = QLabel('输入课程id删除', self)
        self.course_label_7.setGeometry(QRect(80, 320, 121, 20))
        self.course_lineEdit2 = QLineEdit(self)
        self.course_lineEdit2.setGeometry(QRect(80, 350, 161, 20))
        self.course_delete_button = QPushButton('删除', self)
        self.course_delete_button.setGeometry(QRect(250, 350, 75, 24))
        self.course_delete_button.clicked.connect(self.course_delete_open)

        # 8. stu_course part
        self.stu_cou_back_button = QPushButton('<---Back', self)
        self.stu_cou_back_button.setGeometry(QRect(0, 0, 200, 25))
        self.stu_cou_back_button.clicked.connect(self.display_main_page)

        self.stu_cou_label_1 = QLabel('一、学生选课信息查询', self)
        self.stu_cou_label_1.setGeometry(QRect(80, 70, 141, 20))
        self.stu_cou_label_2 = QLabel('输入学生学号查询', self)
        self.stu_cou_label_2.setGeometry(QRect(80, 110, 121, 20))
        self.stu_cou_lineEdit1 = QLineEdit(self)
        self.stu_cou_lineEdit1.setGeometry(QRect(80, 140, 161, 20))
        self.stu_cou_button1 = QPushButton('查询', self)
        self.stu_cou_button1.setGeometry(QRect(250, 140, 75, 24))
        self.stu_cou_button1.clicked.connect(self.stu_cou_search_by_id)

        self.stu_cou_label_3 = QLabel('二、学生选课', self)
        self.stu_cou_label_3.setGeometry(QRect(80, 170, 141, 20))
        self.stu_cou_label_4 = QLabel('输入学生学号选课', self)
        self.stu_cou_label_4.setGeometry(QRect(80, 200, 121, 20))
        self.stu_cou_lineEdit2 = QLineEdit(self)
        self.stu_cou_lineEdit2.setGeometry(QRect(80, 230, 161, 20))
        self.stu_cou_label_5 = QLabel('输入课程id选课', self)
        self.stu_cou_label_5.setGeometry(QRect(80, 260, 121, 20))
        self.stu_cou_lineEdit3 = QLineEdit(self)
        self.stu_cou_lineEdit3.setGeometry(QRect(80, 290, 161, 20))
        self.stu_cou_button2 = QPushButton('选课', self)
        self.stu_cou_button2.setGeometry(QRect(250, 290, 75, 24))
        self.stu_cou_button2.clicked.connect(self.stu_cou_select)

        self.stu_cou_label_6 = QLabel('三、学生退课', self)
        self.stu_cou_label_6.setGeometry(QRect(80, 320, 141, 20))
        self.stu_cou_label_7 = QLabel('输入学生学号退课', self)
        self.stu_cou_label_7.setGeometry(QRect(80, 350, 121, 20))
        self.stu_cou_lineEdit4 = QLineEdit(self)
        self.stu_cou_lineEdit4.setGeometry(QRect(80, 380, 161, 20))
        self.stu_cou_label_8 = QLabel('输入课程id退课', self)
        self.stu_cou_label_8.setGeometry(QRect(80, 410, 121, 20))
        self.stu_cou_lineEdit5 = QLineEdit(self)
        self.stu_cou_lineEdit5.setGeometry(QRect(80, 440, 161, 20))
        self.stu_cou_button3 = QPushButton('退课', self)
        self.stu_cou_button3.setGeometry(QRect(250, 440, 75, 24))
        self.stu_cou_button3.clicked.connect(self.stu_cou_delete)

        # 9 score part
        self.score_back_button = QPushButton('<---Back', self)
        self.score_back_button.setGeometry(QRect(0, 0, 200, 25))
        self.score_back_button.clicked.connect(self.display_main_page)

        self.score_label_1 = QLabel('一、成绩信息查询', self)
        self.score_label_1.setGeometry(QRect(80, 70, 141, 20))
        self.score_label_2 = QLabel('输入学生学号查询', self)
        self.score_label_2.setGeometry(QRect(80, 110, 121, 20))
        self.score_lineEdit1 = QLineEdit(self)
        self.score_lineEdit1.setGeometry(QRect(80, 140, 161, 20))
        self.score_button1 = QPushButton('查询', self)
        self.score_button1.setGeometry(QRect(250, 140, 75, 24))
        self.score_button1.clicked.connect(self.score_search_by_id)

        self.score_label_3 = QLabel('二、成绩信息修改', self)
        self.score_label_3.setGeometry(QRect(80, 170, 141, 20))
        self.score_label_4 = QLabel('输入学生学号修改', self)
        self.score_label_4.setGeometry(QRect(80, 200, 121, 20))
        self.score_lineEdit2 = QLineEdit(self)
        self.score_lineEdit2.setGeometry(QRect(80, 230, 161, 20))
        self.score_label_5 = QLabel('输入课程id修改', self)
        self.score_label_5.setGeometry(QRect(80, 260, 121, 20))
        self.score_lineEdit3 = QLineEdit(self)
        self.score_lineEdit3.setGeometry(QRect(80, 290, 161, 20))
        self.score_label_6 = QLabel('输入成绩修改', self)
        self.score_label_6.setGeometry(QRect(80, 320, 121, 20))
        self.score_lineEdit4 = QLineEdit(self)
        self.score_lineEdit4.setGeometry(QRect(80, 350, 161, 20))
        self.score_button2 = QPushButton('修改', self)
        self.score_button2.setGeometry(QRect(250, 350, 75, 24))
        self.score_button2.clicked.connect(self.score_revise)

        self.score_label_7 = QLabel('三、成绩信息添加', self)
        self.score_label_7.setGeometry(QRect(80, 380, 141, 20))
        self.score_label_8 = QLabel('输入学生学号添加', self)
        self.score_label_8.setGeometry(QRect(80, 410, 121, 20))
        self.score_lineEdit5 = QLineEdit(self)
        self.score_lineEdit5.setGeometry(QRect(80, 440, 161, 20))
        self.score_label_9 = QLabel('输入课程id添加', self)
        self.score_label_9.setGeometry(QRect(80, 470, 121, 20))
        self.score_lineEdit6 = QLineEdit(self)
        self.score_lineEdit6.setGeometry(QRect(80, 500, 161, 20))
        self.score_label_10 = QLabel('输入成绩添加', self)
        self.score_label_10.setGeometry(QRect(80, 530, 121, 20))
        self.score_lineEdit7 = QLineEdit(self)
        self.score_lineEdit7.setGeometry(QRect(80, 560, 161, 20))
        self.score_button3 = QPushButton('添加', self)
        self.score_button3.setGeometry(QRect(250, 560, 75, 24))
        self.score_button3.clicked.connect(self.score_add)

        self.score_label_11 = QLabel('四、成绩信息删除', self)
        self.score_label_11.setGeometry(QRect(80, 590, 141, 20))
        self.score_label_12 = QLabel('输入学生学号删除', self)
        self.score_label_12.setGeometry(QRect(80, 620, 121, 20))
        self.score_lineEdit8 = QLineEdit(self)
        self.score_lineEdit8.setGeometry(QRect(80, 650, 161, 20))
        self.score_label_13 = QLabel('输入课程id删除', self)
        self.score_label_13.setGeometry(QRect(80, 680, 121, 20))
        self.score_lineEdit9 = QLineEdit(self)
        self.score_lineEdit9.setGeometry(QRect(80, 710, 161, 20))
        self.score_button4 = QPushButton('删除', self)
        self.score_button4.setGeometry(QRect(250, 710, 75, 24))
        self.score_button4.clicked.connect(self.score_delete)

        # 启动！
        self.display_login_page()

    def hide_all_widgets(self):
        for widget in self.findChildren(QWidget):
            widget.hide()

    def display_login_page(self):
        self.hide_all_widgets()
        self.signin.show()
        self.user.show()
        self.username_input.show()
        self.password.show()
        self.password_input.show()
        self.login_button.show()

    def display_main_page(self):
        self.hide_all_widgets()
        self.student_button.show()
        self.class_button.show()
        self.course_button.show()
        self.score_button.show()
        self.stu_cou_button.show()

    def display_student_page(self):
        self.hide_all_widgets()
        self.student_button1.show()
        self.student_back_button.show()
        self.student_button2.show()

    def display_student_search_page(self):
        self.hide_all_widgets()
        self.student_search_back_button.show()
        self.stu_search_label_1.show()
        self.stu_search_label_2.show()
        self.stu_search_lineEdit1.show()
        self.stu_search_button1.show()
        self.stu_search_label_3.show()
        self.stu_search_lineEdit2.show()
        self.stu_search_button2.show()

    def display_student_update_page(self):
        self.hide_all_widgets()
        self.student_update_back_button.show()
        self.student_revise_label_1.show()
        self.student_revise_label_2.show()
        self.student_revise_lineEdit1.show()
        self.student_revise_button1.show()
        self.student_add_label_1.show()
        self.student_add_button.show()
        self.student_delete_label_1.show()
        self.student_delete_label_2.show()
        self.student_delete_lineEdit1.show()
        self.student_delete_button1.show()

    def display_class_page(self):
        self.hide_all_widgets()
        self.class_back_button.show()
        self.class_label_1.show()
        self.class_search_button.show()
        self.class_label_2.show()
        self.class_label_5.show()
        self.class_lieEdit1.show()
        self.class_revise_button.show()
        self.class_label_3.show()
        self.class_add_button.show()
        self.class_label_4.show()
        self.class_label_6.show()
        self.class_delete_lineEdit1.show()
        self.class_delete_button.show()

    def display_course_page(self):
        self.hide_all_widgets()
        self.course_back_button.show()
        self.course_label_1.show()
        self.course_label_2.show()
        self.course_search_button.show()
        self.course_label_3.show()
        self.course_label_4.show()
        self.course_lineEdit1.show()
        self.course_revise_button.show()
        self.course_label_5.show()
        self.course_add_button.show()
        self.course_label_6.show()
        self.course_label_7.show()
        self.course_lineEdit2.show()
        self.course_delete_button.show()

    def display_score_page(self):
        self.hide_all_widgets()
        self.score_back_button.show()
        self.score_label_1.show()
        self.score_label_2.show()
        self.score_lineEdit1.show()
        self.score_button1.show()
        self.score_label_3.show()
        self.score_label_4.show()
        self.score_lineEdit2.show()
        self.score_label_5.show()
        self.score_lineEdit3.show()
        self.score_label_6.show()
        self.score_lineEdit4.show()
        self.score_button2.show()
        self.score_label_7.show()
        self.score_label_8.show()
        self.score_lineEdit5.show()
        self.score_label_9.show()
        self.score_lineEdit6.show()
        self.score_label_10.show()
        self.score_lineEdit7.show()
        self.score_button3.show()
        self.score_label_11.show()
        self.score_label_12.show()
        self.score_lineEdit8.show()
        self.score_label_13.show()
        self.score_lineEdit9.show()
        self.score_button4.show()

    def display_stu_cou_page(self):
        self.hide_all_widgets()
        self.stu_cou_back_button.show()
        self.stu_cou_label_1.show()
        self.stu_cou_label_2.show()
        self.stu_cou_lineEdit1.show()
        self.stu_cou_button1.show()
        self.stu_cou_label_3.show()
        self.stu_cou_label_4.show()
        self.stu_cou_lineEdit2.show()
        self.stu_cou_label_5.show()
        self.stu_cou_lineEdit3.show()
        self.stu_cou_button2.show()
        self.stu_cou_label_6.show()
        self.stu_cou_label_7.show()
        self.stu_cou_lineEdit4.show()
        self.stu_cou_label_8.show()
        self.stu_cou_lineEdit5.show()
        self.stu_cou_button3.show()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == 'admin' and password == 'password':
            self.display_main_page()
        else:
            QMessageBox.warning(self, 'Login failed',
                                'Invalid username or password')

    def stu_show_page(self, data, photo_address):
        self.stu_showpage = QWidget()
        self.stu_showpage.setWindowTitle('学生基本信息查询结果')
        self.stu_showpage.setGeometry(450, 250, 450, 450)
        self.stu_showpage_label1 = QLabel(
            '学号：' + str(data[0]), self.stu_showpage)
        self.stu_showpage_label1.setGeometry(QRect(30, 30, 121, 20))
        self.stu_showpage_label2 = QLabel('姓名：' + data[1], self.stu_showpage)
        self.stu_showpage_label2.setGeometry(QRect(30, 60, 121, 20))
        self.stu_showpage_label3 = QLabel('性别：' + data[2], self.stu_showpage)
        self.stu_showpage_label3.setGeometry(QRect(30, 90, 71, 20))
        self.stu_showpage_label4 = QLabel('政治面貌：' + data[3], self.stu_showpage)
        self.stu_showpage_label4.setGeometry(QRect(130, 90, 181, 20))
        self.stu_showpage_label5 = QLabel(
            '出生日期：' + str(data[4]), self.stu_showpage)
        self.stu_showpage_label5.setGeometry(QRect(30, 120, 201, 20))
        self.stu_showpage_label6 = QLabel('民族：' + data[5], self.stu_showpage)
        self.stu_showpage_label6.setGeometry(QRect(30, 150, 111, 20))
        self.stu_showpage_label7 = QLabel('身份证号：' + data[6], self.stu_showpage)
        self.stu_showpage_label7.setGeometry(QRect(30, 180, 301, 20))
        self.stu_showpage_label8 = QLabel('联系电话：' + data[7], self.stu_showpage)
        self.stu_showpage_label8.setGeometry(QRect(30, 210, 301, 20))
        self.stu_showpage_label9 = QLabel('年级：' + data[9], self.stu_showpage)
        self.stu_showpage_label9.setGeometry(QRect(30, 240, 301, 20))
        self.stu_showpage_label10 = QLabel(
            '学制：' + str(data[8]), self.stu_showpage)
        self.stu_showpage_label10.setGeometry(QRect(180, 240, 141, 20))
        self.stu_showpage_label11 = QLabel('班级：' + data[10], self.stu_showpage)
        self.stu_showpage_label11.setGeometry(QRect(30, 270, 301, 20))
        self.stu_showpage_label12 = QLabel('专业：' + data[11], self.stu_showpage)
        self.stu_showpage_label12.setGeometry(QRect(30, 300, 301, 20))
        # 将照片显示在姓名右侧
        self.stu_showpage_label13 = QLabel(self.stu_showpage)
        self.stu_showpage_label13.setGeometry(QRect(300, 60, 200, 100))
        photo_path = photo_address[0]
        photo = QPixmap(photo_path)
        self.stu_showpage_label13.setPixmap(photo)

        self.stu_showpage.show()

    def stu_search_by_id(self):
        student_id = self.stu_search_lineEdit1.text()
        if not student_id:
            QMessageBox.warning(self, '查询失败', '请输入学号')
            return
        # 判断student_id是否是数字
        if not student_id.isdigit():
            QMessageBox.warning(self, '查询失败', '学号必须是数字')
            return
        cursor = ssms.cursor()
        cursor.execute(f"""
                    select stu_id, stu_name, stu_sex, stu_political_status, 
                    stu_birth, stu_ethnic, stu_iden_num, stu_telephone, stu_academic,
                    class_grade, class_name, major_name
                    from student, class , major 
                    where stu_class_id = class_id and class_major_id = major_id and stu_id = {student_id}
        """)
        data = cursor.fetchone()
        # 获取照片地址
        cursor.execute(f"""
                    select stu_photo_address
                    from student
                    where stu_id = {student_id}
        """)
        photo_address = cursor.fetchone()
        if not data:
            QMessageBox.warning(self, '查询失败', '学号不存在')
            return
        self.stu_show_page(data, photo_address)
        cursor.close()

    def stu_search_by_name(self):
        student_name = self.stu_search_lineEdit2.text()
        if not student_name:
            QMessageBox.warning(self, '查询失败', '请输入姓名')
            return
        cursor = ssms.cursor()
        cursor.execute("""
            select stu_id, stu_name, stu_sex, stu_political_status, 
            stu_birth, stu_ethnic, stu_iden_num, stu_telephone, stu_academic,
            class_grade, class_name, major_name
            from student, class , major 
            where stu_class_id = class_id and class_major_id = major_id and stu_name = %s
        """, (student_name,))
        data = cursor.fetchall()
        # 获取照片地址
        cursor.execute("""
            select stu_photo_address
            from student
            where stu_name = %s
        """, (student_name,))
        photo_address = cursor.fetchall()
        if not data:
            QMessageBox.warning(self, '查询失败', '姓名不存在')
            return
        # 由于可能有多个学生同名，这里我们使用表格显示查询结果，表格中信息不可以编辑
        self.stu_tablepage = QWidget()
        self.stu_tablepage.setWindowTitle('学生基本信息查询结果')
        self.stu_tablepage.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.stu_tablepage)
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(13)
        table.setHorizontalHeaderLabels(
            ['学号', '姓名', '性别', '政治面貌', '出生日期', '民族', '身份证号', '联系电话', '学制', '年级', '班级', '专业', '详情'])
        table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(cell)))
        # 添加查看详情按钮
        for i in range(len(data)):
            button = QPushButton('查看详情', self.stu_tablepage)
            button.clicked.connect(
                lambda checked, i=i: self.stu_show_page(data[i], photo_address[i]))
            table.setCellWidget(i, 12, button)
        self.stu_tablepage.show()
        cursor.close()

    def stu_revise_open(self):
        # 打开查询的表格，
        student_id = self.student_revise_lineEdit1.text()
        if not student_id:
            QMessageBox.warning(self, '查询失败', '请输入学号')
            return
        # 判断student_id是否是数字
        if not student_id.isdigit():
            QMessageBox.warning(self, '查询失败', '学号必须是数字')
            return
        cursor = ssms.cursor()
        cursor.execute(f"""
                    select stu_id, stu_name, stu_sex, stu_political_status, 
                    stu_birth, stu_ethnic, stu_iden_num, stu_telephone, stu_academic,
                    class_grade, class_name, major_name
                    from student, class , major 
                    where stu_class_id = class_id and class_major_id = major_id and stu_id = {student_id}
        """)
        data = cursor.fetchone()
        if not data:
            QMessageBox.warning(self, '查询失败', '学号不存在')
            return
        # 打开修改页面
        self.stu_revise_page = QWidget()
        self.stu_revise_page.setWindowTitle('学生基本信息修改')
        self.stu_revise_page.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.stu_revise_page)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(14)
        table.setHorizontalHeaderLabels(
            ['学号', '姓名', '性别', '政治面貌', '出生日期', '民族', '身份证号', '联系电话', '学制', '年级', '班级', '专业', '修改', '重置'])
        table.setRowCount(1)
        for j, cell in enumerate(data):
            table.setItem(0, j, QTableWidgetItem(str(cell)))
        # 添加修改按钮
        button = QPushButton('修改', self.stu_revise_page)
        button.clicked.connect(lambda checked: self.stu_revise(data))
        table.setCellWidget(0, 12, button)
        # 添加重置按钮
        button = QPushButton('重置', self.stu_revise_page)
        button.clicked.connect(lambda checked: self.stu_no_revise(data))
        table.setCellWidget(0, 13, button)
        self.stu_revise_page.show()
        cursor.close()

    def stu_revise(self, data):
        # 从表格中获取修改后的数据
        new_data = []
        for i in range(12):
            new_data.append(self.stu_revise_page.findChild(
                QTableWidget).item(0, i).text())
        new_data[0] = int(new_data[0])
        # data 中日期为datetime格式，转换为字符串
        data = list(data)
        data[4] = data[4].strftime('%Y-%m-%d')
        # data 中学制与学生id为数字，转换为字符串
        data[8] = str(data[8])
        if new_data == data:
            QMessageBox.warning(self, '修改失败', '信息未修改')
            return
        if new_data[0] != data[0]:
            QMessageBox.warning(self, '修改失败', '学号不可修改')
            return
        # 检测数据是否为空
        for i in range(12):
            if not new_data[i]:
                QMessageBox.warning(self, '修改失败', '信息不可为空')
                return
        # 日期格式检测，格式为yyyy-mm-dd，且日期内为数字
        if len(new_data[4]) != 10 or new_data[4][4] != '-' or new_data[4][7] != '-' or not new_data[4][:4].isdigit() or not new_data[4][5:7].isdigit() or not new_data[4][8:].isdigit():
            QMessageBox.warning(self, '修改失败', '日期格式错误')
            return
        # 检测学制和班级是否是数字
        if not new_data[8].isdigit():
            QMessageBox.warning(self, '修改失败', '学制必须是数字')
            return
        # 年级和专业属于班级，不可以修改
        if new_data[9] != data[9] or new_data[11] != data[11] or new_data[10] != data[10]:
            QMessageBox.warning(self, '修改失败', '班级年级专业不可在此处修改')
            return
        # 修改数据
        cursor = ssms.cursor()
        cursor.execute("""
            update student 
            set stu_name = %s, stu_sex = %s, stu_political_status = %s, stu_birth = %s,
            stu_ethnic = %s, stu_iden_num = %s, stu_telephone = %s, stu_academic = %s
            where stu_id = %s
            """, (new_data[1], new_data[2], new_data[3], new_data[4], new_data[5], new_data[6], new_data[7], int(new_data[8]), data[0]))
        ssms.commit()
        QMessageBox.information(self, '修改成功', '修改成功')
        cursor.close()

    def stu_no_revise(self, data):
        # 重置表格
        for i in range(12):
            self.stu_revise_page.findChild(QTableWidget).item(
                0, i).setText(str(data[i]))

    def stu_add_open(self):
        self.stu_add_page = QWidget()
        self.stu_add_page.setWindowTitle('学生基本信息添加')
        self.stu_add_page.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.stu_add_page)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(9)
        table.setHorizontalHeaderLabels(
            ['姓名', '性别', '政治面貌', '出生日期', '民族', '身份证号', '联系电话', '班级', '添加'])
        table.setRowCount(1)
        # 添加按钮
        button = QPushButton('添加', self.stu_add_page)
        button.clicked.connect(lambda checked: self.stu_add(table))
        table.setCellWidget(0, 8, button)
        # 性别只有男女，政治面貌只有群众、共青团员、党员，设置下拉框
        combobox1 = QtWidgets.QComboBox()
        combobox1.addItem('男')
        combobox1.addItem('女')
        table.setCellWidget(0, 1, combobox1)
        combobox2 = QtWidgets.QComboBox()
        combobox2.addItem('群众')
        combobox2.addItem('共青团员')
        combobox2.addItem('党员')
        table.setCellWidget(0, 2, combobox2)
        # 出生日期设置为日期选择框
        dateedit = QtWidgets.QDateEdit()
        dateedit.setDisplayFormat('yyyy-MM-dd')
        table.setCellWidget(0, 3, dateedit)
        # 班级设置为下拉框
        cursor = ssms.cursor()
        cursor.execute('select class_name from class')
        class_name = cursor.fetchall()
        combobox3 = QtWidgets.QComboBox()
        for i in class_name:
            combobox3.addItem(i[0])
        table.setCellWidget(0, 7, combobox3)
        cursor.close()

        self.stu_add_page.show()

    def stu_add(self, table):
        # 从表格中获取数据
        new_data = []
        new_data.append(table.item(0, 0).text())
        for i in range(1, 3):
            combobox = table.cellWidget(0, i)
            new_data.append(combobox.currentText())
        # 日期
        dateedit = table.cellWidget(0, 3)
        new_data.append(dateedit.text())
        # 4-6
        for i in range(4, 7):
            new_data.append(table.item(0, i).text())
        # 7是班级
        combobox = table.cellWidget(0, 7)
        new_data.append(combobox.currentText())
        print(new_data)
        # 姓名不可以为空
        if not new_data[0]:
            QMessageBox.warning(self, '添加失败', '姓名不可为空')
            return
        # 找到班级名字对应的班级id
        cursor = ssms.cursor()
        cursor.execute('select class_id from class where class_name = %s',
                       (new_data[7],))
        class_id = cursor.fetchone()
        if not class_id:
            QMessageBox.warning(self, '添加失败', '班级不存在')
            return
        #  使用数据库中的函数get_max_id()获取当前学生id的最大值
        cursor.execute('select get_max_id()')
        stu_id = cursor.fetchone()[0] + 1
        # 插入数据
        cursor.execute("""
            insert into student(stu_id, stu_name, stu_birth,stu_sex,stu_political_status,stu_ethnic,stu_iden_num,stu_telephone,stu_academic,stu_class_id)
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (stu_id, new_data[0], new_data[3], new_data[1], new_data[2], new_data[4], new_data[5], new_data[6], 4, class_id))
        ssms.commit()
        QMessageBox.information(self, '添加成功', '添加成功')
        cursor.close()

    def stu_delete(self):
        student_id = self.student_delete_lineEdit1.text()
        if not student_id:
            QMessageBox.warning(self, '删除失败', '请输入学号')
            return
        # 判断student_id是否是数字
        if not student_id.isdigit():
            QMessageBox.warning(self, '删除失败', '学号必须是数字')
            return
        # 调用数据库存储过程delete_student()删除学生其他信息
        cursor = ssms.cursor()
        cursor.execute('call delete_student(%s)', (student_id,))
        # 删除学生基本信息
        cursor.execute('delete from student where stu_id = %s', (student_id,))
        ssms.commit()
        QMessageBox.information(self, '删除成功', '删除成功')
        cursor.close()

    def class_search(self):
        # 将所有班级信息显示在表格中
        # 显示的信息为班级id，班级名，年级，专业名，班级人数
        cursor = ssms.cursor()
        cursor.execute("""
            select class_id, class_name, class_grade, major_name, class_stu_num
            from class, major
            where class_major_id = major_id
        """)
        data = cursor.fetchall()
        self.class_tablepage = QWidget()
        self.class_tablepage.setWindowTitle('班级信息查询结果')
        self.class_tablepage.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.class_tablepage)
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(
            ['班级id', '班级名', '年级', '专业名', '班级人数'])
        table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(cell)))
        self.class_tablepage.show()
        cursor.close()

    def class_revise_open(self):
        # 显示班级信息
        class_id = self.class_lieEdit1.text()
        if not class_id:
            QMessageBox.warning(self, '查询失败', '请输入班级id')
            return
        # 判断class_id是否是数字
        if not class_id.isdigit():
            QMessageBox.warning(self, '查询失败', '班级id必须是数字')
            return
        cursor = ssms.cursor()
        cursor.execute("""
            select class_id, class_name, class_grade, major_name, class_stu_num
            from class, major
            where class_major_id = major_id and class_id = %s
        """, (class_id,))
        data = cursor.fetchone()
        if not data:
            QMessageBox.warning(self, '查询失败', '班级id不存在')
            return
        # 打开修改页面
        self.class_revise_page = QWidget()
        self.class_revise_page.setWindowTitle('班级信息修改')
        self.class_revise_page.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.class_revise_page)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(
            ['班级id', '班级名', '年级', '专业名', '班级人数', '修改', '重置'])
        table.setRowCount(1)
        for j, cell in enumerate(data):
            table.setItem(0, j, QTableWidgetItem(str(cell)))
        # 添加修改按钮
        button = QPushButton('修改', self.class_revise_page)
        button.clicked.connect(lambda checked: self.class_revise(data, table))
        table.setCellWidget(0, 5, button)
        # 添加重置按钮
        button = QPushButton('重置', self.class_revise_page)
        button.clicked.connect(
            lambda checked: self.class_no_revise(data, table))
        table.setCellWidget(0, 6, button)
        self.class_revise_page.show()
        cursor.close()

    def class_revise(self, data, table):
        new_data = []
        for i in range(5):
            new_data.append(table.item(0, i).text())
        new_data[0] = int(new_data[0])
        new_data[4] = int(new_data[4])
        if new_data == data:
            QMessageBox.warning(self, '修改失败', '信息未修改')
            return
        # 只有班级名字和年级可以修改
        if new_data[0] != data[0] or new_data[3] != data[3] or new_data[4] != data[4]:
            QMessageBox.warning(self, '修改失败', '班级id和专业名和班级人数不可修改')
            return

        # 年级只有'大一','大二','大三','大四'四个选项
        if new_data[2] not in ['大一', '大二', '大三', '大四']:
            QMessageBox.warning(self, '修改失败', '年级不正确')
            return
        cursor = ssms.cursor()
        cursor.execute("""
            update class set class_name = %s, class_grade = %s
            where class_id = %s 
        """, (new_data[1], new_data[2], new_data[0]))
        ssms.commit()
        QMessageBox.information(self, '修改成功', '修改成功')
        cursor.close()

    def class_no_revise(self, data, table):
        for i in range(5):
            table.item(0, i).setText(str(data[i]))

    def class_add_open(self):
        # 添加班级信息
        self.class_add_page = QWidget()
        self.class_add_page.setWindowTitle('班级信息添加')
        self.class_add_page.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.class_add_page)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(
            ['班级名', '年级', '专业名', '添加'])
        table.setRowCount(1)
        # 添加按钮
        button = QPushButton('添加', self.class_add_page)
        button.clicked.connect(lambda checked: self.class_add(table))
        table.setCellWidget(0, 3, button)
        # 年级只有'大一','大二','大三','大四'四个选项
        combobox = QtWidgets.QComboBox()
        combobox.addItem('大一')
        combobox.addItem('大二')
        combobox.addItem('大三')
        combobox.addItem('大四')
        table.setCellWidget(0, 1, combobox)
        # 专业名下拉框
        cursor = ssms.cursor()
        cursor.execute('select major_name from major')
        major_name = cursor.fetchall()
        combobox = QtWidgets.QComboBox()
        for i in major_name:
            combobox.addItem(i[0])
        table.setCellWidget(0, 2, combobox)
        cursor.close()
        self.class_add_page.show()

    def class_add(self, table):
        new_data = []
        # 从表格中获取数据，1，2表格中为下拉框，需要获取当前选中的值
        new_data.append(table.item(0, 0).text())
        combobox = table.cellWidget(0, 1)
        new_data.append(combobox.currentText())
        combobox = table.cellWidget(0, 2)
        new_data.append(combobox.currentText())
        # 班级人数默认为0
        new_data.append(0)
        # 班级名不可以为空
        if not new_data[0]:
            QMessageBox.warning(self, '添加失败', '班级名不可为空')
            return
        # 添加
        cursor = ssms.cursor()
        cursor.execute('select major_id from major where major_name = %s',
                       (new_data[2],))
        major_id = cursor.fetchone()
        if not major_id:
            QMessageBox.warning(self, '添加失败', '专业不存在')
            return
        cursor.execute('select max(class_id) from class')
        class_id = cursor.fetchone()[0] + 1
        cursor.execute("""
            insert into class(class_id, class_name, class_grade, class_major_id, class_stu_num)
            values(%s, %s, %s, %s, %s)
        """, (class_id, new_data[0], new_data[1], major_id, new_data[3]))
        ssms.commit()
        QMessageBox.information(self, '添加成功', '添加成功')
        cursor.close()

    def class_delete_open(self):
        # 删除班级信息
        class_id = self.class_delete_lineEdit1.text()
        if not class_id:
            QMessageBox.warning(self, '删除失败', '请输入班级id')
            return
        # 判断class_id是否是数字
        if not class_id.isdigit():
            QMessageBox.warning(self, '删除失败', '班级id必须是数字')
            return
        # 班级人数为0才可以删除
        cursor = ssms.cursor()
        cursor.execute('select class_stu_num from class where class_id = %s',
                       (class_id,))
        class_stu_num = cursor.fetchone()
        if not class_stu_num:
            QMessageBox.warning(self, '删除失败', '班级id不存在')
            return
        if class_stu_num[0] != 0:
            QMessageBox.warning(self, '删除失败', '班级人数不为0')
            return
        # 删除班级
        cursor.execute('delete from class where class_id = %s', (class_id,))
        ssms.commit()
        QMessageBox.information(self, '删除成功', '删除成功')
        cursor.close()

    def course_search(self):
        # 查询所有课程信息
        # 输出为课程id，课程名，学分，课程必修选修，课程状态（开课，未开课，已结课），开设学期
        cursor = ssms.cursor()
        cursor.execute("""
            select course_id, course_name, course_credit, course_if_compulsory, course_status, course_semester
            from course
        """)
        # course_if_compulsory = 1 为必修，0为选修
        # course_status = 0 为未开课，1为开课，2为已结课
        # 需要通过专业id找到专业名
        data = cursor.fetchall()
        if not data:
            QMessageBox.warning(self, '查询失败', '无课程信息')
            return
        modify_data = []
        for item in data:
            item = list(item)
            item[3] = int(item[3])
            if item[3] == 1:
                item[3] = '必修'
            else:
                item[3] = '选修'
            if item[4] == 0:
                item[4] = '未开课'
            elif item[4] == 1:
                item[4] = '开课'
            else:
                item[4] = '已结课'
            modify_data.append(item)

        self.course_tablepage = QWidget()
        self.course_tablepage.setWindowTitle('课程信息查询结果')
        self.course_tablepage.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.course_tablepage)
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(
            ['课程id', '课程名', '学分', '课程类型', '课程状态', '开设学期'])
        table.setRowCount(len(data))
        for i, row in enumerate(modify_data):
            for j, cell in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(cell)))
        self.course_tablepage.show()
        cursor.close()

    def course_revise_open(self):
        # 修改课程信息
        course_id = self.course_lineEdit1.text()
        if not course_id:
            QMessageBox.warning(self, '查询失败', '请输入课程id')
            return
        # 判断course_id是否是数字
        if not course_id.isdigit():
            QMessageBox.warning(self, '查询失败', '课程id必须是数字')
            return
        cursor = ssms.cursor()
        cursor.execute("""
            select course_id, course_name, course_credit, course_if_compulsory, course_status, course_semester
            from course
            where course_id = %s
        """, (course_id,))
        data = cursor.fetchone()
        if not data:
            QMessageBox.warning(self, '查询失败', '课程id不存在')
            return
        # 打开修改页面
        self.course_revise_page = QWidget()
        self.course_revise_page.setWindowTitle('课程信息修改')
        self.course_revise_page.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.course_revise_page)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(8)
        table.setHorizontalHeaderLabels(
            ['课程id', '课程名', '学分', '课程类型', '课程状态', '开设学期', '修改', '重置'])
        table.setRowCount(1)
        # 课程类型只有必修和选修，课程状态只有未开课，开课，已结课，设置下拉框
        combobox1 = QtWidgets.QComboBox()
        combobox1.addItem('必修')
        combobox1.addItem('选修')
        table.setCellWidget(0, 3, combobox1)
        combobox2 = QtWidgets.QComboBox()
        combobox2.addItem('未开课')
        combobox2.addItem('开课')
        combobox2.addItem('已结课')
        table.setCellWidget(0, 4, combobox2)
        # 根据course_if_compulsory和course_status的值设置下拉框的默认值
        if data[3] == 1:
            combobox1.setCurrentIndex(0)
        else:
            combobox1.setCurrentIndex(1)
        if data[4] == 0:
            combobox2.setCurrentIndex(0)
        elif data[4] == 1:
            combobox2.setCurrentIndex(1)
        else:
            combobox2.setCurrentIndex(2)
        # 添加修改按钮
        button = QPushButton('修改', self.course_revise_page)
        button.clicked.connect(lambda checked: self.course_revise(table, data))
        table.setCellWidget(0, 6, button)
        # 添加重置按钮
        button = QPushButton('重置', self.course_revise_page)
        button.clicked.connect(
            lambda checked: self.course_no_revise(table, data))
        table.setCellWidget(0, 7, button)
        # 将数据填入表格的0，1，2，5
        table.setItem(0, 0, QTableWidgetItem(str(data[0])))
        table.setItem(0, 1, QTableWidgetItem(data[1]))
        table.setItem(0, 2, QTableWidgetItem(str(data[2])))
        table.setItem(0, 5, QTableWidgetItem(data[5]))
        self.course_revise_page.show()
        cursor.close()

    def course_revise(self, table, data):
        # 下拉框的值和文本值分开获取
        new_data = []
        new_data.append(table.item(0, 0).text())
        new_data.append(table.item(0, 1).text())
        new_data.append(table.item(0, 2).text())
        combobox = table.cellWidget(0, 3)
        new_data.append(combobox.currentText())
        combobox = table.cellWidget(0, 4)
        new_data.append(combobox.currentText())
        new_data.append(table.item(0, 5).text())

        # id 不可以修改
        new_data[0] = int(new_data[0])
        if new_data[0] != data[0]:
            QMessageBox.warning(self, '修改失败', '课程id不可修改')
            return
        # 课程名不可以为空
        if not new_data[1]:
            QMessageBox.warning(self, '修改失败', '课程名不可为空')
            return
        # 学分必须是数字
        if not new_data[2].isdigit():
            QMessageBox.warning(self, '修改失败', '学分必须是数字')
            return
        # 根据课程类型和课程状态的值设置为1或0
        print(new_data)
        if new_data[3] == '必修':
            new_data[3] = 1
        else:
            new_data[3] = 0
        if new_data[4] == '未开课':
            new_data[4] = 0
        elif new_data[4] == '开课':
            new_data[4] = 1
        else:
            new_data[4] = 2

        print(new_data)

        # 更改
        cursor = ssms.cursor()
        cursor.execute("""
            update course set course_name = %s, course_credit = %s, course_if_compulsory = %s, course_status = %s, course_semester = %s
            where course_id = %s
        """, (new_data[1], int(new_data[2]), new_data[3], new_data[4], new_data[5], new_data[0]))
        ssms.commit()
        QMessageBox.information(self, '修改成功', '修改成功')
        cursor.close()

    def course_no_revise(self, table, data):
        # 重置表格
        table.item(0, 0).setText(str(data[0]))
        table.item(0, 1).setText(data[1])
        table.item(0, 2).setText(str(data[2]))
        table.item(0, 5).setText(data[5])
        # 下拉框的值和文本值分开获取
        if data[3] == 1:
            table.cellWidget(0, 3).setCurrentIndex(0)
        else:
            table.cellWidget(0, 3).setCurrentIndex(1)
        table.cellWidget(0, 4).setCurrentIndex(data[4])

    def course_add_open(self):
        # 添加课程信息
        self.course_add_page = QWidget()
        self.course_add_page.setWindowTitle('课程信息添加')
        self.course_add_page.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.course_add_page)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(
            ['课程名', '学分', '课程类型', '课程状态', '开设学期', '专业', '添加'])
        table.setRowCount(1)
        # 添加按钮
        button = QPushButton('添加', self.course_add_page)
        button.clicked.connect(lambda checked: self.course_add(table))
        table.setCellWidget(0, 6, button)
        # 课程类型只有必修和选修，课程状态只有未开课，开课，已结课，
        combobox1 = QtWidgets.QComboBox()
        combobox1.addItem('选修')
        combobox1.addItem('必修')
        table.setCellWidget(0, 2, combobox1)
        combobox2 = QtWidgets.QComboBox()
        combobox2.addItem('未开课')
        combobox2.addItem('开课')
        combobox2.addItem('已结课')
        table.setCellWidget(0, 3, combobox2)
        # 开设学期设置为下拉框，2023_1，2023_2，2024_1，2024_2
        combobox3 = QtWidgets.QComboBox()
        combobox3.addItem('2023_1')
        combobox3.addItem('2023_2')
        combobox3.addItem('2024_1')
        combobox3.addItem('2024_2')
        table.setCellWidget(0, 4, combobox3)
        # 专业设置为下拉框
        cursor = ssms.cursor()
        cursor.execute('select major_name from major')
        major_name = cursor.fetchall()
        combobox4 = QtWidgets.QComboBox()
        for i in major_name:
            combobox4.addItem(i[0])
        table.setCellWidget(0, 5, combobox4)
        cursor.close()
        self.course_add_page.show()

    def course_add(self, table):
        new_data = []
        # 从表格中获取数据，2，3，4表格中为下拉框，需要获取当前选中的值
        new_data.append(table.item(0, 0).text())
        new_data.append(table.item(0, 1).text())
        combobox = table.cellWidget(0, 2)
        new_data.append(combobox.currentText())
        combobox = table.cellWidget(0, 3)
        new_data.append(combobox.currentText())
        combobox = table.cellWidget(0, 4)
        new_data.append(combobox.currentText())
        combobox = table.cellWidget(0, 5)
        new_data.append(combobox.currentText())
        # id 为数据库自增，不需要添加
        # 课程名不可以为空
        if not new_data[0]:
            QMessageBox.warning(self, '添加失败', '课程名不可为空')
            return
        # 学分必须是数字
        if not new_data[1].isdigit():
            QMessageBox.warning(self, '添加失败', '学分必须是数字')
            return
        # 根据课程类型和课程状态的值设置为1或0
        if new_data[2] == '必修':
            new_data[2] = 1
        else:
            new_data[2] = 0
        if new_data[3] == '未开课':
            new_data[3] = 0
        elif new_data[3] == '开课':
            new_data[3] = 1
        else:
            new_data[3] = 2
        # 根据开设学期的值设置为2023_1，2023_2，2024_1，2024_2
        if new_data[4] not in ['2023_1', '2023_2', '2024_1', '2024_2']:
            QMessageBox.warning(self, '添加失败', '开设学期不正确')
            return
        # 找到专业名对应的专业id
        cursor = ssms.cursor()
        cursor.execute('select major_id from major where major_name = %s',
                       (new_data[5],))
        major_id = cursor.fetchone()
        if not major_id:
            QMessageBox.warning(self, '添加失败', '专业不存在')
            return
        # 添加
        cursor.execute('select max(course_id) from course')
        course_id = cursor.fetchone()[0] + 1
        cursor.execute("""
            insert into course(course_id, course_name, course_credit, course_if_compulsory, course_status, course_semester, course_major_id)
            values(%s, %s, %s, %s, %s, %s, %s)
        """, (course_id, new_data[0], int(new_data[1]), new_data[2], new_data[3], new_data[4], major_id))
        ssms.commit()
        QMessageBox.information(self, '添加成功', '添加成功')
        cursor.close()

    def course_delete_open(self):
        # 删除课程信息
        course_id = self.course_lineEdit2.text()
        if not course_id:
            QMessageBox.warning(self, '删除失败', '请输入课程id')
            return
        # 判断course_id是否是数字
        if not course_id.isdigit():
            QMessageBox.warning(self, '删除失败', '课程id必须是数字')
            return
        course_id = int(course_id)
        # 删除课程,没有人选课才可以删除
        cursor = ssms.cursor()
        cursor.execute('select count(*) from student_course where sc_course_id = %s',
                       (course_id,))
        course_stu_num = cursor.fetchone()
        if course_stu_num[0] != 0:
            QMessageBox.warning(self, '删除失败', '课程有学生选课')
            return
        # 判断课程是否存在
        cursor.execute('select course_id from course where course_id = %s',
                       (course_id,))
        course_id = cursor.fetchone()
        if not course_id:
            QMessageBox.warning(self, '删除失败', '课程id不存在')
            return
        cursor.execute('delete from course where course_id = %s', (course_id,))
        ssms.commit()
        QMessageBox.information(self, '删除成功', '删除成功')
        cursor.close()

    def stu_cou_search_by_id(self):
        # 通过学号查询学生选课信息
        student_id = self.stu_cou_lineEdit1.text()
        if not student_id:
            QMessageBox.warning(self, '查询失败', '请输入学号')
            return
        # 判断student_id是否是数字
        if not student_id.isdigit():
            QMessageBox.warning(self, '查询失败', '学号必须是数字')
            return
        cursor = ssms.cursor()
        # 查询学生选课的课程名
        cursor.execute("""
            select course_name
            from student_course, course
            where sc_course_id = course_id and sc_stu_id = %s
        """, (student_id,))
        data = cursor.fetchall()
        if not data:
            QMessageBox.warning(self, '查询失败', '学号不存在或未选课')
            return
        self.stu_cou_tablepage = QWidget()
        self.stu_cou_tablepage.setWindowTitle('学生选课信息查询结果')
        self.stu_cou_tablepage.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.stu_cou_tablepage)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(1)
        table.setHorizontalHeaderLabels(['课程名'])
        table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(cell)))
        self.stu_cou_tablepage.show()
        cursor.close()

    def stu_cou_select(self):
        # 添加学生选课信息
        student_id = self.stu_cou_lineEdit2.text()
        course_id = self.stu_cou_lineEdit3.text()
        if not student_id or not course_id:
            QMessageBox.warning(self, '选课失败', '请输入学号和课程id')
            return
        # 判断student_id和course_id是否是数字
        if not student_id.isdigit() or not course_id.isdigit():
            QMessageBox.warning(self, '选课失败', '学号和课程id必须是数字')
            return
        student_id = int(student_id)
        course_id = int(course_id)
        # 判断学号和课程id是否存在
        cursor = ssms.cursor()
        cursor.execute('select stu_id from student where stu_id = %s',
                       (student_id,))
        student_id = cursor.fetchone()
        if not student_id:
            QMessageBox.warning(self, '选课失败', '学号不存在')
            return
        cursor.execute('select course_id from course where course_id = %s',
                       (course_id,))
        course_id = cursor.fetchone()
        if not course_id:
            QMessageBox.warning(self, '选课失败', '课程id不存在')
            return
        # 调用数据库存储过程select_course()添加学生选课信息
        cursor.callproc('select_course', (student_id, course_id))
        cursor.execute('select @result')
        result = cursor.fetchone()[0]
        if result == 1:
            QMessageBox.information(self, '选课成功', '添加成功')
        else:
            QMessageBox.warning(self, '选课失败', '添加失败')
        cursor.close()

    def stu_cou_delete(self):
        # 删除学生选课信息
        student_id = self.stu_cou_lineEdit4.text()
        course_id = self.stu_cou_lineEdit5.text()
        if not student_id or not course_id:
            QMessageBox.warning(self, '退课失败', '请输入学号和课程id')
            return
        # 判断student_id和course_id是否是数字
        if not student_id.isdigit() or not course_id.isdigit():
            QMessageBox.warning(self, '退课失败', '学号和课程id必须是数字')
            return
        student_id = int(student_id)
        course_id = int(course_id)
        # 判断学号和课程id是否存在
        cursor = ssms.cursor()
        cursor.execute('select stu_id from student where stu_id = %s',
                       (student_id,))
        student_id = cursor.fetchone()
        if not student_id:
            QMessageBox.warning(self, '退课失败', '学号不存在')
            return
        cursor.execute('select course_id from course where course_id = %s',
                       (course_id,))
        course_id = cursor.fetchone()
        if not course_id:
            QMessageBox.warning(self, '退课失败', '课程id不存在')
            return
        # 判断学生是否选择了要删除的课程
        cursor.execute('select count(*) from student_course where sc_stu_id = %s and sc_course_id = %s',
                       (student_id, course_id))
        student_course = cursor.fetchone()
        if not student_course:
            QMessageBox.warning(self, '退课失败', '学生未选课')
            return
        # 如果成绩表有记录，不可以退课
        cursor.execute('select count(*) from score where score_stu_id = %s and score_course_id = %s',
                       (student_id, course_id))
        score = cursor.fetchone()[0]
        if score:
            QMessageBox.warning(self, '退课失败', '已有成绩，不可退课')
            return
        # 删除学生选课信息
        cursor.execute('delete from student_course where sc_stu_id = %s and sc_course_id = %s',
                       (student_id, course_id))
        ssms.commit()
        QMessageBox.information(self, '退课成功', '删除成功')
        cursor.close()

    def score_search_by_id(self):
        # 通过学号查询学生成绩
        student_id = self.score_lineEdit1.text()
        if not student_id:
            QMessageBox.warning(self, '查询失败', '请输入学号')
            return
        # 判断student_id是否是数字
        if not student_id.isdigit():
            QMessageBox.warning(self, '查询失败', '学号必须是数字')
            return
        cursor = ssms.cursor()
        # 查询学生成绩
        cursor.execute("""
            select course_name, score_num
            from score, course
            where score_course_id = course_id and score_stu_id = %s
        """, (student_id,))
        data = cursor.fetchall()
        if not data:
            QMessageBox.warning(self, '查询失败', '学号不存在或无成绩')
            return
        self.score_tablepage = QWidget()
        self.score_tablepage.setWindowTitle('学生成绩查询结果')
        self.score_tablepage.setGeometry(450, 250, 800, 450)
        table = QTableWidget(self.score_tablepage)
        table.setGeometry(30, 30, 740, 400)
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(['课程名', '成绩'])
        table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(cell)))
        self.score_tablepage.show()
        cursor.close()

    def score_add(self):
        # 添加学生成绩
        student_id = self.score_lineEdit5.text()
        course_id = self.score_lineEdit6.text()
        score = self.score_lineEdit7.text()
        if not student_id or not course_id or not score:
            QMessageBox.warning(self, '添加失败', '请输入学号，课程id和成绩')
            return
        # 判断student_id和course_id是否是数字
        if not student_id.isdigit() or not course_id.isdigit():
            QMessageBox.warning(self, '添加失败', '学号和课程id必须是数字')
            return
        student_id = int(student_id)
        course_id = int(course_id)
        # 判断学号和课程id是否存在
        cursor = ssms.cursor()
        cursor.execute('select stu_id from student where stu_id = %s',
                       (student_id,))
        student_id = cursor.fetchone()[0]
        if not student_id:
            QMessageBox.warning(self, '添加失败', '学号不存在')
            return
        cursor.execute('select course_id from course where course_id = %s',
                       (course_id,))
        course_id = cursor.fetchone()[0]
        if not course_id:
            QMessageBox.warning(self, '添加失败', '课程id不存在')
            return
        # 成绩必须是数字
        if not score.isdigit():
            QMessageBox.warning(self, '添加失败', '成绩必须是数字')
            return
        # print(student_id, course_id, score)
        # 判断学生是否选择了要添加成绩的课程
        cursor.execute('select count(*) from student_course where sc_stu_id = %s and sc_course_id = %s',
                       (student_id, course_id))
        student_course = cursor.fetchone()[0]
        if not student_course:
            QMessageBox.warning(self, '添加失败', '学生未选课')
            return
        # 判断是否已经有成绩
        cursor.execute('select count(*) from score where score_stu_id = %s and score_course_id = %s',
                       (student_id, course_id))
        score_num = cursor.fetchone()[0]
        if score_num:
            QMessageBox.warning(self, '添加失败', '已有成绩')
            return
        # 添加成绩
        cursor.execute('insert into score values(%s, %s, %s,%s)',
                       (student_id, course_id, score, 0))
        ssms.commit()
        QMessageBox.information(self, '添加成功', '添加成功')
        cursor.close()

    def score_revise(self):
        # 修改学生成绩
        student_id = self.score_lineEdit2.text()
        course_id = self.score_lineEdit3.text()
        score = self.score_lineEdit4.text()
        if not student_id or not course_id or not score:
            QMessageBox.warning(self, '修改失败', '请输入学号，课程id和成绩')
            return
        # 判断student_id和course_id是否是数字
        if not student_id.isdigit() or not course_id.isdigit():
            QMessageBox.warning(self, '修改失败', '学号和课程id必须是数字')
            return
        student_id = int(student_id)
        course_id = int(course_id)
        # 判断学号和课程id是否存在
        cursor = ssms.cursor()
        cursor.execute('select stu_id from student where stu_id = %s',
                       (student_id,))
        student_id = cursor.fetchone()[0]
        if not student_id:
            QMessageBox.warning(self, '修改失败', '学号不存在')
            return
        cursor.execute('select course_id from course where course_id = %s',
                       (course_id,))
        course_id = cursor.fetchone()[0]
        if not course_id:
            QMessageBox.warning(self, '修改失败', '课程id不存在')
            return
        # 成绩必须是数字
        if not score.isdigit():
            QMessageBox.warning(self, '修改失败', '成绩必须是数字')
            return
        # 判断成绩表是否有记录且成绩没有修改过
        cursor.execute('select score_num,score_if_modify from score where score_stu_id = %s and score_course_id = %s',
                       (student_id, course_id))
        score_num = cursor.fetchone()
        if not score_num:
            QMessageBox.warning(self, '修改失败', '无成绩')
            return
        if score_num[1]:
            QMessageBox.warning(self, '修改失败', '成绩已修改过')
            return
        # 修改成绩,修改成绩后score_if_modify为1
        cursor.execute('update score set score_num = %s, score_if_modify = 1 where score_stu_id = %s and score_course_id = %s',
                       (score, student_id, course_id))
        ssms.commit()
        QMessageBox.information(self, '修改成功', '修改成功')
        cursor.close()

    def score_delete(self):
        # 删除学生成绩
        student_id = self.score_lineEdit8.text()
        course_id = self.score_lineEdit9.text()
        if not student_id or not course_id:
            QMessageBox.warning(self, '删除失败', '请输入学号和课程id')
            return
        # 判断student_id和course_id是否是数字
        if not student_id.isdigit() or not course_id.isdigit():
            QMessageBox.warning(self, '删除失败', '学号和课程id必须是数字')
            return
        student_id = int(student_id)
        course_id = int(course_id)
        # 判断学号和课程id是否存在
        cursor = ssms.cursor()
        cursor.execute('select stu_id from student where stu_id = %s',
                       (student_id,))
        student_id = cursor.fetchone()[0]
        if not student_id:
            QMessageBox.warning(self, '删除失败', '学号不存在')
            return
        cursor.execute('select course_id from course where course_id = %s',
                       (course_id,))
        course_id = cursor.fetchone()[0]
        if not course_id:
            QMessageBox.warning(self, '删除失败', '课程id不存在')
            return
        # 删除学生成绩
        cursor.execute('delete from score where score_stu_id = %s and score_course_id = %s',
                       (student_id, course_id))
        ssms.commit()
        QMessageBox.information(self, '删除成功', '删除成功')
        cursor.close()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
