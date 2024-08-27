'''Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
 escrevê-los em ordem crescente.'''
#        exercicio importante, refazer sempre que possivel 
#        (CTRL + ;) adiciona comentario

valores = []
valores.append(int(input("Insira o primeiro número: ")))
valores.append(int(input("Insira o segundo número: ")))
valores.append(int(input("Insira o terceiro número: ")))


if(valores[0] > valores[1] ):
    valorTemp = valores[1]
    valores[1] = valores[0]
    valores[0] = valorTemp
if(valores[0] > valores[2] ):
    valorTemp = valores[2]
    valores[2] = valores[0]
    valores[0] = valorTemp
if(valores[1] > valores[2] ):
    valorTemp = valores[2]
    valores[2] = valores[1]
    valores[1] = valorTemp

print(valores)
