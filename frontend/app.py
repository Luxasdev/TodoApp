import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QListWidget, QLabel
)
from frontend.api import add_todo, get_todos


class App(QWidget):
    def __init__(self):
        super().__init__()

        # Fenster
        self.setWindowTitle("Todo App")
        self.resize(700, 500)

        # Hauptlayout
        self.layout = QVBoxLayout()

        # Titel
        self.title = QLabel("📋 Meine Todos")
        self.title.setStyleSheet("font-size: 22px; font-weight: bold;")

        # Todo Liste
        self.todo_list = QListWidget()

        # Input Bereich (horizontal)
        self.input_layout = QHBoxLayout()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Neues Todo eingeben...")

        self.add_button = QPushButton("Hinzufügen")
        self.add_button.clicked.connect(self.add_todo)

        self.input_layout.addWidget(self.input_field)
        self.input_layout.addWidget(self.add_button)

        # Alles ins Hauptlayout
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.todo_list)
        self.layout.addLayout(self.input_layout)

        self.setLayout(self.layout)

        # Todos laden
        self.load_todos()

    # 👉 Todo hinzufügen
    def add_todo(self):
        text = self.input_field.text()

        if text.strip() != "":
            add_todo(text)
            self.input_field.clear()
            self.load_todos()

    # 👉 Todos laden
    def load_todos(self):
        self.todo_list.clear()

        try:
            todos = get_todos()
            for todo in todos:
                self.todo_list.addItem(todo["title"])
        except Exception as e:
            self.todo_list.addItem("Fehler beim Laden 😢")
            print(e)


# 🚀 App starten
app = QApplication(sys.argv)

# 🎨 Dark Mode Styling
app.setStyleSheet("""
    QWidget {
        background-color: #1e1e1e;
        color: white;
        font-family: Arial;
    }

    QListWidget {
        background-color: #2d2d2d;
        border: none;
        padding: 5px;
    }

    QLineEdit {
        padding: 8px;
        border-radius: 5px;
        background-color: #2d2d2d;
        border: 1px solid #444;
    }

    QPushButton {
        background-color: #3a7afe;
        padding: 8px;
        border-radius: 5px;
    }

    QPushButton:hover {
        background-color: #5a90ff;
    }
""")

window = App()
window.show()

app.exec()