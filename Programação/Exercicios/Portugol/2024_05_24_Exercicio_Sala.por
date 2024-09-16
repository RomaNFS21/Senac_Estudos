programa {
  funcao inicio() {
    /*Crie Três variáveis ou mais , utilize operadores relacionais , armazene as informações nas variáveis valores, execute as quatro operações ( + - * / ) , utilize SE , OU , SENÃO e imprima na tela
    Comparar 253 com 368
    Se for verdadeiro 
    multiplique 25 por 3
    se não divida 9 por 3
    se for igual some 1578 por 2586 e subtraia 78 
    imprima na tela o resultado das 4 operações */

    //Declaração de variáveis
    inteiro soma, subtracao, multiplicacao, divisao , valor1, valor2
    logico comparar

    //Pega e grava na memória dois números digitados pelo usuário
    escreva(" Escreva o valor do primeiro numero ")
    leia(valor1)
    escreva(" Escreva o valor do segundo numero ")
    leia(valor2)

    //Começo das comparação dos dois valores digitados pelo usuário
    se (valor1 >= valor2) {
        multiplicacao = 25 * 3
    } 

      senao {
        divisao = 9 / 3  
    }
              se (valor1 == valor2) {
                  soma = 1578 + 2586
                  subtracao = soma - 78
    }
    //Imprime o resultado das operações que foram e não foram executadas
      escreva("A soma da: ", soma, " a subtração da: ", subtracao, " a multiplicação da: ", multiplicacao, " e a divisão da: ", divisao)
    }

    }
    
  


  