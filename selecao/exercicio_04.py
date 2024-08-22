''' Acrescente ao exercício anterior a mensagem Você foi REPROVADO! Estude mais... caso a
 média calculada seja menor que 6.0.'''


notaAv1 = float(input("Qual a primeira nota? "))
notaAv2 = float(input("Qual a segunda nota? "))
def calculoMedia ():
    mediaSemestral = (notaAv1 + notaAv2) / 2
    if mediaSemestral > 6.0:
     return 'PARABÉNS! Você foi aprovado!'
    else:
     return 'Você foi REPROVADO! Estude mais...'
print(calculoMedia())      