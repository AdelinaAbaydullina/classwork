import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QTextEdit, QPushButton,
    QListWidget, QMessageBox
)


class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Manager 2.0")
        self.resize(500, 500)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)


        self.title = QLineEdit()
        self.title.setPlaceholderText("Название задачи")

        self.description = QTextEdit()
        self.description.setPlaceholderText("Описание задачи")

        self.counter = QLabel("Название: 0 символов")

        self.tasks = QListWidget()

        self.status = QLabel("Задач: 0")

        self.add_button = QPushButton("Добавить задачу")
        self.clear_button = QPushButton("Очистить список")


        layout.addWidget(QLabel("Название:"))
        layout.addWidget(self.title)
        layout.addWidget(self.counter)
        layout.addWidget(QLabel("Описание:"))
        layout.addWidget(self.description)
        layout.addWidget(self.add_button)
        layout.addWidget(self.tasks)
        layout.addWidget(self.status)
        layout.addWidget(self.clear_button)

        self.add_button.clicked.connect(self.add_task)
        self.clear_button.clicked.connect(self.clear_tasks)
        self.title.textChanged.connect(self.count_symbols)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f4f8;
            }
            QLineEdit, QTextEdit, QListWidget {
                background-color: white;
                border: 1px solid #999999;
                border-radius: 5px;
                padding: 6px;
            }
            QPushButton {
                background-color: #3478c8;
                color: white;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #245a99;
            }
            QPushButton:disabled {
                background-color: gray;
            }
        """)

    def add_task(self):
        title = self.title.text().strip()
        description = self.description.toPlainText().strip()

        if not title:
            QMessageBox.warning(
                self, "Ошибка", "Введите название задачи!"
            )
            return

        if description:
            text = title + " — " + description
        else:
            text = title

        self.tasks.addItem(text)

        self.title.clear()
        self.description.clear()

        self.status.setText(f"Задач: {self.tasks.count()}")

    def count_symbols(self, text):
        self.counter.setText(
            f"Название: {len(text)} символов"
        )

    def clear_tasks(self):
        if self.tasks.count() == 0:
            QMessageBox.information(
                self, "Информация", "Список уже пуст."
            )
            return

        answer = QMessageBox.question(
            self,
            "Подтверждение",
            "Вы действительно хотите очистить список?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.tasks.clear()
            self.status.setText("Задач: 0")


app = QApplication(sys.argv)
window = TaskManager()
window.show()
sys.exit(app.exec())
