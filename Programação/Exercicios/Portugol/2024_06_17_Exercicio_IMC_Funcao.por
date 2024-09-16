//Feito por: Victor Barros Roma
// 17/06/2024
// Objetivo: Calcular o IMC 

programa {

  //Fun��o para calcular o IMC atraves do peso e altura fornecidos pelo usu�rio
  funcao imc(real peso, real altura){
  
  real imc

  //Calculo do IMC
  imc = peso / (altura * altura)
  escreva("\n Seu IMC � de ", imc)

  //Verifica��o da classifica��o a partir do IMC
  se (imc <17){
    escreva("Voc� esta muito abaixo do peso")
  }

  senao se (imc >= 17 e imc < 18.5){
    escreva("Voc� esta abaixo do peso")
  }

  senao se (imc >= 18.5 e imc < 25){
    escreva("Voc� esta no peso ideal")
  }

  senao se (imc >= 25 e imc < 30){
    escreva("Voc� esta acima do peso")
  }

  senao se (imc >= 30 e imc < 35){
    escreva("Voce esta com obesidade grau 1")
  }

  senao se (imc >= 35 e imc < 40){
    escreva("Voce esta com obesidade grau 2")
  }

  senao {
    escreva("Voce esta com obesidade grau 3")
  }

  }
  
  // Inicio do Programa 
  funcao inicio() {

    //Declara��o das variaveis
    real Altura, Peso
    cadeia Nome

    //Elicita��o do nome da pessoa que quer calcular o IMC
    escreva("Ola, bem vindo ao medidor de IMC, qual � seu nome ?  \n")
    leia(Nome)

    //Elicita��o da altura da pessoa
    escreva("Qual � sua altura ? \n")
    leia(Altura)

    //Elicita��o do peso da pessoa
    escreva("Qual � seu peso ? \n")
    leia(Peso)

    //Escreva o nome e chamado a fun��o de IMC para calcular
    escreva(Nome) 
    imc(Peso, Altura)

  }
}
