programa {
  funcao inicio() {
    //Declaração de variaveis
    cadeia Alunos[5]
    real Notas[5]
    inteiro Contador

    //Cadastro dos alunos e notas
    para(Contador = 0 ; Contador < 5 ; Contador++){
      escreva("Qual é o nome do aluno(a)? \n")
      leia(Alunos[Contador])
      escreva("Qual é a nota do aluno(a)? \n")
      leia(Notas[Contador])
    }
    escreva("\n -------------------------- Alunos Reprovados -------------------------- \n ")
    //Verificação e informação dos alunos reprovados
    para(Contador = 0 ; Contador < 5 ; Contador++){
      se (Notas[Contador] < 7){
        escreva(Alunos[Contador],"- Status - Reprovado(a) \n")
      }
      senao {}
    }

  }
}
