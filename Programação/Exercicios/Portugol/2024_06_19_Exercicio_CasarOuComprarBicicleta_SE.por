// Feito por Victor Barros Roma
// Data: 19/06/2024
// Objetivo : Problema de comprar uma bicicleta ou casar

programa {
  funcao inicio() {
  
  //Declaração de variaveis
  cadeia Resposta

  //Primeira pergunta -  Se estar gordo
  escreva("Você esta gordo(a)? /n Responda SIM ou NÃO ")
  leia(Resposta)

  // Se esta gordo
  se ( (Resposta == "Sim") ou (Resposta == "sim") ou (Resposta == "SIM") ){
    
    //Segunda pergunta caminho 1 - Se quer emagrecer
    escreva("Quer emagrecer? /n Responda SIM ou NÃO ")
    leia(Resposta)

    //Se quer emagrecer
      se ( (Resposta == "Sim") ou (Resposta == "sim") ou (Resposta == "SIM") ){
        escreva("Então compre uma bicicleta !")
      }
    //Se não quer emagrecer
      senao se((Resposta == "Não") ou (Resposta == "não") ou (Resposta == "NÃO")){
        escreva("Então case !")
      }
  }
  // Se não esta gordo
  senao se((Resposta == "Não") ou (Resposta == "não") ou (Resposta == "NÃO")) {
    // Segunda pergunta caminho 2 - Se quer engordar
    escreva("Quer engordar ? /n Responda SIM ou NÃO ")
    leia(Resposta)
  
  // Se quiser engordar
    se ((Resposta == "Sim") ou (Resposta == "sim") ou (Resposta == "SIM")) {
      escreva("Então case !")
    }
  //Se não quiser engordar
    senao se ((Resposta == "Não") ou (Resposta == "não") ou (Resposta == "NÃO")){
      escreva("Então compre uma bicicleta !")
    }
  }
  }
}
