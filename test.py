from PyQt5.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QApplication,
    QPushButton,
    QLineEdit,
)

class TaschenRechner(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(400, 400)
        self.setWindowTitle('Taschenrechner')

        # Поле для відображення
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 18px; text-align: right;")

        # Створення кнопок
        self.buttons = {}
        buttons_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['AC', 'DEL']
        ]

        grid_layout = QVBoxLayout()
        grid_layout.addWidget(self.display)

        # Layout для кнопок
        for row in buttons_layout:
            row_layout = QHBoxLayout()
            row_layout.setSpacing(5)  # Дистанція між кнопками
            for button in row:
                btn = QPushButton(button)
                btn.setFixedSize(60, 40)  # Розмір кнопки
                btn.clicked.connect(lambda checked, text=button: self.on_button_click(text))
                self.buttons[button] = btn
                row_layout.addWidget(btn)
            grid_layout.addLayout(row_layout)

        self.setLayout(grid_layout)

    def on_button_click(self, button_text):
        current_text = self.display.text()

        if button_text == "AC":
            self.display.clear()
        elif button_text == "DEL":
            self.display.setText(current_text[:-1])
        elif button_text == "=":
            try:
                result = str(eval(current_text.replace('x', '*').replace(':', '/')))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(current_text + button_text)

app = QApplication([])

win = TaschenRechner()
win.show()
app.exec()
