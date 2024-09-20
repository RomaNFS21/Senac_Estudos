# 1-Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

continuar = ""
while continuar.upper().lower() != "não" :

    velocidade = float(input("A que velocidade o carro passou pelo radar ? \n"))
    limiteVelocidade = 80
    valorPorKmExcedido = 5
    multa = (velocidade - 80) * valorPorKmExcedido

    if velocidade <= limiteVelocidade :
        print("\n Esse carro não ultrapassou o limite de velocidade e não foi multado \n")

    else:
        print(f" \n O carro foi multado por andar acima do limite de velocidade, sua multa é de R$ {multa:,.2f} \n")
        

    continuar = str(input(" Deseja verificar se mais algum carro foi multado ? \n Digite SIM para nova consulta e NÃO para encerrar \n"))