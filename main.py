import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLineEdit


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Add chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 400, 320)
        self.chat_area.setReadOnly(True)

        # Add input area
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 400, 40)

        # Add button area
        self.button = QPushButton('Send', self)
        self.button.setGeometry(500, 340, 100, 40)

        self.show()


class Chatbot:
    pass


app = QApplication(sys.argv)
mian_window = ChatbotWindow()
sys.exit(app.exec())