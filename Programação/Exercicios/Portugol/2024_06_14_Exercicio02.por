// Feito por Victor Barros Roma
// 14/06/2024
// Objetivo: Calcular o salario liquido
programa {
  funcao inicio() {
    //Declaração de variaveis
    real SalarioBruto, SalarioLiquido
    inteiro NumeroFilhos

    //Adiquirindo valor do salario bruto
    escreva("Quanto é seu salário bruto ? ")
    leia(SalarioBruto)
    //Adiquirindo quantos filhos o funcionario tem
    escreva("Quantos filhos você tem ? ")
    leia(NumeroFilhos)

    //Calculo do Salario Liquido
    SalarioLiquido = (SalarioBruto * 70) / 100

    //Verificação para saber se tem 2 ou menos filhos
    se (NumeroFilhos <=2 ){
      escreva("Seu salário liquido é de ", SalarioLiquido, " reais")
    }

    //Caso o funcionario tiver mais de 2 filhos
    senao {
      SalarioLiquido = SalarioLiquido + 300
      escreva("Seu salário liquido é de ", SalarioLiquido, " reais com um acréssimo por ter ", NumeroFilhos, " filhos.")
    }

  }
}
