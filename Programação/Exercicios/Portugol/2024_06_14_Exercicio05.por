// Feito por Victor Barros Roma
// 14/06/2024
// Objetivo: Calcular a media de 4 notas de um aluno e informar seu desempenho
programa {
  funcao inicio() {

    //Declara��o de variaveis
    real Nota1, Nota2, Nota3, Nota4, Media
    cadeia NomeAluno

    //Solicita��o do nome do aluno
    escreva("Qual � o nome do aluno(a) ? ")
    leia(NomeAluno)

    //Solicita��o das notas do aluno
    escreva("Qual � a primeira nota ? ")
    leia(Nota1)

    escreva("Qual � a segunda nota ? ")
    leia(Nota2)

    escreva("Qual � a terceira nota ? ")
    leia(Nota3)

    escreva("Qual � a quarta nota ? ")
    leia(Nota4)

    //Calcular a media do aluno
    Media = (Nota1 + Nota2 + Nota3 + Nota4)/4

    //Mostra ao usuario o nome do aluno e sua media
    escreva("A media do ", NomeAluno," foi ", Media)
    
    //Verifica se o aluno foi reprovado
    se (Media < 5 ){
      escreva(" REPROVADO")
    }
    //Verifica se o aluno foi para recupera��o    
    se (Media >= 5 e Media <7){
      escreva(" RECUPERA��O")
    }
    //Verifica se o aluno foi aprovado
    se (Media >= 7 ){
      escreva(" APROVADO")
    }
  }
}
