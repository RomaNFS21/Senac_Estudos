# Programa 04 -  Informar um saldo e imprimir o saldo com reajuste de 1%.

saldo = float(input("Qual é seu saldo ? "))

reajuste = saldo * 0.01
novo_saldo = saldo + reajuste

print(f"o seu novo saldo é de R$ {novo_saldo:,.2f}")