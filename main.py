import sys
import threading

from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLineEdit

from backend import Chatbot

chatbot = Chatbot()

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

    def send_message(self):
            user_input = self.input_field.text().strip()
            self.chat_area.append(f'<p style="color: red">Me: {user_input}</p>')
            self.input_field.clear()

            thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
            thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f'Bot: {response}')

class Chatbot:
    pass


app = QApplication(sys.argv)
mian_window = ChatbotWindow()
sys.exit(app.exec())