#Programa 2 Ler um ano de nascimento e ano atual. Imprimir a idade da pessoa. 
# Se a idade for maior ou igual a 18 leia o nome da pessoa e imprima o nome digitado e uma mensagem informando que sua entrada é permitida

nome_pessoa = str(input("Bem vindo a festa informe seu nome por favor: "))
ano_nascimento = int(input("Favor informe o ano do seu nascimento: "))
ano_atual = int(input("Favor informe em que ano estamos: "))

diferenca_ano = (ano_atual - ano_nascimento)

if diferenca_ano < 18:
    print(f"{nome_pessoa} sua entrada não é permitida")

if diferenca_ano >= 18:
    print(f"{nome_pessoa} sua entrada é permitida")
