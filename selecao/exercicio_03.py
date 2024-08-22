'''Escreva um programa para ler as notas das duas avaliações de um aluno no semestre, calcular e
 escrever a média semestral e a seguinte mensagem: PARABÉNS! Você foi aprovado! somente se o
 aluno foi aprovado (considere 6.0 a média mínima para aprovação)'''


notaAv1 = float(input("Qual a primeira nota? "))
notaAv2 = float(input("Qual a segunda nota? "))
def calculoMedia ():
    mediaSemestral = (notaAv1 + notaAv2) / 2
    if mediaSemestral > 6.0:
     return 'PARABÉNS! Você foi aprovado!'
print(calculoMedia())