programa {
  funcao inicio() {
    //Declara��o de variaveis
    cadeia Times[20]
    inteiro Contador

    //para (Contador = 0 ; Contador <20; Contador++)
    Times[0] = "Flamengo"
    Times[1] = "Bahia"
    Times[2] = "Botafogo"
    Times[3] = "Palmeiras"
    Times[4] = "Cruzeiro"
    Times[5] = "Athetico-PR" 
    Times[6] = "S�o Paulo"
    Times[7] = "Bragantino"
    Times[8] = "Internacional"
    Times[9] = "Atl�tico-MG"
    Times[10] = "Fortaleza"
    Times[11] = "Juventude"
    Times[12] = "Crici�ma"
    Times[13] = "Cuiab�"
    Times[14] = "EC Vit�ria"
    Times[15] = "Vasco Da Gama" 
    Times[16] = "Atl�tico-GO"
    Times[17] = "Corinthians"
    Times[18] = "Gr�mio"
    Times[19] = "Fluminense"

    escreva("\n ==================================== TABELA DO BRASILEIR�O ==================================== \n \n ==================================== LIBERTADORES ==================================== \n")
    para(Contador = 0 ; Contador <4 ; Contador++){
      escreva(Contador+1,"- " ,Times[Contador],"\n")
    }

    escreva("\n ==================================== PRE-LIBERTADORES ==================================== \n")
    para(Contador = 4 ; Contador <6 ; Contador++){
      escreva(Contador+1,"- " ,Times[Contador],"\n")
    }

    escreva("\n ==================================== SUL-AMERICANA ==================================== \n")
    para(Contador = 6 ; Contador <12 ; Contador++){
      escreva(Contador+1,"- " ,Times[Contador],"\n")
    }
    
    escreva("\n ======================================================================== \n")
    para(Contador = 12 ; Contador <16 ; Contador++){
      escreva(Contador+1,"- " ,Times[Contador],"\n")
    }
  

    escreva("\n ==================================== REBAIXADOS ==================================== \n")
    para(Contador = 16 ; Contador <20 ; Contador++){
      escreva(Contador+1,"- " ,Times[Contador],"\n")
    }
  }
}
