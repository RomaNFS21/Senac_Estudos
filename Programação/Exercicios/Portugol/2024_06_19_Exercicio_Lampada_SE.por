// Feito por Victor Barros Roma
// Data: 19/06/2024
// Objetivo : Problema da l�mpada n�o funciona

programa {
  funcao inicio() {
    //Declara��o de variaveis
    cadeia Resposta

    //Pergunta inicial do programa
    escreva("A lampada esta plugada ? \nResponda com SIM ou N�O \n ")
    leia(Resposta)

    //Caso a primeira pergunta seja SIM
    se ( (Resposta == "SIM") ou (Resposta == "Sim") ou (Resposta == "sim") ){

      //Faz a segunda pergunta
      escreva("O bulbo queimou ? \nResponda com SIM ou N�O \n ")
      leia(Resposta)

      //Caso a segunda pergunta seja SIM
        se ( (Resposta == "SIM") ou (Resposta == "Sim") ou (Resposta == "sim")  ){
          escreva("Troque o bulbo")
        }
      
      //Caso a segunda pergunta seja N�O
        senao se ( (Resposta == "N�O") ou (Resposta == "N�o") ou (Resposta == "n�o") ){
          escreva("Compre uma nova l�mpada")
        }
    }

    //Caso a primeira pergunta seja N�O
    senao se ( (Resposta == "N�O") ou (Resposta == "N�o") ou (Resposta == "n�o") ){
      escreva("Pluge a l�mpada! ")
    }
  }
}
