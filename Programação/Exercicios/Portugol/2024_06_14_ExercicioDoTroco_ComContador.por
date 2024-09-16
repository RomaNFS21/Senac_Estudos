/* Suponha que um caixa disponha apenas de notas de 1, 10 e 100.
Considerando que algu�m est� pagando uma compra. 
escreva um algoritmo que mostre
o n�mero m�nimo de cada nota que o caixa deve 
fornecer como troco. O algoritmo recber�
como entrada o Valor da Compra e Valor do pagamento,
 ambos os valores s�o inteiro.
Caso o valor do pagamento seja inferior ao valor da compra
o c�lculo n�o ser� eftuado dever� imprimir a sguinte mensagem: 
�Pagamento Negado�. Por xemplo:
valor da compra = 725
valor do pagamnto = 1.000
Troco = 275
Neste caso deve xibir 2 notas de R$ 100,
 7 notas de R$ 10 e 5 notas de R$ 1 
*/

// Feito por Victor Barros Roma
// 14/06/2024
// Objetivo: Negar ou Confirmar pagamento com troco ou sem

programa {
  funcao inicio() {

//Declara��o de variaveis 
inteiro ValorDaCompra, ValorDoPagamento, Contador, Troco, TrocoInicial, QtdNotas100, QtdNotas10, QtdNotas1

//Elicita��o dos valores de Compra e Pagamento
escreva("Qual o valor da compra que voc� quer pagar ? ")
leia(ValorDaCompra)
escreva("Com quanto o Sr(a) quer pagar essa compra? ")
leia(ValorDoPagamento)

Troco = ValorDoPagamento - ValorDaCompra
TrocoInicial = Troco

// Verifica��o para valor insuficiente de pagamento
se (ValorDoPagamento < ValorDaCompra){
  escreva("Pagamento Negado")
}

// Verifica��o de valor exato de pagamento
se (ValorDoPagamento == ValorDaCompra){
  escreva("Pagamento Efetuado")
}

// Verifica��o de valor a mais de pagamento
se (ValorDoPagamento > ValorDaCompra)  {

  //Contar notas de 100
  para (Contador = 0; Contador <= Troco; Contador+=100) 
    QtdNotas100 = Contador / 100
    Troco = Troco % 100

  //Contar notas de 10
  para (Contador = 0; Contador <= Troco; Contador+= 10)
    QtdNotas10 = Contador / 10
    Troco = Troco % 10
  
  //Contar Notas de 1
  para (Contador = 0; Contador <= Troco; Contador+=1)
    QtdNotas1 = Contador
    
  //Mensagem de pagamento realizado com valor total do troco e a divis�o das notas de 100, 10 e 1 real
  escreva("Pagamento realizado, seu troco � de ", TrocoInicial," reais , sendo ", QtdNotas100, " notas de 100, ", QtdNotas10, " notas de 10 e ",QtdNotas1, " notas de 1.")
}
  }
}
