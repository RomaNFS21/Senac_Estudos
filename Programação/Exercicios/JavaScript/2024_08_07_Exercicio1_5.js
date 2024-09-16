const animais = ["Cão", "Gato", "Sapo", "Cavalo", "Porco"];

const comLetraS = animais.findIndex(letra => {
    return letra.charAt() == "S"
})

console.log(comLetraS)