# lab5.py
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from lab5_ui import Ui_MainWindow
import math
import threading
import configparser

class MyForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Связываем события
        self.ui.actionButton.clicked.connect(self.on_button_click)
        self.ui.modeCheckBox.stateChanged.connect(self.on_checkbox_changed)
        self.ui.sizeSlider.valueChanged.connect(self.on_slider_changed)
        
        # Инициализация переменных
        self.button_mode = 1  # 1 - обычный режим, 2 - особый режим
        
        # Таймер для анимации
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.animate_button)
        self.angle = 0
        self.hue = 0

        self.radius = 20
        self.center_x = 200
        self.center_y = 200

    def on_button_click(self):
        """Обработчик нажатия кнопки"""
        if self.button_mode == 1:
            self.ui.actionButton.setText("Нажато!")
        else:
            self.ui.actionButton.setText("Особый режим")

    def on_checkbox_changed(self, state):
        """Обработчик изменения флажка"""
        self.button_mode = 2 if state else 1

    def on_slider_changed(self, value):
        """Обработчик изменения ползунка - меняет размер шрифта QCheckBox"""
        # Получаем текущий шрифт
        current_font = self.ui.modeCheckBox.font()
        
        # Рассчитываем новый размер шрифта
        font_size = value
        
        # Устанавливаем новый размер шрифта
        current_font.setPointSize(font_size)
        self.ui.modeCheckBox.setFont(current_font)

        self.radius = value * 4

    def animate_button(self):
        """Анимация кнопки: движение и изменение цвета"""
        # Движение по кругу с текущим радиусом
        x = self.center_x + self.radius * math.cos(self.angle)
        y = self.center_y + self.radius * math.sin(self.angle)
        self.ui.actionButton.move(int(x), int(y))
        self.angle += 0.1
        
        # Градиент цвета (HSL)
        self.hue = (self.hue + 1) % 360
        color = QtGui.QColor.fromHsl(self.hue, 255, 150)
        gradient = f"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {color.name()}, stop:1 white);"
        self.ui.actionButton.setStyleSheet(gradient)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyForm()
    window.show()
    
    # Запуск анимации
    window.timer.start(30)
    
    sys.exit(app.exec())
