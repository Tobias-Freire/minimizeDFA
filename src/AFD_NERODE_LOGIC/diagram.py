from graphviz import Digraph
import os

def gerar_diagrama_automato(automato: dict, path:str):
    """
    Função que gera um png com o diagrama de um autômato

    Args:
        automato (dict): Dicionário contendo um autômato
        path (str): caminho para o autômato a ser gerado, necessário para dar nome ao arquivo png

    Returns:
        Uma imagem contendo o diagrama do autômato
    """
    nome_arq = os.path.splitext(os.path.basename(path))[0]

    diagram = Digraph('DFA', filename=f'{nome_arq}_minimized', format='png')

    # Adiciona estados
    for estado in automato['estados']:
        if estado in automato['estados_finais']:
            diagram.node(estado, shape='doublecircle')  
        else:
            diagram.node(estado, shape='circle')  

    # Adiciona transições 
    for transicao in automato['transicoes']:
        estado_origem, estado_destino, simbolo = transicao
        diagram.edge(estado_origem, estado_destino, label=simbolo)

    # Adiciona estado inicial
    diagram.node('', shape='none')  
    diagram.edge('', automato['estado_inicial'], label='start')

    print(f"\033[92mDiagrama do autômato pode ser visto em: {path}\033[0m\n")

    # Renderiza o diagrama
    diagram.view()