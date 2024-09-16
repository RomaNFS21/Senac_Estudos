programa {
  funcao inicio() {
    real nota, media, somanotas = 0
    inteiro contador

    para (contador=1; contador<=5 ; contador+=1){
      escreva ("digite uma nota: ")
      leia(nota)
      somanotas = somanotas + nota
    }
    media = somanotas
      escreva("Soma: ", media)
  }
}
