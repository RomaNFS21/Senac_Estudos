# Início do programa
N = int(input("Digite o valor de N: "))
M = int(input("Digite o valor de M: "))

if N < M:
    if N % 2 == 0:
        N = N + 1  # Se N é par, começa com N+1
    else:
        N = N      # Se N é ímpar, começa com N

    SOMA = 0
    while N <= M:
        if N > 0:
            SOMA += N  # Soma N se for maior que 0
        N += 2  # Incrementa N de 2 em 2

    print(f"N: {N}, M: {M}, SOMA: {SOMA}")
else:
    print("INTERVALO INCORRETO")  # Mensagem de intervalo incorreto
