function calculoAcrecimo (valor , porcetagem){
    valorDaPorcetagem = (valor * (porcetagem/100))

valorFinal = valor + valorDaPorcetagem
console.log(valorFinal)
}

dinheiro = 100;
margemLucro = 30;

calculoAcrecimo (dinheiro , margemLucro)
