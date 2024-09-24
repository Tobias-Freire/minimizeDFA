import os

def writeAutomaton(automato: dict, name: str, path: str):
    """
    Função que escreve o autômato definido por um mapa em um arquivo de texto

    Args:
        automaton (dict): dicionário que define o automato passado como argumento
        name (str): nome do automato
        path (str): caminho para onde o usuário quer salvar o arquivo de texto

    Returns:
        Nenhum, mas um arquivo de texto é escrito e armazenado no local especificado
    """
    
    # Montar o conteúdo do arquivo
    conteudo = []
    
    # Escreve o alfabeto
    conteudo.append("alfabeto:" + ",".join(automato["alfabeto"]))
    
    # Escreve os estados
    conteudo.append("estados:" + ",".join(automato["estados"]))
    
    # Escreve o estado inicial
    conteudo.append("inicial:" + automato["estado_inicial"])
    
    # Escreve os estados finais
    conteudo.append("finais:" + ",".join(automato["estados_finais"]))
    
    # Escreve as transições
    conteudo.append("transicoes")
    for origem, destino, simbolo in automato["transicoes"]:
        conteudo.append(f"{origem}, {destino}, {simbolo}")
    
    # Define o caminho completo para salvar o arquivo
    caminho_completo = os.path.join(path, name + "_minimized.txt")
    
    # Escreve o conteúdo no arquivo
    with open(caminho_completo, "w") as arquivo:
        arquivo.write("\n".join(conteudo))
    
    print(f"Autômato salvo em: {caminho_completo}")