//Pedro Leon, Victor Roma e João Vitor; 26/06/2024; pedro51376376@edu.pe.senac.br.

programa {
  funcao inicio() {
    
    real ValorA, ValorB, TrocaA, TrocaB

    escreva("Qual o valor de A ? ")
    leia(ValorA)
    escreva("Qual o valor de B? ")
    leia(ValorB)

   TrocaB = ValorA
   TrocaA = ValorB

   ValorA = TrocaA
   ValorB = TrocaB

    escreva("O valor de A é ",ValorA," e o valor de B é ",ValorB)
  }
}
