import sys

from PyQt5 import QtWidgets

import sqlite3

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.create_connection()

        self.init_ui()

    def create_connection(self):
        connection = sqlite3.connect("user_database.db")

        self.cursor = connection.cursor()

        self.cursor.execute("Create Table If not exists members(username TEXT,password TEXT)")

        connection.commit()

    def init_ui(self):
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.text_area = QtWidgets.QLabel("")

        vertical_box = QtWidgets.QVBoxLayout()

        vertical_box.addWidget(self.username)
        vertical_box.addWidget(self.password)
        vertical_box.addWidget(self.text_area)
        vertical_box.addStretch()
        vertical_box.addWidget(self.login)

        horizontal_box = QtWidgets.QHBoxLayout()
        horizontal_box.addStretch()
        horizontal_box.addLayout(vertical_box)
        horizontal_box.addStretch()

        self.setLayout(horizontal_box)

        self.setWindowTitle("User Login")

        self.login.clicked.connect(self.login_to_system)

        self.show()

    def login_to_system(self):
        name = self.username.text()
        pw = self.password.text()

        self.cursor.execute("Select * From members where username = ? and password = ?", (name, pw))
        data = self.cursor.fetchall()

        if len(data) == 0:
            self.text_area.setText("There is no user with these information\nPlease try again...")

        else:
            self.text_area.setText("Welcome " +name)


app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())



























