import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)

        # Line edit for display
        self.display = QLineEdit(self)
        self.display.setGeometry(20, 20, 260, 40)
        self.display.setReadOnly(True)

        # Buttons
        self.create_button("1", 60, 120, 40, 40)
        self.create_button("2", 110, 120, 40, 40)
        self.create_button("3", 160, 120, 40, 40)
        self.create_button("+", 210, 120, 40, 40)
        self.create_button("4", 60, 170, 40, 40)
        self.create_button("5", 110, 170, 40, 40)
        self.create_button("6", 160, 170, 40, 40)
        self.create_button("-", 210, 170, 40, 40)
        self.create_button("7", 60, 220, 40, 40)
        self.create_button("8", 110, 220, 40, 40)
        self.create_button("9", 160, 220, 40, 40)
        self.create_button("*", 210, 220, 40, 40)
        self.create_button("C", 60, 270, 40, 40)
        self.create_button("0", 110, 270, 40, 40)
        self.create_button("=", 160, 270, 90, 40)

    def create_button(self, text, x, y, width, height):
        button = QPushButton(text, self)
        button.setGeometry(x, y, width, height)
        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        sender = self.sender()
        if sender.text() == "=":
            result = eval(self.display.text())
            self.display.setText(str(result))
        elif sender.text() == "C":
            self.display.clear()
        else:
            self.display.setText(self.display.text() + sender.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
