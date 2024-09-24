from PyQt5.QtWidgets import QDesktopWidget

def centralizar_janela(janela):
    # Obtém o quadro da janela
    qr = janela.frameGeometry()
    
    # Obtém a resolução da tela e calcula o ponto central
    centro_tela = QDesktopWidget().availableGeometry().center()
    
    # Move o quadro da janela para o centro da tela
    qr.moveCenter(centro_tela)
    
    # Move a janela para o ponto calculado
    janela.move(qr.topLeft())