class Licenciamento:
    def __init__(self,nomeVeiculo,fabricanteVeiculo,corVeiculo,anoVeiculo,placaVeiculo):
        self.nomeVeiculo = nomeVeiculo
        self.fabricanteVeiculo = fabricanteVeiculo
        self.corVeiculo = corVeiculo
        self.anoVeiculo = anoVeiculo
        self.placaVeiculo = placaVeiculo

    def registro(self):
        print(f"Nome do modelo: {self.nomeVeiculo}")
        print(f"Fabricante do veiculo: {self.fabricanteVeiculo}")
        print(f"Cor da unidade: {self.corVeiculo}")
        print(f"Ano de fabricação: {self.anoVeiculo}")
        print(f"Placa do veiculo: {self.placaVeiculo}")
        print("       ")


veiculo1 = Licenciamento("Lancer", "Mitsubishi", "Branco", "2015", "PCI3886")
veiculo1.registro()

veiculo2 = Licenciamento("Uno", "Fiat", "Azul", "2013", "PGG7987")
veiculo2.registro()

veiculo3 = Licenciamento("Corolla", "Toyota", "Branco", "2020", "QYD2JR5")
veiculo3.registro()

veiculo4 = Licenciamento("Mobi", "Fiat", "Marrom", "2018", "GUT2385")
veiculo4.registro()