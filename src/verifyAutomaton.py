# Função para verificar se o autômato é um AFD válido
def verify(transicoes: list) -> bool:
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
