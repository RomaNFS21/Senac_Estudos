# 3.Escreva um programa  de forma a perguntar também o valor depositado mensalmente. 
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte

encerramento = ""
valorConta = 0
investimento = 0
tempoAplicado = 0
porcentagem = 0

while encerramento.upper().lower() != "não":

    nomeCliente = str(input("Olá qual o nome do investidor ? "))
    valorConta = float(input("Qual o valor que ele ja possui em conta ? "))
    investimento = float(input("Qual o valor que será aplicado todo mês ? "))
    tempoAplicado = int(input("Quantos meses pretende deixar esse valor rendendo ? "))
    porcentagem = float(input("Qual a porcentagem de rendimento mensal ? "))
    
    for tempoAplicado in range (0, tempoAplicado+1, 1):
        valorConta = valorConta + investimento
        rendimento = ((valorConta * porcentagem)/100)
        valorConta = valorConta + rendimento
    
    print(f"O Sr(a): {nomeCliente} tera em conta depois de {tempoAplicado} meses um total de R$ {valorConta}")
    
    encerramento = str(input("Deseja fazer um novo calculo de investimento ? digite SIM para fazer um novo calculo, digite NÃO para encerrar "))

    


    
