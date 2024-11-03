# Template de Apoio à Atividade de Teste de Software
**Criado para o Exercício Final  da UC 13 - Executar Teste e Implantação de Aplicativos Computacionais**
**Turma 109 - Tecnico de informatica - Alunos: Debora e Victor Barros Roma**

---

## 1. Cenário geral do rock_paper_scissors.py (o quê será testado)
O algoritmo é um jogo de pedra papel e tesoura, ele pega a opção informada do usuario e compara com a sorteada para o algoritomo, determinando se o usuario ganhou, perdeu ou empatou, a funcionalidade a ser testada sera da entrada do usuario. 

---

## 2. Estratégia(s) de Teste (como será testado)
-  Sera realizado um teste de funcionalidade dos tipos de entrada do usuario sendo elas: com letras maiusculas, palavras completas, letras com numeros, duas opções e letras com caracteres especiais com o fim de verificar quais são as entradas validas e invalidas.

- Sera gerado um grafo de fluxo de controle daonde sera feito os testes de nos e arcos que são acionados com fim de ver todos os nos e arcos acessados utilizando o pycfg para criar o cfg e enumerando os nos para fazer os registros do fluxo.

- Será criado testes para verificar vitoria, derrota e empate com a utilização do **pytest** e **mutpy** os testes de mutação serão gerados do módulo "play" e do "is_win" com a finalidade de verificar a eficiência dos testes criados com a intenção que seus mutantes sejam variações mortas.

---

## 3. Projeto de Casos de Teste (como será testado)
#### - TESTE FUNCIONAL

| ID           |        Módulo          | Descrição      | Roteiro | Resultado Esperado |
|:--------------:|:------------------------|:----------------|:---------|:--------------------|	
| 1            | Entrada do usuário com letras maiúsculas. | Testar a entrada com caracteres maiúsculos na escolha. | Ao executar o código quando solicitar a escolha responder "P". | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. |
| 2            | Entrada do usuário com a palavra completa da opção desejada. | Testar a entrada com palavras completas da opção desejada pelo usuário. | Ao executar o código quando solicitar a escolha responder "ROCK". | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. |
| 3            | Entrada do usuário com letras e números da opção desejada. | Testar a entrada com letras e números da opção desejada pelo usuário. | Ao executar o código quando solicitar a escolha responder "sc1ss0rs". | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. |
| 4            | Entrada do usuário com duas opções das opções desejada. | Testar a entrada com duas opções das opções desejadas pelo usuário. | Ao executar o código quando solicitar a escolha responder "p e". | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. |
| 5            | Entrada do usuário com letras com caracteres especiais da opção desejada. | Testar a entrada com letras com caracteres especiais da opção desejadas pelo usuário. | Ao executar o código quando solicitar a escolha responder "p@per#". | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. |
| 6            | Entrada do usuário com a primeira letra minúscula da opção desejada. | Testar a entrada com a primeira letra minúscula da opção desejadas pelo usuário. | Ao executar o código quando solicitar a escolha responder "r". | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. |

#### - TESTE ESTRUTURAL DE NOS E ARCOS

![<CFG_Part1>](<https://i.vgy.me/6XNPE2.png>)
![<CFG_Part2>](<https://i.vgy.me/ouyzT9.png>)
![<CFG_Legenda>](<https://i.vgy.me/XUYOFk.png>)

A partir do CFG gerado acima pelo pycfg a cima será enumerado os nos e a partir disso serão testados quais nos e arcos são atigidos dependendo da sua entrada



#### - TESTE MUTACIONAIS

---

## 4. Execução (quando e como será testado)
Detalhes sobre a execução: explique como o teste foi executado. Foi utilizada alguma ferramenta, mesmo que não tenha sido apresentada no curso? Para os casos de teste considerados anteriormente, especifique o resultado retornado (resultado do teste), descrição dos erros (caso tenham ocorrido).

#### - TESTE FUNCIONAL

| ID           | Roteiro  | Resultado Esperado |Resultado do Teste | Problema Encontrado |
|:--------------:|:--------------------|:---------------------|:-----------|:--------------------|	
| 1            | Ao executar o código quando solicitar a escolha responder "P".| Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. | O programa informou que o usuário perdeu em vários testes. | Ao repetir mais de uma vez o teste o resultado é sempre a derrota por não haver um comparativo para a condição de derrota sendo assim não verificado a entrada do usuário e a opção da maquina. |
| 2            | Ao executar o código quando solicitar a escolha responder "ROCK".     | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. |  O programa informou que o usuário perdeu em vários testes. | Ao repetir mais de uma vez o teste o resultado é sempre a derrota por não haver um comparativo para a condição de derrota sendo assim não verificado a entrada do usuário e a opção da maquina. |
| 3            | Ao executar o código quando solicitar a escolha responder "sc1ss0rs". | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. | O programa informou que o usuário perdeu em vários testes. | Ao repetir mais de uma vez o teste o resultado é sempre a derrota por não haver um comparativo para a condição de derrota sendo assim não verificado a entrada do usuário e a opção da maquina. |
| 4            | Ao executar o código quando solicitar a escolha responder "p e".      | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. | O programa informou que o usuário perdeu em vários testes. | Ao repetir mais de uma vez o teste o resultado é sempre a derrota por não haver um comparativo para a condição de derrota sendo assim não verificado a entrada do usuário e a opção da maquina. |
| 5            | Ao executar o código quando solicitar a escolha responder "p@per#".   | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. | O programa informou que o usuário perdeu em vários testes. | Ao repetir mais de uma vez o teste o resultado é sempre a derrota por não haver um comparativo para a condição de derrota sendo assim não verificado a entrada do usuário e a opção da maquina. |
| 6            | Ao executar o código quando solicitar a escolha responder "r".        | Ser informado se o usuário ganhou, perdeu ou empatou com a maquina. | O programa informou que o usuário ganhou, perdeu e empatou em testes diferentes. | Nenhum problema encontrado durante a repetições do teste. |

#### - TESTE ESTRUTURAL DE NOS E ARCOS

###### - CFG NUMERADO

![<CFG_Part1>](<https://i.vgy.me/SwuwH7.png>)
![<CFG_Part2>](<https://i.vgy.me/F7vphH.png>)
![<CFG_Legenda>](<https://i.vgy.me/XUYOFk.png>)

###### - NOS
| ENTRADA | SORTEADO COMPUTADOR |CAMINHOS DOS NOS |
|:---------|:---------------------:|:-----------------|
|   r (rock)     | s (scissors)     | 0, 1, 2, 3, 7, 8, 3, 5  |
|   p (paper)    | p (paper)        | 0, 1, 2, 6    |
|   s (scissors) | r (rock)         | 0, 1, 2, 3, 7, 3, 4  |

**OBS: Todos os NOS foram ativados com os testes realizados**

 ###### - ARCOS

| ENTRADA | SORTEADO COMPUTADOR |ARCOS FEITOS |
|:---------|:---------------------:|:-----------------|
|   r (rock)     |  s (scissors)    | 0-1, 1-2, 2-3, 3-7, 7-8, 8-3, 3-5 |
|   p (paper)    |  p (paper)       | 0-1, 1-2, 2-6 |
|   s (scissors) |  r (rock)        | 0-1, 1-2, 2-3, 3-7, 7-3, 3-4 |

**OBS: Todos os ARCOS foram ativados com os testes realizados**

#### - TESTE MUTACIONAIS


---

## 5. Análise dos Resultados e Próximos Passos
Após o teste, que conclusão você chegou? Outras técnicas ou ferramentas são necessárias? Tendo mais tempo para realizar os testes, quais seriam os próximos passos que poderiam ser realizados?
