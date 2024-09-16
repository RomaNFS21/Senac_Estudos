const prompt = require('prompt-sync')();

const numero = prompt("Informe um numéro ");


const numeroNaoPositivo = new Error("O número informado não pode ser negativo! ");

try {    
    if (numero < 0) {
        throw numeroNaoPositivo;
    }   
}
catch (error){
    console.log(error);
}
