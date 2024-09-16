// Equipe: SINERGIA
// Data: 10/06/2024 Recife PE
// Contato:
// Objetivo: Corrigir e comentar erros

programa {
  funcao inicio() {
    real x, y, soma, sub, mult , div //variavel mult e div declaradas diferentes 

  escreva("Informe o primeiro número: ")  //não tem aspas duplas fechando o texto
  leia(y)
  escreva("Informe o segundo número:" )  //não tem aspas duplas fechando o texto
  leia(x)                             //ta sobre escrevendo o primeiro numero, nao pega um valor para X
  soma = x + y            //operações erradas em relação ao nome            
  sub = x - y
  mult = x * y
  div = x / y
escreva("\nMUltiplicar: ", mult) // chamada de resultados erradas / diferentes
escreva("\nSomar: ", soma)  // chamada de resultados erradas / diferentes
escreva("\nDividir: ", div) // chamada de resultados erradas / diferentes
escreva("\nSubtrair: ", sub, "\n")   //nao esta fechando aspas duplas para escrever, variavel errada,  tem um pular linha fora do aspas duplas
   
///código 2
 
// declaração de variáveis
 inteiro idade
 real altura
 cadeia nome
 caracter inicial, nome
 logico exemplo
 
 // atribuição de valores
 inicial = 'v'  //tem que ser aspas duplas
 exemplo = verdadeiro
 
 // entrada de dados
 escreva ("Informe o nome: \n")  //aspas erradas e pular linha para esteticamente ficar melhor visivel
 leia (nome) // nao tem nome declarado como variavel e so exibe a primeira letra do que foi escrito , caso queira exibir tudo mudar para cadeia
 escreva ("lnforme a aItura: \n") //aspas erradas e pular linha para esteticamente ficar melhor visivel
 leia (altura)
 // saída de dados
 escreva (nome)
 escreva (" \n AItura ", altura)  //Variavel chamada errada, aspas duplas erradas, texto espaçado e quebra de linha
  }
}
