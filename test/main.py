import sys 
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        self.set_surface()
        self.last_x, self.last_y = None, None

        # self.draw_line()
        # self.draw_point()
        # self.draw_square()
        # self.draw_square_line()

    # Desenha em pontos
    # def mouseMoveEvent(self, e):
    #     canvas = self.label.pixmap()
    #     painter = QtGui.QPainter(canvas)
    #     painter.drawPoint(int(e.position().x()), int(e.position().y()))
    #     painter.end()
    #     self.label.setPixmap(canvas)

    def set_surface(self):
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
    
    # Desenha em pontos
    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = int(e.position().x())
            self.last_y = int(e.position().y())
            return
        # print(dir(e))
        print(e.position())
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(self.last_x, self.last_y, int(e.position().x()), int(e.position().y()))
        painter.end()
        self.label.setPixmap(canvas)

        self.last_x = int(e.position().x())
        self.last_y = int(e.position().y())

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def draw_line(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(10, 10, 300, 200)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_point(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawPoint(200, 150)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_square(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(40)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(200, 150)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_square_line(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(10)
        pen.setColor(QtGui.QColor("#30F2F2"))
        painter.setPen(pen)
        # Existe o drawRects
        painter.drawRect(50, 50, 100, 100)
        painter.end()
        self.label.setPixmap(canvas)

    def draw_colored_square(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#30F2F2"))
        painter.setPen(pen)

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("#FF0000"))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(10, 10, 90, 90)
        painter.end()
        self.label.setPixmap(canvas)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()