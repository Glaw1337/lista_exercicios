'''Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem:
“Múltiplo de 10”.'''

# Qual o multiplo que ele deva mostrar na lista

mult = int(input("Insira o multiplo desejado: "))
valorFinal = int(input("Qual seria o valor final? "))
valorInicial =int(input("Qual seria o valor inicial? "))

if(valorFinal > valorInicial):
    for i in range(valorInicial,valorFinal+1):
        if(i % mult == 0):
            print(i,f"é multiplo de {mult}")
        else:
            print(i)
else:
    print("Valor de entrada inválido!")