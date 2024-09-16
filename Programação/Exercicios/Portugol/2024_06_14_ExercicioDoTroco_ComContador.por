/* Suponha que um caixa disponha apenas de notas de 1, 10 e 100.
Considerando que alguém está pagando uma compra. 
escreva um algoritmo que mostre
o número mínimo de cada nota que o caixa deve 
fornecer como troco. O algoritmo recberá
como entrada o Valor da Compra e Valor do pagamento,
 ambos os valores são inteiro.
Caso o valor do pagamento seja inferior ao valor da compra
o cálculo não será eftuado deverá imprimir a sguinte mensagem: 
“Pagamento Negado”. Por xemplo:
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

//Declaração de variaveis 
inteiro ValorDaCompra, ValorDoPagamento, Contador, Troco, TrocoInicial, QtdNotas100, QtdNotas10, QtdNotas1

//Elicitação dos valores de Compra e Pagamento
escreva("Qual o valor da compra que você quer pagar ? ")
leia(ValorDaCompra)
escreva("Com quanto o Sr(a) quer pagar essa compra? ")
leia(ValorDoPagamento)

Troco = ValorDoPagamento - ValorDaCompra
TrocoInicial = Troco

// Verificação para valor insuficiente de pagamento
se (ValorDoPagamento < ValorDaCompra){
  escreva("Pagamento Negado")
}

// Verificação de valor exato de pagamento
se (ValorDoPagamento == ValorDaCompra){
  escreva("Pagamento Efetuado")
}

// Verificação de valor a mais de pagamento
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
    
  //Mensagem de pagamento realizado com valor total do troco e a divisão das notas de 100, 10 e 1 real
  escreva("Pagamento realizado, seu troco é de ", TrocoInicial," reais , sendo ", QtdNotas100, " notas de 100, ", QtdNotas10, " notas de 10 e ",QtdNotas1, " notas de 1.")
}
  }
}
