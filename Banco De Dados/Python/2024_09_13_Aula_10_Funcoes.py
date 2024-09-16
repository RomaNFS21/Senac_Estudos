'''
def saudade ():
    print("Ola, seja bem vindo")

saudade()
'''

#####################
'''
def soma(a,b):
    return a + b

resultado = soma(5,5)
print(resultado)
 '''   

####################
'''
def calcularMedia (listaNumeros):
    somaTotal = sum(listaNumeros)
    divisor = len(listaNumeros)
    mediaTotal = somaTotal / divisor
    return mediaTotal

notas = [5,10,3,10]
media = calcularMedia(notas)
print(media)
'''

########################
'''
n1 = 50
n2 = 20

def soma():
    r = n1 + n2
    print(f"A soma de {n1} + {n2} é {r}")
    print("Hello python")

def subtrair():
    r = n1 - n2
    print(f"A subtração de {n1} - {n2} é {r}")

def multiplicar():
    r = n1 * n2 
    print(f"A multiplicação de {n1} x {n2} é {r}")

def divisão():
    r = n1 / n2 
    print(f"A multiplicação de {n1} / {n2} é {r}")

soma()
subtrair()
multiplicar()
divisão()
'''
###################################
'''
acesso = "Global"

def mudarAcesso():
    acesso = "Local"
    print("Acesso no interior da função: ", acesso)

mudarAcesso()
print("Acesso no exterior da função: ", acesso)
'''
#######################################
'''
def cadastrar(nome, idade, mensagem = "Dados com sucesso"):
    print(nome, "Possui a idade de ", idade, "anos")
    print(mensagem)

cadastrar("Marilia", 18, "Parabéns")
'''

################################