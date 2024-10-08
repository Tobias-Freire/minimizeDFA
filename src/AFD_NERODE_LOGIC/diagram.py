from graphviz import Digraph

def gerar_diagrama_automato(automato):
    fsm = Digraph('DFA', filename='dfa_diagram', format='png')

    # Adicionar estados
    for estado in automato['estados']:
        if estado in automato['estados_finais']:
            fsm.node(estado, shape='doublecircle')  # Estado final com círculo duplo
        else:
            fsm.node(estado, shape='circle')  # Estado regular

    # Adicionar transições (ajustado para o formato fornecido)
    for transicao in automato['transicoes']:
        estado_origem, estado_destino, simbolo = transicao
        fsm.edge(estado_origem, estado_destino, label=simbolo)

    # Adicionar estado inicial
    fsm.node('', shape='none')  # Estado vazio (para a seta inicial)
    fsm.edge('', automato['estado_inicial'], label='start')

    # Renderizar o diagrama
    fsm.view()