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
| 5 | Exibir as estatísticas e encerrar a sessão |

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
| Pessoa 1 — Devglawkkj | Criação e exibição do tabuleiro, validação das entradas, integração dos turnos, regras, menu e reinício |
| Pessoa 2 — Ricardo | Mapa de minas, contagem de vizinhas, abertura de casas, resultado, placar, histórico e estatísticas da sessão |

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
| `contar_minas_vizinhas(linha, coluna, minas, tamanho)` | Conta e devolve o número de minas nas casas vizinhas, respeitando os limites do tabuleiro |
| `abrir_casa(tabuleiro, linha, coluna, minas)` | Atualiza a casa escolhida e devolve `True` ao atingir uma mina ou `False` ao abrir uma casa segura |
| `contar_casas_seguras_restantes(tabuleiro, minas)` | Conta e devolve a quantidade de casas seguras ainda fechadas |
| `verificar_resultado(tabuleiro, minas, pontos, jogador_atual, atingiu_mina)` | Determina o estado após a jogada e devolve `EM_ANDAMENTO`, `P1`, `P2` ou `Empate` |
| `registrar_resultado(resultado, placar, historico)` | Atualiza o placar e acrescenta o resultado ao histórico; ignora resultados inválidos ou partidas em andamento |
| `mostrar_placar(placar)` | Exibe as vitórias de cada jogador e os empates acumulados |
| `mostrar_historico(historico)` | Exibe os resultados na ordem das partidas ou informa que nenhuma foi registrada |
| `mostrar_estatisticas(placar, historico)` | Exibe o total de partidas, o placar, as porcentagens e as maiores sequências de vitórias de cada jogador |

As funções de exibição e registro não devolvem um valor explícito.

## Desafio de lógica

O desafio **Estatísticas da sessão** está implementado em `mostrar_estatisticas(placar, historico)` e é exibido ao escolher **5 — Sair** no menu.

- Total de partidas encerradas, vitórias de P1 e P2 e quantidade de empates.
- Porcentagem de vitórias de cada jogador sobre o total de partidas, incluindo os empates no denominador, arredondada para uma casa decimal.
- Maior sequência de vitórias consecutivas de cada jogador. Um empate ou uma vitória do adversário interrompe a sequência.
- Se nenhuma partida tiver sido jogada, os totais, as porcentagens e as sequências aparecem zerados, sem divisão por zero.

Por exemplo, o histórico `P1, P1, Empate, P2` resulta em quatro partidas, duas vitórias de P1 (50,0%), uma de P2 (25,0%) e um empate. As maiores sequências são duas vitórias para P1 e uma para P2. No terminal, os percentuais usam ponto decimal.

## Arquivos do projeto

| Arquivo | Conteúdo |
| --- | --- |
| [campo_minado.py](campo_minado.py) | Código do jogo, menu e estatísticas da sessão |
| [README.md](README.md) | Instruções de execução, regras e documentação das funções |

## Entregas em preparação

Além do código, a dupla preparará o relatório técnico no template do professor e o vídeo explicativo com participação dos dois integrantes. Os links serão incluídos quando estiverem disponíveis.
