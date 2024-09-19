from getAutomaton import getAutomaton
from verifyAutomaton import verify

def minimizeAutomaton(path_to_automaton: str) -> int:
    """
    Função que executa o algoritmo de Myhill Nerode (Table Filling Method)
    para minimizar um AFD

    Args: None
    
    Returns:
        - Retorna 0 se acontecer algum erro
        - Retorna 1 se tudo ocorrer bem e o autômato for minimizado
            - Nesse caso, um novo arquivo txt é escrito com a definição do autômato
              minimizado
    """
    
    automato = getAutomaton(path_to_automaton)
    automatonIsCorrect = verify(automato["alfabeto"], automato["estados"], automato["transicoes"])

    if(not automatonIsCorrect):
        print("O autômato passado não é um AFD")
        return 0
    else:
        print("O autômato passado é um AFD!\nComeçando processamento de minimização...")
        return 1