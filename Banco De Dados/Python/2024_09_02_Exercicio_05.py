listaNumeros = [3,7,9,10,15,21]

final = ''

while final.upper().lower() != "não" :

    numeroUsuario = float(input("Pense num número e digite ele aqui ! "))

    if listaNumeros.count(numeroUsuario):
        print(f"O numero {numeroUsuario}, que você pensou ele esta na lista !")

    else :
        print(f"Infelizmente o {numeroUsuario}, que você pensou naão esta na lista !")

    final = str(input("Digite SIM para tentar novamente e NÃO para parar "))