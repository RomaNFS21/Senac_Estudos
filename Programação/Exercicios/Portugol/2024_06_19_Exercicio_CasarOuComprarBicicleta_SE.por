// Feito por Victor Barros Roma
// Data: 19/06/2024
// Objetivo : Problema de comprar uma bicicleta ou casar

programa {
  funcao inicio() {
  
  //Declara��o de variaveis
  cadeia Resposta

  //Primeira pergunta -  Se estar gordo
  escreva("Voc� esta gordo(a)? /n Responda SIM ou N�O ")
  leia(Resposta)

  // Se esta gordo
  se ( (Resposta == "Sim") ou (Resposta == "sim") ou (Resposta == "SIM") ){
    
    //Segunda pergunta caminho 1 - Se quer emagrecer
    escreva("Quer emagrecer? /n Responda SIM ou N�O ")
    leia(Resposta)

    //Se quer emagrecer
      se ( (Resposta == "Sim") ou (Resposta == "sim") ou (Resposta == "SIM") ){
        escreva("Ent�o compre uma bicicleta !")
      }
    //Se n�o quer emagrecer
      senao se((Resposta == "N�o") ou (Resposta == "n�o") ou (Resposta == "N�O")){
        escreva("Ent�o case !")
      }
  }
  // Se n�o esta gordo
  senao se((Resposta == "N�o") ou (Resposta == "n�o") ou (Resposta == "N�O")) {
    // Segunda pergunta caminho 2 - Se quer engordar
    escreva("Quer engordar ? /n Responda SIM ou N�O ")
    leia(Resposta)
  
  // Se quiser engordar
    se ((Resposta == "Sim") ou (Resposta == "sim") ou (Resposta == "SIM")) {
      escreva("Ent�o case !")
    }
  //Se n�o quiser engordar
    senao se ((Resposta == "N�o") ou (Resposta == "n�o") ou (Resposta == "N�O")){
      escreva("Ent�o compre uma bicicleta !")
    }
  }
  }
}
