const prompt = require('prompt-sync')();

const erroDeLeitura = new Error("Esse array não tem nada dentro dele")

const nomes = []

try {
    
        if (nomes.length == 0){
            throw erroDeLeitura  
        }   
    }
    

catch(error){
    console.log(error)
}
