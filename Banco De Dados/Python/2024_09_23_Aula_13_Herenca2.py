from Herenca import Cliente
from Herenca import Funcionario

cliente1 = Cliente("Matheus","Alves","0000000085",50.0)
funcionario1 = Funcionario("Ana","Oliveira","5888888888",8)

print(f"{cliente1.nome_completo()}, {funcionario1.nome_completo()}")