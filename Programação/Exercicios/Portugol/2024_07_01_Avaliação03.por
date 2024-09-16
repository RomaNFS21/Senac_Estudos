//Feito por Victor Roma e Wanderson
//01/07/2024
//Problema 3

programa {
 funcao inicio() {

//Declaração De Variaveis
 cadeia nome, nomeMaior, nomeMenor
 inteiro idade, cont
 inteiro idadeMaior = 0             //Variavel com valor inicial declarado
 inteiro idadeMenor = 999           //Variavel com valor inicial declarado
 real soma = 0.0                    //Variavel com valor inicial declarado
 real media = 0.0                   //Variavel com valor inicial declarado

//Contador para armazenar 10 vezes a informação solicitadas de Nome e Idade
 para (cont = 0; cont < 10; cont++) {
 escreva("Nome: ")
 leia(nome)
 escreva("Idade: ")
 leia(idade)

 //Se a nova idade for menor em relação a armazenada ele guarda a nova menor idade e o nome de quem é essa idade
 se (idade < idadeMenor) {
 idadeMenor = idade
 nomeMenor = nome
 }
 //Se a nova idade for maior em relação a armazenada ele guarda a nova maior idade e o nome de quem é essa idade
 se (idade > idadeMaior) {
 idadeMaior = idade
 nomeMaior = nome
 }
 //Soma todas as idades
 soma = soma + idade
 }
 //Calcula a média de todas as idades
 media = soma / 10

 //Descreve a media das idades, quem possui a menor idade e sua idade, quem possui a maior idade e sua idade
 escreva("A média de idades é: ", media, "\n")
 escreva(nomeMenor , " tem a menor idade que é: ", idadeMenor , " anos.\n")
 escreva(nomeMaior , " tem a maior idade que é: ", idadeMaior , " anos.\n")
 }
} } }