# Campo Minado

Jogo de tabuleiro no terminal, desenvolvido em Python para dois jogadores humanos, como trabalho da disciplina Lógica, Algoritmos e Programação da Faculdade PIT.

## Como executar

É necessário ter Python 3 instalado. O jogo não usa bibliotecas externas.

1. Baixe o repositório pelo botão **Code > Download ZIP** do GitHub e extraia os arquivos, ou clone o repositório se tiver acesso.
2. Abra o terminal dentro da pasta que contém `campo_minado.py`.
3. Execute:

```powershell
python campo_minado.py
```

No Windows, se o Python estiver disponível pelo inicializador, também é possível usar:

```powershell
py campo_minado.py
```

Informe os nomes dos dois jogadores. Nomes vazios ou iguais são recusados; espaços nas extremidades são removidos e os nomes são convertidos para maiúsculas.

## Menu e controles

| Opção | Ação |
| --- | --- |
| 1 | Iniciar uma partida |
| 2 | Consultar as regras |
| 3 | Consultar o placar acumulado |
| 4 | Consultar o histórico das partidas |
| 5 | Encerrar a sessão |

Durante a partida, digite primeiro a linha e depois a coluna, de 1 a 5. Após o resultado, responda **S** para uma nova partida ou **N** para voltar ao menu. Letras minúsculas e espaços nas extremidades são aceitos nessa confirmação.

## Regras

- O tabuleiro compartilhado tem 5 linhas, 5 colunas e quatro minas fixas.
- P1 inicia cada partida. Os jogadores alternam uma jogada válida por vez.
- Uma casa fechada aparece como `-`.
- Abrir uma casa segura vale um ponto e mostra a quantidade de minas nas até oito casas vizinhas, inclusive zero.
- Cada jogada abre somente uma casa; não há abertura em cascata.
- Quem abrir uma mina perde imediatamente; o outro jogador vence. A mina aberta aparece como `*`.
- Quando todas as casas seguras são abertas, vence quem somou mais pontos; pontuações iguais resultam em empate.
- Letras, símbolos, campos vazios, números fora do intervalo e casas já abertas são recusados sem consumir a vez.
- Cada partida nova limpa o tabuleiro e os pontos da partida. O mapa fixo de minas é mantido.
- Placar e histórico permanecem em memória durante a sessão. Ao encerrar o programa, esses dados não são salvos.

Com quatro minas, o tabuleiro padrão possui 21 casas seguras: se todas forem abertas, P1 terá 11 pontos e P2 terá 10. O empate por pontos é previsto pela lógica e pode ser verificado em um cenário de teste com cinco minas e 20 casas seguras; não é uma opção do menu atual.

## Organização e divisão de tarefas

O programa fica em um único arquivo, `campo_minado.py`, organizado em funções. Usa matriz de listas, laços, listas, dicionários, tuplas e conjuntos, sem imports, classes ou bibliotecas externas.

| Integrante | Parte |
| --- | --- |
| Pessoa 1 — Glauckyon (Devglawkkj) | Criação e exibição do tabuleiro, validação das entradas, integração dos turnos, regras, menu e reinício |
| Pessoa 2 — Ricardo (joaodeoliveira2811-debug) | Mapa de minas, contagem de vizinhas, abertura de casas, resultado, placar, histórico e estatísticas da sessão |

### Funções da Pessoa 1

| Função | Finalidade e retorno |
| --- | --- |
| `criar_tabuleiro(tamanho)` | Cria e devolve uma matriz quadrada de casas fechadas, com linhas independentes |
| `mostrar_tabuleiro(tabuleiro)` | Exibe as casas com linhas e colunas numeradas, sem modificar a matriz |
| `ler_numero(mensagem, minimo, maximo)` | Repete a leitura até receber um inteiro válido no intervalo e devolve esse número |
| `ler_jogada(tabuleiro)` | Recusa coordenadas inválidas ou casas abertas e devolve uma tupla de índices iniciados em zero |
| `jogar_partida(jogadores, minas, tamanho)` | Integra jogadas, pontos e alternância; devolve `P1`, `P2` ou `Empate` |
| `mostrar_regras()` | Exibe as regras sem revelar as posições das minas |
| `confirmar_reinicio()` | Valida S/N e devolve um booleano indicando se haverá nova partida |
| `menu_principal()` | Identifica os jogadores e mantém a navegação, o placar e o histórico da sessão |

### Funções da Pessoa 2

| Função | Finalidade e retorno |
| --- | --- |
| `contar_minas_vizinhas(linha, coluna, minas, tamanho)` | Percorre as vizinhas válidas e devolve a quantidade de minas |
| `abrir_casa(tabuleiro, linha, coluna, minas)` | Atualiza uma casa; devolve True se atingiu mina e False se abriu casa segura |
| `contar_casas_seguras_restantes(tabuleiro, minas)` | Percorre a matriz e devolve quantas casas seguras continuam fechadas |
| `verificar_resultado(tabuleiro, minas, pontos, jogador_atual, atingiu_mina)` | Devolve P1, P2, Empate ou EM_ANDAMENTO |
| `registrar_resultado(resultado, placar, historico)` | Atualiza o placar e adiciona o resultado ao histórico; não devolve valor explícito |
| `mostrar_placar(placar)` | Exibe vitórias e empates acumulados |
| `mostrar_historico(historico)` | Exibe os resultados na ordem das partidas |
| `mostrar_estatisticas(placar, historico)` | Exibe total, vitórias, empates, porcentagens e maiores sequências |

A divisão e os contratos estão em [DIVISAO_DO_TRABALHO.md](DIVISAO_DO_TRABALHO.md).

## Desafio de lógica

O desafio **Estatísticas da sessão** está implementado em `mostrar_estatisticas(placar, historico)`, chamada pelo menu ao escolher **5 - Sair**. Usa `len()` para o total, `count()` para as vitórias e laços sobre o histórico para as sequências. Empate ou vitória do adversário interrompe a sequência. As porcentagens consideram todas as partidas e são arredondadas para uma casa decimal. Sem partidas, apresenta zero sem dividir por zero.

## Revisão de requisitos

A revisão do código e os resultados de 20 casos de teste estão em [REVISAO_REQUISITOS.md](REVISAO_REQUISITOS.md). O documento inclui as verificações de conteúdo permitido e as pendências externas ao programa.

## Entregas em preparação

Além do código, a dupla preparará o relatório técnico no template do professor e o vídeo explicativo com participação dos dois integrantes. Os links serão incluídos quando estiverem disponíveis.
