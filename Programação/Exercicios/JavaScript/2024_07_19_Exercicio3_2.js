function ePrimo (valor){
    if ( valor % valor === 0 && valor % 1 === 0 && valor > 1){
        console.log("Esse número é primo !");
    }
    else {
        console.log("Esse número não é primo");
    }
}

numero = 4;

ePrimo (numero);