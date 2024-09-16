import sqlite3

conn=sqlite3.connect('texte2907.db')
query=('''create table if not exists doctor
    (
    id_doctor integer primary key,
    nome text not null,
    telefone char(20) not null,
    email text);''')
conn.execute(query)

query=('''create table if not exists paciente
    (
    id_paciente integer primary key,
    nomepaciente text not null,
    telefonepaciente char(20) not null,
    problema text not null,
    id_doctor interger,
    foreign key (id_doctor) references doctor(id_doctor)
    );''')
conn.execute(query)

query=('''create table if not exists medicamento
    (
    id_medicamento integer primay key,
    nomemedicamento tex not null,
    quantidade interger
    );''')
conn.execute(query)

query=('''create table if not exists pacientemedicamento
    (
    id_pacimedi integer primary key,
    id_paciente integer,
    id_medicamento integer,
    foreign key (id_paciente) references paciente(id_paciente),
    foreign key (id_medicamento) references medicamento(id_medicamento)
    );''')

conn.execute(query)
conn.close