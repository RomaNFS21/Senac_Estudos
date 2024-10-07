from calculadora import soma
from calculadora import subtrair 
from calculadora import multiplicar 
from calculadora import divisao 

def test_soma():
    assert soma(3,6) == 9    
    
def test_subtrair(): 
    assert subtrair(3,6) == 9    

def test_multiplicacao(): 
    assert multiplicar(3,6) == 9    

def test_divisao(): 
    assert divisao(3,6) == 9   