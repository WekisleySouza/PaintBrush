import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPainter, QPixmap, QColor, QPen, QPainterPath
from collections import deque

class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Apagar Última Figura')
        self.setGeometry(100, 100, 400, 400)

        self.canvas = QLabel(self)
        self.setCentralWidget(self.canvas)
        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(QColor("white"))
        self.canvas.setPixmap(self.pixmap)

        self.drawn_shapes = deque()  # Uma fila para armazenar as formas desenhadas
        self.current_pen = QPen(QColor("black"))
        self.current_path = QPainterPath()

    def paintEvent(self, event):
        painter = QPainter(self.canvas.pixmap())
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # Opcional para desenho suave

        for shape in self.drawn_shapes:
            painter.setPen(shape['pen'])
            if shape['type'] == 'point':
                painter.drawPoint(shape['point'])
            elif shape['type'] == 'path':
                painter.setPen(shape['pen'])
                painter.drawPath(shape['path'])

        painter.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.current_path.moveTo(event.localPos())
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.current_path.lineTo(event.localPos())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawn_shapes.append({'type': 'path', 'path': self.current_path, 'pen': self.current_pen})
            self.current_path = QPainterPath()
            self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Z and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if self.drawn_shapes:
                self.drawn_shapes.pop()
                self.repaint()  # Redesenha a imagem sem a última forma

def main():
    app = QApplication(sys.argv)
    window = DrawingApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
