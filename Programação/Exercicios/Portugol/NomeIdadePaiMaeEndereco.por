programa {
  funcao inicio() {
    // declaração de variaveis
    cadeia nome, sobrenome, nome_pai, nome_mae, endereco , estado, pais
    inteiro idade
    
    // inicio do codigo que pega e armazena as informações nas variaveis declaradas
    escreva (" Informe a sua idade: ")
    leia(idade)
    
    escreva (" Informe seu nome: ")
    leia(nome)
    
    escreva (" Informe seu sobrenome: ")
    leia(sobrenome)
    
    escreva("Qual o nome do seu pai ?  ")
    leia(nome_pai)
    
    escreva("Qual o nome da sua mãe ? ")
    leia(nome_mae)
    
    escreva("Em que rua voce mora ? ")
    leia(endereco)
    
    escreva("Qual é seu estado ? ")
    leia(estado)
    
    escreva("Qual é seu País ? ")
    leia(pais)

    // exibe todas as informações em um texto
    escreva("Seu nome é ", nome, " " ,sobrenome, " você tem ", idade ,"anos, o nome dos seu pai é ", nome_pai, " o nome da sua mãe é ", nome_mae, " voce mora na rua ", endereco, " no estado de ", estado, " no país ", pais  )
    
  }
}
