# 5- começa em 4 e vai até 0 de forma decrescente

repetir = ""
while repetir.upper() != "NÃO":
    
    ListaNumeros = []

    # Coletando informação do tamanho da lista
    QtdNumeros = int(input("Quantos números você quer na lista? "))

    # Adicionando numeros a lista pela quantidade informada
    for c1 in range(QtdNumeros):
        ListaNumeros.append(float(input(f"Informe o {c1+1}º número: ")))

    # Fazer a listas crescente e decrecente
    crescente = sorted(ListaNumeros)  # Retorna uma nova lista ordenada em ordem crescente
    decrescente = sorted(ListaNumeros, reverse=True)  # Retorna uma nova lista ordenada em ordem decrescente

    # Imprime as listas criadas
    print(f"Os números informados foram: {ListaNumeros}")
    print(f"A lista em ordem crescente: {crescente}")
    print(f"A lista em ordem decrescente: {decrescente}")

    # Verificação do loop
    repetir = input("Quer fazer novamente? SIM ou NÃO: ")
