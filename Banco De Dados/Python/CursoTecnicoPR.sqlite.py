import sqlite3

conn=sqlite3.connect('Cursos_Tecnicos_PR.db')
query=('''create table if not exists Professor
    (
    ID_Professor integer primary key not null,
    Nome_Professor text not null,
    CPF_Professor text not null,
    Endereco_Professor text not null,
    Telefone_Professor_1 text not null,
    Telefone_Professor_2 text not null,
    Email_Professor text not null,
    Conta_Bancaria_Professor text not null
    );''')
conn.execute(query)

query=('''create table if not exists Curso
    (
    ID_Curso integer primary key not null,
    Nome_Curso text not null,
    Descricao_Curso text not null,
    Tipo_Curso text not null,
    Data_Inicio_Curso date not null,
    Data_Fim_Curso date not null,
    Mensalidade_Curso float not null,
    Turno_Curso text not null,
    ID_Professor int not null,
    foreign key (ID_Professor) references Professor (ID_Professor)
    );''')
conn.execute(query)

query=('''create table if not exists Aluno
    (
    ID_Aluno integer primary key not null,
    Nome_Aluno text not null,
    CPF_Aluno text not null,
    Endereco_Aluno text not null,
    Telefone_Aluno_1 text not null,
    Telefone_Aluno_2 text not null,
    Email_Aluno text not null,
    Forma_Pagamento_Aluno text not null
    );''')
conn.execute(query)

query=('''create table if not exists CursoAluno
    (
    ID_CursoAluno integer primary key not null,
    ID_Curso integer not null,
    ID_Aluno integer not null,
    foreign key (ID_Curso) references Curso(ID_Curso),
    foreign key (ID_Aluno) references Aluno(ID_Aluno)
    );''')
conn.execute(query)

query=('''create table if not exists Sala
    (
    ID_Sala integer primary key not null,
    Predio_Sala text not null,
    Andar_Sala text not null,
    Numero_Sala text not null
    );''')
conn.execute(query)

query=('''create table if not exists CursoSala
    (
    ID_CursoSala integer primary key not null,
    ID_Curso integer not null,
    ID_Sala integer not null,
    foreign key (ID_Curso) references Curso(ID_Curso),
    foreign key (ID_Sala) references Sala(ID_Sala)
    );''')
conn.execute(query)

query=('''create table if not exists Avaliacao
    (
    ID_Avaliacao integer primary key not null,
    Data_Avaliacao date not null,
    Nota_Avaliacao interger not null,
    Tipo_Avaliacao  text not null,
    ID_Curso integer not null,
    ID_Aluno integer not null,
    ID_Professor integer not null,
    foreign key (ID_Curso) references Curso(ID_Curso),
    foreign key (ID_Aluno) references Aluno(ID_Aluno),
    foreign key (ID_Professor) references Professor(ID_Professor)
    );''')
conn.execute(query)
conn.close