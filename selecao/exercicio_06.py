'''Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se for
 digitado o valor zero, escrever a palavra zero.'''

    #''=='' é igual a ''igual''

valor = int(input("Insira um numero: "))
def IdentificarNumero(ValorNum):
    if ValorNum < 0:
        return "negativo"
    elif ValorNum > 0:
        return "positivo"
    else:
        return "zero"
print(f"Seu número é {IdentificarNumero(valor)}") 