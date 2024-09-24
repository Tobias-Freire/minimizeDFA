import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from centerWindow import centralizar_janela
from estado_final import estadoFinal   
from estado import estado 
from minimizeAutomaton import minimizeAutomaton

class MainWindow(QMainWindow):
    def __init__(self, automato: dict):
        super().__init__()
        self.automato = automato
        self.setWindowTitle("MinimizeDFA")
        self.resize(1920, 1080)
        centralizar_janela(self)

        layout = QVBoxLayout()
        x = y = 0
        for estado_info in automato["estados"]:
            x += 100
            y += 100
            automaton = estado(estado_info, x, y)
            # Adiciona o widget ao layout
            layout.addWidget(automaton)

        # Define o layout em um widget central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    # Use um caminho absoluto para o arquivo de texto
    automato_path = os.path.join(os.path.dirname(__file__), '../../automatos/automatoV.txt')
    automato = minimizeAutomaton(automato_path)
    app = QApplication(sys.argv)
    janela = MainWindow(automato)
    janela.show()
    sys.exit(app.exec_())
