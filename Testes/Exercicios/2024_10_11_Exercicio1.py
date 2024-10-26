#Programa 07 Ler um número e imprimir igual a 20, menor que 20, maior que 20.

numero_informado = float(input("Favor informar um número ! "))

if numero_informado < 20:
    print(f"{numero_informado} é menor que 20 !")

elif numero_informado == 20:
    print(f"{numero_informado} é igual a 20 !")

elif numero_informado > 20:
    print(f"{numero_informado} é maior que 20 !")