//Traduza o c�digo adicionando coment�rios em cada bloco,  crie um c�digo que exiba de 0 a 1000, adicione coment�rios e insira sua assinatura, anexe o arquivo do seu c�digo nesta atividade. 
 
programa {
  //Incluir a biblioteca Ultil
  inclua biblioteca Util
  funcao inicio() {
    //Declara��o de variaveis
    inteiro i, vet[20]

    //Contador que cria um vetor de tamanho aleatorio apos vinte vezes
    para(i = 0; i<20; i++){
    vet[i] = Util.sorteia(0,100)
    //escreva("\n",vet[i])
    }
    //Contador que conta 20 vezes e mostra em qual vez esta
    para(i=0; i<20;i++){
    escreva("\n",i)
    }
  }
}