#3-Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve
# perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

# Função para verificação do emprestimo 
def emprestimo (valorCasa, salario, meses):
    
    salario30 = round(salario * 0.3)
    prestacao = round(valorCasa / meses)

    print(f"{salario30} aaaa {prestacao}")

    if prestacao > salario30 :
        print("Não é possivel realizar esse emprestimo ")
    
    if prestacao < salario30 :
        print(f"É possivel realizar o emprestimo, serão prestações de R$ {prestacao} durante {meses} meses")


novaConsulta = ""

# Repetição para fazer mais de uma consulta 
while novaConsulta.upper().lower() != "não" :
    
    # Captação das informações pra o emprestimo
    print("\n Bem vindo ao banco Pernambuco informe abaixo para verificarmos se é viavel o emprestimo \n ")
    valorCasa = float((input("Qual o valor da casa que você deseja adiquirir \n")))
    salario = float(input("Qual a sua renda total atualmente \n"))
    anos = int(input("Em quantos anos você pensa em pagar o emprestimo \n"))

    meses = anos * 12

    # Chamando a função para verificar o emprestimo
    emprestimo(valorCasa,salario,meses)

    # Verificação se quer fazer uma nova consulta ou não
    novaConsulta = input("\n Deseja tentar fazer um novo emprestimo ? \n Digite SIM para uma nova consulta e NÃO para encerrar ")