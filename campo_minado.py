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


# Pessoa 2 - Ricardo: conta somente as casas seguras que continuam fechadas.
def contar_casas_seguras_restantes(tabuleiro, minas):
    restantes = 0
    # Percorre todas as linhas e colunas, sem contar as posicoes das minas.
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] == "-" and (linha, coluna) not in minas:
                restantes = restantes + 1
    return restantes


# Recebe o estado apos a jogada e devolve o resultado, sem alterar os dados.
# jogador_atual identifica quem acabou de jogar: "P1" ou "P2".
def verificar_resultado(tabuleiro, minas, pontos, jogador_atual, atingiu_mina):
    # A derrota por mina tem prioridade sobre as casas restantes e os pontos.
    if atingiu_mina:
        if jogador_atual == "P1":
            return "P2"
        return "P1"
    if contar_casas_seguras_restantes(tabuleiro, minas) > 0:
        return "EM_ANDAMENTO"
    if pontos["P1"] > pontos["P2"]:
        return "P1"
    elif pontos["P2"] > pontos["P1"]:
        return "P2"
    return "Empate"


# Lê um inteiro positivo no intervalo informado e repete até a entrada ser válida.
def ler_numero(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem).strip()
        # Limita o texto antes de converter e rejeita dígitos fora de 0 a 9.
        if entrada.isdigit() and len(entrada) <= len(str(maximo)):
            digitos_validos = True
            for caractere in entrada:
                if caractere not in "0123456789":
                    digitos_validos = False
            if digitos_validos:
                numero = int(entrada)
                if numero >= minimo and numero <= maximo:
                    return numero
        print("Entrada inválida! Digite de " + str(minimo) + " a " + str(maximo) + ".")


# Devolve uma posição fechada, com índices internos a partir de zero.
def ler_jogada(tabuleiro):
    while True:
        linha = ler_numero("Escolha a linha (1 a " + str(len(tabuleiro)) + "): ", 1, len(tabuleiro)) - 1
        coluna = ler_numero("Escolha a coluna (1 a " + str(len(tabuleiro[linha])) + "): ", 1, len(tabuleiro[linha])) - 1
        if tabuleiro[linha][coluna] == "-":
            return (linha, coluna)
        print("Essa casa já foi aberta! Escolha outra posição.")


# Conduz uma partida nova e devolve somente o resultado para o menu registrar.
def jogar_partida(jogadores, minas, tamanho):
    tabuleiro = criar_tabuleiro(tamanho)
    pontos = {"P1": 0, "P2": 0}
    identificadores = ("P1", "P2")
    indice_jogador = 0
    resultado = "EM_ANDAMENTO"
    mostrar_tabuleiro(tabuleiro)

    while resultado == "EM_ANDAMENTO":
        jogador_atual = identificadores[indice_jogador]
        print("Vez de " + jogadores[indice_jogador] + " (" + jogador_atual + ").")
        posicao = ler_jogada(tabuleiro)
        atingiu_mina = abrir_casa(tabuleiro, posicao[0], posicao[1], minas)
        if atingiu_mina:
            print(jogadores[indice_jogador] + " abriu uma mina!")
        else:
            pontos[jogador_atual] = pontos[jogador_atual] + 1

        mostrar_tabuleiro(tabuleiro)
        print("Pontos: " + jogadores[0] + " = " + str(pontos["P1"])
              + " | " + jogadores[1] + " = " + str(pontos["P2"]))
        resultado = verificar_resultado(tabuleiro, minas, pontos, jogador_atual, atingiu_mina)
        # Só troca o jogador depois de uma jogada válida e se a partida continuar.
        if resultado == "EM_ANDAMENTO":
            indice_jogador = 1 - indice_jogador

    if resultado == "Empate":
        print("A partida terminou empatada!")
    elif resultado == "P1":
        print("Vencedor: " + jogadores[0] + " (P1)!")
    else:
        print("Vencedor: " + jogadores[1] + " (P2)!")
    return resultado


# Pessoa 2 - Ricardo: registra um resultado final no placar e no historico.
# O menu deve chamar esta funcao uma unica vez por partida encerrada.
def registrar_resultado(resultado, placar, historico):
    if resultado == "P1" or resultado == "P2":
        placar[resultado] = placar[resultado] + 1
    elif resultado == "Empate":
        placar["Empates"] = placar["Empates"] + 1
    else:
        # Uma partida em andamento ou um resultado invalido nao e registrado.
        return
    historico.append(resultado)


# Exibe o placar acumulado sem modificar as quantidades registradas.
def mostrar_placar(placar):
    print("\nPlacar da sessão:")
    print("Vitórias de P1: " + str(placar["P1"]))
    print("Vitórias de P2: " + str(placar["P2"]))
    print("Empates: " + str(placar["Empates"]))


# Exibe os resultados na ordem das partidas, numeradas a partir de um.
def mostrar_historico(historico):
    print("\nHistórico das partidas:")
    if len(historico) == 0:
        print("Nenhuma partida foi registrada.")
    else:
        for indice in range(len(historico)):
            if historico[indice] == "Empate":
                print("Partida " + str(indice + 1) + ": empate.")
            else:
                print("Partida " + str(indice + 1) + ": vencedor " + historico[indice] + ".")
