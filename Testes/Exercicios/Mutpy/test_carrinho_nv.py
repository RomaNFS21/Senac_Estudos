from carrinho import Item, Carrinho

# Adicionar um unico item
def teste_addUmItem():
    carrinho = Carrinho()
    item = Item("Laranja", 3.0, 10)
    carrinho.adicionar_item(item)
    assert carrinho.calcular_total() == 30.0

# Remover um item do carrinho
def teste_removerCarrinho():
    carrinho = Carrinho()
    itemDelete = Item("Caneta", 1.0, 6)
    itemDelete2 = Item("Caderno", 10.0, 1)
    carrinho.adicionar_item(itemDelete)
    carrinho.adicionar_item(itemDelete2)
    carrinho.remover_item("Caneta")
    assert carrinho.calcular_total() == 10.0

# Aplicação de desconto 

def test_desconto():
    carrinho = Carrinho()
    itemCarrinho = Item("Picanha", 100.0, 1)
    carrinho.adicionar_item(itemCarrinho)
    assert carrinho.aplicar_desconto(30) == 70.0

# Limpar Todos Itens do carrinho

def test_limparCarrinho():
    carrinho = Carrinho()
    itemLimpo1 = Item("Mouse", 50, 2)
    itemLimpo2 = Item("Teclado", 100, 3)
    carrinho.adicionar_item(itemLimpo1)
    carrinho.adicionar_item(itemLimpo2)
    carrinho.limpar_carrinho()
    assert carrinho.calcular_total() == 0

# Calcular Total de valor da quantidade de um unico item

def test_total_itens():
    item_Valor_Total = Item("Notebook", 1500.0, 10)
    assert item_Valor_Total.calcular_total() == 15000.0