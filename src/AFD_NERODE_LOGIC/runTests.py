from minimizeAutomaton import minimizeAutomaton

path_to_automaton = str(input('Digite o caminho para seu automato a partir da pasta "automatos" (com a extensão .txt): '))
minimizeAutomaton(f"automatos/{path_to_automaton}")


