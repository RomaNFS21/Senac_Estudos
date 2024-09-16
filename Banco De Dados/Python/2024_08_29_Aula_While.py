'''
i = 1
while i < 10:
    print(i)
    i = i + 1
print("Acabou") 
'''

############################

'''
linguagem = ""
while linguagem !="python":
    print("Qual a linguagem que estamos estudando? ")
    linguagem = input()

print("Parabéns você acertou! ")
'''

#############################

'''
texto = "\n Digite 'sair' para encerrar o programa"
texto += "\n Digite alguma mensagem: "
mensagem = ""

while mensagem != 'sair':
    mensagem = input(texto)

print(mensagem)
'''

###########################

'''
num = 1
while num <= 10:
    print(num)
    if num == 7:
        break
    num = num + 1
    '''

############################

'''
num = 1
while num <= 30:
    if num % 5 == 0:
        print(num)
    num = num + 1
'''

#############################

'''
ranking = ['joão', 'maria', 'igor', 'paulo', 'laura', 'andré', 'alex']
print('top 3: ')

for nome in ranking[:3]:
    print('\t' + nome)

print("lista 3: ")
for nome in ranking[-3:]:
        print("\t " + nome)
'''

##############################

cores = ['Preto', 'Azul', 'Amarelo', 'Rosa']
'''
for i in range (0, len(cores), 1):
    print(f"{i} {cores[i]}")
    '''
for indice, cor in enumerate(cores):
    print(indice)