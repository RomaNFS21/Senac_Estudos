const nomeUsuario = ["Amanda123", "Aluno321", "Roma"]
const senhaUsuario = ["Amanda123", "Aluno321", "123456"]


    for (contador = 0 ; contador < 3 ; contador++){
        if (nomeUsuario[contador] === senhaUsuario[contador]){
            console.log("Senha invalida favor utilizar outra senha")
        }
        if (nomeUsuario[contador] !== senhaUsuario[contador]) {
            console.log("Senha valida")
        }
    }
