// Data: 07/06/2024
// Feito por Victor Barros Roma
// Contato: (81)9-9594-3410

programa {
  funcao inicio() {
    //Declara��o de variaveis
    cadeia Alternativa

    //Exibir pergunta
    escreva(" Se forem escolhidos quaisquer 6 moradores de um determinado bairro, pelo menos 2 deles se vacinaram contra a dengue. \n Considerando que nesse bairro residem 120 moradores, � correto afirmar que existem: \n")
    escreva(" (A) no m�nimo, 116 moradores que se vacinaram contra a dengue. \n (B) no m�ximo, 116 moradores que se vacinaram contra a dengue. \n")
    escreva(" (C) no m�nimo, 116 moradores que n�o se vacinaram contra a dengue. \n (D) no m�ximo, 116 moradores que n�o se vacinaram contra a dengue.")
    escreva(" \n Qual � a alternativa correta ? ")
    
    //Capta��o da resposta
    leia(Alternativa)
    
    //Verifica��o da resposta
    se (Alternativa == "a" ou Alternativa == "A" ou Alternativa == "Letra A" ou Alternativa == "Letra a" ou Alternativa == "letra a" ou Alternativa == "letra A") {
      escreva("Resposta correta")
    }
    senao {
      escreva("Resposta incorreta")
    }
  }
}