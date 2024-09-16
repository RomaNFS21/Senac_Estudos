const prompt = require('prompt-sync')();

var cilindro = {
    altura : 0,
    pi : 3.14,
    raio : 0,
    volume : 0
}

// Para pegar a altura do cilindro
cilindro.altura = prompt(" Qual a altura do cilindro? ")
// Para pegar o raio do cilindro
cilindro.raio = prompt(" Qual o raio do cilindro? ")
// Calcula o volume
cilindro.volume = cilindro.pi*cilindro.raio*cilindro.raio*cilindro.altura
// Exibe o volume com 4 casas decimais
console.log(cilindro.volume.toFixed(4))
