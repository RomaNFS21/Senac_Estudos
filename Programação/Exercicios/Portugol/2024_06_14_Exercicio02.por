// Feito por Victor Barros Roma
// 14/06/2024
// Objetivo: Calcular o salario liquido
programa {
  funcao inicio() {
    //Declara��o de variaveis
    real SalarioBruto, SalarioLiquido
    inteiro NumeroFilhos

    //Adiquirindo valor do salario bruto
    escreva("Quanto � seu sal�rio bruto ? ")
    leia(SalarioBruto)
    //Adiquirindo quantos filhos o funcionario tem
    escreva("Quantos filhos voc� tem ? ")
    leia(NumeroFilhos)

    //Calculo do Salario Liquido
    SalarioLiquido = (SalarioBruto * 70) / 100

    //Verifica��o para saber se tem 2 ou menos filhos
    se (NumeroFilhos <=2 ){
      escreva("Seu sal�rio liquido � de ", SalarioLiquido, " reais")
    }

    //Caso o funcionario tiver mais de 2 filhos
    senao {
      SalarioLiquido = SalarioLiquido + 300
      escreva("Seu sal�rio liquido � de ", SalarioLiquido, " reais com um acr�ssimo por ter ", NumeroFilhos, " filhos.")
    }

  }
}
