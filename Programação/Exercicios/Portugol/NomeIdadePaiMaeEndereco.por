programa {
  funcao inicio() {
    // declara��o de variaveis
    cadeia nome, sobrenome, nome_pai, nome_mae, endereco , estado, pais
    inteiro idade
    
    // inicio do codigo que pega e armazena as informa��es nas variaveis declaradas
    escreva (" Informe a sua idade: ")
    leia(idade)
    
    escreva (" Informe seu nome: ")
    leia(nome)
    
    escreva (" Informe seu sobrenome: ")
    leia(sobrenome)
    
    escreva("Qual o nome do seu pai ?  ")
    leia(nome_pai)
    
    escreva("Qual o nome da sua m�e ? ")
    leia(nome_mae)
    
    escreva("Em que rua voce mora ? ")
    leia(endereco)
    
    escreva("Qual � seu estado ? ")
    leia(estado)
    
    escreva("Qual � seu Pa�s ? ")
    leia(pais)

    // exibe todas as informa��es em um texto
    escreva("Seu nome � ", nome, " " ,sobrenome, " voc� tem ", idade ,"anos, o nome dos seu pai � ", nome_pai, " o nome da sua m�e � ", nome_mae, " voce mora na rua ", endereco, " no estado de ", estado, " no pa�s ", pais  )
    
  }
}
