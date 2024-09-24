def getAutomaton(path_to_automaton: str) -> dict:
    """
    Função para pegar as informações do autômado contidas num arquivo txt

    Args:
        path_to_automaton (str): caminho para arquivo do autômato

    Returns:
        (dict): dicionário com as informações do autômato
    """

    # lendo o arquivo
    with open(path_to_automaton, 'r') as f:
        linhas = f.readlines()

    # Variáveis para armazenar as informações
    alfabeto = []
    estados = []
    estado_inicial = None
    estados_finais = []
    transicoes = []

    for linha in linhas:
        linha = linha.strip()
        
        # Dividindo as linhas de acordo com o tipo de informação
        if linha.startswith("alfabeto"):
            alfabeto = linha.split(":")[1].split(",")
        elif linha.startswith("estados"):
            estados = linha.split(":")[1].split(",")
        elif linha.startswith("inicial"):
            estado_inicial = linha.split(":")[1].strip()
        elif linha.startswith("finais"):
            estados_finais = linha.split(":")[1].split(",")
        elif linha.startswith("transicoes"):
            continue
        elif "," in linha:  # Cada transição é no formato "estado de origem, estado de destino, simbolo"
            origem, destino, simbolo = [x.strip() for x in linha.split(",")]
            transicoes.append([origem, destino, simbolo])
    
    return {
        "alfabeto": alfabeto,
        "estados": estados,
        "estado_inicial": estado_inicial,
        "estados_finais": estados_finais,
        "transicoes": transicoes
    }