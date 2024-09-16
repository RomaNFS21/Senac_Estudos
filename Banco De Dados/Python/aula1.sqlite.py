#Importar a biblioteca sqlite
import sqlite3

#Criar o arquivo do banco
banco=sqlite3.connect('primeiro_banco.db')

#
cursor=banco.cursor()

#Comando para criar a tabela e suas colunas com seu tipo da informação
#cursor.execute("create table pessoas(nome text, idade interger, email text)")
#banco.commit()


#Comando para inserir as informações na tabela
#cursor.execute("INSERT INTO pessoas VALUES('jorge', 32, 'jorge@gmail.com')")
#banco.commit()

#Para selecionar o que quer ser visualizado da tabela
cursor.execute("select * from pessoas")
#Para exibir no console as informações contidas no select
print(cursor.fetchall())