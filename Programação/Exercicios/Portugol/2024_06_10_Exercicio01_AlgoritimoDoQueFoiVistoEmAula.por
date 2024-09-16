//Data: 10/06/2024
//Feito por: Victor Barros Roma
//ContatoS: (81)9-9594-3410 victor.b.roma@gmail.com
//Objetivo: Listar todos os assuntos vistos até o dia de hoje

programa {
  funcao inicio() {
    
    //Declarar Variaveis
    cadeia Hora


    //Inicio do codigo

    //Pergunta inicial para saber o momento do dia
    escreva("Agora é de: ? \n")
    escreva(" 1- Manhã \n 2- Tarde \n 3- Noite \n \n Responda com o numero correspondente ao momento do dia atual (1, 2 ou 3) \n ")
    
    //Captar do usuário a resposta
    leia(Hora)
    escreva("\n")

    //Verificação qual o momento do dia

    //Manhã
    se(Hora == 1) { 
      escreva("\t\t\t\t\t\t\tBom Dia \n\n")
    }

    //Tarde
    se(Hora == 2) { 
      escreva("\t\t\t\t\t\t\tBom Tarde \n\n")
    }

    //Noite
    se(Hora == 3) { 
      escreva("\t\t\t\t\t\t\tBom Noite \n\n") 
    }
    
    //Escreve na tela todas informações a serem informadas pelo programa
    escreva("Segue abaixo todos os assuntos abordados até o momento na UC 09 Desenvolver Algoritmos: \n \n")
    escreva(" -Tipos de variaveis (Inteiro, Real, Logico, Caractere e Cadeia) \n -Operadores Matemáticos ( + , - , * e /) \n ")
    escreva("-Operadores Logicos ( > , < , >= , <= , =/) \n -Editores de texto (Pular linha , Espaço, Aspas, Comentar o texto)\n")
    escreva(" -Assinar o codigo \n -Como escrever mensagem no console pelo comando ESCREVA \n -Como abrir o console para capturar o que o usuário escrever pelo comando LEIA \n")
    escreva(" -Metodo de desenvolvimento agil SCRUM \n -Ferramentas de produtividade \n -O que são requisitos funcionais e não funcionais \n")
    escreva(" -A usar a estrutura de SE e SENAO \n -A necessidade de ter conhecimento de outras 2 linguas \n -Tipos de levantamentos de requisitos \n")
    escreva(" -Formas de analise de requisitos \n -Especificação de requisitos \n -Verificação de requsitos \n")
    escreva(" -Gerenciamento de requisitos \n -O que são algoritmos \n -Portugol \n -Github \n -Comentar o codigo \n -Indentar o codigo ")
    escreva(" \n\n Fim")

  }
}
