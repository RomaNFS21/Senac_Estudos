# Biblioteca para usar funções matematicas
import math

encerramento = ""
nomePassageiro = ""
valorPassagem = 0


while encerramento.upper().lower() != "confirmado" :

# Declaração de variavel e sua captação de valor pelo usuario
    nomePassageiro = str(input("Ola bem vindo a rodoviaria, para quem sera a passagem ? "))
    distanciaDestino = math.ceil(float(input("Qual a distancia em quilometros para o seu destino ? ")))

# Variaveis do valor de acordo com a distancia
    valorKmCurto = 0.5
    valorKmLongo = 0.45

# Verificação da distancia para realizar o calculo do valor da viagem

    if distanciaDestino <= 200 :
        valorPassagem = distanciaDestino * valorKmCurto
    

    elif distanciaDestino > 200 :
        valorPassagem = distanciaDestino * valorKmLongo
# Imprime o valor da passagem
    print(f"Sr(a) {nomePassageiro} o valor da sua passagem é de R$ {valorPassagem}")
# Verificação para encerrar a compra da passagem
    encerramento = str(input("Escreva Confirmado para emitir a passagem ou Cancelar para cancelar a passagem "))