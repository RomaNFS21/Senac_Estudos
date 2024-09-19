class Produto:
    def __init__(self,nomeProduto,precoProduto,quantidadeProduto):
        self.nomeProduto = nomeProduto
        self.precoProduto = precoProduto
        self.quantidadeProduto = quantidadeProduto

    def mostra_info(self):
        print(f"Nome: {self.nomeProduto}")
        print(f"Preco: R${self.precoProduto:,.2f} a unidade")
        print(f"Quantidade: {self.quantidadeProduto} unidades em estoque")
        print("                                       ")


p1 = Produto("Água", 2.50, 60)
p1.mostra_info()        


p2 = Produto("Misto Quente", 5.0, 100)
p2.mostra_info()

p3 = Produto("Brigadeiro", 3.00, 50)
p3.mostra_info()

p4 = Produto("Refrigerante", 5.0, 45)
p4.mostra_info()

p5 = Produto("Pastel de forno", 5.0, 70)
p5.mostra_info()