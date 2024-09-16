const prompt = require('prompt-sync')();

var numero1 = prompt("Informe um numéro ");
var numero2 = prompt("Informe um segundo numéro ");
var soma = 0

const numeroNaoPodeSer0 = new Error("O número informado não pode ser 0 ");

try {    
    if (numero2 == 0) {
        throw numeroNaoPodeSer0;
    }
    if (numero2 != 0) {
        soma = (+numero1) + (+numero2)
        console.log(soma)
    }
    
}
catch (error){
    console.log(error);
}
