from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QPen, QBrush, QFont, QFontMetrics
from PyQt5.QtWidgets import QWidget

class estado(QWidget):
    def __init__(self, texto="", x=None, y=None, parent=None):
        super().__init__(parent)
        self.texto = texto
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0

    def paintEvent(self, event):
        painter = QPainter(self)

        # Define a fonte e calcula o tamanho do texto
        font = QFont("Arial", 24)
        painter.setFont(font)
        font_metrics = QFontMetrics(font)
        text_width = font_metrics.horizontalAdvance(self.texto)  # Largura do texto
        text_height = font_metrics.height()  # Altura do texto

        # Ajusta o tamanho da elipse com base no tamanho do texto
        elipse_width = max(100, text_width + 40)  # Largura mínima 100, ou mais se o texto for maior
        elipse_height = max(100, text_height + 40)  # Altura mínima 100, ou mais se o texto for maior

        # Desenha a elipse externa (grande)
        rect = QRectF(self.x, self.y, elipse_width, elipse_height)

        # Desenha o círculo/elipse amarelo preenchido
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(rect)

        # Desenha o círculo/elipse de contorno preto (grande)
        painter.setBrush(Qt.NoBrush)
        painter.setPen(QPen(Qt.black, 4))
        painter.drawEllipse(rect)

        painter.setPen(Qt.black)
        painter.drawText(rect, Qt.AlignCenter, self.texto)

    def isFinal(self):
        return False
