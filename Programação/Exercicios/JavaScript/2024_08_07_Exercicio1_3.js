// array com 5 numeros inteiros
const numeros = [100, 300, 150, 102, 10]

const divididosPor100 = numeros.map(divisao => {
    if (divisao % 100 == 0){
        return divisao
    }

    if (divisao % 100 != 0){
        return "Não Divisivel"
    }
})

console.log(divididosPor100)