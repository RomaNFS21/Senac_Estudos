# carrinho.py

class Item:
    def __init__(self, nome, preco, quantidade=1):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, nome_item):
        self.itens = [item for item in self.itens if item.nome != nome_item]

    def calcular_total(self):
        return sum(item.calcular_total() for item in self.itens)

    def aplicar_desconto(self, percentual):
        desconto = self.calcular_total() * (percentual / 100)
        return self.calcular_total() - desconto

    def limpar_carrinho(self):
        self.itens.clear()
