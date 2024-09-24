class Pessoa:

    def __init__(self,nome,idade,cpf,telefone,email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        
class Profressor(Pessoa):

    def __init__(self, nome, idade, cpf, telefone, email,disciplina):
        Pessoa.__init__(self,nome,idade,cpf,telefone,email)
        self.disciplina = disciplina

    def nome_professor(self):
        return f"Nome do professor: {self.nome} \n Idade: {self.idade} \n CPF: {self.cpf} \n Telefone: {self.telefone} \n Email: {self.email} \n Disciplina: {self.disciplina}"

class Aluno(Pessoa):

    def __init__(self, nome, idade, cpf, telefone,email, escolaridade):
        Pessoa.__init__(self,nome,idade,cpf,telefone,email)
        self.escolaridade = escolaridade

    def nome_aluno(self):
        return f"Nome do professor: {self.nome} \n Idade: {self.idade} \n CPF: {self.cpf} \n Telefone: {self.telefone} \n Email: {self.email} \n Escolaridade: {self.escolaridade}"
