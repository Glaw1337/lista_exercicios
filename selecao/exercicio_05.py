'''Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.'''

#Entrada
valor = int(input("Insira um numero: "))

#Processamento
def IdentificarNumero(ValorNum):
    if ValorNum < 0:
        return "negativo"
    else:
        return "positivo"
numero = IdentificarNumero(valor)    
#Saída
print(f"Seu número é {numero}")
