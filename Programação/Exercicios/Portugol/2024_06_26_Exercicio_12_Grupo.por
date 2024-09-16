//Pedro Leon, Victor Roma e João Vitor; 26/06/2024; pedro51376376@edu.pe.senac.br.

programa {
  //Inclusão da biblioteca matematica para fazer arrendondamento
  inclua biblioteca Matematica
  
  funcao inicio() {

    //Declaração de variavéis
    real Valor, ValorPagamento, ValorParcela, DescontoPixDinheiro = 0.85, DescontoCartao = 0.9, Juros = 0.1, Parcelas, ValorParcelas, ValorJuros
    inteiro FormaPagamento

    //Saber Valor do produto
    escreva("Olá qual é o valor do produto? ")
    leia(Valor)
    
    //Saber qual a forma de Pagamento
    escreva("Qual a forma que você deseja pagar? (responda com 1,2,3 ou 4 para a forma desejada) ")
    escreva("\n 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto")
    escreva("\n 2 - À Vista no cartão de crédito, recebe 10% de desconto")
    escreva("\n 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros")
    escreva("\n 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10% \n")
    leia(FormaPagamento)

    //Casos de acordo com a forma de pagamento
  	escolha(FormaPagamento){

      //Pagamento à vista ou pix
      caso 1:
      ValorPagamento = (Valor * DescontoPixDinheiro)
      escreva("Você escolheu pagar à vista em dinheiro ou no pix, o valor da compra é de ", ValorPagamento, " reais")
      pare

      //Pagamento à vista no cartão
      caso 2:
      ValorPagamento = (Valor * DescontoCartao )
      escreva("Você escolheu pagar à vista no cartão, o valor da compra é de ", ValorPagamento, " reais")
      pare

      //Pagamento no cartão em duas vezes sem juros
      caso 3:
      ValorParcelas = (Valor / 2)
      escreva("Você escolheu pagar parcelado no cartão em duas vezes sem juros, o valor da compra é de ", Valor, " reais, sendo duas parcelas de ", ValorParcelas, " reais cada.")
      pare

      //Pagamento no cartão com juros com 3 ou mais parcelas até 12
      caso 4:
      ValorJuros = Valor * Juros
      Valor = (Valor + ValorJuros)
      escreva("Você vai querer em quantas parcelas a compra ? \n Lembrando que no minimo 3 e maximo 12 ")
      leia(Parcelas)

      se (Parcelas < 3 ou Parcelas > 12){
        escreva("Número de parcelas invalido")
      }

      senao {
        ValorParcelas = Matematica.arredondar(Valor / Parcelas,2)

        escreva("Você escolheu pagar parcelado em ", Parcelas, " vezes com 10% de juros, o valor de cada parcela é ", ValorParcelas," reais, num total de ",Valor, " reais" )
      }
      pare
      }
    }
  }

