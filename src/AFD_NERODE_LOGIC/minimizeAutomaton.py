import os
from getAutomaton import getAutomaton
from verifyAutomaton import verify
from write_automaton import writeAutomaton

def minimizeAutomaton(path_to_automaton: str) -> int:
    """
    Função que executa toda a lógica para minimização de um AFD

    Args: 
        path_to_automaton (str): caminho para o txt que define o autômato
    
    Returns:
        - Retorna 0 se acontecer algum erro
        - Retorna 1 se tudo ocorrer bem e o autômato for minimizado
            - Nesse caso, um novo arquivo txt é escrito com a definição do autômato
              minimizado
    """

    def nerodeAlgorithm(automato: dict) -> dict:
        """
        Função que executa o algoritmo de Myhill Nerode para minimizar um AFD

        Args:
            automato (dict): dicionário com as definições do autômato a ser minimizado

        Returns:
            (dict): dicionário com as definições do autômato minimizado
        """
        
        estados = automato["estados"]
        estados_finais = set(automato["estados_finais"])
        transicoes = automato["transicoes"]
        alfabeto = automato["alfabeto"]
        
        # Passo 1: Inicialização - Separar estados finais e não finais
        P = [estados_finais, set(estados) - estados_finais]  # Partição inicial
        W = [estados_finais]  # Conjunto de trabalho

        # Função que retorna o estado de destino para uma transição com um dado símbolo
        def transicao(estado, simbolo):
            for origem, destino, s in transicoes:
                if origem == estado and s == simbolo:
                    return destino
            return None  # Se não houver transição, retorna None
        
        # Função para refinar a partição
        def refina(P, W):
            while W:
                A = W.pop()
                for simbolo in alfabeto:
                    # Estados que possuem transições para estados em A com o símbolo atual
                    X = {q for q in estados if transicao(q, simbolo) in A}
                    for Y in P[:]:
                        intersecao = X & Y
                        diferenca = Y - X
                        if intersecao and diferenca:
                            # Atualiza a partição P dividindo Y em interseção e diferença
                            P.remove(Y)
                            P.append(intersecao)
                            P.append(diferenca)
                            # Adiciona interseção ou diferença a W para refinar mais tarde
                            if Y in W:
                                W.remove(Y)
                                W.append(intersecao)
                                W.append(diferenca)
                            else:
                                if len(intersecao) <= len(diferenca):
                                    W.append(intersecao)
                                else:
                                    W.append(diferenca)
                            print("Partição atual: \n", P, "\n")
            return P

        # Passo 2: Refinar a partição até encontrar estados equivalentes
        P = refina(P, W)
        
        # Passo 3: Construir o autômato minimizado
        grupo_para_estado = {}
        novos_estados = []
        for grupo in P:
            nome_grupo = ''.join(sorted(grupo))  # Concatenar e ordenar os estados do grupo
            novos_estados.append(nome_grupo)
            for estado in grupo:
                grupo_para_estado[estado] = nome_grupo  # Mapear estados originais para seus grupos

        novo_estado_inicial = grupo_para_estado[automato['estado_inicial']]
        novos_estados_finais = {grupo_para_estado[estado] for estado in estados_finais if estado in grupo_para_estado}

        # Nova lista de transições com estados minimizados
        novas_transicoes = []
        for origem, destino, simbolo in transicoes:
            novo_origem = grupo_para_estado[origem]
            novo_destino = grupo_para_estado[destino]
            if [novo_origem, novo_destino, simbolo] not in novas_transicoes:
                novas_transicoes.append([novo_origem, novo_destino, simbolo])
        
        # Retornar o autômato minimizado
        automato_minimizado = {
            "alfabeto": alfabeto,
            "estados": novos_estados,
            "estado_inicial": novo_estado_inicial,
            "estados_finais": list(novos_estados_finais),
            "transicoes": novas_transicoes
        }
        
        return automato_minimizado
        

    
    automato = getAutomaton(path_to_automaton)
    automatonIsCorrect = verify(automato["alfabeto"], automato["estados"], automato["transicoes"])

    if(automatonIsCorrect):
        print("\033[92mO autômato passado é um AFD!\033[0m\nComeçando processamento de minimização...\n")
        automato_mini = nerodeAlgorithm(automato)
        print(automato_mini)
        # Obtém o nome do arquivo de texto do automato original a partir do caminho
        archive_original_name = os.path.basename(path_to_automaton)
        # Remove a extensão (pois em write_automaton ele adiciona a extensão .txt)
        archive_original_name = os.path.splitext(archive_original_name)[0]
        writeAutomaton(automato_mini, archive_original_name, '././automatos')
        return 1
    else:
        print("\033[91mO autômato passado não é um AFD\033[0m")
        return 0