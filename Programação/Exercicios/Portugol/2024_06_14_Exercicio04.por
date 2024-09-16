// Feito por Victor Barros Roma
// 14/06/2024
// Objetivo: Sortear um numero e dizer se � o mesmo que o usu�rio escolheu entre 0 e 10
programa {
  //Incluindo Biblioteca Util para usar o sorteador/gerador de numeros
  inclua biblioteca Util --> u

  funcao inicio() {

    //Declara��o das variaveis
    inteiro NumeroSorteado, NumeroEscolhido
    
    //Sorteio do numero para o usu�rio tentar adivinhar
    NumeroSorteado = u.sorteia(0,10)

    //Pegar o numero que o usu�rio digitar 
    escreva("Qual o numero de 0 a 10 voc� quer ? ")
    leia(NumeroEscolhido)

    //Verifica��o se o numero escolhido e igual ao digitado
    se (NumeroEscolhido == NumeroSorteado){
      escreva("Parabens voc� acertou")
    }

    //Caso esteja errado o numero digitado
    senao {
      escreva("Voc� errou tente de novo")
    }


    
  }
}
