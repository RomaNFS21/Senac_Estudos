//Feito por: Victor Barros Roma
// 17/06/2024
// Objetivo: Calcular o IMC 

programa {

  //Função para calcular o IMC atraves do peso e altura fornecidos pelo usuário
  funcao imc(real peso, real altura){
  
  real imc

  //Calculo do IMC
  imc = peso / (altura * altura)
  escreva("\n Seu IMC é de ", imc)

  //Verificação da classificação a partir do IMC
  se (imc <17){
    escreva("Você esta muito abaixo do peso")
  }

  senao se (imc >= 17 e imc < 18.5){
    escreva("Você esta abaixo do peso")
  }

  senao se (imc >= 18.5 e imc < 25){
    escreva("Você esta no peso ideal")
  }

  senao se (imc >= 25 e imc < 30){
    escreva("Você esta acima do peso")
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

    //Declaração das variaveis
    real Altura, Peso
    cadeia Nome

    //Elicitação do nome da pessoa que quer calcular o IMC
    escreva("Ola, bem vindo ao medidor de IMC, qual é seu nome ?  \n")
    leia(Nome)

    //Elicitação da altura da pessoa
    escreva("Qual é sua altura ? \n")
    leia(Altura)

    //Elicitação do peso da pessoa
    escreva("Qual é seu peso ? \n")
    leia(Peso)

    //Escreva o nome e chamado a função de IMC para calcular
    escreva(Nome) 
    imc(Peso, Altura)

  }
}
