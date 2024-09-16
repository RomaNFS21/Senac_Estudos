// Feito por Victor Barros Roma
// 14/06/2024
// Objetivo: Calcular a media de 4 notas de um aluno e informar seu desempenho
programa {
  funcao inicio() {

    //Declaração de variaveis
    real Nota1, Nota2, Nota3, Nota4, Media
    cadeia NomeAluno

    //Solicitação do nome do aluno
    escreva("Qual é o nome do aluno(a) ? ")
    leia(NomeAluno)

    //Solicitação das notas do aluno
    escreva("Qual é a primeira nota ? ")
    leia(Nota1)

    escreva("Qual é a segunda nota ? ")
    leia(Nota2)

    escreva("Qual é a terceira nota ? ")
    leia(Nota3)

    escreva("Qual é a quarta nota ? ")
    leia(Nota4)

    //Calcular a media do aluno
    Media = (Nota1 + Nota2 + Nota3 + Nota4)/4

    //Mostra ao usuario o nome do aluno e sua media
    escreva("A media do ", NomeAluno," foi ", Media)
    
    //Verifica se o aluno foi reprovado
    se (Media < 5 ){
      escreva(" REPROVADO")
    }
    //Verifica se o aluno foi para recuperação    
    se (Media >= 5 e Media <7){
      escreva(" RECUPERAÇÃO")
    }
    //Verifica se o aluno foi aprovado
    se (Media >= 7 ){
      escreva(" APROVADO")
    }
  }
}
