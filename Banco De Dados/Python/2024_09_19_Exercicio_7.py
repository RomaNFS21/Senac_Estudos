## 7-Criar uma Class Cliente
## Nome, Sobrenome, Cpf, Renda
## adicionar 3 clientes
## -Criar uma Class Funcionario
## Nome, Sobrenome, Cpf, Matricula
## adicionar 3 clientes

class Cliente:
    def __init__(self,nomeCliente,sobrenomeCliente,cpfCliente,rendaCliente):
        self.nomeCliente = nomeCliente
        self.sobrenomeCliente = sobrenomeCliente
        self.cpfCliente = cpfCliente
        self.rendaCliente = rendaCliente

    def cadastroCliente(self):
        print(f"\nNome: {self.nomeCliente} {self.sobrenomeCliente}")
        print(f"CPF: {self.cpfCliente}")
        print(f"Renda: R$ {self.rendaCliente:,.2f}")

class Funcionario:
    def __init__(self,nomeFuncionario,sobrenomeFuncionario,cpfFuncionario,matriculaFuncionario):
        self.nomeFuncionario = nomeFuncionario
        self.sobrenomeFuncionario = sobrenomeFuncionario
        self.cpfFuncionario = cpfFuncionario
        self.matriculaFuncionario = matriculaFuncionario

    def cadastroFuncionario(self):
        print(f"\nNome: {self.nomeFuncionario} {self.sobrenomeFuncionario}")
        print(f"CPF: {self.cpfFuncionario}")
        print(f"Matricula: {self.matriculaFuncionario}")

cliente1 = Cliente("João","Silva","123.456.789-09", 3500)
cliente1.cadastroCliente()

cliente2 = Cliente("Maria ","Oliveira","987.654.321-00", 5200)
cliente2.cadastroCliente()

cliente3 = Cliente("Carlos ","Santos","111.222.333-44", 4800)
cliente3.cadastroCliente()

funcionario1 = Funcionario("Ana","Souza","123.456.789-01", "20231001")
funcionario1.cadastroFuncionario()

funcionario2 = Funcionario("Paulo","Ribeiro","987.654.321-02", "20231002")
funcionario1.cadastroFuncionario()

funcionario2 = Funcionario("Fernanda","Costa","111.222.333-03", "20231003")
funcionario1.cadastroFuncionario()