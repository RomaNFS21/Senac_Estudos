//Feito por Victor Roma e Wanderson
//01/07/2024
//Problema 3

programa {
 funcao inicio() {

//Declara��o De Variaveis
 cadeia nome, nomeMaior, nomeMenor
 inteiro idade, cont
 inteiro idadeMaior = 0             //Variavel com valor inicial declarado
 inteiro idadeMenor = 999           //Variavel com valor inicial declarado
 real soma = 0.0                    //Variavel com valor inicial declarado
 real media = 0.0                   //Variavel com valor inicial declarado

//Contador para armazenar 10 vezes a informa��o solicitadas de Nome e Idade
 para (cont = 0; cont < 10; cont++) {
 escreva("Nome: ")
 leia(nome)
 escreva("Idade: ")
 leia(idade)

 //Se a nova idade for menor em rela��o a armazenada ele guarda a nova menor idade e o nome de quem � essa idade
 se (idade < idadeMenor) {
 idadeMenor = idade
 nomeMenor = nome
 }
 //Se a nova idade for maior em rela��o a armazenada ele guarda a nova maior idade e o nome de quem � essa idade
 se (idade > idadeMaior) {
 idadeMaior = idade
 nomeMaior = nome
 }
 //Soma todas as idades
 soma = soma + idade
 }
 //Calcula a m�dia de todas as idades
 media = soma / 10

 //Descreve a media das idades, quem possui a menor idade e sua idade, quem possui a maior idade e sua idade
 escreva("A m�dia de idades �: ", media, "\n")
 escreva(nomeMenor , " tem a menor idade que �: ", idadeMenor , " anos.\n")
 escreva(nomeMaior , " tem a maior idade que �: ", idadeMaior , " anos.\n")
 }
} } }