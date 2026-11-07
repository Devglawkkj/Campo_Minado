# Revisão de requisitos do Campo Minado

Revisão realizada em 07/11/2026, com base no enunciado Trabalho - 3ª Avaliação e no código da main em [b036bd5](https://github.com/Devglawkkj/Campo_Minado/blob/b036bd522dc1b9d70ce087aaa70138077062e83c/campo_minado.py).

## Resultado

O código do jogo atende aos requisitos de funcionalidades e de conteúdo permitidos verificados. Não foi necessário modificar campo_minado.py. Foram corrigidas informações desatualizadas no README e na divisão do trabalho. Esta revisão não substitui o relatório no template do professor, o vídeo nem o formulário de entrega.

## Conferência do código

| Requisito | Evidência | Resultado |
| --- | --- | --- |
| Python no terminal e dois jogadores | menu_principal identifica dois jogadores humanos | Atendido |
| Matriz de pelo menos 5x5 | criar_tabuleiro(5), com listas e append() | Atendido |
| Criação e exibição com for aninhado | criar_tabuleiro e mostrar_tabuleiro | Atendido |
| Linhas/colunas numeradas e tabuleiro a cada jogada | mostrar_tabuleiro chamada antes e após jogadas | Atendido |
| Minas fixas sem random | Conjunto de quatro tuplas declarado no código | Atendido |
| Número de minas nas até oito vizinhas | contar_minas_vizinhas, respeitando bordas e excluindo a própria casa | Atendido |
| Validação antes de int() | ler_numero valida texto, comprimento e intervalo | Atendido |
| Casa repetida não consome turno | ler_jogada solicita outra posição antes de retornar | Atendido |
| Vitória/empate automáticos com laços e return | verificar_resultado usa contar_casas_seguras_restantes, que percorre a matriz | Atendido |
| Menu em while e decisões | menu_principal | Atendido |
| Placar em dicionário entre partidas | placar criado uma vez no menu e atualizado por registrar_resultado | Atendido |
| Histórico em vetor com append() | historico e registrar_resultado; consulta pelo menu | Atendido |
| Jogar novamente com tabuleiro novo | confirmar_reinicio e nova chamada de jogar_partida | Atendido |
| Cinco funções; duas com parâmetros e duas com return | 16 funções; 13 recebem parâmetros; múltiplas devolvem valores | Atendido |
| Tuplas e conjuntos com propósito | Coordenadas, identificadores, minas e respostas válidas S/N | Atendido |
| append(), strip(), upper(), isdigit() | Criação da matriz, nomes e leitura das respostas | Atendido |
| Operadores aritméticos, relacionais e lógicos | Pontos, porcentagens, limites e consultas às posições | Atendido |
| Desafio Estatísticas da sessão | mostrar_estatisticas, chamada ao sair: len, count, porcentagens e sequências | Atendido |
| Ausência de recursos proibidos | Análise sintática e inspeção de todas as funções e chamadas | Atendido |

Não há imports, bibliotecas externas, lambda, comprehensions, try/except ou classes no programa. As chamadas são funções do próprio jogo ou print, input, int, str, len e range. Os métodos usados são append, strip, upper, isdigit e count.

Os exemplos de linhas, colunas e diagonais vencedoras do enunciado são adaptados ao jogo escolhido: no Campo Minado, o critério é contar casas seguras com laços, sem introduzir sequências de peças.

## Casos executados

Os testes foram executados sobre uma cópia do código revisado. O programa permaneceu sem alterações. Na tabela, coordenadas digitadas começam em 1; posições explicitamente indicadas como índices começam em zero.

| Caso | Entrada ou cenário | Esperado | Obtido |
| --- | --- | --- | --- |
| Matriz independente | Criar 5x5 e modificar [0][0] | True | True |
| Letra | a; depois 3 | 3 com aviso | 3 com aviso |
| Vazio | ; depois 3 | 3 com aviso | 3 com aviso |
| Fora do intervalo | 6; depois 3 | 3 com aviso | 3 com aviso |
| Símbolo | @; depois 3 | 3 com aviso | 3 com aviso |
| Negativo | -1; depois 3 | 3 com aviso | 3 com aviso |
| Unicode | ²; depois 3 | 3 com aviso | 3 com aviso |
| Entrada longa | 5000 dígitos; depois 3 | 3 com aviso | 3 com aviso |
| Espaços |  5  | 5 | 5 |
| Casa ocupada | (1,1) aberta; depois (1,2) | (0, 1) | (0, 1) |
| Confirmação | x; depois s com espaços | True | True |
| Vizinhas | Todas as 25 posições, incluindo cantos/bordas | 25 | 25 |
| Casa segura | Abrir índice (0,0) | False | False |
| Mina | Abrir índice (0,3) | True | True |
| Vitória por pontos | 21 casas seguras abertas | P1 | P1 |
| Empate | 20 casas seguras abertas | Empate | Empate |
| Derrota de P2 por mina | P1 abre (1,1); P2 abre (1,4) | P1 | P1 |
| Estatísticas | P1,P1,Empate,P2,P1 | 60.0%;20.0%;sequências 2 e 1 | 60.0%;20.0%;sequências 2 e 1 |
| Sessão vazia | Sem partidas | Sem divisão por zero | Sem divisão por zero |
| Sessão completa | Regras, consultas, duas partidas, repetição e S/N | P1=1;P2=1;histórico com 2;estatísticas 50% | P1=1;P2=1;histórico com 2;estatísticas 50% |

Foram conferidas adicionalmente as 25 posições para contagem de vizinhas, a preservação das demais casas ao abrir uma posição, a prioridade da derrota por mina sobre a pontuação e a ausência de alterações dos argumentos nas estatísticas.

## Empate e demonstração

O mapa padrão tem quatro minas e 21 casas seguras. Como P1 começa e cada jogada segura vale um ponto, o esgotamento das casas seguras termina em 11 a 10. Isso não é falha na comparação dos pontos.

Para verificar empate, a revisão executou uma partida completa com cinco minas, acrescentando (2, 2) ao conjunto apenas no ambiente de teste. Foram abertas as 20 casas seguras, com dez pontos para cada jogador, e a função devolveu Empate. Esse cenário já está previsto na divisão da dupla; não foi acrescentada uma opção de teste ao menu nem alterado o mapa padrão. O vídeo deve identificar claramente quando estiver apresentando esse cenário.

## Versionamento e participação

Contagem anterior aos commits desta revisão, excluindo merges e preservando autoria e datas:

| Conta | Commits sem merge | Datas locais de autoria (America/Fortaleza) |
| --- | --- | --- |
| Devglawkkj | 8 no total, incluindo 5 etapas de programação | 28/10, 31/10, 02/11 e 03/11/2026; programação em 31/10, 02/11 e 03/11 |
| joaodeoliveira2811-debug | 5 etapas de programação | 31/10, 02/11 e 03/11/2026 |

As duas contas possuem o mínimo numérico de cinco commits e três dias diferentes. A avaliação da distribuição ao longo do período cabe ao professor; esta conferência não garante nota.

## Pendências fora do programa

- A consulta de permissão do usuário profmartinz ao repositório retornou none. Garantir acesso efetivo ao professor, conforme o enunciado. Nenhum convite ou mudança de visibilidade foi realizado nesta revisão.
- O repositório revisado contém o código, o README e a divisão. Relatório e vídeo podem estar sendo preparados fora dele; sua conclusão e seus links não foram comprovados nesta revisão.
- Conferir o relatório no template oficial: explicação dos conteúdos, tabela de funções com parâmetros e retornos, teste de mesa de for aninhado, ao menos oito testes com quatro entradas inválidas, desafio, integrantes e links. A tabela de testes acima pode fornecer evidências, mas não substitui o relatório.
- Conferir o vídeo: 3 a 10 minutos, ambos os integrantes falando, tela/código, vitória, empate ou equivalente, pelo menos três entradas inválidas, placar, histórico e estatísticas. Publicar no YouTube como não listado.
- Enviar os links e o relatório PDF pelo formulário até 08/11/2026 às 23:59, conforme o enunciado. Nenhum envio foi feito nesta revisão.
