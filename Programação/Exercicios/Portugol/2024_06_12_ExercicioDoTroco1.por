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

programa {
  funcao inicio() {
    inteiro NotaDe1, NotaDe10, NotaDe100, ValorDeCompra, ValorDoPagamento, ValorRestante, ValorTroco

    escreva("Ol� qual o valor da compra? ")
    leia(ValorDeCompra)
    escreva("Com quanto dinheiro voc� esta para o pagamento? ")
    leia(ValorDoPagamento)

    se(ValorDoPagamento < ValorDeCompra){
      escreva("Pagamento Negado")
    }

    se(ValorDoPagamento == ValorDeCompra){
      escreva("Pagamento efetuado")
    }

    se (ValorDoPagamento > ValorDeCompra) {
      ValorTroco = ValorDoPagamento - ValorDeCompra
      NotaDe100 = ValorTroco / 100
      ValorRestante = ValorTroco - (100 * NotaDe100)
      NotaDe10 = ValorRestante / 10
      ValorRestante = ValorRestante - (10 * NotaDe10)
      NotaDe1 = ValorRestante / 1
      escreva("Pagamento efetuado e seu troco � de ", ValorTroco, " reais, sendo ", NotaDe100, " notas de 100 reais, ", NotaDe10, " notas de 10 reais, ", NotaDe1, " notas de 1 real" ) 
    }
  }
}
