programa {
  funcao inicio() {
  cadeia Alunos[2]
  real Nota[2]
  inteiro i

  Alunos[0] = "Matheus"
  Alunos[1] = "Maria"

  Nota[0] = 7.1
  Nota[1] = 6.0

  para (i=0 ; i<2; i++){

    escreva (Alunos[i])
    escreva ("\n")
    
    se (Nota[i]<7){
      escreva ("Status - Reprovado! \n")
      }
      senao {
        escreva ("Status - Aprovado! \n")
          }
    }

  }
}
