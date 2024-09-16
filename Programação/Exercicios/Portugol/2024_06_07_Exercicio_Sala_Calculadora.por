// Data: 07/06/2024
// Feito por Victor Barros Roma
// Contato: (81)9-9594-3410

programa {
  funcao inicio() {

    //Declaração de variaveis
    real Numero1, Numero2, Resultado
    cadeia Soma, Subtracao, Multiplicacao, Divisao, Operacao

  //Solicitação para o usuario qual operaçao deseja realizar
  escreva("Qual a operação que você deseja realizar ? \n Digite 1 para SOMA \n Digite 2 para SUBTRAÇÃO \n Digite 3 para MULTIPLICAÇÃO \n Digite 4 para DIVISÃO \n")
  leia(Operacao)
  
  // Verificação se é uma soma
  se (Operacao == "1"){
    escreva(" Você escolheu somar \n Digite o primeiro número: ")
    leia(Numero1)
    escreva(" Digite o segundo número: ")
    leia(Numero2)
    Resultado = Numero1 + Numero2
    escreva(" O total da sua soma deu: ", Resultado)
  }
  
  // Verificação se é uma subtração
  se (Operacao == "2"){
    escreva(" Você escolheu subtrair \n Digite o primeiro número: ")
    leia(Numero1)
    escreva(" Digite o segundo número: ")
    leia(Numero2)
    Resultado = Numero1 - Numero2
    escreva(" O total da sua subtração deu: ", Resultado)
  }
  
  // Verificação se é uma multiplicação
  se (Operacao == "3"){
    escreva(" Você escolheu multiplicar \n Digite o primeiro número: ")
    leia(Numero1)
    escreva(" Digite o segundo número: ")
    leia(Numero2)
    Resultado = Numero1 * Numero2
    escreva(" O total da sua multiplicação deu: ", Resultado)
  }
  
  // Verificação se é uma divisão
  se (Operacao == "4"){
    escreva(" Você escolheu dividir \n Digite o primeiro número: ")
    leia(Numero1)
    escreva(" Digite o segundo número: ")
    leia(Numero2)
    Resultado = Numero1 / Numero2
    escreva(" O total da sua divisão deu: ", Resultado)
  }
  
  // Caso o usuario informar um numero que não tem operador
  senao {
    escreva("O operador solicitado náo existe")
  }
  }
}