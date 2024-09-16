programa {

  funcao media(real Nota1, real Nota2, real Nota3, cadeia Nome){

    
    real Media 
    Media = (Nota1 + Nota2 + Nota3)/3

    se (Media <7) {
      escreva(Nome, " você esta REPROVADO com media ", Media)
    }

    senao {
      escreva(Nome, " você esta APROVADO com media ", Media)
    }
  }

  funcao inicio() {
    //Declaração de variaveis
    cadeia Nome
    real Nota1, Nota2, Nota3, Media

    //Captar nome do aluno
    escreva("Ola qual é o nome do aluno? \n")
    leia(Nome)

    //Captar as três notas
    escreva("Qual a primeira nota ? \n")
    leia(Nota1)
    escreva("Qual a primeira nota ? \n")
    leia(Nota2)
    escreva("Qual a primeira nota ? \n")
    leia(Nota3)

    media(Nota1,Nota2,Nota3,Nome)
  }
}
