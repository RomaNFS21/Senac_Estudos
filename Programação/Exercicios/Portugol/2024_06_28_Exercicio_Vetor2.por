programa {
  funcao inicio() {
    cadeia Aluno[2]
    real Nota[2]
    inteiro Posicao, I 

    //Prencher o vetor
    para (Posicao = 0; Posicao < 2; Posicao++){
      escreva("Qual o Nome do aluno(a)? \n")
      leia(Aluno[Posicao])
      escreva("Qual a nota do aluno(a)? \n")
      leia(Nota[Posicao])
    }

    escreva("\n ----------------------------- Apresentando Notas ----------------------------- \n")
    //Apresentar o vetor
    para( I = 0 ; I < 2 ; I++){
      escreva("Aluno(a): ", Aluno[I], "\n")
      se (Nota[I]<7){
        escreva(" Status - Reprovado(a)! \n")
      }
      senao {
        escreva(" Status - Aprovado!(a)! \n")
      }
    }    
  }
}
