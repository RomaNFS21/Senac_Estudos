programa {
  funcao inicio() {
    /*Crie Tr�s vari�veis ou mais , utilize operadores relacionais , armazene as informa��es nas vari�veis valores, execute as quatro opera��es ( + - * / ) , utilize SE , OU , SEN�O e imprima na tela
    Comparar 253 com 368
    Se for verdadeiro 
    multiplique 25 por 3
    se n�o divida 9 por 3
    se for igual some 1578 por 2586 e subtraia 78 
    imprima na tela o resultado das 4 opera��es */

    //Declara��o de vari�veis
    inteiro soma, subtracao, multiplicacao, divisao , valor1, valor2
    logico comparar

    //Pega e grava na mem�ria dois n�meros digitados pelo usu�rio
    escreva(" Escreva o valor do primeiro numero ")
    leia(valor1)
    escreva(" Escreva o valor do segundo numero ")
    leia(valor2)

    //Come�o das compara��o dos dois valores digitados pelo usu�rio
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
    //Imprime o resultado das opera��es que foram e n�o foram executadas
      escreva("A soma da: ", soma, " a subtra��o da: ", subtracao, " a multiplica��o da: ", multiplicacao, " e a divis�o da: ", divisao)
    }

    }
    
  


  