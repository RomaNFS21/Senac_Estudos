# importar bibliotecas necessárias
from isPrime import isPrime 

# caso de teste para verificar números não primos
def test_nonprime(): 
    assert isPrime(12) == False

# caso de teste para verificar números primos 
def test_prime(): 
    assert isPrime(19) == True

# caso de teste para verificar entrada inválida
def test_invalid(): 
    assert isPrime(-1) == False