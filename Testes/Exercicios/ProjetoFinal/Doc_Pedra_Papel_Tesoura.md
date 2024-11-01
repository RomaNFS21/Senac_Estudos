# Template de Apoio à Atividade de Teste de Software
**Criado para o Exercício Final  da UC 13 - Executar Teste e Implantação de Aplicativos Computacionais**

---

## 1. Cenário geral do 7_rock_paper_scissors (o quê será testado)
Apresente aqui uma visão geral do algoritmo, módulo ou do software que será testado. O que ele é? O que ele faz ou permite aos usuários fazerem? Quais são as principais funcionalidades? Ou quais funcionalidades serão testadas e consideradas aqui neste template? Ou quais módulos serão verificados?

O algoritmo é um jogo de pedra papel e tesoura, ele pega a opção informada do usuario e compara com a sorteada para o algoritomo, determinando se o usuario ganhou, perdeu ou empatou, a funcionalidade a ser testada sera da entrada do usuario 

---

## 2. Estratégia(s) de Teste (como será testado)
De acordo com o cenário/escopo daquilo que será testado, descreva quais atividades de teste serão conduzidas. Quais técnicas de teste serão usadas e com qual objetivo/finalidade? Qual ou quais critérios serão utilizados para cada técnica? Se alguma ferramenta for utilizada, descreva-a(s) aqui, de forma geral.

Sera realizado um teste de funcionalidade dos tipos de entrada do usuario sendo elas: com letras maiusculas, palavras completas, letras com numeros, duas opções e letras com caracteres especiais

Sera gerado um grafo de fluxo de controle daonde sera feito os testes de nos e arcos que são acionados

Sera feito teste de mutações testando o modulo play e o is_win


---

## 3. Projeto de Casos de Teste (como será testado)
Apresente, para cada técnica e critério considerados, quais são os casos de testes a serem utilizados (roteiro e/ou dados de entrada, resultados esperados).

*Exemplo*: Se usar Teste Funcional e Critério Análise do Valor Limite, apresente a tabela final considerando as variáveis de entrada, as classes de equivalência válidas e inválidas, bem como os casos considerando os limites.

---

## 4. Execução (quando e como será testado)
Detalhes sobre a execução: explique como o teste foi executado. Foi utilizada alguma ferramenta, mesmo que não tenha sido apresentada no curso? Para os casos de teste considerados anteriormente, especifique o resultado retornado (resultado do teste), descrição dos erros (caso tenham ocorrido).

---

## 5. Análise dos Resultados e Próximos Passos
Após o teste, que conclusão você chegou? Outras técnicas ou ferramentas são necessárias? Tendo mais tempo para realizar os testes, quais seriam os próximos passos que poderiam ser realizados?
