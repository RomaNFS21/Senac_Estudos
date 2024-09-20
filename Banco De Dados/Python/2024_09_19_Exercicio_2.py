# 2-Escreva um programa que leia três números e que imprima o maior e o menor.

repetir = ""

# Estrutura de repetição para caso o usuario queira fazer mais de uma vez a consulta
while repetir.upper().lower() != "não" :

    listaNumeros = []
    # Captação das informações a serem verificadas
    print("A seguir informe três números para verificar qual é o maior e o menor número ")
    listaNumeros.append(float(input("Informe o primeiro número ")))
    listaNumeros.append(float(input("Informe o segundo número ")))
    listaNumeros.append(float(input("Informe o terceiro número ")))

    # Declaração do maior e menor numero
    menorNumero = listaNumeros[0]
    maiorNumero = listaNumeros[0]

    # Verificação do menor numero
    for c1 in range(len(listaNumeros)):
        if listaNumeros[c1] < menorNumero :
            menorNumero = listaNumeros[c1]
    
    # Verificação do maior numero
    for c2 in range(len(listaNumeros)):
        if listaNumeros[c2] > maiorNumero :
            maiorNumero = listaNumeros[c2]

    # Mostra o resultado das verificações 
    print(f"O maior número é {maiorNumero} e o menor é {menorNumero}")

    # Pergunta para o usuario para realizar nova consulta
    repetir = str(input("\n Deseja realizar uma nova consulta ? \n Digite SIM para realizar uma nova consulta e NÃO para encerrar "))