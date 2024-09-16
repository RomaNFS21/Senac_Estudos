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

programa {
  funcao inicio() {
    inteiro ValorDeCompra = 725, ValorDoPagamento = 1000, ValorTroco = 275

  escolha (ValorDoPagamento > ValorDeCompra ) {

    caso falso :
    escreva("Pagamento Negado")
    pare

    caso contrario:
    escreva("2 Notas de 100 reais, 7 notas de 10 reais e 5 notas de 1 real")
    
  }
    } 

  }

