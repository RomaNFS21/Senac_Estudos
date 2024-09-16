'''
idade = int(input("Por favor informe sua idade ! "))

if idade < 12 :
    print("Você é uma criança ")

elif idade <= 18 :
    print("Você é um adolescente ")

elif idade <= 60 :
    print("Você é um adulto ")

else :
    print("Você é um idoso ")
    '''

#######################################

'''
serie = str(input("Qual serie ou anime você quer saber quantas temporadas tem ? "))

if serie == "Naruto" or serie == "naruto" :
    print("Naruto possui 9 temporadas ")

elif serie == "The Chosen" or serie == "the chosen" :
    print("The Chosen possui 4 temporadas")

elif serie == "O Agente Noturno" or serie == "o agente noturno" :
    print("O Agente Noturno possui 7 temporadas")

else :
    print("Não encontramos dados desse anime ou serie em nosso banco de dados")
    '''

#########################################

'''
valorInvestido = float(input("Quanto você quer investir ? "))
aplicacao = str(input("Qual forma de aplicação o Sr(a) quer investir Poupança ou CDB ? "))

rendimentoPoupanca = valorInvestido * 0.005
rendimentoCDB = valorInvestido * 0.01

if aplicacao == "Poupança" or aplicacao == "poupança" :
    print("Após um mês o seu investimento de ", valorInvestido, " de reais vai ter rendido ", rendimentoPoupanca," reais sendo seu novo saldo de ", valorInvestido + rendimentoPoupanca)

elif aplicacao == "CDB" or aplicacao == "cdb" :
    print("Após um mês o seu investimento de ", valorInvestido, " de reais vai ter rendido ", rendimentoCDB," reais sendo seu novo saldo de ", valorInvestido + rendimentoCDB)
'''

###########################################

letra = str(input("Digite uma letra "))

if letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "u" or letra == "U" or letra == "i" or letra == "I" or letra == "o" or letra == "O" :
    print("Você digitou uma vogal")

elif letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" or letra == "6" or letra == "7" or letra == "8" or letra == "9" or letra == "0" :
    print("Você não digitou uma letra")

else :
    print("Você digitou uma consoante ")