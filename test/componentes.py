import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

def funcao():
    label.setText("Botao 1 pressionado!")
    label.adjustSize()

def funcao2():
    label.setText("Botao 2 pressionado!")
    label.adjustSize()


app = QApplication(sys.argv)
janela = QWidget()
janela.resize(800, 600)
janela.setWindowTitle("Janela de teste")

btn = QPushButton("Botão 1", janela)
btn.setGeometry(100, 100, 150, 80)
btn.setStyleSheet(
        'background-color: blue;'
        'color: white;'
    )
btn.clicked.connect(funcao)

btn2 = QPushButton("Botão 2", janela)
btn2.setGeometry(300, 100, 150, 80)
btn2.setStyleSheet(
        'background-color: blue;'
        'color: white;'
    )
btn2.clicked.connect(funcao2)

label = QLabel("Texto", janela)
label.move(100, 400)

janela.show()

app.exec()