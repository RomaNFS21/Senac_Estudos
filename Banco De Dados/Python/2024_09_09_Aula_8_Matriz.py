"""carro = [
    ['Modelo', 'Palio'],
    ['Fabricante', 'Fiat'],
    ['Ano', 2016]
]
for l, c in carro:
    print("Linha: " + l + " | Coluna: " + str(c) + "\n")


carro.append(["Cor","Vermelho"])

print(carro)
"""
###############

notas = [
    [5.0, 4.5, 7.0, 5.2, 6.1],
    [10.0, 5.9 , 8.0, 9.0, 7.8],
    [4.8, 6.9 , 7.0, 8.8, 8.0]
]

# print(len(notas[1]))
# print(sum(notas[1]))

somaTodasNotas = 0
qtdNotas = 0
mediaNotas = 0

for i in range (0, len(notas), 1) :
    somaTodasNotas = somaTodasNotas + sum(notas[i])
    qtdNotas = qtdNotas + len(notas[i])

mediaNotas = somaTodasNotas / qtdNotas

print(f"A media da turma é {mediaNotas}")