'''
import numpy as np
import math
import random



colunas = int(input("Quantas colunas você vai querer na matriz ? "))
linhas = int(input("Quantas linhas você vai querer na matriz ? "))
maiorNumero = int(input("Qual o maior você quer que apareça ? "))
menorNumero = int(input("Qual o menor você quer que apareça ? "))

matriz = np.random.randint(menorNumero, maiorNumero, size=(linhas, colunas))

print(matriz)     
 '''
            ####################################3
'''

n=int(input("Digite a dimensão n da matriz: "))
m=int(input("Digite a dimensão m da matriz: "))

matriz = []

for i in range(n):
    matriz.append([0]*m)

for i in range(n):
    print(matriz[i])

'''

        ########################################
'''
notas = [
    [5.0, 4.5, 7.0, 5.2, 6.1],
    [2.1, 6.5, 8.8, 7.0, 6.7],
    [8.6, 7.0, 9.1, 8.7, 9.3]
    ]

novaConsulta = ''

while novaConsulta.upper().lower() != 'não' : 
    aluno = (int(input("De qual aluno você quer saber as notas ?\n ")) - 1)
    nota = (int(input("Qual a nota que você quer saber ?\n ")) - 1)

    print(" A nota ", (nota + 1) ," do aluno ", (aluno + 1), " é ", notas[aluno][nota])
    novaConsulta = input("Você deseja fazer uma nova consulta de nota ? \n Digite SIM para fazer uma nova consulta ou NÃO para encerrar ")
'''

#############################
'''
import numpy as np
import random

contadorPares = 0

colunas = int(input("Quantas colunas você vai querer na matriz ? "))
linhas = int(input("Quantas linhas você vai querer na matriz ? "))
maiorNumero = int(input("Qual o maior você quer que apareça ? "))
menorNumero = int(input("Qual o menor você quer que apareça ? "))

matriz = np.random.randint(menorNumero, maiorNumero, size=(linhas, colunas))
print(matriz)

for i in range (0,colunas,1) :
    for j in range (0,colunas,1):
        if matriz[i][j] % 2 == 0 :
            contadorPares = contadorPares + 1

print(f"Na matriz gerada tem {contadorPares} números pares")
'''
##########################
'''
colunas = 2 #int(input("Quantas informações você vai querer salvar das pessoas ? "))
linhas = 5 #int(input("Quantas pessoas você vai querer armazenar a idade ? "))


matriz = []

for i in range(linhas) :
    linha = []
    linha.append(input("Qual o nome da pessoa ? \n"))
    linha.append(int(input("Qual a idade da pessoa ? \n")))
    matriz.append(linha)

print(matriz)

# VERIFICAR A PESSOA COM MENOR IDADE
menorIdade = 100
menorIdadeNome = ''
for i in range(linhas) :
    for j in range(1,linhas,1) :
        if menorIdade < matriz[i][j] :
            menorIdade = matriz[i][j]
            menorIdadeNome = matriz[i][i]

print(f"A pessoa com menor idade é {menorIdadeNome} com {menorIdade} anos")
'''
########################

m=[]

for i in range(4):
    #Preenchendo a matriz
    linha=[]
    linha.append(input('Digite o nome da Pessoal '+ str(i)+' : '))
    linha.append(int(input('Digite a idade de ' + linha[0]+ ' : ')))
    m.append(linha)

#Procurando a pessoa mais nova
menor=m[0][1]
pos=0

for i in range(4):
    if m[i][1]<menor:
        menor=m[i][1]
        pos=i

#Imprimir a Matriz
for i in range(4):
    print(m[i])

print('A pessoa mais nova é', m[pos][0])
