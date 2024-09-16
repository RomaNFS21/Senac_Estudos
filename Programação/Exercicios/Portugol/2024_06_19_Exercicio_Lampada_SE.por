// Feito por Victor Barros Roma
// Data: 19/06/2024
// Objetivo : Problema da lâmpada não funciona

programa {
  funcao inicio() {
    //Declaração de variaveis
    cadeia Resposta

    //Pergunta inicial do programa
    escreva("A lampada esta plugada ? \nResponda com SIM ou NÃO \n ")
    leia(Resposta)

    //Caso a primeira pergunta seja SIM
    se ( (Resposta == "SIM") ou (Resposta == "Sim") ou (Resposta == "sim") ){

      //Faz a segunda pergunta
      escreva("O bulbo queimou ? \nResponda com SIM ou NÃO \n ")
      leia(Resposta)

      //Caso a segunda pergunta seja SIM
        se ( (Resposta == "SIM") ou (Resposta == "Sim") ou (Resposta == "sim")  ){
          escreva("Troque o bulbo")
        }
      
      //Caso a segunda pergunta seja NÃO
        senao se ( (Resposta == "NÃO") ou (Resposta == "Não") ou (Resposta == "não") ){
          escreva("Compre uma nova lâmpada")
        }
    }

    //Caso a primeira pergunta seja NÃO
    senao se ( (Resposta == "NÃO") ou (Resposta == "Não") ou (Resposta == "não") ){
      escreva("Pluge a lâmpada! ")
    }
  }
}
