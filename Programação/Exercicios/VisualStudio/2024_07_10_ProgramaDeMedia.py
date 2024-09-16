## Declaração de variaveis
media = 0.0

## Captação de informações para as variaveis ainda não declaradas
NomeAluno = str(input("Qual o nome do aluno? \n"))
Nota1 = float(input("Qual a nota na disciplina de matemática? \n"))
Nota2 = float(input("Qual a nota na disciplina de portugês? \n"))
Nota3 = float(input("Qual a nota na disciplina de ciências? \n"))

## Calculo da media das tres notas
Media = (Nota1 + Nota2 + Nota3)/3

## Verificação se o aluno esta aprovado
if Media >= 7:
    print(NomeAluno," esta aprovado com média ",Media)
    
## Verificação se o aluno esta em recuperação
elif Media < 7 and Media >= 5:
    print(NomeAluno," esta em recuperação com média ",Media)

## Verificação se o aluno esta reprovado
elif Media < 5:
     print(NomeAluno," esta reprovado com média ",Media)

     