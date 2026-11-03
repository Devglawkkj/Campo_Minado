# Diagnóstico do Campo Minado

Data: 03/11/2026 (America/Sao_Paulo). Responsável pela verificação: João Ricardo, Pessoa 2.

## Parecer

O jogo está funcionalmente completo em relação à proposta aprovada e aos requisitos de programação conferidos no enunciado. Não foram encontradas falhas funcionais nos cenários executados. Menu, dois jogadores, abertura de casas, resultado, reinício, placar, histórico e desafio de estatísticas estão implementados e integrados à main.

Isso não significa que a entrega acadêmica esteja concluída: documentação final, relatório no template do professor, vídeo e comprovação de acesso do professor ainda precisam ser finalizados ou conferidos. Este diagnóstico é um registro de verificação, não substitui o relatório técnico no template exigido.

## Versão e método

- Versão analisada: main no commit `b036bd5`, que integra o PR #11 de estatísticas; código do jogo no commit `ec02505`.
- Ambiente: Python 3.12.14, Linux. Não houve execução em Windows nem teste de gravação do vídeo.
- Revisão integral das 16 funções e leitura da divisão de trabalho e do README, comparadas com o PDF do enunciado já analisado.
- Verificação de sintaxe por árvore sintática, testes isolados das funções e 17 execuções completas em processos separados, com entradas de terminal simuladas, saída capturada e limite de dez segundos por execução.
- Estatísticas conferidas contra cálculo independente em todos os 9.841 históricos possíveis de zero a oito partidas, com resultados P1, P2 e Empate.
- O código de produção não foi alterado. O programa auxiliar de verificação usa bibliotecas fora do jogo; essas bibliotecas não são dependências de campo_minado.py.

Os testes comprovam o comportamento dos casos descritos; não constituem garantia para toda entrada ou ambiente possível.

## Revisão das funções

| Função | Verificação e diagnóstico |
| --- | --- |
| criar_tabuleiro | Matriz 5 x 5 fechada, linhas independentes e nova matriz por partida: aprovado |
| mostrar_tabuleiro | Colunas e linhas numeradas, sem revelar minas ou modificar o estado: aprovado |
| contar_minas_vizinhas | Todas as 25 posições do mapa comparadas com cálculo independente; canto, borda, centro, zero e oito vizinhas: aprovado |
| abrir_casa | Todas as 25 posições verificadas: modifica uma única casa, grava número ou asterisco e retorna o booleano correto; sem cascata: aprovado |
| contar_casas_seguras_restantes | Inicialmente 21; zero após abrir todas as seguras; minas fechadas não impedem o fim: aprovado |
| verificar_resultado | Mina tem prioridade, ambos os perdedores possíveis, partida em andamento, comparação de pontos para P1/P2 e empate: aprovado |
| ler_numero | Valida antes de converter; rejeita vazio, letra, símbolo, números fora dos limites, decimal, negativo, Unicode e texto longo: aprovado |
| ler_jogada | Coordenadas internas iniciadas em zero; entrada inválida e casa repetida são recusadas sem avançar o turno: aprovado |
| jogar_partida | Alternância, ponto apenas em casa segura, mina encerra imediatamente, vitória por pontos e empate no mapa de teste: aprovado |
| registrar_resultado | Atualiza placar e acrescenta resultado ao histórico; ignora resultados não finais; menu registra uma vez por partida: aprovado |
| mostrar_placar | Vitórias e empates correspondem aos resultados registrados: aprovado |
| mostrar_historico | Lista vazia, ordem das partidas, vencedores e empate: aprovado |
| mostrar_estatisticas | Total, porcentagens com uma casa decimal, sequências, empate interrompendo sequências, sessão vazia e preservação dos dados: aprovado |
| mostrar_regras | Acessível pelo menu e coerente com o mapa padrão: aprovado |
| confirmar_reinicio | Recusa respostas inválidas; aceita S/N com espaços e letras minúsculas: aprovado |
| menu_principal | Nomes vazios/iguais recusados, normalização, todas as cinco opções, reinício, preservação da sessão e estatísticas na saída: aprovado |

## Cenários de execução e resultados

As coordenadas desta tabela começam em 1, como na interface. Nomes usados: Ana e Bia. As entradas de uma partida foram seguidas de N e opção 5, salvo indicação diferente.

| Caso | Entrada ou cenário | Esperado | Obtido |
| --- | --- | --- | --- |
| 1 | Informar nomes e escolher 5, sem jogar | Total zero; porcentagens zero; sem erro | Aprovado |
| 2 | Consultar opções 2, 3 e 4 antes de jogar | Regras; placar zerado; histórico vazio | Aprovado |
| 3 | Nome vazio, depois ` ana `; segundo nome `ANA`, depois ` bia ` | Recusar vazio e duplicado; usar ANA/BIA | Aprovado |
| 4 | Linha `a`, depois linha 1 e coluna 4 | Recusar letra e manter P1; mina encerra a partida | Aprovado |
| 5 | Linha vazia, depois linha 1 e coluna 4 | Recusar vazio e manter P1 | Aprovado |
| 6 | Linha `@`, depois linha 1 e coluna 4 | Recusar símbolo e manter P1 | Aprovado |
| 7 | Linha 0, depois linha 1 e coluna 4 | Recusar limite inferior inválido | Aprovado |
| 8 | Linha 6, depois linha 1 e coluna 4 | Recusar limite superior inválido | Aprovado |
| 9 | Linha `-1`, depois linha 1 e coluna 4 | Recusar negativo sem erro | Aprovado |
| 10 | Linha `1.5`, depois linha 1 e coluna 4 | Recusar decimal sem erro | Aprovado |
| 11 | Linha `²`, depois linha 1 e coluna 4 | Recusar dígito Unicode não conversível | Aprovado |
| 12 | Linha `５`, depois linha 1 e coluna 4 | Recusar dígito fora do conjunto ASCII aprovado | Aprovado |
| 13 | Linha com 5.000 caracteres `9`, depois linha 1 e coluna 4 | Recusar antes de converter, sem erro | Aprovado |
| 14 | P1 abre (1,1); P2 repete (1,1), depois abre mina (1,4) | Repetição não consome turno; P1 vence com 1 ponto; P2 permanece com zero | Aprovado |
| 15 | Abrir todas as casas seguras, em ordem de linha e coluna | P1 vence 11 x 10; histórico registra P1 uma vez | Aprovado |
| 16 | P1 abre mina; confirmação `?`, vazio e ` s `; nova partida abre (1,1) e depois mina (1,4); responder ` n ` | Reinício validado; tabuleiro/pontos limpos; histórico P2/P1; total 2; 50% para cada | Aprovado |
| 17 | Mapa de teste com quinta mina em (1,1); abrir as 20 seguras | Empate 10 x 10; histórico e placar com um empate; estatísticas sem vitórias | Aprovado |

### Reprodução da vitória por pontos

Após os nomes, selecionar 1 e abrir estas casas na ordem indicada:

`(1,1), (1,2), (1,3), (1,5), (2,1), (2,3), (2,4), (2,5), (3,1), (3,2), (3,3), (3,4), (3,5), (4,1), (4,2), (4,4), (4,5), (5,1), (5,2), (5,3), (5,4)`.

Digitar linha e coluna separadamente. Resultado confirmado: ANA/P1 com 11 pontos e BIA/P2 com 10.

### Reprodução do empate

O mapa padrão tem 21 casas seguras, portanto a alternância de uma casa por turno não permite empate ao esgotá-las. Isso decorre das regras aprovadas, não é falha no resultado.

No processo de teste, foi acrescentada somente em memória a mina interna `(0, 0)` ao conjunto original. Nenhuma linha do arquivo de produção foi modificada. Executou-se o mesmo menu e a mesma partida, abrindo as casas da sequência acima exceto `(1,1)`. As 20 casas restantes produziram empate 10 x 10. A mensagem das regras continua descrevendo o mapa padrão; o cenário alternativo não é uma opção do menu.

## Estatísticas

Foram verificadas todas as combinações de P1/P2/Empate com até oito partidas: 9.841 históricos. Em cada histórico, a saída foi comparada com contagens, percentuais e agrupamentos de resultados calculados independentemente, verificando também que placar e histórico não foram modificados.

Resultados confirmados incluem: sessão vazia com 0.0%; duas vitórias em três partidas com 66.7%; vitória do adversário interrompendo a sequência; empate interrompendo as sequências de ambos; maior sequência no início, no meio ou no fim; apenas empates; vitórias alternadas; porcentagens considerando empates no total.

## Conformidade de programação

| Requisito | Situação |
| --- | --- |
| Dois humanos no terminal; matriz e for aninhado | Atendido |
| Pelo menos cinco funções, duas com parâmetros e duas com return | Atendido: 16 funções; parâmetros e retornos presentes em quantidade suficiente |
| while, for, decisões, operadores e variáveis | Presentes e com finalidade no jogo |
| Lista, dicionário, tupla e conjunto | Presentes e com finalidade no jogo |
| append, strip, upper e isdigit | Presentes em criação/histórico e leituras |
| Sem imports, bibliotecas, lambda, comprehensions, try/except ou classes no jogo | Nenhuma ocorrência encontrada na inspeção de sintaxe |
| Menu, validação, resultado automático com laços e reinício | Atendidos nos testes |
| Placar acumulado e histórico no menu | Atendidos nos testes |
| Desafio de estatísticas ao sair | Implementado e testado |

## Histórico de participação

Conferência de commits de programação não relacionados a merges, na main analisada, agrupando Ricardo pelo mesmo e-mail apesar da variação do nome de autor:

| Integrante | Commits de programação identificados | Datas registradas |
| --- | --- | --- |
| Glauckyon Rocha | 5: tabuleiro, exibição, entradas, partida, menu | 31/10, 02/11 e 03/11/2026 |
| João Ricardo / Ricardo | 5: minas vizinhas, abertura, resultado, placar/histórico, estatísticas | 31/10, 02/11 e 03/11/2026 |

A contagem mínima de cinco commits em três dias distintos está registrada. Isso não garante a pontuação: o enunciado também avalia participação real e distribuição ao longo do período e alerta sobre concentração perto da entrega. Autoria vinculada no GitHub e explicação individual no vídeo devem ser conferidas pela dupla. Nenhuma autoria, data ou histórico foi alterado nesta análise.

## Pendências para concluir a entrega

1. Atualizar o README: ainda declara que as estatísticas estão pendentes e não detalha as oito funções da Pessoa 2.
2. Atualizar a divisão compartilhada: ainda aparece como proposta em validação, com nomes pendentes e descrições de etapas já executadas. A aprovação já ocorreu na conversa, mas não está refletida no documento.
3. Preparar o relatório técnico no template do professor, após consultá-lo: incluir explicação dos conteúdos, tabela de funções com parâmetros e retornos, teste de mesa com for aninhado, casos com esperado/obtido e links. Este diagnóstico fornece evidências, mas não contém o teste de mesa exigido nem segue o template.
4. Gravar e conferir vídeo de 3 a 10 minutos, com ambas as vozes, tela/código e demonstrações exigidas; disponibilizar como não listado por ação autorizada da dupla.
5. Conferir acesso do professor ao repositório, links e envio do formulário até 08/11/2026 às 23:59. Acesso, vídeo e envio não foram verificados nesta análise.

Não foi identificado recurso de jogo ainda faltante. As pendências acima dizem respeito à documentação, comprovação e entrega.

## Limites e condições de uso

O uso previsto é um terminal com entrada interativa disponível, mapa fixo válido e matriz 5 x 5. Fechar a entrada (EOF) ou interromper o processo pelo teclado não possui tratamento especial; persistência entre execuções não foi proposta. Funções internas dependem dos contratos de coordenadas válidas e de consistência entre placar e histórico, garantidos pelo menu. Tamanhos arbitrários, matrizes vazias e dados internos corrompidos não foram considerados interfaces públicas do jogo.

O programa está pronto para a dupla executar e demonstrar dentro dessas condições. Recomenda-se executar a mesma demonstração no computador que será usado na gravação, pois os testes desta análise ocorreram em Linux.
