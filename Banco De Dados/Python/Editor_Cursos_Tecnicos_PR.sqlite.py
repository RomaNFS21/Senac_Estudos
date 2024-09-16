import sqlite3

banco=sqlite3.connect('Cursos_Tecnicos_PR.db')

cursor=banco.cursor()

#                              TABELA SALA
# cursor.execute("INSERT INTO Sala VALUES('1', 'Alfa', '1', '101')")
# cursor.execute("INSERT INTO Sala VALUES('2', 'Alfa', '1', '102')")
# cursor.execute("INSERT INTO Sala VALUES('3', 'Alfa', '2', '201')")
# cursor.execute("INSERT INTO Sala VALUES('4', 'Beta', '1', '101')")
# cursor.execute("INSERT INTO Sala VALUES('5', 'Beta', '2', '101')")
# banco.commit()

#                              TABELA ALUNO

# cursor.execute("INSERT INTO Aluno VALUES( 1, 'Roberto', '26081547000', 'Rua numero 1', '8338133431', '6427846512', 'Roberto.gmail.com', 'A vista'  )")
# cursor.execute("INSERT INTO Aluno VALUES( 2, 'Flavia', '34663173047', 'Rua numero 2', '4532863756', '3228146186', 'Flavia.gmail.com', 'A Prazo'  )")
# cursor.execute("INSERT INTO Aluno VALUES( 3, 'Alessandra', '19352927060', 'Rua numero 3', '4538665543', '6439828803', 'Alessandra.gmail.com', 'A vista'  )")
# cursor.execute("INSERT INTO Aluno VALUES( 4, 'Tyson', '97917673006', 'Rua numero 4', '8539731155', '4721562811', 'Tyson.gmail.com', 'A vista'  )")
# cursor.execute("INSERT INTO Aluno VALUES( 5, 'Julio', '95069093002', 'Rua numero 5', '6634926386', '8836365613', 'Julio.gmail.com', 'A Prazo'  )")
# banco.commit()


#                            TABELA PROFESSOR

#cursor.execute("INSERT INTO Professor VALUES( 1, 'Zamira', '42763320015', 'Rua numero 34', '8735077702', '8737674760', 'Zamira.gmail.com', '1240181-1'  )")
#cursor.execute("INSERT INTO Professor VALUES( 2, 'Laura', '76492216016', 'Rua numero 50', '8735531675', '8731028764', 'Laura.gmail.com', '1251372-5'  )")
#cursor.execute("INSERT INTO Professor VALUES( 3, 'Diogo', '55047615065', 'Rua numero 193', '8721493045', '8727363831', 'Diogo.gmail.com', '48555592-4'  )")
#cursor.execute("INSERT INTO Professor VALUES( 4, 'Bruno', '44402719011', 'Rua numero 23', '8139214218', '8728248794', 'Bruno.gmail.com', '48545-1'  )")
#cursor.execute("INSERT INTO Professor VALUES( 5, 'Carolina', '63177717079', 'Rua numero 65', '8732366344', '8122381984', 'Carolina.gmail.com', '32183-1'  )")

#banco.commit()

#                            TABELA CURSO

#cursor.execute("INSERT INTO Curso VALUES( 1, 'Desenho', 'Curso de desenho iniciante', 'Basico', '02/09/2024', '30/09/2024', '200', 'Manhã', 1 )")
#cursor.execute("INSERT INTO Curso VALUES( 2, 'Desenho', 'Curso de desenho iniciante', 'Basico', '02/09/2024', '30/09/2024', '200', 'Tarde', 2 )")
#cursor.execute("INSERT INTO Curso VALUES( 3, 'Desenho', 'Curso de desenho iniciante', 'Basico', '02/09/2024', '30/09/2024', '200', 'Noite', 3 )")
#cursor.execute("INSERT INTO Curso VALUES( 4, 'Informatica', 'Curso de informatica iniciante', 'Basico', '02/09/2024', '30/09/2024', '300', 'Manhã', 4  )")
#cursor.execute("INSERT INTO Curso VALUES( 5, 'Informatica', 'Curso de informatica iniciante', 'Basico', '02/09/2024', '30/09/2024', '300', 'Tarde', 5  )")
#banco.commit()

#                           TABELA AVALIAÇÃO

#cursor.execute("INSERT INTO Avaliacao VALUES( 1, '30/09/2024', '', 'Final', '1', '1', '1')")
#cursor.execute("INSERT INTO Avaliacao VALUES( 2, '30/09/2024', '', 'Final', '2', '2', '2')")
#cursor.execute("INSERT INTO Avaliacao VALUES( 3, '30/09/2024', '', 'Final', '3', '3', '3')")
#cursor.execute("INSERT INTO Avaliacao VALUES( 4, '30/09/2024', '', 'Final', '4', '4', '4')")
#cursor.execute("INSERT INTO Avaliacao VALUES( 5, '30/09/2024', '', 'Final', '5', '5', '5')")
#banco.commit()

#                          TABELA CURSOALUNO

#cursor.execute("INSERT INTO CursoAluno VALUES( '1', '1', '1')")
#cursor.execute("INSERT INTO CursoAluno VALUES( '2', '2', '2')")
#cursor.execute("INSERT INTO CursoAluno VALUES( '3', '3', '3')")
#cursor.execute("INSERT INTO CursoAluno VALUES( '4', '4', '4')")
#cursor.execute("INSERT INTO CursoAluno VALUES( '5', '5', '5')")
#banco.commit()

#                          TABELA CURSOSALA

#cursor.execute("INSERT INTO CursoSala VALUES( '1', '1', '1')")
#cursor.execute("INSERT INTO CursoSala VALUES( '2', '2', '1')")
#cursor.execute("INSERT INTO CursoSala VALUES( '3', '3', '1')")
#cursor.execute("INSERT INTO CursoSala VALUES( '4', '4', '4')")
#cursor.execute("INSERT INTO CursoSala VALUES( '5', '5', '4')")
#banco.commit()


#cursor.execute("delete from Aluno where Nome_Aluno = 'Julio'")
#banco.commit()

#cursor.execute("select * from pessoas")
#print(cursor.fetchall())