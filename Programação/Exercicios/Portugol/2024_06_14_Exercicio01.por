// Feito por Victor Barros Roma
// 14/06/2024
// Objetivo: Informar qual a pessoa mais alta atraves dos dados informados
programa {
  funcao inicio() {
    //Declaração das variaveis para armazenar altura e nome das duas pessoas
    real AlturaPessoa1, AlturaPessoa2
    cadeia  Nome1, Nome2

    //Receptação dos dados da primeira pessoa
    escreva("Qual é o nome da primeira pessoa? ")
    leia(Nome1)
    escreva("Qual é a altura da primeira pessoa? ")
    leia(AlturaPessoa1)

    //Receptação dos dados da segunda pessoa
    escreva("Qual é o nome da segunda pessoa? ")
    leia(Nome2)
    escreva("Qual é a altura da segunda pessoa? ")
    leia(AlturaPessoa2)

    //Verificação de quem é o mais alto
    se (AlturaPessoa1 > AlturaPessoa2){
      escreva(Nome1, " é mais alto(a) que ",Nome2)
    }

    senao {
      escreva(Nome2, " é mais alto(a) que ",Nome1)
    }

    
  }
}
