# Programa 5 Informar um número e imprimir se é par ou ímpar.

numero = int(input("Favor informar um número para verificar se ele é impar ou par ! "))

if numero % 2 == 0:
    print(f"{numero} é par !")

if numero % 2 != 0:
    print(f"{numero} é impar !")