//Pedro Leon, Victor Roma e Jo�o Vitor; 26/06/2024; pedro51376376@edu.pe.senac.br.

programa {
  //Inclus�o da biblioteca matematica para fazer arrendondamento
  inclua biblioteca Matematica
  
  funcao inicio() {

    //Declara��o de variav�is
    real Valor, ValorPagamento, ValorParcela, DescontoPixDinheiro = 0.85, DescontoCartao = 0.9, Juros = 0.1, Parcelas, ValorParcelas, ValorJuros
    inteiro FormaPagamento

    //Saber Valor do produto
    escreva("Ol� qual � o valor do produto? ")
    leia(Valor)
    
    //Saber qual a forma de Pagamento
    escreva("Qual a forma que voc� deseja pagar? (responda com 1,2,3 ou 4 para a forma desejada) ")
    escreva("\n 1 - � Vista em Dinheiro ou Pix, recebe 15% de desconto")
    escreva("\n 2 - � Vista no cart�o de cr�dito, recebe 10% de desconto")
    escreva("\n 3 - Parcelado no cart�o em duas vezes, pre�o normal do produto sem juros")
    escreva("\n 4 - Parcelado no cart�o em tr�s vezes ou mais, pre�o normal do produto mais juros de 10% \n")
    leia(FormaPagamento)

    //Casos de acordo com a forma de pagamento
  	escolha(FormaPagamento){

      //Pagamento � vista ou pix
      caso 1:
      ValorPagamento = (Valor * DescontoPixDinheiro)
      escreva("Voc� escolheu pagar � vista em dinheiro ou no pix, o valor da compra � de ", ValorPagamento, " reais")
      pare

      //Pagamento � vista no cart�o
      caso 2:
      ValorPagamento = (Valor * DescontoCartao )
      escreva("Voc� escolheu pagar � vista no cart�o, o valor da compra � de ", ValorPagamento, " reais")
      pare

      //Pagamento no cart�o em duas vezes sem juros
      caso 3:
      ValorParcelas = (Valor / 2)
      escreva("Voc� escolheu pagar parcelado no cart�o em duas vezes sem juros, o valor da compra � de ", Valor, " reais, sendo duas parcelas de ", ValorParcelas, " reais cada.")
      pare

      //Pagamento no cart�o com juros com 3 ou mais parcelas at� 12
      caso 4:
      ValorJuros = Valor * Juros
      Valor = (Valor + ValorJuros)
      escreva("Voc� vai querer em quantas parcelas a compra ? \n Lembrando que no minimo 3 e maximo 12 ")
      leia(Parcelas)

      se (Parcelas < 3 ou Parcelas > 12){
        escreva("N�mero de parcelas invalido")
      }

      senao {
        ValorParcelas = Matematica.arredondar(Valor / Parcelas,2)

        escreva("Voc� escolheu pagar parcelado em ", Parcelas, " vezes com 10% de juros, o valor de cada parcela � ", ValorParcelas," reais, num total de ",Valor, " reais" )
      }
      pare
      }
    }
  }

