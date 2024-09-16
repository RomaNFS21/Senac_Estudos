let produtos = {
    videos : {
    comedia: ["comedia1","comedia2"],
    romance: ["romance1", "romance2"]
    },
    revistas : {                   // para ser um objeto as informações devem estar dentro {}
    moda : ["lalala", "lililili"], // trocar o = por :
    saude : ["lalala", "lililili"] // trocar o = por : e retirar a , do segunda chaves
    },
    jogos : {
    rpg: ["rpg1", "rpg2", "rpg3"], // na terceira informação colocar entre ""
    acao: ["acao1", "God of War"]
    }
    }

    console.log(produtos.jogos.acao[2]) // indice que veio é uma informação indefinida, caso queira exibir algo mudar para 0 ou 1