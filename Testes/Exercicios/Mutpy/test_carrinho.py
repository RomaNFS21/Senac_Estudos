# test_carrinho.py

from carrinho import Item, Carrinho

def test_adicionar_item():    #
    carrinho = Carrinho()
    item = Item("Maçã", 2.0, 5)
    carrinho.adicionar_item(item)
    assert carrinho.calcular_total() == 10.0

def test_remover_item():     #
    carrinho = Carrinho()
    item = Item("Banana", 1.5, 2)
    carrinho.adicionar_item(item)
    carrinho.remover_item("Banana")
    assert carrinho.calcular_total() == 0.0

def test_calcular_total():
    carrinho = Carrinho()
    item1 = Item("Laranja", 3.0, 3)
    item2 = Item("Uva", 5.0, 1)
    carrinho.adicionar_item(item1)
    carrinho.adicionar_item(item2)
    assert carrinho.calcular_total() == 14.0

def test_aplicar_desconto():  #
    carrinho = Carrinho()
    item = Item("Manga", 4.0, 5)
    carrinho.adicionar_item(item)
    total_com_desconto = carrinho.aplicar_desconto(10)
    assert total_com_desconto == 18.0  # Total original é 20.0

def test_limpar_carrinho():
    carrinho = Carrinho()
    item = Item("Morango", 2.5, 4)
    carrinho.adicionar_item(item)
    carrinho.limpar_carrinho()
    assert carrinho.calcular_total() == 0.0
