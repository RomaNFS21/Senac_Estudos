// Feito por Victor Barros Roma
// 14/06/2024
// Objetivo: Informar qual a pessoa mais alta atraves dos dados informados
programa {
  funcao inicio() {
    //Declara��o das variaveis para armazenar altura e nome das duas pessoas
    real AlturaPessoa1, AlturaPessoa2
    cadeia  Nome1, Nome2

    //Recepta��o dos dados da primeira pessoa
    escreva("Qual � o nome da primeira pessoa? ")
    leia(Nome1)
    escreva("Qual � a altura da primeira pessoa? ")
    leia(AlturaPessoa1)

    //Recepta��o dos dados da segunda pessoa
    escreva("Qual � o nome da segunda pessoa? ")
    leia(Nome2)
    escreva("Qual � a altura da segunda pessoa? ")
    leia(AlturaPessoa2)

    //Verifica��o de quem � o mais alto
    se (AlturaPessoa1 > AlturaPessoa2){
      escreva(Nome1, " � mais alto(a) que ",Nome2)
    }

    senao {
      escreva(Nome2, " � mais alto(a) que ",Nome1)
    }

    
  }
}
