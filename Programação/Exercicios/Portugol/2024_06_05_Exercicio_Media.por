programa {
  funcao inicio() {
    //Programa para fazer a media escolar do aluno para sua aprovação ou reprovação

    //Declaração de variaveis
    real Unidade1, Unidade2, Unidade3, Unidade4
    real Media_Final , Nota_Trabalho
    cadeia Aluno 
    
    //Qual o nome do aluno
    escreva ("Qual o nome do aluno?: ")
    leia(Aluno)

    //Qual a nota de cada unidade
    escreva("Qual a nota da unidade 1 ? ")
    leia(Unidade1)

    escreva("Qual a nota da unidade 2 ? ")
    leia(Unidade2)

    escreva("Qual a nota da unidade 3 ? ")
    leia(Unidade3)

    escreva("Qual a nota na unidade 4 ? ")
    leia(Unidade4)

    escreva("Qual a nota do tabalho ?")
    leia(Nota_Trabalho)

    //Verificações se passou ou não na unidade
    //Verificação da unidade 1
    se (Unidade1 < 7) {
      escreva("O aluno ", Aluno, " esta reprovado na unidade 1 com nota ", Unidade1, "\n")
    }
    senao {
      escreva("O aluno ", Aluno, " esta aprovado na unidade 1 com nota ", Unidade1, "\n")
    }

    
    
    //Verificação da unidade 2

    se (Unidade2 >= 7) {
      escreva("O aluno ", Aluno, " esta APROVADO na unidade 2 com nota ", Unidade2, "\n")
    }
    senao {
      escreva("O aluno ", Aluno, " esta REPROVADO na unidade 2 com nota ", Unidade2, "\n")
    }

    
    
    //Verificação da unidade 3

    se (Unidade3 >= 7){
      escreva("O aluno ", Aluno, " esta APROVADO na unidade 3 com nota ", Unidade3, "\n")
    }
    senao {
      escreva("O aluno ", Aluno, " esta REPROVADO na unidade 3 com nota ", Unidade3, "\n")
    }

    
    
    //Verificação da unidade 4

    se (Unidade4 < 7){
      escreva("O aluno ", Aluno, " esta REPROVADO na unidade 4 com nota ", Unidade4, "\n")
    }
    senao{
      escreva("O aluno ", Aluno, " esta APROVADO na unidade 4 com nota ", Unidade4, "\n")
    }
    


    //Verificar a media final
    Media_Final = (Unidade1 + Unidade2 + Unidade3 + Unidade4) / 4

    se (Media_Final <=5 e Nota_Trabalho >= 2){
      Media_Final = Media_Final + Nota_Trabalho
    }

    se (Media_Final >5){
      escreva("Aprovado com a nota do trabalho")
    }
    senao { escreva(" Larguei até sexta se deus quiser ")}
    /* se (Media_Final <=5){
      escreva("O ", Aluno, " esta REPROVADO na final com média ", Media_Final)
    }

    senao {
      escreva("O ", Aluno, " esta APROVADO na final com média ", Media_Final)
    } */
  }
}
