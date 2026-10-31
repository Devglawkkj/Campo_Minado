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


# Pessoa 2 - Ricardo: mapa fixo do tabuleiro padrao de 5 x 5.
# As coordenadas internas comecam em zero: (linha, coluna).
minas = {(0, 3), (1, 1), (3, 2), (4, 4)}


# Recebe uma casa, o conjunto de minas e o tamanho do tabuleiro.
# Devolve a quantidade de minas nas ate oito casas vizinhas.
def contar_minas_vizinhas(linha, coluna, minas, tamanho):
    quantidade = 0
    # Percorre o quadrado de 3 x 3 ao redor da casa escolhida.
    for linha_vizinha in range(linha - 1, linha + 2):
        for coluna_vizinha in range(coluna - 1, coluna + 2):
            # Ignora posicoes fora do tabuleiro, inclusive nos cantos e bordas.
            if 0 <= linha_vizinha < tamanho and 0 <= coluna_vizinha < tamanho:
                # A propria casa nao faz parte das suas vizinhas.
                if linha_vizinha != linha or coluna_vizinha != coluna:
                    if (linha_vizinha, coluna_vizinha) in minas:
                        quantidade = quantidade + 1
    return quantidade


# Pessoa 2 - Ricardo: abre somente a casa escolhida, sem abertura em cascata.
# Recebe coordenadas validas de uma casa fechada, conferidas pela leitura da jogada.
# Devolve True ao atingir uma mina e False ao abrir uma casa segura.
def abrir_casa(tabuleiro, linha, coluna, minas):
    if (linha, coluna) in minas:
        tabuleiro[linha][coluna] = "*"
        return True
    tabuleiro[linha][coluna] = contar_minas_vizinhas(linha, coluna, minas, len(tabuleiro))
    return False
