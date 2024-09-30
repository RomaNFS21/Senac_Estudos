novaconsulta = ""

while novaconsulta.upper().lower() != "não" :

    # 
    print("Bem vindo ao media de notas")

    # Pergunta quantas notas serão usadas para fazer a média
    qtdNotas = int(input("Quantas notas vão ser usadas para tirar a média ? "))

    # Lista para receber as notas
    listaNotas = []

    # Preenchimento da lista pelo numero informado de notas
    for c1 in range(qtdNotas):
        listaNotas.append(float(input(f"Qual é a {c1+1}° nota do aluno ? ")))

    # Cacula a media
    media = sum(listaNotas) / qtdNotas

    # Verificação se esta aprovado
    if media >= 7 :
        print(f"Média \033[1;36m {media:,.2f} \033[m Aluno está \033[1;0;42m APROVADO \033[m")

    # Verificação se esta em recuperação
    if media >= 5 and media < 7.0 :
        print(f"Média \033[1;36m {media:,.2f} \033[m Aluno está em \033[1;0;43m RECUPERAÇÃO \033[m")

    # Verificação se esta reprovado
    if  media < 5 :
        print(f"Média \033[1;36m {media:,.2f} \033[m Aluno está \033[1;0;41m REPROVADO \033[m")

    #Checagem para uma nova consulta ou encerrar o programa
    novaconsulta = str(input("Deseja fazer uma nova consulta ? Digite \033[1;0;44m SIM \033[m para fazer uma nova consulta e \033[1;0;41m NÃO \033[m para encerrar "))