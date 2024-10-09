from minimizeAutomaton import minimizeAutomaton
from diagram import gerar_diagrama_automato

path_to_automaton = str(input('Digite o caminho para seu automato a partir da pasta "automatos" (com a extensão .txt): '))
minimized = minimizeAutomaton(f"./automatos/{path_to_automaton}")
gerar_diagrama_automato(minimized, path_to_automaton)
