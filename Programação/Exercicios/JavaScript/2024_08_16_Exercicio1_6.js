const prompt = require('prompt-sync')();

const palavra = prompt ("Digite uma palavra ")

const erroDeEscrita = new Error("Você não escreveu nada! ")

try {
    
    if (palavra == "" || palavra == " "){
        throw erroDeEscrita
    }   
}


catch(error){
console.log(error)
}