//Feito por Victor Roma e Wanderson
//01/07/2024
//Problema 5
programa {
  funcao inicio() {
    //Declara��o de vari�veis
    inteiro NumeroRecebido, Centena, Dezena, Unidade, Soma

    //Capta��o do n�mero dito pelo usu�rio
    escreva("Digite um n�mero inteiro, positivo e com tr�s d�gitos: ")
    leia(NumeroRecebido)

    // Verifica se o n�mero � positivo e tem tr�s d�gitos
    se (NumeroRecebido <= 0 ou NumeroRecebido > 999) {
      escreva("N�mero digitado incorreto.")
    }
    senao {
      // Calcula as centenas, dezenas e unidades
      Centena = NumeroRecebido / 100
      Dezena = (NumeroRecebido % 100) / 10
      Unidade = NumeroRecebido % 10

      // Calcula a soma dos algarismos
      Soma = Centena + Dezena + Unidade
      
      // Verifica se a soma dos algarismos � �mpar ou par
      se (Soma % 2 != 0) {
        escreva("A soma dos algarismos do n�mero informado � �mpar.")
      }
      senao {
        escreva("A soma dos algarismos do n�mero informado � par e o n�mero ainda � positivo.")
      }
    }
  }
}
