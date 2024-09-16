'''
lista_nomes = ['luciana']
print(lista_nomes)
'''


################################

'''
lista_numeros = [10,'20',30,11]
print(type(lista_numeros[1]))
'''

###############################

'''lista_nomes = ['João', 'Pedro', 'Lucas', 'Jose']
print(len(lista_nomes))'''

#############################

'''
nomeProcurado = input("Qual o nome você esta procurando ")
lista_nomes = ['João', 'Pedro', 'Sergio', 'Jose']

if nomeProcurado.upper().lower() in lista_nomes:
    print(f"O nome de {nomeProcurado} esta na lista")

else :
    print(f'O nome {nomeProcurado} não se encontra na lista')
'''

################################

'''
listaHomens = ['Rodrigo', 'Sergio', 'Luis', 'Paulo']
listaMulheres = ['Camila', 'Joana', 'Luiza', 'Paula']

listaTotal = listaHomens + listaMulheres
print(listaTotal)
'''

##################################

'''
qtdRepeticao = int(input("Quantas vezes você quer que repita a lista ? "))

lista_nova = []
lista_frutas = ['banana', 'caju', 'uva', 'melancia']

for i in range (0,qtdRepeticao,1):
    lista_nova = lista_nova + lista_frutas

print(lista_nova)
'''

#################################

'''
lista_Numeros = [2,4,5,9]
menorNumero = min(lista_Numeros)
maiorNumero = max(lista_Numeros)
soma = sum(lista_Numeros)

print(f"O menor numero é {menorNumero} o maior numero é {maiorNumero} e a soma de todos os elementos da lista {soma}")
'''

#################################

'''
lista_nomes = ['João', 'Pedro', 'Lucas', 'Jose']
lista_nomes.append("Maria")
print(lista_nomes)
'''

##################################

'''
lista_nomes = ['João', 'Pedro', 'Lucas', 'Jose']
lista_nomes.insert(1,"Maria")
print(lista_nomes)
'''

##################################

'''
lista_nomes = ['João', 'Pedro', 'Lucas', 'Jose']
lista_nomes.pop(2)
print(lista_nomes)
'''

##############################

'''
lista_nomes = ['João', 'Pedro', 'Lucas', 'Jose']
lista_nomes.reverse()
print(lista_nomes)
'''

###############################

'''
lista_nomes = ['João', 'Pedro', 'Lucas', 'Jose', 'Lucas', 'Jose','Mario', 'Jeferson']
print(lista_nomes.count('Lucas'))
'''

#################################

palavras = ['python', 'javascript', 'codigo', 'web', 'programação','paralelepipedo']
palavraMenor = min(palavras, key=len)
palavraMaior = max(palavras, key=len)

print(f"a palavra maior é {palavraMaior} a palavra menor é {palavraMenor}")