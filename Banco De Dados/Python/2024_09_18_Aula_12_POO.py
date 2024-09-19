#Programação orientada a objeto no python
#Classe metodo herança

# Classe vendedor 
class Vendedor():                           #Nome da classe começa com lentra maiuscula 

    def __init__(self,nomeVendedor):
        self.nomeVendedor = nomeVendedor
        self.vendasVendedor = 0

    def vendeu(self,vendasVendedor):
        self.vendasVendedor = vendasVendedor

    def metaVendedor(self,metaVendedor):
        if self.vendasVendedor > metaVendedor:
            print(self.nomeVendedor, " bateu a meta !")
        else :
            print(self.nomeVendedor, " não bateu a meta")

Vendedor1 = Vendedor("Paulo")
Vendedor1.vendeu(5000)
Vendedor1.metaVendedor(3000)

print(Vendedor1.nomeVendedor ," conseguiu em vendas R$" , Vendedor1.vendasVendedor)


Vendedor2 = Vendedor("Antonio")
Vendedor2.vendeu(2500)
Vendedor2.metaVendedor(5000)

Vendedor3 = Vendedor("Claudia")
Vendedor3.vendeu(4500)
Vendedor3.metaVendedor(6000)