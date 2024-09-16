const numerosAleatorios = [];

for (contador = 0 ; contador < 5 ; contador++){
    numerosAleatorios[contador] = Math.round((Math.random() * 1000))
    
}
console.log(numerosAleatorios);

const menores250 = numerosAleatorios.filter(menor => {
    return menor < 250;
    }
)
console.log(menores250)
