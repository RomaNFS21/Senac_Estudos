const prompt = require('prompt-sync')();

const numeroInteiro = prompt("Informe um numéro inteiro ");

const numeroNaoInteiro = new Error("O número informado não é inteiro ");

try {    
    if (numeroInteiro % 1 != 0); {
        
        throw numeroNaoInteiro;
    }
}
catch (error){
    console.log(error);
}
