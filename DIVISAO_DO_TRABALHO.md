# Campo Minado: proposta de divisão para validação

Status: rascunho para aprovação da dupla. Ainda não autoriza implementar as etapas abaixo.
Integrantes: Pessoa 1 (nome a confirmar) e Pessoa 2 (nome a confirmar).
Repositório: https://github.com/Devglawkkj/Campo_Minado

## 1. Regras propostas para o jogo

- Python no terminal, com dois jogadores humanos alternando as jogadas.
- Tabuleiro compartilhado de 5 x 5, com linhas e colunas numeradas de 1 a 5.
- Quatro minas fixas no código, em conjunto de tuplas. Não usar sorteio.
- Uma jogada válida abre exatamente uma casa; mostrar nela o número de minas vizinhas, inclusive zero. Sem abertura automática em cascata.
- Quem abrir uma mina perde imediatamente; o outro jogador vence.
- Ao abrir todas as casas seguras, vence quem abriu mais casas; pontuações iguais geram empate.
- Entrada inválida ou casa repetida não consome a vez. Reinício limpa o tabuleiro e os pontos da partida, preservando placar e histórico da sessão.
- Desafio escolhido: estatísticas da sessão ao sair, com total, vitórias, empates, porcentagens e maior sequência de vitórias de cada jogador. Empate interrompe a sequência; sessão vazia não pode dividir por zero.
- Como 25 casas menos quatro minas deixa 21 casas seguras, o modo padrão termina por pontos sem empate. Para testar e demonstrar empate, usar cenário documentado com cinco minas (20 casas seguras), sem alterar as regras de pontuação.

Estas são decisões de implementação propostas, não exigências adicionais atribuídas ao professor.

## 2. Restrições do trabalho

Usar matriz, for aninhado, while, if/elif/else, funções def, parâmetros e return, listas, dicionários, tuplas e conjuntos. Usar append(), strip(), upper() e isdigit() com finalidade real.

Proibidos no programa: import (inclusive entre arquivos próprios), bibliotecas, lambda, comprehensions, try/except, classes e orientação a objetos. Manter o jogo em campo_minado.py, com comentários indicando os blocos de cada pessoa. Evitar recursos fora do conteúdo permitido no PDF.

Ter pelo menos cinco funções, duas com parâmetros e duas com return. Validar texto antes de int(); limitar o comprimento e aceitar apenas os dígitos ASCII esperados para impedir conversões problemáticas, inclusive caracteres Unicode que isdigit() aceita.

Adaptar a verificação ao Campo Minado: percorrer a matriz com laços para contar casas seguras restantes; linhas de peças e diagonais vencedoras dos exemplos de Jogo da Velha não são regras deste jogo.

## 3. Divisão de implementação

| Pessoa | Responsabilidade | Funções propostas |
| --- | --- | --- |
| 1 | Criação e exibição da matriz | criar_tabuleiro(tamanho), mostrar_tabuleiro(tabuleiro) |
| 1 | Entradas, regras e menu | ler_numero(mensagem, minimo, maximo), ler_jogada(tabuleiro), mostrar_regras(), confirmar_reinicio(), menu_principal() |
| 1 | Integração da partida e alternância dos jogadores | jogar_partida(jogadores, minas, tamanho) |
| 2 | Minas vizinhas e abertura de casas | contar_minas_vizinhas(linha, coluna, minas, tamanho), abrir_casa(tabuleiro, linha, coluna, minas) |
| 2 | Fim da partida por mina ou casas seguras esgotadas | contar_casas_seguras_restantes(tabuleiro, minas), verificar_resultado(tabuleiro, minas, pontos, jogador_atual, atingiu_mina) |
| 2 | Placar, histórico e desafio | registrar_resultado(resultado, placar, historico), mostrar_placar(placar), mostrar_historico(historico), mostrar_estatisticas(placar, historico) |

Ambas programam, testam e explicam suas funções. Pessoa 1 não implementa antecipadamente as funções da Pessoa 2 e vice-versa.

## 4. Contrato entre as partes

- Matriz: casas fechadas usam "-"; casas abertas guardam número de 0 a 8; mina aberta usa "*". Exibição não revela minas escondidas.
- Coordenadas internas começam em zero. ler_jogada devolve a tupla (linha, coluna), válida e ainda fechada.
- criar_tabuleiro devolve uma matriz nova, com linhas independentes, criada com for e append().
- minas: conjunto fixo de tuplas (linha, coluna), sem duplicatas e dentro dos limites. O mapa final será definido na etapa da lógica.
- jogadores: lista com dois nomes distintos; usar identificadores estáveis "P1" e "P2" nos resultados. pontos e placar usam esses identificadores; placar também possui "Empates".
- abrir_casa modifica uma única casa e devolve True se atingiu mina; False se abriu casa segura. O controlador soma um ponto apenas no segundo caso.
- verificar_resultado devolve "EM_ANDAMENTO", "P1", "P2" ou "Empate". Primeiro trata mina, depois conta casas seguras com for aninhado, depois compara pontos. Não lê teclado nem altera placar.
- jogar_partida devolve somente o resultado final. O menu registra esse resultado uma única vez, exibe placar e oferece nova partida.
- historico: lista de resultados "P1", "P2" ou "Empate", alimentada por append(). registrar_resultado atualiza o placar e o histórico.
- Estatísticas usam count() no histórico e laço para calcular sequências. Porcentagens consideram todas as partidas, inclusive empates.

Se um contrato precisar mudar, combinar primeiro no pull request e atualizar este documento antes de integrar código dependente.

## 5. Etapas pequenas e branches

Após aprovar este documento, estabelecer main como base compartilhada. Como o repositório ainda não tem commits, a primeira publicação precisa criar essa base; depois as mudanças entram por pull request.

As branches são nomeadas pela tarefa, sem nome ou número do integrante. A autoria fica registrada nos commits com a identidade Git de cada pessoa.

Todas as branches seguintes nascem da main atualizada. Não criar branches independentes a partir de repositório vazio em cada computador.

| Ordem | Pessoa | Branch e finalidade | Commit sugerido |
| --- | --- | --- | --- |
| 0 | 1 | docs/divisao-trabalho: proposta atual para validação | Documenta divisão do trabalho |
| 1 | 1 | feat/tabuleiro: criar a matriz | Cria função de tabuleiro |
| 2 | 1 | feat/exibicao: exibir matriz numerada | Exibe linhas e colunas do tabuleiro |
| 3 | 1 | feat/entradas: validar números e casas | Valida entradas e casas repetidas |
| 4 | 2 | feat/minas-vizinhas: mapa e contagem | Conta minas vizinhas |
| 5 | 2 | feat/abertura: atualizar casa escolhida | Implementa abertura de casas |
| 6 | 2 | feat/resultado: determinar vencedor e empate | Verifica resultado da partida |
| 7 | 2 | feat/placar-historico: acumular resultados | Registra placar e histórico |
| 8 | 2 | feat/estatisticas: implementar desafio | Calcula estatísticas da sessão |
| 9 | 1 | feat/partida: conectar regras e turnos | Integra turnos da partida |
| 10 | 1 | feat/menu: menu, regras e reinício | Adiciona menu e nova partida |
| 11 | Ambas, em sequência | docs/entrega: README, relatório e roteiro | Descrever cada entrega em commit separado |

A ordem é intencional: como import é proibido, as duas pessoas editarão o mesmo arquivo Python em turnos de integração. Enquanto uma edita código, a outra pode revisar a lógica e planejar seus testes sem alterar esse arquivo. Só iniciar a próxima etapa dependente após integrar e atualizar main.

Cada pessoa deve ter pelo menos cinco commits reais de programação, distribuídos em pelo menos três dias diferentes. A tabela fornece tarefas suficientes, mas não substitui essa distribuição. Não mudar datas nem autoria para simular participação. Não concentrar tudo perto da entrega; o PDF prevê desconto. Planejar as datas da dupla antes de começar.

## 6. Fluxo de colaboração entre os integrantes

1. Ler este documento no início do trabalho e identificar a tarefa do integrante responsável.
2. Confirmar a pessoa responsável e sua identidade Git real. Não usar a conta da outra pessoa para atribuir commits.
3. Atualizar main e criar somente a branch da etapa escolhida. Explicar nome, finalidade e origem ao usuário.
4. Implementar e verificar somente a etapa. Informar arquivos, funções e comportamento alterados.
5. Fazer um commit simples e descritivo da etapa. Não incluir alterações alheias.
6. Publicar a branch e abrir pull request para main, explicando mudança, responsável, verificações feitas, limitações e dependências.
7. A outra pessoa revisa. Integrar somente quando a etapa estiver pronta e revisada; não fazer merge automático sem orientação da dupla.
8. Preservar os commits e sua autoria ao integrar, preferindo merge commit. Evitar squash que elimine os commits individuais exigidos.
9. Atualizar main nos dois computadores antes da próxima etapa dependente. Resolver conflitos preservando o trabalho das duas pessoas.

Esta proposta será commitada localmente para revisão. Publicação e pull request ficam para depois da validação solicitada nesta etapa.

## 7. Testes e entregas

Testar cada função separadamente quando estiver pronta. Na integração, registrar entrada, esperado e obtido em pelo menos oito casos, incluindo letra, vazio, fora do intervalo e casa repetida. Acrescentar símbolo, borda/canto na contagem, mina, vitória por pontos, empate no mapa de teste, reinício e estatísticas sem partidas e com sequências interrompidas.

- Pessoa 1: documentar execução, regras, funções de interface e sua autoria no README; preparar teste de mesa da criação/exibição da matriz; relatar testes de entradas.
- Pessoa 2: documentar funções de lógica e desafio no README; preparar teste de mesa da contagem de casas ou vizinhas; relatar testes de resultado e estatísticas.
- Ambas: consolidar o relatório no template do professor, com explicação de todos os conteúdos, tabela de funções (parâmetros/retorno/finalidade), teste de mesa, tabela de testes, divisão e links. Consultar o template antes de redigir; ele ainda não foi analisado nesta etapa.
- Ambas: gravar vídeo de 3 a 10 minutos, mostrando tela e código, com as duas vozes; demonstrar vitória, empate ou situação equivalente, três entradas inválidas, placar, histórico e desafio. Publicar como não listado no YouTube.
- Repositório privado: garantir acesso ao professor @profmartinz; não mudar visibilidade nem convidar colaborador nesta etapa.
- Entrega: GitHub, relatório PDF e vídeo pelo formulário informado no enunciado, até 08/11/2026 às 23:59.

## 8. Validação solicitada

Confirmar: nomes e associação Pessoa 1/Pessoa 2; divisão das funções; regras do jogo; desafio de estatísticas; uso do mapa com cinco minas para demonstrar empate; integração em sequência e revisão por pull request.

Após aprovação: preparar a base compartilhada e seguir uma etapa por vez. Nenhum código do jogo foi criado nesta proposta.

