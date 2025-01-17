def verify(alfabeto: list, estados: list, transicoes: list) -> bool:
    """
    Função para verificar se o autômato é um AFD válido

    Args:
        alfabeto (list): lista que contém todos os símbolos do autômato
        estados (list): lista que contém todos os estados do autômato
        transicoes (list): lista que contém todas as transições do autômato

    Returns:
        (bool): retorna True ou False dependendo se o autômato for um AFD válido 
                ou não
    """


    def verifyUniDestiny(transicoes: list) -> bool:
        """
        Função que verifica se existe mais de um estado-destino diferente para um único símbolo 
        processado de cada estado

        Args:
            transicoes (list): lista que contém todas as transições do autômato

        Returns:
            (bool): True se em cada estado ao processar um símbolo esse processamento leva a
                    um único estado-destino
        """
    
        pares = {}
        
        for estado_origem, estado_destino, simboloProcessado in transicoes:
            par = (estado_origem, simboloProcessado)
            if par in pares:
                if estado_destino not in pares[par]:
                    return False
            else:
                pares[par] = set()
                pares[par].add(estado_destino)
        
        return True
    

    def verifyStateSymbols(alfabeto: list, estados:list, transicoes: list) -> bool:
        """
        Função que verifica se cada estado processa todos os símbolos
        do alfabeto

        Args:
            alfabeto (list): lista que contém todos os símbolos do autômato
            estados (list): lista que contém todos os estados do autômato
            transicoes (list): lista que contém todas as transições do autômatos 

        Returns:
            (bool): True se cada um dos estados processa todos os símbolos do alfabeto
        """

        transicoes_dict = {estado: set() for estado in estados}
        
        for origem, destino, simbolo in transicoes:
            if origem in transicoes_dict:
                transicoes_dict[origem].add(simbolo)
        
        for estado, simbolos_processados in transicoes_dict.items():
            if set(alfabeto) != simbolos_processados:
                return False  
        
        return True  

    hasUniDestiny = verifyUniDestiny(transicoes)
    processAllSymbols = verifyStateSymbols(alfabeto, estados, transicoes)

    if (hasUniDestiny and processAllSymbols):
        return True
    else:
        return False
