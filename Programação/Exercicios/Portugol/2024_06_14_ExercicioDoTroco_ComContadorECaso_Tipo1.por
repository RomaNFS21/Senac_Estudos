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

escolha ( ValorDoPagamento < ValorDaCompra){

caso verdadeiro:
escreva("PAGAMENTO NEGADO")
pare

caso falso:

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
