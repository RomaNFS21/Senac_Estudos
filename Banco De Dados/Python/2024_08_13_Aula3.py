 #trabalhando com strings

'''
valor = input('Digite uma palavra! ')
print('o tipo primitivo é: ', type(valor)) #saber o tipo da variavel
print("tem espaço ? ", valor.isspace()) #saber se é somente um espaço digitado
print("é um numero ? ", valor.isnumeric()) 
print("é alfabetico ? ", valor.isalpha()) 
print("é alfanumerico ? ", valor.isalnum())
print("está em maiusculo ?", valor.isupper())
print("está em menusculo ?", valor.islower())
print("a prmeira letra é maiuscula ?", valor.istitle()) 
'''
##############################################
'''
valor2 = "asdamwohhghghhdinasdasdw@gmail.com"
print(len(valor2)) #saber o tamanho da variavel
print(valor2[5]) #saber a letra de acordo com o index
print(valor2.find('@')) #mostra a posição da primeiro termo procurado
print(valor2[3:]) # exibe o valor a partir do index informado
print(valor2[3:5]) # exibe o valor do intervalo dos index informados

print(valor2[valor2.find('@')])
'''
##############################################

'''
idade = int(input("Informe sua idade: "))

if idade < 18 :
    print("Você não é maior de idade")
    
else :
    print("Você é adulto")
'''
##############################################

'''
salarioAtual = float(input("Informe seu salario "))

if salarioAtual >= 5000 :
    salarioNovo = (salarioAtual + ((salarioAtual * 15)/100))
    print(f"Seu novo salario é {salarioNovo}")

else :
    salarioNovo = (salarioAtual + ((salarioAtual * 5)/100))
    print(f"Seu novo salario é {salarioNovo}")
    '''

###############################################

numero1 = int(input("Informe um numero "))
numero2 = int(input("Informe um numero "))

if numero1 == numero2 :
    print("Os números são iguais ")
else :
    print("Os números são diferentes ")
