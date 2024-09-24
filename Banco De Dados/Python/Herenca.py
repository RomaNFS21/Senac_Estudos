class Pessoa:

    def __init__(self,nome,sobrenome,cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        
    
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
################################

class Cliente(Pessoa):

    def __init__(self,nome,sobrenome,cpf,renda):
        Pessoa.__init__(self,nome,sobrenome,cpf)
        self.renda = renda
    
    def nome_completo(self):
        return f" Nome Cliente: {self.nome} {self.sobrenome} Sua renda é de: {self.renda}"
    
################################

class Funcionario(Pessoa):
    def __init__(self,nome,sobrenome,cpf,matricula):
        Pessoa.__init__(self,nome,sobrenome,cpf)
        self.matricula = matricula
    
    def nome_completo(self):
        return f" Nome Funcionario: {self.nome} {self.sobrenome} Numero da matricula: {self.matricula}"
        

cliente1 = Cliente("Matheus","Alves","0000000085",50.0)
funcionario1 = Funcionario("Ana","Oliveira","5888888888",8)

#print(cliente1.nome_completo())
#print(funcionario1.nome_completo())