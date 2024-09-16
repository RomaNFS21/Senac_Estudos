novamente = ''

while novamente.upper().lower() != "não" :
    nomePaciente = str(input("Qual é seu nome ? "))
    alturaPaciente = float(input("Qual é sua altura ? "))
    pesoPaciente = float(input("Qual o seu peso em quilogramas ? "))

    imc = ((pesoPaciente) / (alturaPaciente**2))

    if imc < 18.5 :
        print(f"Sr(a) {nomePaciente}, você se encontra abaixo do peso ")
    
    if imc >= 18.5 and imc < 24.9 :
        print(f"Sr(a) {nomePaciente}, você se encontra no peso normal ")

    if imc >= 24.9 and imc < 29.9  :
        print(f"Sr(a) {nomePaciente}, você se encontra com sobrepeso")

    if imc >= 29.9 and imc < 34.9  :
        print(f"Sr(a) {nomePaciente}, você se encontra com obesidade grau 1")

    if imc >= 34.9 and imc < 39.9  :
        print(f"Sr(a) {nomePaciente}, você se encontra com obesidade grau 2")

    if imc >= 39.9 :
        print(f"Sr(a) {nomePaciente}, você se encontra com obesidade grau 3 ou mórbida")

    
    novamente = str(input("Deseja fazer um novo calculo de IMC ? digite SIM para fazer novamente ou digite NÃO para encerrar "))
