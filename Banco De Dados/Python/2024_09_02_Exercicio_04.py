listaCidades = []

qtdCidades = int(input("Quantas cidades você deseja colocar na sua lista ? "))

for qtdCidades in range (0,qtdCidades,1):
    novaCidade = str(input("Qual o nome da cidade ? "))
    listaCidades.append(novaCidade)    
    


print(listaCidades)