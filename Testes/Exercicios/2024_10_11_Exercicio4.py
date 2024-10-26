# Programa 01 - Fazer um programa que imprima a média aritmética dos números 8,9 e 7. A media dos números 4, 5 e 6. A soma das duas médias. A media das medias.

numero1 = int(input("Informe o primeiro número para a primeira media "))
numero2 = int(input("Informe o segundo número para a primeira media "))
numero3 = int(input("Informe o terceiro número para a primeira media "))

media1 = (numero1 + numero2 + numero3)/3

numero4 = int(input("Informe o primeiro número para a segunda media "))
numero5 = int(input("Informe o segundo número para a segunda media "))
numero6 = int(input("Informe o terceiro número para a segunda media "))

media2 = (numero4 + numero5 + numero6)/3

soma_media = media1 + media2

media_das_medias = (media1 + media2)/2

print(f"A primeira media é {media1}, a segunda media é {media2}, a soma das medias da {soma_media} e a media das medias é {media_das_medias}")

