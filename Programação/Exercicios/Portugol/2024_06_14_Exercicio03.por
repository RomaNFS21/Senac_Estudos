// Feito por Victor Barros Roma
// 14/06/2024
// Objetivo: Informar Nome, Salario fixo e o salario com comiss�es de um vendedor
programa {
  funcao inicio() {
    //Declara��o de variaveis
    cadeia NomeFuncionario
    real SalarioFixo, Comissao, SalarioTotal

    //Pegar o nome do funcionario
    escreva("Qual o nome do funcionario ? ")
    leia(NomeFuncionario)

    //Saber quanto � o salario fixo
    escreva("Quanto � seu salario fixo ? ")
    leia(SalarioFixo)

    //Saber quanto que ele fez em vendas
    escreva("Quanto em reais que ele fez em vendas no mes ? ")
    leia(Comissao)

    //Calcular a comiss�o que � de 15%
    Comissao = (Comissao * 15) / 100

    //Calculo do salario total
    SalarioTotal = Comissao + SalarioFixo

    //Informar o nome, salario fixo e o salario total no final do mes
    escreva(NomeFuncionario, " tem um salario de ",SalarioFixo, " reais, com as comiss�es no fim do m�s ele vai receber ", SalarioTotal, " reais.")

  }
}
