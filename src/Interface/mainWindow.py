import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from centerWindow import centralizar_janela
from estado_final import estadoFinal   
from estado import estado 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MinimizeDFA")
        self.resize(1920, 1080)
        centralizar_janela(self)

        layout = QVBoxLayout()

        estado_normal = estado("q0", 50, 50)
        estado_final = estadoFinal("q1", 50, 80)
        # Adiciona o widget ao layout
        layout.addWidget(estado_normal)
        layout.addWidget(estado_final)
        # Define o layout em um widget central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    # Use um caminho absoluto para o arquivo de texto
    automato_path = os.path.join(os.path.dirname(__file__), '../../automatos/automatoV.txt')
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec_())
