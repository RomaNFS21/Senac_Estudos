//Feito por Victor Roma e Wanderson
//01/07/2024
//Problema 1

programa {
  inclua biblioteca Matematica

  funcao inicio() {
   real NumeroRecebido
   inteiro ParteInteira , Contador

  

  escreva("Qual n�mero real voc� quer saber a parte inteira dele ")
  leia(NumeroRecebido)

  para (Contador = 0 ; Contador <= NumeroRecebido; Contador++){
    ParteInteira = Contador
  }


  escreva("A parte inteira do n�mero informado � ",ParteInteira)

  }
}
