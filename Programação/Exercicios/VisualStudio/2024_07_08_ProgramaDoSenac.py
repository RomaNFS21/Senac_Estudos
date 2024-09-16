Resposta_Area = str(input("\nOlá seja bem vindo ao Senac PE \nQual das areas você esta procurando um curso ? \nDigite o número correspondente a area \n1- Tecnologia da Informação  2- Negócios  3- Saúde\n"))

if Resposta_Area == "1":
    Resposta_Curso = str(input("Digite o número correspondente ao curso desejado\n1- Técnico em Informatica\n2- Analise e desenvolvimento de sistemas\n3- Redes\n"))
#Tipo De Curso 1
    if Resposta_Curso == "1":
        print("Parabens você acaba de declarar interesse no curso de técnico em informatica")

    elif Resposta_Curso == "2":
        print("Parabens você acaba de declarar interesse no curso de analise e desenvolvimento de sistemas")

    elif Resposta_Curso =="3":
        print("Parabens você acaba de declarar interesse no curso de redes")
    else :
        print("Curso invalido")
#Tipo De Curso 2
elif Resposta_Area == "2":
        Resposta_Curso = str(input("Digite o número correspondente ao curso desejado\n1- Relações internacionais\n2- Marketing e Vendas.\n3- Estratégia e Negócios\n"))

        if Resposta_Curso == "1":
            print("Parabens você acaba de declarar interesse no curso de relações internacionais")

        elif Resposta_Curso == "2":
            print("Parabens você acaba de declarar interesse no curso de Marketing e Vendas")

        elif Resposta_Curso =="3":
            print("Parabens você acaba de declarar interesse no curso de Estratégia e Negócios")
        else :
            print("Curso invalido")
#Tipo De Curso 3
elif Resposta_Area == "3":
        Resposta_Curso = str(input("Digite o número correspondente ao curso desejado\n1- Enfermagem\n2- Odontologia\n3- Farmácia\n"))

        if Resposta_Curso == "1":
            print("Parabens você acaba de declarar interesse no curso de Enfermagem")

        elif Resposta_Curso == "2":
            print("Parabens você acaba de declarar interesse no curso de Odontologia")

        elif Resposta_Curso =="3":
            print("Parabens você acaba de declarar interesse no curso de Farmácia")
        else :
            print("Curso invalido")
else :
     print("Area de curso invalida")