//Pergunta
console.log("Segundo as informações apresentadas você consegue responder ?");

//Gerador do numero aleatorio para decidir qual resposta sera exibida
const resposta = Math.round(Math.random()*7);

//Teste para ver o numero gerado
console.log(resposta);

//Verificação de qual resposta sera exibida
if (resposta == 0) {
    console.log("Sim");
    }
    else if (resposta == 1) {
            console.log("Não sei, só sei que foi assim");
    }
    else if (resposta == 2){
            console.log("Não conte com isso");
    }
    else if (resposta == 3){
            console.log("Minhas fontes dizem que não");
    }
    else if (resposta == 4){
            console.log("Perspectiva não tão boa");
    }
    else if (resposta == 5){
            console.log("Sinais apontam para que sim");
    }
    else if (resposta == 6){
            console.log("Definitivamente não");
    }
else if (resposta == 7){
            console.log("Difícil prever, tente novamente");
    }