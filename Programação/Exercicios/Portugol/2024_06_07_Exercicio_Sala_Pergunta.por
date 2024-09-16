// Data: 07/06/2024
// Feito por Victor Barros Roma
// Contato: (81)9-9594-3410

programa {
  funcao inicio() {
    //Declaração de variaveis
    cadeia Alternativa

    //Exibir pergunta
    escreva(" Se forem escolhidos quaisquer 6 moradores de um determinado bairro, pelo menos 2 deles se vacinaram contra a dengue. \n Considerando que nesse bairro residem 120 moradores, é correto afirmar que existem: \n")
    escreva(" (A) no mínimo, 116 moradores que se vacinaram contra a dengue. \n (B) no máximo, 116 moradores que se vacinaram contra a dengue. \n")
    escreva(" (C) no mínimo, 116 moradores que não se vacinaram contra a dengue. \n (D) no máximo, 116 moradores que não se vacinaram contra a dengue.")
    escreva(" \n Qual é a alternativa correta ? ")
    
    //Captação da resposta
    leia(Alternativa)
    
    //Verificação da resposta
    se (Alternativa == "a" ou Alternativa == "A" ou Alternativa == "Letra A" ou Alternativa == "Letra a" ou Alternativa == "letra a" ou Alternativa == "letra A") {
      escreva("Resposta correta")
    }
    senao {
      escreva("Resposta incorreta")
    }
  }
}