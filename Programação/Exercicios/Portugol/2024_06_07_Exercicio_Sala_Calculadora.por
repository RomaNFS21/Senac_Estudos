// Data: 07/06/2024
// Feito por Victor Barros Roma
// Contato: (81)9-9594-3410

programa {
  funcao inicio() {

    //Declara��o de variaveis
    real Numero1, Numero2, Resultado
    cadeia Soma, Subtracao, Multiplicacao, Divisao, Operacao

  //Solicita��o para o usuario qual opera�ao deseja realizar
  escreva("Qual a opera��o que voc� deseja realizar ? \n Digite 1 para SOMA \n Digite 2 para SUBTRA��O \n Digite 3 para MULTIPLICA��O \n Digite 4 para DIVIS�O \n")
  leia(Operacao)
  
  // Verifica��o se � uma soma
  se (Operacao == "1"){
    escreva(" Voc� escolheu somar \n Digite o primeiro n�mero: ")
    leia(Numero1)
    escreva(" Digite o segundo n�mero: ")
    leia(Numero2)
    Resultado = Numero1 + Numero2
    escreva(" O total da sua soma deu: ", Resultado)
  }
  
  // Verifica��o se � uma subtra��o
  se (Operacao == "2"){
    escreva(" Voc� escolheu subtrair \n Digite o primeiro n�mero: ")
    leia(Numero1)
    escreva(" Digite o segundo n�mero: ")
    leia(Numero2)
    Resultado = Numero1 - Numero2
    escreva(" O total da sua subtra��o deu: ", Resultado)
  }
  
  // Verifica��o se � uma multiplica��o
  se (Operacao == "3"){
    escreva(" Voc� escolheu multiplicar \n Digite o primeiro n�mero: ")
    leia(Numero1)
    escreva(" Digite o segundo n�mero: ")
    leia(Numero2)
    Resultado = Numero1 * Numero2
    escreva(" O total da sua multiplica��o deu: ", Resultado)
  }
  
  // Verifica��o se � uma divis�o
  se (Operacao == "4"){
    escreva(" Voc� escolheu dividir \n Digite o primeiro n�mero: ")
    leia(Numero1)
    escreva(" Digite o segundo n�mero: ")
    leia(Numero2)
    Resultado = Numero1 / Numero2
    escreva(" O total da sua divis�o deu: ", Resultado)
  }
  
  // Caso o usuario informar um numero que n�o tem operador
  senao {
    escreva("O operador solicitado n�o existe")
  }
  }
}