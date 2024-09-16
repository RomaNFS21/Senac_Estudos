import sqlite3

nome = "Ana Maria"
Idade = 20
email = "anamaria@hotmail.com"

banco=sqlite3.connect('primeiro_banco.db')
cursor=banco.cursor()

#                   COMANDO PARA CRIAR A TABELA
#cursor.execute("CREATE TABLE cliente (nome text, idade integer, email text) ")

#                   COMANDO PARA INSERIR AS INFORMAÇÕES NO BANCO A PARTIR DE VARIAVEIS
#cursor.execute("INSERT INTO cliente VALUES ('"+nome+"',"+str(Idade)+",'"+email+"')")
# banco.commit()

#                   COMANDO PARA TROCAR UMA INFORMAÇÃO DE UM CAMPO
#cursor.execute("UPDATE pessoas SET Idade = 30 where nome = 'helio' ")
#banco.commit()

#                   COMANDO PARA DELETAR UMA LINHA DE INFORMAÇÕES
#cursor.execute("delete from pessoas where nome = 'breno'")
#banco.commit()