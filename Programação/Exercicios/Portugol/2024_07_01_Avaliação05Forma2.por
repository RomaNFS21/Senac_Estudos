//Feito por Victor Roma e Wanderson
//01/07/2024
//Problema 5
programa {
  funcao inicio() {
    //Declaração de variáveis
    inteiro NumeroRecebido, Centena, Dezena, Unidade, Soma

    //Captação do número dito pelo usuário
    escreva("Digite um número inteiro, positivo e com três dígitos: ")
    leia(NumeroRecebido)

    // Verifica se o número é positivo e tem três dígitos
    se (NumeroRecebido <= 0 ou NumeroRecebido > 999) {
      escreva("Número digitado incorreto.")
    }
    senao {
      // Calcula as centenas, dezenas e unidades
      Centena = NumeroRecebido / 100
      Dezena = (NumeroRecebido % 100) / 10
      Unidade = NumeroRecebido % 10

      // Calcula a soma dos algarismos
      Soma = Centena + Dezena + Unidade
      
      // Verifica se a soma dos algarismos é ímpar ou par
      se (Soma % 2 != 0) {
        escreva("A soma dos algarismos do número informado é ímpar.")
      }
      senao {
        escreva("A soma dos algarismos do número informado é par e o número ainda é positivo.")
      }
    }
  }
}
