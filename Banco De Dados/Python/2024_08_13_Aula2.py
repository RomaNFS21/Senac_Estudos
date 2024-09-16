''' 
n1 = "10"
n2 = "8"

soma = n1 + n2

print("O valor da soma é ",soma)

'''
'''
var = 1
print(type(var))
'''
'''
n1 = (input("digite seu nome"))
print(type(n1))
'''
'''
numero1 = float(input("Informe um numero "))
numero2 = float(input("Informe outro numero "))

soma = numero1 + numero2

print("A soma dos dois valores é: R$",soma)
'''

## EXERCICIO 01

'''salarioInformado = float(input("Qual o valor atual do salario?:"))
porcentagemAumento = float(input("Qual a porcentagem de aumento?"))

salarioNovo = ((salarioInformado * porcentagemAumento) / 100) + salarioInformado

print("O novo salario com aumento de",porcentagemAumento,"% é de: R$",salarioNovo)
'''

## EXERCICIO 02

'''nomeUsuario = str(input("Informe seu nome completo "))
idadeUsuario = int(input("Qual é sua idade ? "))
anoAtual = int(input("Em que anos estamos ? "))
anoNascimento = anoAtual - idadeUsuario

print(f"{nomeUsuario} a sua idade é {idadeUsuario} você nasceu em {anoNascimento}")'''

## EXERCICIO 03

valorFralda = float(input("Qual o valor de uma unica fralda ? "))
fraldaPorDia = int(input("Quantas fraldas usa por dia ? "))
diasDoMes = int(input("Quantos dias tem no mês ? "))

fraldasTotais = fraldaPorDia * diasDoMes
gastoFralda = fraldasTotais * valorFralda

print(f"No mês com {diasDoMes} dias, você ira comprar {fraldasTotais} fraldas dando um total de {gastoFralda} reais")