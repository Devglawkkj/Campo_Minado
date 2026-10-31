# Cria e devolve uma matriz quadrada com todas as casas fechadas.
def criar_tabuleiro(tamanho):
    tabuleiro = []
    for linha in range(tamanho):
        # Cada linha precisa ser uma lista nova para manter as casas independentes.
        casas = []
        for coluna in range(tamanho):
            casas.append("-")
        tabuleiro.append(casas)
    return tabuleiro


# Mostra as casas e a numeração das linhas e colunas, sem alterar a matriz.
def mostrar_tabuleiro(tabuleiro):
    print("   ", end="")
    for coluna in range(len(tabuleiro[0])):
        print(str(coluna + 1) + " ", end="")
    print()

    # O laço externo percorre as linhas; o interno mostra cada casa da linha.
    for linha in range(len(tabuleiro)):
        print(str(linha + 1) + "  ", end="")
        for coluna in range(len(tabuleiro[linha])):
            print(str(tabuleiro[linha][coluna]) + " ", end="")
        print()
