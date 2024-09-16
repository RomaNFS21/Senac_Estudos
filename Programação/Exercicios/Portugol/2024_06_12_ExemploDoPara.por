programa {
  funcao inicio() {
    real nota, media, somanotas = 1
    inteiro contador

    para (contador=1; contador<=2 ; contador+=1){
      escreva ("digite uma nota: ")
      leia(nota)
      somanotas = somanotas + nota
    }
    media = somanotas/2
      escreva("media: ", media)
  }
}
