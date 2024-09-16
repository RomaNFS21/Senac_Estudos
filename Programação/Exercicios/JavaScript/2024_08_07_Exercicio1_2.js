// criação de um array com 7 animais
const animais = ["Cão", "Gato", "Pasarinho", "Cavalo", "Porco", "Vaca", "Galo"];

// pega o array e de todas as palavras ele vai captar a primeira letra
const primeiraLetra = animais.map(letra => {
    return letra.charAt() //função para pegar somente a primeira letra da string
})
// imprme o array criado com as primeiras letras de cada palavra do array original
console.log(primeiraLetra)