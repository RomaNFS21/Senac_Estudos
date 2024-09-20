#6-Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
#informação no seu respectivo vetor. Imprima a idade e a altura na ordem
#inversa a ordem lida.

repetir = ""

while repetir.upper().lower() != "não" :
    listaIdades = [] 
    listaAlturas = [] 

    # Saber quantas pessoas terão informações coletadas
    qtdPessoas = int(input(" Quantas pessoas serão cadastradas ? \n"))

    # Coleta das informações 
    for c1 in range(qtdPessoas):
        listaIdades.append(int(input(f" Qual a idade da {c1+1}º pessoa?  \n")))
        listaAlturas.append(float(input(f" Qual a altura da {c1+1}º pessoa?  \n")))


    print(listaIdades)
    print(listaAlturas)   

    # Imprime do ultimo cadastrado ao primeiro
    for c2 in range (len(listaAlturas)-1, 0, -1):
        print(f"Altura: {listaAlturas[c2]:,.2f} Idade: {listaIdades[c2]} ")
    
    repetir = str(input("Deseja fazer uma nova lista ? SIM ou NÃO"))