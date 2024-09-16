//Feito por Victor Roma e Wanderson
//01/07/2024
//Problema 5
programa {
  funcao inicio() {
    //Declaração de variaveis
    inteiro NumeroRecebido, Centena, Dezena, Unidade, Contador, Soma

    //Captação do numero dito pelo usuario
    escreva("Digite um numero inteiro, positivo e com três digitos ")
    leia(NumeroRecebido)

    //Numero ser negativo
    se(NumeroRecebido <= 0){
      escreva("Número digitado incorreto ")
    }
    // Numero ser Positivo
    senao se(NumeroRecebido > 0) {
        
         //Para Saber Qual a Centena
        para (Contador = 0; Contador <= NumeroRecebido; Contador+100)
        Centena = Contador
        NumeroRecebido = NumeroRecebido % 100

        //Se não tiver centena
        se(Centena == 0){
          escreva("Número digitado incorreto ")
        }

        //Se tiver centena
        senao se(Centena > 0){
          
           //Para Saber Qual a Dezena
          para (Contador = 0; Contador <= NumeroRecebido; Contador+10)
          Dezena = Contador
          NumeroRecebido = NumeroRecebido % 10

           //Para Saber Qual a Unidade
          para (Contador = 0; Contador <= NumeroRecebido; Contador+1)
          Centena = Contador
          
          Soma = Centena + Dezena + Unidade
          se (Soma % 2 != 0){
            escreva("A soma dos algarismos do número informado é impar")
          }
          senao{
            escreva("A soma dos algarismos do número informado é par e o número ainda é positivo")
          }
          
        }


    }

  }
}
