// Feito por Victor Barros Roma
// 14/06/2024
// Objetivo: Sortear um numero e dizer se é o mesmo que o usuário escolheu entre 0 e 10
programa {
  //Incluindo Biblioteca Util para usar o sorteador/gerador de numeros
  inclua biblioteca Util --> u

  funcao inicio() {

    //Declaração das variaveis
    inteiro NumeroSorteado, NumeroEscolhido
    
    //Sorteio do numero para o usuário tentar adivinhar
    NumeroSorteado = u.sorteia(0,10)

    //Pegar o numero que o usuário digitar 
    escreva("Qual o numero de 0 a 10 você quer ? ")
    leia(NumeroEscolhido)

    //Verificação se o numero escolhido e igual ao digitado
    se (NumeroEscolhido == NumeroSorteado){
      escreva("Parabens você acertou")
    }

    //Caso esteja errado o numero digitado
    senao {
      escreva("Você errou tente de novo")
    }


    
  }
}
