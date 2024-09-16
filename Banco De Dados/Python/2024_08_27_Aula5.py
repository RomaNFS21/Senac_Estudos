valorUm = float(input("Qual o primeiro valor ? "))
valorDois = float(input("Qual o segundo valor ? "))
print("OPERAÇÕES DISPONIVEIS: SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO")
operacao = str(input("Que operação você deseja executar com os dois números ? "))
resultado = 0

if (operacao == "+" or "soma" == operacao.upper().lower() or "somar" == operacao.upper().lower()):
    resultado = (valorUm + valorDois)
    print("O valor da soma dos dois valores é ",resultado)

elif (operacao == "-" or "subtração" == operacao.upper().lower() or "subtrair" == operacao.upper().lower()):
    resultado = (valorUm - valorDois)
    print("O valor da subtração dos dois valores é ",resultado)

elif (operacao == "*" or "multiplicação" == operacao.upper().lower() or "multiplicar" == operacao.upper().lower()):
    resultado = (valorUm * valorDois)
    print("O valor da multiplicação dos dois valores é ",resultado) 

elif (operacao == "/" or "divisão" == operacao.upper().lower() or "dividir" == operacao.upper().lower() ):
    resultado = (valorUm / valorDois)
    print("O valor da divisão dos dois valores é ",resultado)

else:
    print("Operador invalido")
