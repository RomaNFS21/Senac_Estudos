const prompt = require('prompt-sync')();

//Solicita ao usuario o tamanho do array e os valores max e min
const tamanhoArray = prompt ("Qual o tamanho do array que você quer ? ");
const valorMinimo = prompt ("Qual o menor valor que você quer que apareça ? ");
const valorMaximo = prompt ("Qual o maior valor que você quer que apareça ? ");


//Função para criar um array/linha
function geradorArray(Tamanho, max, min){

    if (Tamanho < 0 || min > max){
        throw new Error("Argumentos invalidos");
    }
    
    const novoArray = [];
    
    for (i = 0 ; i < Tamanho ; i++){
        const numeroGerado = Math.round(Math.random() * (max - min + 1) + min);
        novoArray.push(numeroGerado);
    }
    
    console.log(novoArray);
    return novoArray;
    
    }
//              Gerar 3 linhas
const matriz1 = geradorArray(tamanhoArray, valorMaximo, valorMinimo)
const matriz2 = geradorArray(tamanhoArray, valorMaximo, valorMinimo)
const matriz3 = geradorArray(tamanhoArray, valorMaximo, valorMinimo)


// FUNÇÃO PARA PEGAR MATRIZES E MOSTRAR AS LINHAS E COLUNAS
function linhaColuna(primeiraMatrix, segundaMatrix, terceiraMatrix){
//              Imprimir linhas
console.log("As linhas das matrizes são : ");
console.log(primeiraMatrix);
console.log(segundaMatrix);
console.log(terceiraMatrix);

//              Imprimir colunas
for (coluna = 0 ; coluna < primeiraMatrix.length ; coluna++){
    console.log("Coluna", coluna, " : ");
    console.log("[",primeiraMatrix[coluna],",",segundaMatrix[coluna],",",terceiraMatrix[coluna],"]");
    }
}
// Saber as linhas e colunas das 3 arrays gerados

linhaColuna (matriz1,matriz2,matriz3);
