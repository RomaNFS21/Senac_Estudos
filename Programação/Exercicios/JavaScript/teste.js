const prompt = require('prompt-sync')();
// Solicita ao usuário que digite seu nome
const nome = prompt('Qual é o seu nome? ');
// Mostra uma mensagem de saudação usando o nome fornecido pelo usuário
console.log("Olá, " + nome);