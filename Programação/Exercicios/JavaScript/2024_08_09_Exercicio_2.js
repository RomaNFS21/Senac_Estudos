const prompt = require('prompt-sync')();

//Informações do cadastro
const nomeParticipante = [];
const idadeParticipante = [];
const horaInscricao = [];
const numeroParticipante = [];
const horaCorrida = [];

//Saber quantas pessoas vão ser cadastradas
const qtdCadastro = prompt('Quantas pessoas vão ser cadastradas ')

//Levantamento de dados das pessoas que vão ser cadastradas
for (contadorCad = 0 ; contadorCad < qtdCadastro ; contadorCad++){
    nomeParticipante[contadorCad] = prompt('Qual o nome do participante ? ')
    idadeParticipante[contadorCad] = prompt('Qual a idade do participante ? ')
    horaInscricao[contadorCad] = prompt('Que horas são agora? inscrições até as 10:30 favor resgistrar horas.minutos ')
}

//Determinar numero do participante
for (contadorp = 0 ; contadorp < nomeParticipante.length ; contadorp++){
    if (idadeParticipante[contadorp] < 18){
        numeroParticipante[contadorp] = 1 + contadorp;
    }
    if (idadeParticipante[contadorp] >= 18){
        numeroParticipante[contadorp] = 1000 + contadorp;
    }
}

//Determinar hora da corrida
for (contadorc = 0 ; contadorc < nomeParticipante.length ; contadorc++){
    if (horaInscricao[contadorc] <= 9 && idadeParticipante[contadorc] >= 18){
        horaCorrida[contadorc] = "9:30";
    }
    else if (horaInscricao[contadorc] > 9 && idadeParticipante[contadorc] >= 18){
        horaCorrida[contadorc] = "11:00";
    }
    else if (idadeParticipante[contadorc] < 18){
        horaCorrida[contadorc] = "12:30";
    }
}

//Visualização de todas as informações teste
//console.log(nomeParticipante)
//console.log(idadeParticipante)
//console.log(horaInscricao)
//console.log(numeroParticipante)
//console.log(horaCorrida)

console.log("------ INFORMAÇÕES DOS PARTICIPANTES ------")
console.log(" ")

//Apresentação dos dados dos participantes
for (contadori = 0 ; contadori < nomeParticipante.length ; contadori++){
    console.log("Nome: " + nomeParticipante[contadori])
    console.log("Idade: " + idadeParticipante[contadori] + " anos")
    console.log("Numero do participante: " + numeroParticipante[contadori])
    //console.log("Horario da inscrição: " + horaInscricao[contadori]) Preferi retirar da exibição por causa do metodo que usei para comparar não ficar bom para exibir a informação
    console.log("Hora da corrida: " + horaCorrida[contadori])
    console.log("--------------------------------------------")    
}
