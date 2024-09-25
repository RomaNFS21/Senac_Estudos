from ExercicioHeranca import Profressor
from ExercicioHeranca import Aluno

aluno1 = Aluno("Mariana Pereira","27","123.456.789-00","(41) 99876-5432","mariana.pereira@emailficticio.com","Ensino Superior Completo")
professor1 = Profressor("Lucas Martins","24","123.456.789-10","(11) 91234-5678","lucas.martins@emailficticio.com","Matemática")

print(aluno1.nome_aluno())
print("")
print(professor1.nome_professor())