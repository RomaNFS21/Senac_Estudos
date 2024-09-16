## Declaração das variaveis e captação pelo console dos seus valores pelo usuario
precoMercadoria = float(input("Qual o valor da mercadoria ? "))
descontoMercadoria = int(input("De quanto sera o desconto ? "))

## Declaração de variaveis que serão produtos de variaveis anteriores
descontoMercadoria = ((precoMercadoria * descontoMercadoria)/100)
novoPreco = (precoMercadoria - descontoMercadoria )

## Exibe o resultado dos produtos das variaveis
print(f"O desconto ser no valor de R$ {descontoMercadoria} ficando assim o valor final da mercadoria de R$ {novoPreco}")