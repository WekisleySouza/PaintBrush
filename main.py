import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidgetAction, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QCommandLinkButton
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor, QIcon
from PyQt6.QtCore import Qt

class PaintApp(QWidget):
    def __init__(self):
        super().__init__()

        self.__layout = QVBoxLayout()
        self.__options_layout = QHBoxLayout()
        self.screen_label = QLabel()
        self.lista = []

        self.last_x = None
        self.last_y = None
        self.__drawned = 0
        self.__selected_action = 'Pencil'
        self.__selected_color = 'black'
        self.__selected_pencil_width = 6
        self.__selected_eraser_width = 20

        # Initial structure construction methods
        self.setLayout(self.__layout)
        self.create_options_layout()
        self.set_drawning_screen()

        self.create_button('Pincel', lambda:self.set_selected_action('Pencil'))
        self.create_button('Borracha', lambda:self.set_selected_action('Eraser'))
        self.create_button('Quadrado', lambda:self.set_selected_action('Square'))
        self.create_button('teste', lambda:self.set_selected_action('teste'))
        self.create_button('Quadrado', lambda:self.set_selected_action('Square'))
        self.create_button('Quadrado', lambda:self.set_selected_action('Square'))
        self.create_button('Quadrado', lambda:self.set_selected_action('Square'))
        self.create_button('Quadrado', lambda:self.set_selected_action('Square'))
    
    def create_options_layout(self):

        self.__layout.addLayout(self.__options_layout)

    def set_selected_action(self, name):
        print(f"{name} selecionado!")
        self.__selected_action = name

    def set_drawning_screen(self):
        canvas = QPixmap(800, 700)
        canvas.fill(Qt.GlobalColor.white)
        self.screen_label.setPixmap(canvas)
        self.__layout.addWidget(self.screen_label)
        self.draw()

    def create_button(self, text, func):
        button = QPushButton(text)
        button.clicked.connect(func)
        self.__options_layout.addWidget(button)

    def pencil_action(self, current_x, current_y):
        if self.last_x is None:
            self.last_x = current_x
            self.last_y = current_y
            return
        
        canvas = self.screen_label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(self.__selected_pencil_width)
        pen.setColor(QColor(self.__selected_color))
        painter.setPen(pen)
        painter.drawLine(self.last_x, self.last_y, current_x, current_y)
        painter.end()

        self.lista.append(canvas)
        self.last_x = current_x
        self.last_y = current_y

    def eraser_action(self, current_x, current_y):
        if self.last_x is None:
            self.last_x = current_x
            self.last_y = current_y
            return
        
        canvas = self.screen_label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(self.__selected_eraser_width)
        pen.setColor(QColor('white'))
        painter.setPen(pen)
        painter.drawLine(self.last_x, self.last_y, current_x, current_y)
        painter.end()
        self.lista.append(canvas)
        self.last_x = current_x
        self.last_y = current_y

    def draw_square(self, current_x, current_y):
        if self.last_x is None:
            self.last_x = current_x
            self.last_y = current_y
            return
        
        possible_x = current_x - self.last_x
        possible_y = current_y - self.last_y
        new_width = possible_x if possible_x > possible_y else possible_y
        new_width = new_width if new_width >= 0 else 1
        new_x = int(current_x - possible_x / 2)
        new_y = int(current_y - possible_y / 2)

        if new_width > 1:
            canvas = self.screen_label.pixmap()
            painter = QPainter(canvas)
            pen = QPen()
            pen.setWidth(new_width)
            pen.setColor(QColor(self.__selected_color))
            painter.setPen(pen)
            painter.drawPoint(new_x, new_y)
        
            if len(self.lista) > 0 and self.last_x is not None:
                self.set_drawning_screen()
                self.lista.pop()
            
            self.lista.append(canvas)

    def draw(self):
        for i in self.lista:
            self.screen_label.setPixmap(i)

    def mouseMoveEvent(self, e):
        current_x = int(e.position().x()) - 10
        current_y = int(e.position().y()) - 40

        if self.__selected_action == 'Pencil':
            self.pencil_action(current_x, current_y)
        elif self.__selected_action == 'Eraser':
            self.eraser_action(current_x, current_y)
        elif self.__selected_action == 'Square':
            self.draw_square(current_x, current_y)

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def paintEvent(self, event):
        self.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaintApp()
    window.show()
    sys.exit(app.exec())
