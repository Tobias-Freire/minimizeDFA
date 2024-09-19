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
    
        pares_dict = {}
        
        for a, b, s in transicoes:
            par = (a, s)
            if par in pares_dict:
                if b not in pares_dict[par]:
                    return False
            else:
                pares_dict[par] = set()
                pares_dict[par].add(b)
        
        return True
    

    def verifyStateSymbols(alfabeto: list, estados:list, transicoes: list) ->bool:
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
