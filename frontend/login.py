from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
import requests

BASE_URL = "http://127.0.0.1:8000"

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        layout = QVBoxLayout()

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")

        self.button = QPushButton("Login")
        self.button.clicked.connect(self.login)

        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def login(self):
        response = requests.post(f"{BASE_URL}/login", json={
            "username": self.username.text(),
            "password": self.password.text()
        })

        print(response.json())