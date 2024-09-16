const numeros = [30, 5, 14, 3, 80]
const numeroMaior = 0


for (contador = 0 ; contador <= 6 ; contador++){
    
    if (numeros[contador] > numeroMaior){
        numeroMaior = numeros[contador]
    }
}

console.log("O maior número informado foi" + numeroMaior);