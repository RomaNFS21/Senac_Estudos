// Equipe: SINERGIA
// Data: 10/06/2024 Recife PE
// Contato:
// Objetivo: 

programa {
  funcao inicio() {

  //Declara��o de variavel
  real Dinheiro, Troco, ValorSalgado = 3, ValorRefri = 2, ValorDoce = 5, ValorTotal, DinheiroFalta
  inteiro QtdSalgado, QtdRefri, QtdDoce
  
  //Perguntas para recolhimento de informa��es do que sera comprado
  //Inicio do pedido
  escreva("Ola o que voc� vai pedir hoje ? \n")

  //Salgados
  escreva("Quantos salgados voc� vai querer ?\n ")
  leia(QtdSalgado)

  //Refrigerantes
  escreva("Quantos refrigerantes voc� vai querer? \n")
  leia(QtdRefri)

  //Doces
  escreva("Quantos doces voc� vai querer? \n")
  leia(QtdDoce)

  //Calculo da conta
  ValorTotal = (QtdSalgado * ValorSalgado) + (QtdRefri * ValorRefri) + (QtdDoce * ValorDoce)
  escreva("Sua conta deu: ", ValorTotal, " reais \n")

  //Pagamento
  escreva("Voc� vai pagar com quantos reais?\n ")
  leia(Dinheiro)

  //Verifica��o do pagamento e se precisa de troco

  //Se n�o tem dinheiro para pagar
  se (Dinheiro < ValorTotal){
    DinheiroFalta = ValorTotal - Dinheiro
    escreva("Voc� n�o tem dinheiro suficiente, faltam ",DinheiroFalta, " reais para pagar")
  }

  //Se tem o valor igual a conta
  se (Dinheiro == ValorTotal){
    escreva("Conta paga, aqui esta o(s) seu(s) ", QtdSalgado, " salgado(s), seus ", QtdRefri," refrigerante(s) e seus ", QtdDoce, " doce(s). \n")
  }

  //Se tem mais dinheiro que o pedido
  se (Dinheiro > ValorTotal){
    Troco = Dinheiro - ValorTotal
    escreva("Conta paga, seu troco � de ",Troco, " reais, aqui esta o(s) seu(s)", QtdSalgado, " salgado(s), seus ", QtdRefri," refrigerante(s) e seus ", QtdDoce, " doce(s). \n")
  }
  }
}
